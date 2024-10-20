import paramiko

def connect_to_server(server):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=server["host"],
        username=server["user"],
        password=server["password"]
    )
    return client