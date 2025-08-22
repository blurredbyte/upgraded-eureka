# Solution: Secrets in the Code

This challenge demonstrates the risk of committing secrets to version control systems like Git, even if they are removed later.

## Steps to Solve

1.  The `files` directory contains two files: `config.py` and `config.py.old`. This simulates two different versions of the same file.
2.  First, inspect the current `config.py` file. It will contain some configuration, but no flag.
    ```python
    # config.py
    DATABASE_URL = "prod_db_url"
    API_KEY = "prod_api_key"
    ```
3.  Next, inspect the `config.py.old` file. This represents the older version of the file that was committed by mistake.
    ```python
    # config.py.old
    DATABASE_URL = "dev_db_url"
    API_KEY = "ICIMS{G1T_H1ST0RY_1S_F0R3V3R}" # TODO: Remove this before production
    ```
4.  The flag `ICIMS{G1T_H1ST0RY_1S_F0R3V3R}` is found in the older version of the file.
5.  Alternatively, you could use a `diff` tool to compare the two files, which would immediately highlight the removed line containing the flag.
    ```bash
    diff files/config.py.old files/config.py
    ```

This challenge teaches participants that once something is committed to a version control system, it should be considered compromised. The history is still accessible, and anyone who can read the repository can find the secret. The correct way to handle this is to rotate the secret (e.g., generate a new API key).

## Organizer Notes

*   **Hosting:** This is a static challenge. The two files, `config.py` and `config.py.old`, should be provided to the participants. The `.old` extension is used to simulate a previous version of the file.
*   **Flag:** `ICIMS{G1T_H1ST0RY_1S_F0R3V3R}`
