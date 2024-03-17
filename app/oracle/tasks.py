import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def is_valid_uri(uri: str) -> bool:
    try:
        result = urlparse(uri)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def process_verify_image(url: str):
    if not is_valid_uri(url):
        return {"status": 400, "error": "Invalid URL"}

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        meta_tag = soup.find("meta", property="og:description")
        if meta_tag:
            content = meta_tag.get("content", "")
            likes_comments = content.split(" - ")[0]
            likes, comments = likes_comments.split(", ")
            likes = int(likes.split(" ")[0])
            comments = int(comments.split(" ")[0])
            return {"status": 200, "likes": likes, "comments": comments}
    return {"status": response.status_code, "error": "Failed to process image"}
