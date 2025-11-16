

 Konfiguracja Laboratorium 

Stworzyłem swoje pierwsze izolowane laboratorium do nauki cyberbezpieczeństwa.

### 1. Maszyny Wirtualne

* **Atakujący (Miecz):** Kali Linux
    * **IP:** `192.168.10.10`
* **Ofiara (Tarcza):** Metasploitable 2
    * **IP:** `192.168.10.11`

### 2. Konfiguracja Sieci

* **Wirtualizator:** VirtualBox
* **Typ Sieci:** "Sieć wewnętrzna" (Internal Network)
* **Nazwa Sieci:** `lab-soc`
* **Rezultat:** Maszyny są w pełni odizolowane od mojej sieci domowej i internetu. Widzą tylko siebie nawzajem.

### 3. Pierwszy Test (Red Team vs Blue Team)

1.  **Atak (Red Team):** Przeprowadziłem skanowanie portów z Kali na Metasploitable za pomocą komendy:
    `nmap -sV 192.168.10.11`
2.  **Obrona (Blue Team):** W tym samym czasie uruchomiłem `Wireshark` na Kali, aby monitorować sieć.
3.  **Wniosek:** Zarejestrowałem tysiące pakietów TCP, co jest wyraźnym dowodem (sygnaturą) skanowania portów. To jest dokładnie to, czego szukałbym jako Analityk SOC.
