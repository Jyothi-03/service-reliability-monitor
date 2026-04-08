from typing import List
from models import Service, Status
import threading

services: List[Service] = []
statuses: List[Status] = []

lock = threading.Lock()
id_counter = 1

def add_service(url: str) -> Service:
    global id_counter
    with lock:
        s = Service(id=id_counter, url=url)
        id_counter += 1
        services.append(s)
        return s

def get_services():
    return services

def update_status(new_status):
    global statuses
    with lock:
        statuses = new_status

def get_status():
    return statuses