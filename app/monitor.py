import time
import requests
from storage import get_services, update_status
from models import Status
import threading

def check(service):
    start = time.time()
    try:
        r = requests.get(service.url, timeout=5)
        status = "UP" if r.status_code == 200 else "DOWN"
    except:
        status = "DOWN"

    return Status(
        service_id=service.id,
        status=status,
        response_time=int((time.time() - start) * 1000)
    )

def monitor_loop():
    while True:
        results = []
        for s in get_services():
            results.append(check(s))

        update_status(results)
        time.sleep(10)

def start_monitor():
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()