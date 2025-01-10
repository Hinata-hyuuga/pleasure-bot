# in this file we only create and save variabes
#variables we will use later in differ files

from os import environ


API_ID = 10911953
API_HASH = "dc093cf9f1d3b3a6c9f1e5acda7b9647"

BOT_TOKEN = environ.get("BOT_TOKEN", "7408540972:AAE3bhj9Hfh9wUxI8_iVimXMTkf5cnEjYn8")
ENDPOINT = environ.get("ENDPOINT", "")
PORT = environ.get("PORT", 8080)
HOST = environ.get("HOST", "cloud")
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")

LogsChannel = -1002308935879
CONTACT_URL = "https://t.me/Maid_Robot?start="
FORCE_SUB = ""