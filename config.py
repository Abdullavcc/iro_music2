from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "11796331")) 
API_HASH = getenv("API_HASH", "a089161b52f234bb90a6eb915551e8c0")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN" "5608081117:AAGgSewSfwqcxQqrEhMcF_qj0AH_-xSWcAI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID" "-1001772857132"))
MONGO_DB_URI = getenv("MONGO_DB_URI" "mongodb+srv://Pikku:pikachu01@cluster0.vcfnxij.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5518757491").split()))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/25a9c988ff420694be7f1.jpg")
START_IMG = getenv("START_IMG","https://te.legra.ph/file/ddcf50a83aa58a0de715b.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/iro_x_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_bot_support")
STRING_SESSION = getenv("STRING_SESSION", "AQAuUbRAR2KVF9VU61Husx2rXhLLjclQ8IpIWW6HRyRfh-OvRxKVJMJQ6Oy9BFjpk0tijFh6T5g9R-SllZjUd8loIbkkmOvlBZzUJ4Q3pUJrDum-WbWXiJHi0a1vfSjYbNR6cFVi78ZKxHfIKWydfinq6kY1KA5hdQ4R2zNP5q_r1JouOEUJxHmvk7_D_zz6UXlk5uZih0VwFjzgW77b-_jcswwQC-310ZCPYpJI7zux2sVYQqOt13QeGTQl1OWXOBlbjfugwo1Kzvf5DpT15-4kTnKN69CI58Yw70BmLgwKVmOp7SPmMyOaHeIllfFqhdnquJHWRIX7K34ogQFyMjUaAAAAAVLMFsEA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2129682352").split()))
