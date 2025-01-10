from pymongo.errors import DuplicateKeyError
from clients import mongo

CLI = mongo["CREDENTIALS"]
Ucli = CLI["USERS"]

def present_user(user_id: int):
    data = Ucli.find_one({'_id': int(user_id)}, {"subscription": 1})
    if data:
        subscription = data.get("subscription")
        return True, subscription
    return None, None


def add_user(user_id: int) -> str:
    try:
        Ucli.insert_one({
            '_id': int(user_id),
            'reff': 5,
            'subscription': None
        })
        return True
    except DuplicateKeyError:
        return False