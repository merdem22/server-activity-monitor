import schedule
import time
from src.ssh_handler import connect_to_server
from src.metrics import collect_metrics
from src.db_handler import log_to_db
from src.config_loader import load_servers

def monitor():
    servers = load_servers()
    for server in servers:
        client = connect_to_server(server)
        metrics = collect_metrics(client)
        log_to_db(server["host"], metrics)
        client.close()

schedule.every(5).minutes.do(monitor)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
