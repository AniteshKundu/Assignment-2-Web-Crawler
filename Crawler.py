import requests
from bs4 import BeautifulSoup
import csv

def get_search_urls(primary_category, secondary_category, geography, date_range):
    # Using Google search as an example
    query = f"{primary_category} {secondary_category} {geography} {date_range}"
    search_url = f"https://www.google.com/search?q={query}"
    return [search_url]

def crawl_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract URLs from search results (Google specific parsing)
        urls = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
        return urls
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return []

def save_to_csv(data, filename='output.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Primary Category', 'Secondary Category', 'Geography', 'Date Range'])
        for row in data:
            writer.writerow(row)

def get_user_input():
    primary_category = input("Enter the Primary Category (e.g., Medical Journal, Blog, News): ")
    secondary_category = input("Enter the Secondary Category (e.g., Orthopedic, Gynecology): ")
    geography = input("Enter the Geography (e.g., India, US, Europe, Latin America): ")
    date_range = input("Enter the Date Range (e.g., 2022, 2022-23, Sep 22): ")
    return {
        "Primary Category": primary_category,
        "Secondary Category": secondary_category,
        "Geography": geography,
        "Date Range": date_range
    }

def web_crawler(parameters):
    primary_category = parameters.get('Primary Category')
    secondary_category = parameters.get('Secondary Category')
    geography = parameters.get('Geography')
    date_range = parameters.get('Date Range')

    search_urls = get_search_urls(primary_category, secondary_category, geography, date_range)
    all_urls = []

    for url in search_urls:
        crawled_urls = crawl_website(url)
        for crawled_url in crawled_urls:
            all_urls.append([crawled_url, primary_category, secondary_category, geography, date_range])

    save_to_csv(all_urls)

if __name__ == "__main__":
    parameters = get_user_input()
    web_crawler(parameters)