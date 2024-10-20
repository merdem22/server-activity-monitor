# server-activity-monitor
A custom server monitor for collecting, storing, and visualizing server metrics, (CPU usage, temperature, uptime...)

## Features
- Collect CPU, memory, disk and network metrics.
- Store metrics in JSON or SQLite.
- Visualize the data in a web-app using Flask.
- Email/SMS alerts in anomalies (threshold breaches).

## Dependencies
- Python 3.x
- Flask
- lm-sensors (for temp monitoring in linux machines)

## Installation
1. Clone the repository:
   "git clone https://github.com/merdem22/server-activity-monitor.git"
2. cd server-activity-monitor
3. Install dependencies: "pip install -r requirements.txt"
4. Run the flask app: "python dashboard.py"
