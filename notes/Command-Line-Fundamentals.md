# Command Line Fundamentals - Windows & Linux

Notatki z modułu Command Line (TryHackMe). Porównanie i kluczowe komendy dla Windows CMD, PowerShell oraz Linux Shells.

## 1. Windows Command Line (CMD)
Klasyczny wiersz poleceń Windowsa. Stary, ale wciąż obecny na każdym serwerze.

### Podstawowe komendy:
* **`dir`** - Wylistuj pliki (odpowiednik `ls`).
* **`cd`** - Zmień katalog.
* **`type [plik]`** - Wyświetl zawartość pliku (odpowiednik `cat`).
* **`whoami`** - Kim jestem?
* **`hostname`** - Nazwa komputera.
* **`systeminfo`** - Szczegóły systemu (OS, wersja, patche).
* **`net user`** - Zarządzanie użytkownikami.
* **`help [komenda]`** lub **`[komenda] /?`** - Pomoc.

> **Wniosek Security:** CMD jest często wykorzystywany przez proste exploity i malware, bo jest zawsze dostępny, ale ma ograniczone możliwości w porównaniu do PowerShella.

---

## 2. Windows PowerShell
Nowoczesny, potężny terminal oparty na obiektach (.NET). Główne narzędzie administratorów i... hakerów (Living off the Land).

### Składnia (Verb-Noun):
Komendy (Cmdlety) mają strukturę **Czasownik-Rzeczownik**.
* `Get-` (Pobierz), `Set-` (Ustaw), `New-` (Stwórz), `Remove-` (Usuń).

### Kluczowe Cmdlety:
* **`Get-Help [komenda]`** - Wyświetl pomoc (Manual).
    * `Get-Help [komenda] -Examples` - Pokaż tylko przykłady użycia.
* **`Get-Command`** - Wyszukaj komendę (np. `Get-Command *process*`).
* **`Get-ChildItem`** - Wylistuj pliki (alias: `ls`, `dir`).
    * `Get-ChildItem -Hidden` - Pokaż ukryte pliki.
* **`Get-Content`** - Wyświetl plik (alias: `cat`, `type`).
* **`Get-Process`** - Pokaż procesy.

### Potęga Rury (Pipe `|`):
PowerShell przekazuje między komendami **obiekty**, a nie tylko tekst.
* `Get-Process | Sort-Object CPU` (Pobierz procesy i posortuj je jako obiekty według zużycia CPU).

---

## 3. Linux Shells (Bash)
Powłoka (Shell) to program, który interpretuje nasze komendy i przekazuje je do jądra (Kernel) systemu.

### Rodzaje powłok:
* **Bash (Bourne Again Shell):** Najpopularniejszy standard w Linuxie (Kali, Ubuntu).
* **Sh:** Stara, podstawowa powłoka.
* **Zsh:** Nowoczesna powłoka (domyślna w nowym Kali Linux), lepsze podpowiadanie i kolory.

### Elementy skryptowe (Bash Scripting):
* **Zmienne:** `imie="Bartek"`. Odwołanie: `echo $imie`.
* **Pętle:** Pozwalają automatyzować zadania (np. pingowanie całej sieci).
* **Pliki konfiguracyjne:**
    * `.bashrc` / `.zshrc`: Pliki w katalogu domowym, które konfigurują wygląd i zachowanie terminala (aliasy, historia).

> **Wniosek:** Haker rzadko widzi pulpit. Umiejętność sprawnego poruszania się między Bash a PowerShell decyduje o sukcesie ataku lub obrony.
