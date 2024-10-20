import curses
import time
from src.metrics_collector import get_metrics

def display_metrics(screen):
    #config curses
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(1000)

    while True:
        screen.clear() #clear for new data.

        #get metrics
        metrics_data = get_metrics()
        
        #display cpu usage
        screen.addstr(1, 2, "CPU Usage: {}%".format(metrics_data["cpu_usage"]))

        #display memory usage
        memory = metrics_data["memory_usage"]
        screen.addstr(2, 2, "Memory Usage: {}%".format(memory["percent"]))
        screen.addstr(3, 4, "Memory Total: {}MB".format(memory["total"] // 1024**2))
        screen.addstr(4, 4, "Memory Used: {}MB".format(memory["used"] // 1024**2))
        screen.addstr(5, 4, "Memory Free: {}MB".format(memory["free"] // 1024**2))

        #display disk usage
        disk = metrics_data["disk_usage"]
        screen.addstr(7, 2, "Disk Usage: {}%".format(disk["percent"]))
        screen.addstr(8, 4, "Disk Total: {}GB".format(disk["total"] // 1024**3))
        screen.addstr(9, 4, "Disk Used: {}GB".format(disk["used"] // 1024**3))
        screen.addstr(10, 4, "Disk Free: {}GB".format(disk["free"] // 1024**3))

        #display network interfaces
        network = metrics_data["network_info"]
        screen.addstr(12, 2, "Network Info:")
        for i, (iface, stats) in enumerate(metrics_data['network_info'].items(), start=13):
            screen.addstr(i, 4, f"{iface}: {'UP' if stats.isup else 'DOWN'}")

        # Handle user input (optional: press 'q' to quit)
        key = screen.getch()
        if key == ord('q'):
            break
        
        screen.refresh()
        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(display_metrics)


