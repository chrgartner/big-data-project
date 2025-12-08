import boto3
from datetime import date, datetime
import pandas as pd
from gdeltdoc import GdeltDoc, Filters
from dateutil.relativedelta import relativedelta
from botocore.exceptions import NoCredentialsError
import requests
import gzip
import os

BUCKET_NAME = "bigdata-mapping-ai-project"
REGION = "eu-central-1"
BASE_PATH = "./data-sourcing/data/"

SOURCE_URL = "http://data.gdeltproject.org/gdeltv2_cloudvision/lastupdate.txt"

gd = GdeltDoc()
s3 = boto3.client("s3", region_name=REGION)

# ==========================================================

def fetch_lastupdate():
  print(f"Fetching lastupdate information...")

  response = requests.get(SOURCE_URL)
  
  if response.status_code != 200:
    print(f"Error: {response.status_code}")
    return None
  
  print("Success")
  return fetch_csv(response)

# ==========================================================

def fetch_csv(response):
  print(f"Fetching gdelt data...")

  data = requests.get(response.text.split()[2])

  if data.status_code != 200:
    print(f"Error: {response.status_code}")
    return None
    
  print(f"Success")
  
  return write_to_file(data.content)

# ==========================================================

def write_to_file(data):
  filename = BASE_PATH + f"gdelt_{datetime.now().date()}.csv"

  print(f"Writing data to {filename}...")

  with open(filename + ".gz", "wb") as file:
    file.write(data)

  with gzip.open(filename + ".gz", 'rb') as file:
    csv = file.read()

  with open(filename, "wb") as file:
    file.write(csv)

  os.remove(filename + ".gz")

  print(f"Done")

  return filename
  
# ==========================================================

def upload_to_S3(filename):
  print(f"Uploading {filename} to {BUCKET_NAME}")

  try:
    s3.upload_file(filename, BUCKET_NAME, f"gdelt/{filename}")
  except FileNotFoundError:
    print(f"Could not find local file {filename}.")
    return
  except NoCredentialsError:
    print("No AWS credentials found. Run 'aws configure'.")
    return
  except Exception as e:
    print(f"Error: {e}")
    return
  
  print("Success")

# ==========================================================

filename = fetch_lastupdate()

print(filename)

upload_to_S3(filename)