# in this file we only create and save variabes
#variables we will use later in differ files

from os import environ


API_ID = 10911953
API_HASH = "dc093cf9f1d3b3a6c9f1e5acda7b9647"

BOT_TOKEN = environ.get("BOT_TOKEN", "")
ENDPOINT = environ.get("ENDPOINT", "")
PORT = environ.get("PORT", 8080)
HOST = environ.GET("HOST", "cloud")

LogsChannel = -100
CONTACT_URL = ""