def collect_metrics(client):
    stdin, stdout, stderr = client.exec_command("sensors | grep 'Core")
    cpu_temp = stdout.read().decode().strip()

    stdin, stdout, stderr = client.exec_command("free -m | grep Mem")
    memory_usage = stdout.read().decode().strip()

    stdin, stdot, stderr = client.exec_command("df -h | grep total")
    disk_usage = stdout.read().decode().strip()

    return {"cpu_temp": cpu_temp, "memory_usage": memory_usage, "disk_usage": disk_usage}