# The Vigenère Cipher

**Category:** Crypto
**Difficulty:** Intermediate
**Points:** 175

## Description

We've intercepted another message, and this time it's encrypted with a stronger cipher than the last one. It seems to be a Vigenère cipher.

The encrypted message is in `encrypted-message.txt`. We also managed to recover a file that might contain a clue to the key, `clue.txt`.

Can you decrypt the message and find the flag?

## Hints

*   The Vigenère cipher is a polyalphabetic substitution cipher. You'll need a key to decrypt it.
*   The key is likely a single word.
*   The `clue.txt` file seems to contain a famous quote. Maybe the author's name is the key? Or a word from the quote?
*   The flag is inside the decrypted text. The format is `ICIMS{...}`. The curly braces and `ICIMS` are not encrypted.
