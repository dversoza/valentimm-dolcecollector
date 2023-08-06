# DolceScraper

Spiders for crawling Dolce Gusto's website.

## Running the spiders

1. Create a virtual environment:

    ```bash
    python3.11 -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

3. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute the spider:

    ```bash
    scrapy crawl <spider_name> -O <output_file_name>.json
    ```

Available spiders:

- `dolcespider`

Example execution:

```bash
scrapy crawl dolcespider -O dolce.json
```
