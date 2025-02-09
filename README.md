# AI HelpDesk

## 📌 Overview

The **AI HelpDesk** is an intelligent assistant designed to help university students with their academic inquiries, including university policies, student guidelines, and general academic-related questions. The chatbot integrates **web scraping, document embeddings, and Large Language Models (LLMs)** to provide precise and contextually relevant answers.

---

## 🧩 Features

- ✅ **Web Scraping**: Dynamically extracts data from university websites using **Playwright** & **BeautifulSoup**.
- ✅ **AI-Powered Answering**: Uses **BART-Large-CNN** for summarization & **LaMini-GPT-1.5B** for response generation.
- ✅ **Efficient Retrieval**: Stores embeddings in **ChromaDB** for fast and accurate search.
- ✅ **Scalable & Fast**: Supports large datasets and multiple queries efficiently.
- ✅ **User-Friendly UI**: Built with **Streamlit** for an intuitive chatbot interface.

---

## 🛠️ Tech Stack

- **Python** (Primary Language)
- **Playwright & BeautifulSoup** (Web Scraping)
- **LangChain** (Retrieval & Document Processing)
- **Hugging Face Transformers** (LLMs for Answering)
- **ChromaDB** (Vector Database)
- **Streamlit** (Frontend UI for Chatbot)

---

## ⚙️ How It Works

### 1️⃣ Data Collection
- Scrapes university web pages using **Playwright** & **BeautifulSoup**.
- Extracts text and stores it in structured files.

### 2️⃣ Document Processing & Embeddings
- Loads university handbooks, student guidelines, and scraped data.
- Splits text into smaller chunks & creates vector embeddings using **sentence-transformers/all-mpnet-base-v2**.
- Stores embeddings in **ChromaDB** for efficient retrieval.

### 3️⃣ Query Processing
- User asks a question via **Streamlit UI**.
- Retrieves the most relevant context using **semantic search** on **ChromaDB**.
- Summarizes retrieved content with **BART-Large-CNN**.
- Generates a final answer using **LaMini-GPT-1.5B**.

---

## 📂 Folder Structure

```
📦 AI-Help-Desk 
 ┣ 📂 bart-large-cnn  # Pre-trained Summarization Model
 ┣ 📂 LaMini-GPT-1.5B  # Pre-trained LLM for Response Generation
 ┣ 📂 chroma_db  # Vector Database Storage
 ┣ 📂 Data  # Scraped Data and Documents
 ┃ ┣ 📜 DataSet.pdf
 ┃ ┣ 📜 Participant-Guide.pdf
 ┃ ┗ 📜 Handbook-Undergraduate-Studies.pdf
 ┣ 📂 Notebooks  # Jupyter Notebooks for Preprocessing
 ┃ ┣ 📜 clean_scraping_data.ipynb
 ┃ ┣ 📜 data_preprocessing.ipynb
 ┃ ┗ 📜 csv_to_pdf.ipynb
 ┣ 📜 scrapping.py  # Web Scraper
 ┣ 📜 embeddings.py  # Embedding Generator
 ┣ 📜 utils.py  # Context Retrieval & Summarization
 ┣ 📜 main.py  # Streamlit UI for Chatbot
 ┣ 📜 design.py  # UI Design
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 LICENSE  # Project License
 ┗ 📜 README.md  # Documentation
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/umt-help-desk/AI-HelpDesk-RAG-Model.git
cd AI-HelpDesk-RAG-Model
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download LLMs (Pre-Trained Models)
```bash
git clone https://huggingface.co/facebook/bart-large-cnn

git clone https://huggingface.co/MBZUAI/LaMini-GPT-1.5B
```
⚠️ Ensure both `bart-large-cnn` and `LaMini-GPT-1.5B` folders are in the project directory.

### 4️⃣ Run Web Scraper (Optional)
```bash
python scrapping.py
```

### 5️⃣ Generate Embeddings & Store in ChromaDB
```bash
python embeddings.py
```

### 6️⃣ Start the Chatbot
```bash
streamlit run main.py
```

---

## 🔍 Troubleshooting

### 🔹 Module Not Found: `ModuleNotFoundError: No module named 'playwright'`
```bash
pip install playwright
playwright install
```

### 🔹 Out of Memory (OOM) Error
- Reduce `chunk_size` in `embeddings.py`.
- Use `device='cpu'` in models if running on a low-GPU machine.

### 🔹 No Response from Chatbot
- Ensure both LLMs are downloaded and placed in the project directory.
- Run `python embeddings.py` again before starting `main.py`.

### 🔹 Missing Dependencies / Python Version Mismatch
```bash
conda create -n ai-help-desk python=3.10.12
conda activate ai-help-desk
pip install -r requirements.txt
```

---

## 🤝 Contributing

We welcome contributions! If you'd like to improve the chatbot, follow these steps:

1. **Fork** the repository.
2. **Create a new branch**: `git checkout -b feature-branch`
3. **Commit your changes**: `git commit -m 'Added new feature'`
4. **Push to the branch**: `git push origin feature-branch`
5. **Create a Pull Request**

---

## 📜 License

This project is licensed under the **MIT License**. See the full license details in the [LICENSE](LICENSE) file.

---

## 📬 Contributors Contact
👤 **Muhammad Rehan Hanif**  
📧 Email: [rehan.hanif2004@gmail.com](mailto:rehan.hanif2004@gmail.com)  
📂 GitHub: [MRH-66](https://github.com/MRH-66)

👤 **Syed Burhan Ahmad**  
📧 Email: [syedburhanahmedd@gmail.com](mailto:syedburhanahmedd@gmail.com)  
📂 GitHub: [SyedBurhanAhmed](https://github.com/SyedBurhanAhmed)

👤 **Kaleemullah Younas**  
📧 Email: [kaleemullahyouus123@gmail.com](mailto:kaleemullahyouus123@gmail.com)  
📂 GitHub: [Kaleemullah-Younas](https://github.com/Kaleemullah-Younas)

👤 **Syed Arman Mehdi Kazmi**  
📧 Email: [kazmiarmanmehdi@gmail.com](mailto:kazmiarmanmehdi@gmail.com)  
📂 GitHub: [ArmanMehdi](https://github.com/ArmanMehdi)

👤 **Ali Hassan**  
📧 LinkedIN: [Ali Hassan](https://www.linkedin.com/in/ali-hassan-96b230244/)  
📂 GitHub: [logsaviour](https://github.com/logsaviour)

---

## 🌟 Acknowledgments

- [Hugging Face](https://huggingface.co/) - Pre-trained LLMs
- [LangChain](https://python.langchain.com/) - Efficient Context Retrieval
- [Streamlit](https://streamlit.io/) - UI for Chatbot
- [ChromaDB](https://www.trychroma.com/) - Vector Database
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Web Scraping

### 🎓 AI-Powered University Assistance
