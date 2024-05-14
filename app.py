from flask_caching import Cache
from datetime import date
from flask import Flask
from time import sleep

config = {
    "DEBUG": True,
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": "127.0.0.1",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_URL": "redis://127.0.0.1:6379/0",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/")
@cache.cached(timeout=40)
def ola_mundo():
    sleep(20)
    today = date.today().strftime("%d/%m/%Y")
    return f"<h1>Data atual: {today}</h1>"