# Inventurwebseite

Dieses Projekt stellt eine einfache Inventur-Webseite auf Basis von Django bereit.

## Einrichtung

1. Repository klonen

```bash
git clone <repo-url>
cd inventurwebseite
```

2. Virtuelles Environment anlegen und Abhängigkeiten installieren

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Datenbank migrieren und Server starten

```bash
cd inventurprojekt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

4. Zugriff von außen (z. B. über Port-Forwarding oder DynDNS) nur für die eigene IP freigeben. Dies kann auf Router-Ebene oder per Firewall-Regel erfolgen.
