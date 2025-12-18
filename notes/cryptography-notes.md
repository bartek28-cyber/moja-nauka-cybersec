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
