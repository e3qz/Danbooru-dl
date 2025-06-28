# Danbooru Image Downloader

A simple Python script for downloading images from [Danbooru](https://danbooru.donmai.us) based on tag queries using the [Danbooru API](https://danbooru.donmai.us/wiki_pages/help:api).

## Features

- Fetches images using the Danbooru API
- Supports login/API key for higher request limits
- Avoids duplicate downloads
- Simple configuration for tag filtering, pagination, and save directory

## Requirements

- Python 3.7+
- `requests` library

Install requirements (if needed):

```bash
pip install requests
```

# Usage
1. Clone this repository or download Danbooru-dl.py.

2. Run the script using python
```bash
python downloader.py
```
3. Follow the prompts to enter your config

4. Once all prompts are followed, the script will download imagess following the config



## Notes
Each page fetches up to 200 posts.

You can adjust MAX_PAGES to control how many results you want.

If you include your Danbooru login and API key, you may bypass stricter rate limits.

Example Config
```
TAGS = "kayoko_(blue_archive) swimsuit"
SAVE_DIR = "downloads"
MAX_PAGES = 5
USERNAME = "your_username"
API_KEY = "your_api_key"
```
