# 🔐 Cryptography: Core Concepts & Practical Security
> Dokumentacja techniczna przygotowana na podstawie modułów TryHackMe. Skupia się na fundamentach bezpieczeństwa danych w nowoczesnych systemach.

---

## 🏗️ 1. Fundamenty: Szyfrowanie Symetryczne
Szyfrowanie symetryczne to podstawa wydajnej ochrony danych. Wykorzystuje ten sam klucz do szyfrowania i deszyfrowania.

* **Mechanizm:** Dane wejściowe (Plaintext) + Klucz + Algorytm = Szyfrogram (Ciphertext).
* **Kluczowe zagadnienia:**
    * **XOR (Exclusive OR):** Logiczna operacja będąca sercem wielu szyfrów. Jeśli wykonasz XOR na danych tym samym kluczem dwukrotnie, wrócisz do oryginału.
    * **Szyfry Blokowe vs. Strumieniowe:** Zrozumienie, jak dane są dzielone na bloki (np. AES - 128 bitów) lub przetwarzane bit po bicie.
* **Zastosowanie DevSecOps:** Szyfrowanie "at rest" w bazach danych i dyskach chmurowych (np. AWS EBS).

## 🔑 2. Rewolucja Asymetryczna (Public Key Cryptography)
Rozwiązuje problem bezpiecznego przekazywania klucza. Wykorzystuje parę: **Klucz Publiczny** (do szyfrowania) i **Klucz Prywatny** (do deszyfrowania).

### RSA (Rivest-Shamir-Adleman)
* **Matematyka:** Opiera się na trudności faktoryzacji dużych liczb pierwszych.
* **Zastosowanie w SSH:** Fundament pracy DevOps. Zrozumienie, że klucz publiczny ląduje na serwerze (`authorized_keys`), a prywatny zostaje na naszej stacji, pozwala na bezpieczną automatyzację (Ansible/Terraform).
* **Podpisy Cyfrowe:** Gwarantują **Autentyczność** i **Niezaprzeczalność**. Jeśli plik jest podpisany kluczem prywatnym, każdy może sprawdzić kluczem publicznym, czy nadawca to rzeczywiście on.

## 🧬 3. Hashing: Cyfrowy Odcisk Palca
Haszowanie to proces jednokierunkowy. Nie da się "odszyfrować" hasha, można go tylko porównać.

* **Cechy dobrego hasha:** Deterministyczny, szybki w obliczeniach, odporny na kolizje (dwie różne dane nie mogą dać tego samego hasha) oraz efekt lawinowy (mała zmiana w pliku = zupełnie inny hash).
* **Algorytmy:** Przejście z MD5/SHA1 (podatne na ataki) na **SHA-256** oraz algorytmy dedykowane hasłom: **Bcrypt/Argon2**.
* **Salting (Solenie):** Dodawanie losowych danych do hasła przed haszowaniem, aby uniemożliwić ataki tablicami tęczowymi (Rainbow Tables).
* **Zastosowanie DevSecOps:** Weryfikacja integralności obrazów kontenerów Dockerowych (Docker Content Trust).

## 🔨 4. Perspektywa Ofensywna: John the Ripper
Zrozumienie jak łamie się zabezpieczenia, pozwala budować lepszą obronę.

* **Atak Słownikowy (Dictionary Attack):** Sprawdzanie milionów haseł z list (np. `rockyou.txt`) poprzez ich haszowanie i porównywanie z celem.
* **Brute-force:** Sprawdzanie wszystkich możliwych kombinacji znaków.
* **Lekcja dla DevOps:** Nigdy nie przechowuj haseł w "plain-text" w plikach konfiguracyjnych czy repozytoriach. Używaj Secret Management (np. HashiCorp Vault).

---

## 🛠️ Podsumowanie Techniczne
| Technologia | Typ | Główna Zaleta | Zastosowanie |
| :--- | :--- | :--- | :--- |
| **AES** | Symetryczny | Szybkość | Szyfrowanie plików/dysków |
| **RSA** | Asymetryczny | Bezpieczna wymiana kluczy | SSH, TLS/SSL, PGP |
| **SHA-256** | Hash | Integralność | Sumy kontrolne, Blockchain |
| **Bcrypt** | Hash + Salt | Odporność na brute-force | Przechowywanie haseł użytkowników |

> "Kryptografia to nie jest produkt, który kupujesz, to proces, który wdrażasz."
