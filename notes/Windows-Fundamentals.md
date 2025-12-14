# Windows Fundamentals - Kompendium

Notatki z modułu Windows Fundamentals (TryHackMe). Podstawy administracji i bezpieczeństwa systemu Windows dla analityka SOC.

## 1. Narzędzia Systemowe i Diagnostyka
Podstawowe narzędzia do sprawdzania "co się dzieje" w systemie.

* **Task Manager (`Ctrl+Shift+Esc`)**: Szybki podgląd procesów.
* **Resource Monitor (`resmon`)**: Głęboka analiza użycia CPU, Dysku i Sieci (kto łączy się z jakim IP?).
* **System Information (`msinfo32`)**: Szczegóły sprzętu, wersja BIOS, wersja systemu.
* **System Configuration (`msconfig`)**: Zarządzanie rozruchem (Boot) i usługami.
    * *Tip:* Zaznacz "Hide all Microsoft services", aby znaleźć podejrzane usługi firm trzecich.

## 2. Zarządzanie i Administracja
* **Computer Management (`compmgmt.msc`)**: Centrum dowodzenia. Dostęp do Harmonogramu zadań, Użytkowników i Dysków.
* **Local Users and Groups (`lusrmgr.msc`)**: Zarządzanie kontami użytkowników i resetowanie haseł.
* **Registry Editor (`regedit`)**: Baza danych ustawień systemu.
    * *Uwaga:* Błędna edycja rejestru może uszkodzić system. Malware często ukrywa się w kluczach `Run` / `RunOnce` w rejestrze.

## 3. Bezpieczeństwo (Windows Security)
Kluczowe mechanizmy obronne wbudowane w system.

### User Account Control (UAC)
Zabezpieczenie przed nieautoryzowanymi zmianami. Wymusza potwierdzenie (lub hasło admina) przy próbie instalacji programu lub zmiany ustawień systemowych.

### Windows Defender Firewall (`wf.msc`)
* **Inbound Rules (Reguły przychodzące):** Kontrolują ruch wchodzący DO komputera (np. blokowanie portu 80, żeby nikt nie widział naszej strony).
* **Outbound Rules (Reguły wychodzące):** Kontrolują ruch wychodzący NA ZEWNĄTRZ (np. malware próbujący połączyć się z serwerem C2 hakera).

### Windows Defender Antivirus
* **Exclusions (Wykluczenia):** Pozwala wyłączyć skanowanie konkretnych plików lub folderów (przydatne dla pentestera, aby antywirus nie usuwał narzędzi do ataku).

### BitLocker
Pełne szyfrowanie dysku. Chroni dane w przypadku fizycznej kradzieży urządzenia.
---
## 4. Active Directory (AD) - Wstęp do Korporacji

Active Directory to baza danych i zestaw usług łączących użytkowników i komputery w jedną sieć (Domenę).

### Kluczowe Różnice
* **Konto Lokalne:** Działa tylko na jednym komputerze (np. `.\phillip`).
* **Konto Domenowe:** Działa w całej firmie (np. `THM\phillip`).
    * *Wniosek:* Logując się przez RDP, zawsze muszę podać domenę (flaga `/d:THM`).

### Struktura AD (Drzewo)
* **Kontener (Containers):** Domyślne foldery (np. `Users`, `Computers`). Nie można do nich przypisywać Polityk Grupowych (GPO).
* **Jednostka Organizacyjna (OU):** Specjalne foldery (np. `Marketing`, `Serwery`), które tworzy administrator. **To tutaj nakłada się polityki bezpieczeństwa** (np. blokada USB, tapeta firmowa).

### Narzędzia Hakerskie (Linux -> Windows)
* **xfreerdp3**: Klient RDP na Linuxa.
    * Komenda: `xfreerdp3 /v:IP /u:user /p:pass /d:DOMAIN /dynamic-resolution /cert:ignore`
* **PowerShell (runas)**: Uruchamianie komend jako inny użytkownik wewnątrz systemu.
    * `runas /user:użytkownik powershell`
