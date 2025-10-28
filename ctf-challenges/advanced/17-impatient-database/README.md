# The Impatient Database

**Category:** Web
**Difficulty:** Advanced
**Points:** 250

## Description

This login form is... strange. It doesn't tell you if your username is correct or not. It just seems to take a long time to respond if you get something wrong.

We believe there is a user in the database with the username 'admin'. Can you find the admin's password?

The flag is the admin's password, in the format `ICIMS{password}`.

The web application code is provided in the `files` directory.

### Local Setup

To run this challenge locally, you will need Python and Flask.

1.  Install the dependencies: `pip install -r files/requirements.txt`
2.  Initialize the database: `cd files; python -c 'from app import init_db; init_db()'`
3.  Run the application: `python app.py`

The application will be running at `http://127.0.0.1:5005`.

**Challenge Link:** [http://challenge.example.com/](http://challenge.example.com/)

## Hints

*   The application's response time seems to depend on the input. This is a clue for a time-based attack.
*   The application is vulnerable to Blind SQL Injection. You can't see the output of the query, but you can infer information based on the time it takes to respond.
*   You can use a subquery with a `CASE` or `IF` statement and the `sleep()` function to make the database wait for a certain amount of time if a condition is true.
*   You will likely need to write a script to automate the process of exfiltrating the password character by character.
*   You can use `substr()` or `substring()` to get one character of the password at a time.
*   You'll need to guess the characters one by one. Is the first character 'a'? 'b'? 'c'? etc. You can use ASCII values to make this easier. `ascii(substring(password, 1, 1)) > 100`.
