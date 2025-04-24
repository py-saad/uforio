# api/client.py

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

BASE_URL = "http://localhost:3123"

@retry(stop=stop_after_attempt(5), wait=wait_exponential(min=2, max=10),
       retry=retry_if_exception_type(requests.exceptions.RequestException))
def get_animals_page(page):
    url = f"{BASE_URL}/animals/v1/animals?page={page}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(min=2, max=10),
       retry=retry_if_exception_type(requests.exceptions.RequestException))
def get_animal_detail(animal_id):
    url = f"{BASE_URL}/animals/v1/animals/{animal_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(min=2, max=10),
       retry=retry_if_exception_type(requests.exceptions.RequestException))
def post_animals_home(payload):
    url = f"{BASE_URL}/animals/v1/home"
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()
