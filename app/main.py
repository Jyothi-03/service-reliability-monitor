from fastapi import FastAPI
from models import Service
from storage import add_service, get_services, get_status
from monitor import start_monitor

app = FastAPI()

start_monitor()

@app.get("/")
def home():
    return {"message": "🚀 Python GitOps App Running"}

@app.post("/services")
def create_service(service: Service):
    return add_service(service.url)

@app.get("/services")
def list_services():
    return get_services()

@app.get("/status")
def status():
    return get_status()