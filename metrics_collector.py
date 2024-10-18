#collects metrics using psutil
import psutil

def get_metrics():
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }