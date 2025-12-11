## 🛡️ Narzędzia SOC
### IP Reputation Auto-Checker (Python)
Katalog: `/check_ip`

Prosty skrypt automatyzujący sprawdzanie reputacji adresów IP w bazach Threat Intelligence.
- **Integracje:** VirusTotal API, AbuseIPDB API.
- **Funkcja:** Pobiera listę IP z pliku `.txt` i generuje raport `.csv`.
- **Zabezpieczenia:** Klucze API podawane przy uruchomieniu (input), brak hardcodowania.
