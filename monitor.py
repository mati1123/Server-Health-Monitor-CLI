
import psutil



cpu_usage = psutil.cpu_percent(interval = 1)

print(f"CPU Usage: {cpu_usage}%")


memory = psutil.virtual_memory()

print(f"Memory Usage: {memory.percent} %")


disc = psutil.disk_usage('/')

print(f"Disc usage: {disc.percent} % ")


connections = psutil.net_connections(kind = 'inet')


print("Active Connections:")
for conn in connections:
    # Hoppa över tomma eller icke-intressanta anslutningar
    if conn.status == psutil.CONN_NONE:
        continue

    # Hantera tom raddr eller pid (vissa saknar det)
    laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
    raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

    print(f"Local: {laddr} → Remote: {raddr} | Status: {conn.status} |")
