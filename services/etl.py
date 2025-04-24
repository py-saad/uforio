# services/etl.py

from api.client import get_animals_page, get_animal_detail, post_animals_home
from utils.transform import transform_animal

def run_etl():
    all_ids = []
    page = 1
    print("fetching the animals all id")

    while True:
        data = get_animals_page(page)
        items = data.get("items", [])
        if not items:
            break
        all_ids.extend(items)

        if page >= data.get("total_pages", 0):
        # if page == 5:
            break
        page += 1

    print(f"total ids: {len(all_ids)}")

    batch = []
    for index, animal in enumerate(all_ids, 1):
        try:
            detail = get_animal_detail(animal["id"])
            transformed = transform_animal(detail)
            batch.append(transformed)


            if len(batch) == 100 or index == len(all_ids):
                print(f"update total {len(batch)} animals...")
                post_animals_home(batch)
                batch = []
        except Exception as e:
            print(f"animal ID {animal['id']}: {e}")
