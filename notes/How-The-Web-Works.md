# How The Web Works - Protokół HTTP i DNS

Notatki z sekcji Pre-Security na TryHackMe. Zrozumienie, jak działają protokoły na Warstwie Aplikacji (L7) jest niezbędne do Web Pentestingu.

## 1. Architektura Aplikacji (HTML, CSS, JS)

Każda strona internetowa składa się z trzech kluczowych komponentów, które hakerzy atakują na różne sposoby:

1.  **HTML (HyperText Markup Language):** **Szkielet.** Odpowiada za strukturę i treść.
2.  **CSS (Cascading Style Sheets):** **Wygląd.** Odpowiada za kolor, czcionki i układ.
3.  **JavaScript (JS):** **Logika/Mięśnie.** Odpowiada za interakcję, walidację i dynamiczne zmiany na stronie.

> **Wniosek Security:** Ataki takie jak **XSS (Cross-Site Scripting)** celują bezpośrednio w podatny kod JavaScript.

## 2. DNS (Domain Name System)

DNS to "Książka Telefoniczna Internetu". Tłumaczy nazwy domen na adresy IP.

* **Proces:** Gdy wpisuję `tryhackme.com`, mój komputer pyta DNS: "Jakie IP ma ta nazwa?". Serwer DNS odpowiada: "To IP to `104.22.61.164`".
* **Ważne rekordy:**
    * **A Record:** Mapuje nazwę na adres IPv4.
    * **CNAME:** Alias — domena wskazuje na inną domenę.

> **Wniosek Security:** Projekty takie jak Pi-hole blokują reklamy/malware, wstrzykując fałszywą (zablokowaną) odpowiedź DNS.

## 3. Protokół HTTP (HyperText Transfer Protocol)

Podstawowy protokół komunikacji Klient (Przeglądarka) - Serwer. Opiera się na cyklu **Request-Response** (Żądanie-Odpowiedź).

### Metody HTTP (Czasowniki)

Najważniejsze metody, które decydują o tym, co dzieje się z danymi:

| Metoda | Funkcja | Gdzie są dane? | Zastosowanie |
| :--- | :--- | :--- | :--- |
| **GET** | Pobranie/Odczytanie danych. | W **adresie URL** (`?param=dane`). | Wyszukiwanie, linki. |
| **POST** | Wysłanie/Stworzenie nowych danych. | W **ciele żądania** (niewidoczne). | **Logowanie**, wysyłanie formularzy. |

> **Wniosek Security:** Nigdy nie należy przesyłać poufnych danych (np. hasła) metodą GET, ponieważ dane te są zapisywane w logach serwera i historii przeglądarki.

### Kody Statusu (Status Codes)

To jest "wiadomość" od serwera o wyniku operacji. Hakerzy często sprawdzają te kody:

* **2xx (Sukces):** `200 OK` (Żądanie się powiodło).
* **3xx (Przekierowanie):** `301 Moved Permanently` (Przekierowanie na inny adres).
* **4xx (Błąd Klienta):** `403 Forbidden` (Brak dostępu), `404 Not Found` (Brak strony).
* **5xx (Błąd Serwera):** `500 Internal Server Error` (Aplikacja na serwerze się "wywaliła").
