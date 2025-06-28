import os
import requests

# === GET CONFIG FROM USER ===
TAGS = input("Enter tag(s) (space-separated, e.g., 'kayoko_(blue_archive) swimsuit'): ").strip()
SAVE_DIR = input("Enter directory to save images: ").strip()
LIMIT = int(input("Enter number of posts per page (max 200): ").strip())
MAX_PAGES = int(input("Enter number of pages to fetch: ").strip())

USERNAME = input("Enter your Danbooru username (leave blank if none): ").strip()
API_KEY = input("Enter your Danbooru API key (leave blank if none): ").strip()

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
        print(f"[WARN] No file_url for post {post.get('id', 'unknown')}, skipping.")
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
