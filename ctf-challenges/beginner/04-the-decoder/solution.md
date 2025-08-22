# Solution: The Decoder

This challenge introduces Base64 encoding, a common method for encoding binary data into text.

## Steps to Solve

1.  The challenge provides a file `message.txt` containing an encoded string.
2.  The hints suggest that the encoding is Base64. The character set and the presence of `=` padding are strong indicators of Base64.
3.  The content of `message.txt` is `SUNJTVN7QjRTMzY0XzFTX04wVF8zTkNSWVBUMTBOfQ==`.
4.  To decode this, you can use an online Base64 decoder or a command-line tool.

    *   **Online Decoder:** Search for "Base64 decoder" and paste the string into it.
    *   **Command Line (Linux/macOS):**
        ```bash
        echo "SUNJTVN7QjRTMzY0XzFTX04wVF8zTkNSWVBUMTBOfQ==" | base64 --decode
        ```
    *   **Python:**
        ```python
        import base64
        encoded_string = "SUNJTVN7QjRTMzY0XzFTX04wVF8zTkNSWVBUMTBOfQ=="
        decoded_string = base64.b64decode(encoded_string).decode('utf-8')
        print(decoded_string)
        ```

5.  Decoding the string reveals the flag: `ICIMS{B4S364_1S_N0T_3NCRYPT10N}`.

This challenge teaches participants to recognize Base64 encoding and understand that it is not a form of encryption, but rather a way to represent data. It can be easily reversed.

## Organizer Notes

*   **Hosting:** This is a static challenge. The `message.txt` file containing the Base64 encoded string should be provided to the participants.
*   **Flag:** `ICIMS{B4S364_1S_N0T_3NCRYPT10N}`
