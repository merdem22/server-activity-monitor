import sqlite3

def log_to_db(host, metrics):
    conn = sqlite3,connect("data/metrics.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS metrics_log (timestamp TEXT, host TEXT, cpu_temp TEXT, memory_usage TEXT, disk_usage TEXT)''')
    cursor.exeute("INSERT INTO metrics_log VALUES (datetime('now'), ?, ?, ?, ?)", (host, metrics["cpu_temp"], metrics["memory_usage"], metrics["disk_usage"]))
    conn.commit()
    conn.close()
