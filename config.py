from os import environ


API_ID = 0
API_HASH = ""

BOT_TOKEN = environ.get("BOT_TOKEN", "")
ENDPOINT = environ.get("ENDPOINT", "")
PORT = environ.get("PORT", 8080)
HOST = environ.GET("HOST", "cloud")

LogsChannel = -100
CONTACT_URL = ""