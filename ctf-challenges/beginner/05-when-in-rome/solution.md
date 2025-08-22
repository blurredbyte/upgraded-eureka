# Solution: When in Rome

This challenge is about the Caesar cipher, a simple substitution cipher where each letter is replaced by a letter some fixed number of positions down the alphabet.

## Steps to Solve

1.  The challenge title, "When in Rome," hints at the Caesar cipher, which is named after Julius Caesar, who used it in his private correspondence.
2.  The `encrypted-message.txt` file contains the message: `ICIMS{P43F4E_J4F_4_E0Z4A}`.
3.  The hint states that the `ICIMS{...}` part is not encrypted, so we only need to decrypt `P43F4E_J4F_4_E0Z4A`.
4.  A Caesar cipher has a key, which is the number of letters to shift. Since there are only 26 letters in the English alphabet, there are only 25 possible keys to try. This is called a brute-force attack. The numbers are not encrypted.
5.  We can use an online Caesar cipher decoder or write a simple script to try all possible shifts.
6.  The most common version of this cipher is ROT13, where the shift is 13. If we apply a shift of 13 to the encrypted text:
    *   `P` becomes `C`
    *   `F` becomes `S`
    *   `E` becomes `R`
    *   ...and so on.
7.  Decrypting `P43F4E_J4F_4_E0Z4A` with a shift of 13 on the letters gives `C43S4R_W4S_4_R0M4N`.
8.  The full flag is `ICIMS{C43S4R_W4S_4_R0M4N}`.

This challenge teaches participants about simple substitution ciphers and the concept of brute-forcing a small key space.

## Organizer Notes

*   **Hosting:** This is a static challenge. The `encrypted-message.txt` file should be provided to the participants.
*   **Flag:** `ICIMS{C43S4R_W4S_4_R0M4N}`
*   **Note:** The Caesar cipher shift used is 13 (ROT13). The `ICIMS{...}` part of the flag and the numbers are not encrypted.
