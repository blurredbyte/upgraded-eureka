# Solution: The Vigenère Cipher

This challenge requires decrypting a message encrypted with a Vigenère cipher. The main difficulty is finding the key.

## Steps to Solve

1.  **Analyze the Files:**
    You are given two files: `encrypted-message.txt` and `clue.txt`.
    *   `encrypted-message.txt` contains: `THE_FLAG_IS_ICIMS{HMWIPEXIVQMKBQMLBEIC}`
    *   `clue.txt` contains: "The greatest glory in living lies not in never falling, but in rising every time we fall." - Nelson Mandela

2.  **Find the Key:**
    The challenge is to find the key for the Vigenère cipher. The `clue.txt` file is a strong hint. The quote is from Nelson Mandela. The most likely key is `MANDELA`.

3.  **Decrypt the Message:**
    We need to decrypt the ciphertext `HMWIPEXIVQMKBQMLBEIC` using the key `MANDELA`. We can use an online Vigenère cipher tool or write a script to do this.

4.  **Get the Flag:**
    Decrypting the ciphertext with the key reveals the plaintext: `VIGENERECIPHERISCLASSIC`.

    The user then needs to apply leetspeak and add underscores to this plaintext to get the flag.
    `VIGENERECIPHERISCLASSIC` -> `V1G3N3R3_C1PH3R_1S_CL4SS1C`.
    The final flag is `ICIMS{V1G3N3R3_C1PH3R_1S_CL4SS1C}`.

## Organizer Notes

*   **Hosting:** This is a static challenge. The two files, `encrypted-message.txt` and `clue.txt`, should be provided to the participants.
*   **Flag:** `ICIMS{V1G3N3R3_C1PH3R_1S_CL4SS1C}`
*   **Key:** `MANDELA`
*   **Note:** The Vigenère cipher is applied to the plaintext `VIGENERECIPHERISCLASSIC`. The user must first decrypt the message and then convert the result to leetspeak to form the final flag. This adds a small extra step to the challenge.
