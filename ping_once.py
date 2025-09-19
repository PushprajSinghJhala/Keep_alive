import requests
import time
import logging

URLS = [
    "https://anti-india-detection.onrender.com",
    "https://mca-econsult-prototype.onrender.com"
]

TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (compatible; KeepAliveBot/1.0; +https://github.com/PushprajSinghJhala/Keep_alive)"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("ping_once")

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT})

def ping(url):
    try:
        start = time.time()
        r = session.get(url, timeout=TIMEOUT)
        elapsed = time.time() - start
        logger.info(f"[{url}] status={r.status_code} time={elapsed:.2f}s")
        return True
    except Exception as e:
        logger.error(f"[{url}] error: {e}")
        return False

def main():
    for u in URLS:
        ping(u)
        time.sleep(1)

if __name__ == "__main__":
    main()
