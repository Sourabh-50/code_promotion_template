from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import datetime
import socket

app = FastAPI(title="CodeProm Backend API")

# Add Prometheus instrumentation
Instrumentator().instrument(app).expose(app, include_in_schema=False, should_gzip=True)


# Allow the frontend to call this API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for demo purposes
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
