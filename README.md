# Server Health Monitor CLI

Ett kommandoradsbaserat Python-verktyg som övervakar systemets hälsa i realtid. 
##  Funktioner

Visar CPU-användning i procent
Visar RAM-användning och diskutrymme
Visar aktiva nätverksanslutningar (lokal IP, fjärr-IP, status)
Hanterar saknade värden (t.ex. `N/A` för fjärradresser)
kriven med tydlig, lättförståelig Python-kod med `psutil`

## Exempel på output
CPU Usage: 3.2%
Memory Usage: 54.7%
Disc Usage: 19.3%

Active Connections:
Local: 127.0.0.1:631 → Remote: N/A | Status: LISTEN
Local: 192.168.1.5:53423 → Remote: 142.250.74.206:443 | Status: ESTABLISHED


##Teknik

- Språk: Python 3.x
- Bibliotek: [psutil](https://pypi.org/project/psutil/)


##Så här kör du

1. Klona projektet:
```bash
git clone https://github.com/mati1123/Server-Health-Monitor-CLI.git
cd Server-Health-Monitor-CLI

2. Skapa och aktivera en virtuell miljö (valfritt men rekommenderas):
python3 -m venv venv
source venv/bin/activate

3. Installera psutil
pip install psutil

4. Kör programmet
python3 monitor.py
