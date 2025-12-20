# Cryptography Basics - Cheat Sheet

## 1. Hashing vs Encryption
- **Hashing:** Jest jednokierunkowy (nie da się odwrócić). Służy do weryfikacji integralności plików. Przykład: MD5, SHA-256.
- **Encryption:** Jest dwukierunkowy (można odwrócić kluczem). Służy do ukrywania danych.

### Public Key Cryptography Basics (THM)

* **Cryptography:** Nauka o zabezpieczaniu komunikacji.
* **Cryptanalysis:** Łamanie szyfrów bez znajomości klucza.
* **Brute-Force:** Atak polegający na sprawdzaniu każdej możliwej kombinacji.
* **Dictionary Attack:** Atak z użyciem listy popularnych słów (słownika).

**Kluczowe technologie:** RSA, Diffie-Hellman, SSH Keys, Digital Signatures, OpenPGP.

> **CTF Tip:** Aby rozpoznać algorytm klucza SSH, sprawdź pierwszą linię pliku:
> `cat id_rsa` -> `-----BEGIN RSA PRIVATE KEY-----` (to jest klucz RSA).
## Hashing Basics (Hashcat)

### Rozpoznawanie hashy (Hash Identification)
| Sygnatura | Algorytm | Tryb Hashcat (-m) |
| :--- | :--- | :--- |
| `$2a$`, `$2y$` | **bcrypt** | `3200` |
| `$6$` | **SHA-512 (Unix)** | `1800` |
| `$1$` | **MD5 (Unix)** | `500` |
| `$5$` | **SHA-256 (Unix)** | `7400` |
| (64 znaki hex) | **SHA-256** | `1400` |

### Podstawowa składnia
`hashcat -m [ID_trybu] -a 0 [plik_z_hashem] [słownik]`

### Przydatne flagi
- `-a 0`: Atak słownikowy (Wordlist mode).
- `-O`: Optimized kernel (przyspiesza łamanie, ale ma limity długości hasła).
- `--show`: Wyświetla złamane hasła (odczyt z `hashcat.potfile`).
- **Słownik:** `/usr/share/wordlists/rockyou.txt`

### Przykłady (Hashing Basics Tasks)
```bash
# Bcrypt ($2a$)
hashcat -m 3200 -a 0 hash1.txt /usr/share/wordlists/rockyou.txt

# SHA2-256 (64 znaki hex)
hashcat -m 1400 -a 0 hash2.txt /usr/share/wordlists/rockyou.txt

# SHA-512 Unix ($6$)
hashcat -m 1800 -a 0 hash3.txt /usr/share/wordlists/rockyou.txt
