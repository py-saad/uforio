from datetime import datetime
import pytz

def transform_animal(animal):

    friends_str = animal.get("friends", "")
    animal["friends"] = [f.strip() for f in friends_str.split(",")] if isinstance(friends_str, str) else []


    born_at = animal.get("born_at")
    if isinstance(born_at, str):
        try:
            dt = datetime.strptime(born_at, "%Y-%m-%d %H:%M:%S")
            dt_utc = dt.astimezone(pytz.UTC)
            animal["born_at"] = dt_utc.isoformat()
        except ValueError:
            animal["born_at"] = None
    else:
        animal["born_at"] = None

    return animal
