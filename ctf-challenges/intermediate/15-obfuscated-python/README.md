# Obfuscated Python

**Category:** Reverse Engineering
**Difficulty:** Intermediate
**Points:** 200

## Description

One of our developers thought it would be a good idea to "secure" a Python script by obfuscating it. We're not so sure it's secure.

Can you reverse engineer this script and find the flag?

The script is in the `files` directory. You can run it with `python script.py`.

## Hints

*   The script is still a Python script, even if it looks like garbage.
*   Try to clean up the code and understand what it's doing, step by step.
*   The script seems to be building a string and then comparing it to your input.
*   There are some `exec` and `base64` calls. What are they doing?
*   You don't necessarily have to understand every single line of the obfuscated code. Sometimes you can find a shortcut to the answer. Can you just print the value of the secret variable right before the comparison?
