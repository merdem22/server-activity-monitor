#collects metrics using psutil
import psutil
import subprocess

def get_temperature():
    try:
        result = subprocess.run(
            ["sensors"], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error fetching temperature: {e}"

        


def get_metrics():
    #cpu usage
    cpu_usage = psutil.cpu_percent(interval=1)
    #memory usage
    memory_info = psutil.virtual_memory()
    #disk usage
    disk_info = psutil.disk_usage('/')
    #network stats
    newtork_info = psutil.net_if_stats()
    
    #construct the metrics data
    metrics_data = {
        "cpu_usage" : cpu_usage,
        "memory_usage" : {
            "total" : memory_info.total,
            "used" : memory_info.used,
            "free" : memory_info.free,
            "percent" : memory_info.percent
        },
        "disk_usage" : {
            "total" : disk_info.total,
            "used" : disk_info.used,
            "free" : disk_info.free,
            "percent" : disk_info.percent
        },
        "network_info" : newtork_info,
        "temperature" : get_temperature()
    }

    return metrics_data
    