# 🛡️ Nmap Cheatsheet
## 🚀 Podstawowe Typy Skanowania (TCP/UDP)

| Flaga | Nazwa | Opis | Wymaga Sudo? |
| :--- | :--- | :--- | :---: |
| `-sT` | **TCP Connect Scan** | Pełny 3-way handshake. Podstawowy, wolniejszy, widoczny w logach. | ❌ |
| `-sS` | **TCP SYN Scan** | "Stealth Scan". Szybszy, nie nawiązuje pełnego połączenia. Domyślny dla roota. | ✅ |
| `-sU` | **UDP Scan** | Skanowanie portów UDP (DNS, SNMP). Bardzo powolne. | ✅ |

## 🔍 Enumeracja Usług i Systemu

| Flaga | Opis |
| :--- | :--- |
| `-sV` | **Service Version** – Wykrywa wersję usługi (np. Apache 2.4). Kluczowe! |
| `-O` | **OS Detection** – Zgaduje system operacyjny hosta. |
| `-A` | **Aggressive** – Włącza OS, wersje, skrypty i traceroute. Głośne! |

## ⚙️ Przydatne Opcje

* `-v`: Verbose (więcej info na ekranie).
* `-p-`: Skanuj wszystkie porty (1-65535).
* `-oN plik.txt`: Zapisz wynik do pliku.

## 🧠 Wnioski z nauki
* **Skanuj, nie zgaduj:** HTTP nie zawsze jest na 80, a SSH na 22.
* **Wersja > OS:** Jeśli `-O` nie działa, użyj `-sV`, żeby zidentyfikować system po wersji aplikacji.
