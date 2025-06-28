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

2. Open the script and modify the CONFIG section:
```
TAGS = ""      # Replace with desired tags (space-separated)
SAVE_DIR = ""         # Directory where images will be saved
USERNAME = ""               # (Optional) Danbooru username
API_KEY = ""                # (Optional) API key for extended access
```

3. run the script
```bash
python downloader.py
```

## Notes
Each page fetches up to 200 posts.

You can adjust MAX_PAGES to control how many results you want.

If you include your Danbooru login and API key, you may bypass stricter rate limits.

Example Config
```
TAGS = "1girl rating:safe"
SAVE_DIR = "downloads"
MAX_PAGES = 5
USERNAME = "your_username"
API_KEY = "your_api_key"
```
