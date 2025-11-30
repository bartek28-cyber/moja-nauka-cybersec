# Network Fundamentals - Kluczowe wnioski

Moje notatki z nauki fundamentów sieci, modelu OSI i protokołów w kontekście cyberbezpieczeństwa.

## 1. Architektura i Urządzenia

* **Star Topology (Gwiazda):** Standard w dzisiejszych sieciach. Wszystkie urządzenia są podpięte do punktu centralnego.
* **Switch:** Łączy urządzenia ze sobą w **Sieć Lokalną (LAN)**. Pozwala im "rozmawiać" między sobą (np. komputer z drukarką).
* **Router:** Brama wyjściowa. To do niego podłączasz Switcha. Dopiero **Router** łączy Waszą sieć lokalną z Internetem (WAN).

### Kluczowa Różnica: L2 vs L3 vs L4
To najważniejszy podział przy analizie ruchu sieciowego:

| Warstwa (Layer) | Kluczowy Adres | Urządzenie | Zasięg |
| :--- | :--- | :--- | :--- |
| **L2: Data Link** | **MAC Address** | Switch | **Lokalny (LAN)**. Komunikacja wewnątrz jednego pomieszczenia/biura. |
| **L3: Network** | **IP Address** | Router | **Globalny (WAN)**. Komunikacja między sieciami (Internet). |
| **L4: Transport** | **Port (TCP/UDP)** | System Operacyjny | **Aplikacja**. Kieruje dane do konkretnej usługi (np. :80 do WWW, :22 do SSH). |

> **Wniosek Security:** Atakujący wewnątrz sieci lokalnej (LAN) może komunikować się bezpośrednio z ofiarą przez L2 (MAC), omijając zabezpieczenia (Firewall/Router) działające na warstwie L3.

## 2. Enkapsulacja (Pakowanie Danych)

Proces "pakowania" danych przy wysyłaniu (np. maila):
1.  **Dane** (L7) są pakowane w **Segment** (L4 - dodanie Portów).
2.  Segment jest pakowany w **Pakiet** (L3 - dodanie IP nadawcy/odbiorcy).
3.  Pakiet jest pakowany w **Ramkę** (L2 - dodanie MAC adresu routera/odbiorcy).

*Jako analityk w Wiresharku widzę ten proces "od zewnątrz" (od Ramki do Danych).*

## 3. Podstawowe Usługi i Porty (Cheat Sheet)

Lista usług, które najczęściej widzę w logach:
* **21** - FTP (Przesył plików)
* **22** - SSH (Szyfrowany dostęp do konsoli - kluczowe dla Linuxa)
* **53** - DNS (Tłumaczenie nazw domen na IP)
* **80** - HTTP (Nieszyfrowany web)
* **443** - HTTPS (Szyfrowany web)

---

## Packets & Frames - Kluczowe mechanizmy

Analiza sposobu, w jaki dane są przesyłane i kontrolowane w sieci.

### 1. Nagłówki (Headers)
Dane są "owijane" w kolejne warstwy informacji. Kluczowe pola dla analityka SOC:
* **IP Header (L3):** Zawiera **Source IP** i **Destination IP** (Kto rozmawia z kim?).
* **TCP/UDP Header (L4):** Zawiera **Source Port** i **Destination Port** (Jaka aplikacja/usługa?).

### 2. TCP vs UDP
* **TCP (Transmission Control Protocol):** Protokół połączeniowy. Gwarantuje dostarczenie danych i ich kolejność.
    * *Zastosowanie:* WWW (HTTP/HTTPS), SSH, Transfer plików (FTP).
* **UDP (User Datagram Protocol):** Protokół bezpołączeniowy ("Fire and forget"). Szybki, ale nie gwarantuje, że pakiet dotrze.
    * *Zastosowanie:* Streaming wideo, DNS, Gry online.

### 3. TCP Three-Way Handshake (Uścisk dłoni)
Mechanizm nawiązywania stabilnego połączenia TCP.
1.  **SYN** (Synchronize) -> Klient: "Dzień dobry, chcę się połączyć".
2.  **SYN/ACK** (Synchronize/Acknowledge) -> Serwer: "Słyszę Cię, zgadzam się, otwieram port".
3.  **ACK** (Acknowledge) -> Klient: "Potwierdzam, zaczynamy transmisję".

> **Wniosek Security:** Zrozumienie tego mechanizmu jest kluczowe do analizy ataków DDoS (np. SYN Flood).

---

## Extending Your Network - Bezpieczeństwo na styku sieci

### 1. Firewall (Zapora Sieciowa)
To "ochroniarz" sieci. Decyduje, co może wejść, a co wyjść.
* **Stateless (Bezstanowy):** Sprawdza tylko pojedyncze pakiety (np. "Blokuj wszystko z IP X"). Nie pamięta kontekstu.
* **Stateful (Stanowy):** Pamięta całe rozmowy (sesje). Wie, że pakiet przychodzący jest odpowiedzią na moje wcześniejsze zapytanie, więc go wpuszcza.

### 2. Port Forwarding (Przekierowanie Portów)
Mechanizm pozwalający na dostęp do usługi wewnątrz sieci lokalnej (LAN) z publicznego Internetu.
* **Ryzyko:** Otwierając port na routerze, robimy "dziurę w murze". Jeśli usługa za tym portem ma podatności, haker wchodzi prosto do sieci domowej.

* ### Ręczne zapytania HTTP (Telnet/Netcat)
Dlaczego nie zawsze używamy przeglądarki?
* Przeglądarka ukrywa surowe nagłówki i "upiększa" odpowiedź.
* W pentestach musimy widzieć dokładnie, co serwer odsyła (wersja oprogramowania, błędy).
* Telnet pozwala wysłać surowe żądanie: `GET / HTTP/1.1` (wymaga podwójnego Entera na końcu!).


## 1. Ping (ICMP)
Służy do sprawdzania, czy host jest osiągalny.
* **Zasada:** Używa protokołu ICMP (Echo Request / Echo Reply).
* **Pułapka:** Sukces Pingu nie oznacza, że usługi (np. WWW, SSH) działają. Porażka Pingu nie oznacza, że serwer nie żyje (Firewall może blokować ICMP, ale przepuszczać TCP).

## 2. Traceroute / Tracert
Pokazuje ścieżkę pakietu przez routery (skoki/hopki) do celu.
* **Gwiazdki (* * *):** Oznaczają, że router po drodze działa (przekazuje ruch), ale jest skonfigurowany tak, aby nie odpowiadać na pakiety diagnostyczne (dla bezpieczeństwa lub wydajności).

## 3. Whois
Baza danych właścicieli domen.
* **Zastosowanie w Security:** Weryfikacja phishingu.
* **Red Flag:** Jeśli domena podszywająca się pod bank/korporację ma w polu właściciela "Privacy Protect" lub "Redacted for Privacy" zamiast nazwy firmy – to prawdopodobnie oszustwo.
