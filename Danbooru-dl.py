import os
import requests

# === CONFIG ===
TAGS = ""  # Replace with your desired tags (space-separated). tag limit of 2 if not using username and API key
SAVE_DIR = "" #input the desired directory for the images to be saved
LIMIT = 200  # Max per page (Danbooru's limit)
MAX_PAGES = 15  # Increase if you want more results

# Optional: Add your Danbooru login/API key for higher limits
USERNAME = ""
API_KEY = ""

# === SCRIPT ===
def get_posts(tags, page=1, limit=LIMIT):
    url = "https://danbooru.donmai.us/posts.json"
    params = {
        "tags": tags,
        "limit": limit,
        "page": page,
    }

    auth = (USERNAME, API_KEY) if USERNAME and API_KEY else None

    print(f"[INFO] Fetching page {page}...")
    response = requests.get(url, params=params, auth=auth)
    response.raise_for_status()
    return response.json()

def download_image(post):
    file_url = post.get("file_url")
    if not file_url:
        print(f"[WARN] No file_url for post {post['id']}, skipping.")
        return

    filename = f"{post['id']}_{os.path.basename(file_url)}"
    save_path = os.path.join(SAVE_DIR, filename)

    if os.path.exists(save_path):
        print(f"[SKIP] {filename} already exists.")
        return

    print(f"[DL] Downloading {filename}...")
    image_data = requests.get(file_url)
    with open(save_path, "wb") as f:
        f.write(image_data.content)

def main():
    os.makedirs(SAVE_DIR, exist_ok=True)

    for page in range(1, MAX_PAGES + 1):
        posts = get_posts(TAGS, page)
        if not posts:
            print("[DONE] No more posts found.")
            break

        for post in posts:
            download_image(post)

if __name__ == "__main__":
    main()
