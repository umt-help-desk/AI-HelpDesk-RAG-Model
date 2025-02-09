from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import os
import asyncio
from urllib.parse import urljoin, urlparse

# Function to clean and format the scraped text


def clean_data(data):
    return " ".join(data.split())

# Function to scrape data from a single page


async def scrape_page(page, base_url, url, output_file):
    try:
        # Normalize relative URL
        full_url = urljoin(base_url, url) if not url.startswith(
            "http") else url

        await page.goto(full_url, timeout=30000, wait_until="networkidle")

        # Get the rendered HTML content
        html = await page.content()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Extract text from relevant tags
        text = " ".join(tag.get_text()
                        for tag in soup.find_all(["p", "div", "span"]))

        # Extract valid links
        links = {urljoin(base_url, a["href"])
                 for a in soup.find_all("a", href=True)}
        links = {link for link in links if is_valid_url(base_url, link)}

        # Save scraped data
        if text.strip():
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(f"Source: {full_url}\n{text}\n\n")

            print(f"✅ Saved data from: {full_url}")

        return links
    except Exception as e:
        print(f"❌ Failed to scrape {url}: {e}")
        return set()

# Function to check if a URL is valid for crawling


def is_valid_url(base_url, url):
    parsed_url = urlparse(url)
    base_domain = urlparse(base_url).netloc

    # Ensure the URL is not external, not a fragment, and is a valid page
    return (parsed_url.netloc == base_domain and parsed_url.scheme in ["http", "https"]
            and parsed_url.path not in ["#", "/", ""])

# Function to crawl a website


async def crawl_website(start_url, max_depth=2, output_file=None):
    visited = set()
    to_crawl = [(start_url, 0)]

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()

        while to_crawl:
            tasks = []
            page = await context.new_page()

            # Process 10 URLs at a time
            for current_url, depth in to_crawl[:10]:
                if depth > max_depth or current_url in visited:
                    continue

                print(f"🌍 Crawling: {current_url}")
                visited.add(current_url)

                # Append coroutine to task list
                tasks.append(scrape_page(
                    page, start_url, current_url, output_file))

            to_crawl = to_crawl[10:]

            # Run scraping tasks concurrently
            results = await asyncio.gather(*tasks)

            # Add new links to the queue
            for links in results:
                for link in links:
                    if link not in visited:
                        to_crawl.append((link, depth + 1))

            await page.close()

        await browser.close()

# Main function


async def main():
    urls = ["https://www.umt.edu.pk/org/PRS.aspx"]

    output_dir = "D:/University/7th Semester/Data Mining/Project/Data"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "scraped_all_data.txt")

    # Open the output file initially
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Scraped Data:\n\n")

    # Start scraping for each URL
    for url in urls:
        print(f"🚀 Starting scraping for {url}...")
        await crawl_website(url, max_depth=2, output_file=output_file)

    print(f"✅ Scraping complete. Data saved to {output_file}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
