# Email Scraper

This project is a web scraper built with Scrapy to extract email addresses from websites.

## Description

The Email Scraper is a Python-based tool that crawls through a given website and collects all email addresses it finds. It uses Scrapy, a powerful web scraping framework, to efficiently navigate through web pages and extract data.

## Features

- Crawls through all pages of a given website
- Extracts email addresses using regular expressions
- Outputs results in JSON format

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install scrapy
   ```

## Usage

To run the spider, use the following command:

```
scrapy crawl email_spider -a start_url="https://example.com" -O emails.json
```

## Project Structure

- `email_scraper/`: Main project directory
  - `spiders/`: Contains the spider code
    - `emailspider.py`: The main spider for crawling and extracting emails
  - `settings.py`: Scrapy settings for the project
  - `items.py`: Defines the data structure for scraped items
  - `pipelines.py`: Defines any data processing pipelines

## Important Notes

- Be respectful of websites' `robots.txt` files and terms of service.
- Scraping may be against some websites' policies. Always ensure you have permission to scrape a website.
- This tool is for educational purposes only. Use responsibly and ethically.

## License

[MIT License](https://opensource.org/licenses/MIT)
