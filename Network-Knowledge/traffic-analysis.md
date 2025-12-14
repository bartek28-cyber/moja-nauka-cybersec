
# 🦈 Traffic Analysis (Wireshark & TCPdump)

Analiza ruchu sieciowego: TCPdump (CLI - zbieranie) oraz Wireshark (GUI - analiza).

## 📟 TCPdump (Terminal / CLI)
Niezbędny na serwerach bez interfejsu graficznego (tylko SSH).

| Komenda | Opis |
| :--- | :--- |
| `tcpdump -i tun0` | Nasłuch na interfejsie VPN (lub `eth0` dla sieci lokalnej). |
| `tcpdump -i eth0 -w plik.pcap` | **Zapis do pliku.** Kluczowe! Zbierasz ruch na serwerze, analizujesz u siebie. |
| `tcpdump -n` | Nie zamieniaj IP na nazwy (szybsze działanie). |
| `tcpdump -A` | Pokaż payload w ASCII (można przeczytać tekst, np. HTML). |
| `tcpdump icmp` | Filtruj tylko pakiety ping. |

## 🔬 Wireshark (Filtry - "The Big 3")
Filtry, które rozwiązują 90% zadań CTF i problemów w pracy.

| Filtr | Zastosowanie |
| :--- | :--- |
| `ip.addr == 10.10.10.5` | Pokaż cały ruch związany z tym konkretnym IP. |
| `http.request.method == "POST"` | **Szukanie haseł.** Pokazuje wysłane formularze logowania. |
| `tcp.port == 21` | Pokaż ruch FTP (często hasła lecą jawnym tekstem). |

### 💡 Pro Tip: Follow TCP Stream
Prawy przycisk myszy na pakiet -> **Follow** -> **TCP Stream**.
* Pozwala zobaczyć całą "rozmowę" między klientem a serwerem w jednym czytelnym oknie (jak czat), zamiast pojedynczych pakietów.
