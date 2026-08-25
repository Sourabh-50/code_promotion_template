from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Gauge
import datetime
import socket
import psutil
import threading
import time

app = FastAPI(title="CodeProm Backend API")

# Custom System Metrics for Grafana
SYSTEM_CPU = Gauge("system_cpu_usage_percent", "System CPU Usage Percentage")
SYSTEM_MEM = Gauge("system_memory_usage_percent", "System Memory Usage Percentage")

def update_system_metrics():
    while True:
        SYSTEM_CPU.set(psutil.cpu_percent(interval=1))
        SYSTEM_MEM.set(psutil.virtual_memory().percent)
        time.sleep(2)

# Start background thread to update hardware metrics
threading.Thread(target=update_system_metrics, daemon=True).start()

# Add Prometheus instrumentation
Instrumentator().instrument(app).expose(app, include_in_schema=False, should_gzip=True)

# Allow the frontend to call this API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
def get_status():
    return {
        "service": "CodeProm Core API",
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "host": socket.gethostname(),
        "database_connected": True,
        "active_connections": 42
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
