# Solution: Obfuscated Python

This challenge requires deobfuscating a Python script to find a hidden flag. The script uses several common obfuscation techniques to make it difficult to read.

## Understanding the Obfuscation

Let's look at the script (`script.py`):

```python
import base64

def check(p):
    # Some useless code
    for i in range(10):
        if i % 2 == 0:
            pass

    # The real check
    s = base64.b64decode("SUNJTVN7RDNCRlU1QzRUMTBONF8xNV9GVU59").decode('utf-8')
    if p == s:
        print("Correct!")
    else:
        print("Wrong!")

var1 = "check(input('Enter the password: '))"
var2 = "v" + "a" + "r" + "1"

exec(eval(var2))
```

The script does the following:
1.  Defines a function `check(p)` that takes a password `p`.
2.  Inside `check`, it decodes a Base64 string and stores it in the variable `s`. This is the correct password.
3.  It compares the user's input `p` with the secret password `s`.
4.  The main part of the script builds a string `var1` which is a command to be executed.
5.  It then builds the name of that variable, `var1`, and stores it in `var2`.
6.  Finally, it uses `exec(eval(var2))` to execute the command. `eval(var2)` returns the value of `var1` (the string command), and `exec` executes it.

## Steps to Solve

There are two main ways to solve this:

### Method 1: Static Analysis (Reading the code)

1.  Read the code and identify the important parts. The `check` function is clearly where the logic is.
2.  Inside `check`, you can see the Base64 string: `SUNJTVN7RDNCRlU1QzRUMTBONF8xNV9GVU59`.
3.  Decode this string to get the flag.
    ```bash
    echo "SUNJTVN7RDNCRlU1QzRUMTBONF8xNV9GVU59" | base64 --decode
    ```
    This gives the flag: `ICIMS{D3BFU5C4T10N_15_FUN}`.

### Method 2: Dynamic Analysis (Modifying the code)

1.  If you don't recognize the Base64 string, you can modify the script to reveal the secret.
2.  Instead of letting the script compare your input, you can change the `check` function to just print the secret password `s`.
    ```python
    import base64

    def check(p):
        s = base64.b64decode("SUNJTVN7RDNCRlU1QzRUMTBONF8xNV9GVU59").decode('utf-8')
        print(f"The secret password is: {s}") # <-- Added this line
        if p == s:
            print("Correct!")
        else:
            print("Wrong!")

    var1 = "check(input('Enter the password: '))"
    var2 = "v" + "a" + "r" + "1"
    exec(eval(var2))
    ```
3.  Running the modified script and entering any password will now print the flag.

## Organizer Notes

*   **Hosting:** This is a static challenge. The `script.py` file should be provided to the participants. They will need Python to run it.
*   **Flag:** `ICIMS{D3BFU5C4T10N_15_FUN}`
*   **Obfuscation Techniques Used:** Base64 encoding, `exec`, `eval`, and useless code to distract the participant. This challenge teaches basic static and dynamic analysis of obfuscated scripts.
