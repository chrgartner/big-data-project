import requests
import boto3
import gzip
import os
from datetime import datetime
from botocore.exceptions import NoCredentialsError

# ==========================================================
# CONFIG
# ==========================================================

BUCKET_NAME = "bigdata-mapping-ai-project"
REGION = "eu-central-1"
BASE_PATH = "./data-sourcing/commoncrawl/"

CC_INDEX_URL = "https://index.commoncrawl.org/collinfo.json"

s3 = boto3.client("s3", region_name=REGION)

# ==========================================================

def fetch_latest_crawl():
    print("Fetching Common Crawl metadata...")

    response = requests.get(CC_INDEX_URL)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    print("asd")
    print(response.content)
    print(response.text)

fetch_latest_crawl()

#     crawls = response.json()
#     latest = sorted(crawls, key=lambda x: x["id"], reverse=True)[0]

#     print(f"Latest crawl: {latest['id']}")

#     return latest["cdx-api"], latest["id"]

# # ==========================================================

# def fetch_file_list(crawl_id, file_type="wet"):
#     """
#     file_type options: 'warc', 'wet', 'wat'
#     """

#     print(f"Fetching {file_type.upper()} file list for {crawl_id}...")

#     base_url = f"https://data.commoncrawl.org/crawl-data/{crawl_id}/"
#     index_list_url = base_url + f"{file_type}.paths.gz"

#     response = requests.get(index_list_url)
#     if response.status_code != 200:
#         print("Could not fetch file list.")
#         return []

#     paths = gzip.decompress(response.content).decode("utf-8").strip().split("\n")

#     print(f"Found {len(paths)} {file_type.upper()} files.")

#     return [base_url + p for p in paths]

# # ==========================================================

# def download_cc_file(url):
#     filename = BASE_PATH + url.split("/")[-1]

#     print(f"Downloading {url}...")

#     response = requests.get(url, stream=True)
#     if response.status_code != 200:
#         print(f"Error downloading file: {response.status_code}")
#         return None

#     with open(filename, "wb") as f:
#         for chunk in response.iter_content(chunk_size=1024 * 1024):
#             if chunk:
#                 f.write(chunk)

#     print(f"Saved to {filename}")
#     return filename

# # ==========================================================

# def upload_to_S3(filename, crawl_id):
#     print(f"Uploading {filename} to S3 bucket {BUCKET_NAME}...")

#     key = f"commoncrawl/{crawl_id}/{os.path.basename(filename)}"

#     try:
#         s3.upload_file(filename, BUCKET_NAME, key)
#     except FileNotFoundError:
#         print("Local file not found.")
#         return
#     except NoCredentialsError:
#         print("No AWS credentials found.")
#         return
#     except Exception as e:
#         print(f"Upload error: {e}")
#         return

#     print("Upload success.")

# # ==========================================================

# def main():
#     api_url, crawl_id = fetch_latest_crawl()
#     if not api_url:
#         return

#     # Choose file type: 'wet', 'warc', or 'wat'
#     file_type = "wet"

#     file_list = fetch_file_list(crawl_id, file_type=file_type)

#     # For demo: download only the first file
#     # Remove slicing to download all
#     for url in file_list[:1]:
#         fname = download_cc_file(url)
#         if fname:
#             upload_to_S3(fname, crawl_id)

#     print("Done.")

# # ==========================================================


