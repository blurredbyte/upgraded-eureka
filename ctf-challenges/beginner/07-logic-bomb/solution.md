# Solution: Logic Bomb

This challenge is about finding a logic flaw in a simple Python script.

## Steps to Solve

1.  The `files` directory contains a Python script `login.py`. Let's examine the code:
    ```python
    import random

    def login():
        # A very secure, randomly generated password.
        # It's a number between 1 and 1,000,000.
        password = random.randint(1, 1000000)

        try:
            user_input = int(input("Enter the password (it's a number): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # A "clever" way to check the password without using ==
        if not (user_input - password):
             print("Login successful!")
             print("Here is your flag: ICIMS{L0G1C_FL4W5_C4N_B3_D4NG3R0US}")
        else:
             print("Login failed. Incorrect password.")

    if __name__ == "__main__":
        login()
    ```
2.  The script generates a random number between 1 and 1,000,000 and asks the user to enter it.
3.  The password check is `if not (user_input - password):`. This is equivalent to `if (user_input - password) == 0:`, which is the same as `if user_input == password:`.
4.  However, the `random.randint(1, 1000000)` function will always generate a positive integer. What if the user enters something else?
5.  The `try-except` block only catches `ValueError`, so non-integer input won't work.
6.  The prompt asks for a number. Let's consider the logic. The developer is trying to be clever, but has overlooked something.
7.  Let's re-read the code. `if not (user_input - password):`. In Python, `not 0` is `True`, and `not <any other number>` is `False`. So the check is correct.
8.  Let's rethink. Is there another way to interpret the code? Maybe there is a mistake in my initial assessment of the `login.py` script. Let me rewrite the script to have an actual vulnerability.

Let's change the vulnerability. The classic "enter a blank password" doesn't work here because of `int()`.
What if the logic was flawed in a different way?

Let's rewrite `login.py` to have a more interesting flaw.
```python
# A better login.py with a flaw
import random

def login():
    # It's a number between 1 and 1,000,000.
    password = random.randint(1, 1000000)

    # The developer added a "backdoor" for testing, but forgot to remove it.
    # The backdoor is any number less than 0.

    try:
        user_input = int(input("Enter the password (it's a number): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if user_input == password or user_input < 0:
        print("Login successful!")
        print("Here is your flag: ICIMS{L0G1C_FL4W5_C4N_B3_D4NG3R0US}")
    else:
        print("Login failed. Incorrect password.")

if __name__ == "__main__":
    login()
```
This is a much clearer beginner-friendly logic flaw. The developer left a backdoor.

Now, let's rewrite the solution based on this new `login.py`.

# Solution: Logic Bomb

This challenge is about finding a logic flaw in a simple Python script.

## Steps to Solve

1.  The `files` directory contains a Python script `login.py`. Let's examine the code:
    ```python
    import random

    def login():
        # The password is a number between 1 and 1,000,000.
        password = random.randint(1, 1000000)

        try:
            user_input = int(input("Enter the password (it's a number): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # There is a logic error in this conditional check.
        if user_input == password or user_input < 0:
             print("Login successful!")
             print("Here is your flag: ICIMS{L0G1C_FL4W5_C4N_B3_D4NG3R0US}")
        else:
             print("Login failed. Incorrect password.")

    if __name__ == "__main__":
        login()
    ```
2.  The script checks for the correct password with `user_input == password`.
3.  However, there is a second condition in the `if` statement: `or user_input < 0`.
4.  This means that if the user enters any negative number, the condition will be true, and the login will be successful.
5.  To solve the challenge, run the script and enter a negative number like `-1`.
6.  The script will print the "Login successful!" message and the flag: `ICIMS{L0G1C_FL4W5_C4N_B3_D4NG3R0US}`.

This challenge teaches participants to read code carefully and look for alternative logic paths that might not be immediately obvious. In this case, a forgotten backdoor provides a simple way to bypass the security check.

## Organizer Notes

*   **Hosting:** This is a static challenge. The `login.py` script should be provided to the participants. They will need to have Python installed to run it.
*   **Flag:** `ICIMS{L0G1C_FL4W5_C4N_B3_D4NG3R0US}`
*   **Note:** The vulnerability is the `or user_input < 0` condition in the `if` statement, which allows any negative number to be accepted as a valid password.
