from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, AutoModelForCausalLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import torch

# Load Summarization Model (facebook/bart-large-cnn)
SUMMARIZATION_MODEL = "bart-large-cnn"
sum_tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL)
sum_model = AutoModelForSeq2SeqLM.from_pretrained(SUMMARIZATION_MODEL)
sum_pipeline = pipeline("summarization", model=sum_model,
                        tokenizer=sum_tokenizer, device="cpu")  # ✅ Fixed

# Load Answer Extraction Model (MBZUAI/LaMini-GPT-1.5B)
ANSWER_MODEL = "LaMini-GPT-1.5B"
ans_tokenizer = AutoTokenizer.from_pretrained(ANSWER_MODEL)
ans_model = AutoModelForCausalLM.from_pretrained(ANSWER_MODEL)
ans_pipeline = pipeline("text-generation", model=ans_model,
                        tokenizer=ans_tokenizer, device="cpu")  # ✅ Fixed

# Retrieve Relevant Context from ChromaDB


def get_relevant_context_from_db(query):
    """Fetches the most relevant context from ChromaDB and formats it properly."""
    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2")
    vector_db = Chroma(persist_directory="./chroma_db",
                       embedding_function=embedding_function)

    search_results = vector_db.similarity_search(query, k=5)

    if not search_results:
        return "❌ No relevant information found. Please contact the PRS office."

    context = "\n\n".join([result.page_content.strip()
                          for result in search_results])
    return context  # ✅ Fixed return (No unpacking issue)

# Refine Retrieved Context (Summarization)


def refine_context(raw_context):
    """Formats the retrieved context into a well-structured summary."""
    if not raw_context.strip():
        return "❌ No context available."

    summary = sum_pipeline(raw_context, max_length=256,
                           min_length=50, do_sample=False)[0]['summary_text']
    return summary

# Generate Final Answer


def generate_answer(query, formatted_context):
    """Extracts the final answer from the formatted context."""
    prompt = f"""Based on the given context, provide a well-explained, direct answer.

    Context: {formatted_context}

    Question: {query}

    Answer (in a single, complete sentence):"""

    response = ans_pipeline(prompt, max_new_tokens=100,
                            do_sample=False, temperature=0.1)

    if not response or "generated_text" not in response[0]:
        return "❌ Error generating an answer. Please try again."

    generated_text = response[0]["generated_text"].strip()

    marker = "Answer (in a single, complete sentence):"
    if marker in generated_text:
        answer = generated_text.split(marker, 1)[-1].strip()
    else:
        answer = generated_text

    return answer


# Full Pipeline (Retrieve → Refine → Answer)


def get_final_answer(query):
    """Runs the full pipeline from retrieval to refinement to answering."""
    raw_context = get_relevant_context_from_db(
        query)  # ✅ Fixed (No unpacking error)

    if "❌" in raw_context:
        return raw_context  # Return error message if no relevant context found

    formatted_context = refine_context(raw_context)
    answer = generate_answer(query, formatted_context)

    return {
        "answer": answer,
        "reference_context": raw_context
    }
