import time
import requests
from datetime import datetime, timezone

urls = [
    "https://anti-india-detection.onrender.com",
    "https://mca-econsult-prototype.onrender.com"
]

print("🚀 Ping script started...")

# 1 minute ke andar 6 baar (every 10 sec) ping karega
for i in range(6):
    now = datetime.now(timezone.utc).isoformat()
    print(f"\n⏰ Tick: {now}")

    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            print(f"[{url}] status={r.status_code} time={r.elapsed.total_seconds():.2f}s")
        except Exception as e:
            print(f"[{url}] error={e}")

    time.sleep(10)  # 10 second ka wait
