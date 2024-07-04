import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24861012"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "51e254ec23e537dfd3cae9d131e95d96")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rahul:rahulkr@cluster0.szdpcp6.mongodb.net/?retryWrites=true&w=majority")
