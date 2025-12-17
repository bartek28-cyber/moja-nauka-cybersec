# Cryptography Basics - Cheat Sheet

## 1. Hashing vs Encryption
- **Hashing:** Jest jednokierunkowy (nie da się odwrócić). Służy do weryfikacji integralności plików. Przykład: MD5, SHA-256.
- **Encryption:** Jest dwukierunkowy (można odwrócić kluczem). Służy do ukrywania danych.

## 2. Przydatne narzędzia w Linuxie
Komendy, których nauczyłem się w tym module:

### Base64 Encoding/Decoding
```bash
# Kodowanie
echo -n "Tekst" | base64

# Odkodowanie
echo -n "VGVrc3Q=" | base64 -d
