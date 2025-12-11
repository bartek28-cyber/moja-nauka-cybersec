import requests
import csv
import time
import os

# Funkcja pytająca o klucze przy starcie (dla bezpieczeństwa)
def get_api_keys():
    print("--- KONFIGURACJA ---")
    print("Podaj klucze API. Jeśli nie masz któregoś, wciśnij ENTER, aby pominąć.")
    vt = input("Klucz VirusTotal: ").strip()
    abuse = input("Klucz AbuseIPDB: ").strip()
    return vt, abuse

def check_abuseipdb(ip, api_key):
    if not api_key: return "N/A", "N/A"
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {'Key': api_key, 'Accept': 'application/json'}
    params = {'ipAddress': ip, 'maxAgeInDays': '90'}
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()['data']
            return data['abuseConfidenceScore'], data['totalReports']
    except Exception as e:
        print(f"Błąd AbuseIPDB: {e}")
    return "Error", "Error"

def check_virustotal(ip, api_key):
    if not api_key: return "N/A", "N/A"
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": api_key}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            stats = response.json()['data']['attributes']['last_analysis_stats']
            return stats['malicious'], stats['suspicious']
        elif response.status_code == 404:
            return 0, 0 # IP nieznane
    except Exception as e:
        print(f"Błąd VirusTotal: {e}")
    return "Error", "Error"

def main():
    vt_key, abuse_key = get_api_keys()
    
    input_file = 'ips.txt'
    output_file = 'raport_ioc.csv'

    try:
        with open(input_file, 'r') as f:
            ips = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Nie znaleziono pliku {input_file}!")
        return

    results = []
    print(f"\n[*] Analizuję {len(ips)} adresów IP...")

    for ip in ips:
        print(f" -> Sprawdzam: {ip}")
        abuse_score, abuse_reports = check_abuseipdb(ip, abuse_key)
        vt_malicious, vt_suspicious = check_virustotal(ip, vt_key)

        results.append({
            'IP Address': ip,
            'AbuseIPDB Score': abuse_score,
            'AbuseIPDB Reports': abuse_reports,
            'VT Malicious': vt_malicious,
            'VT Suspicious': vt_suspicious
        })
        
        # Opóźnienie, żeby nie zablokowali klucza (wymóg darmowej licencji)
        if vt_key: time.sleep(15)

    # Zapis do CSV (Excel)
    if results:
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"\n[SUKCES] Raport gotowy: {output_file}")

if __name__ == "__main__":
    main()