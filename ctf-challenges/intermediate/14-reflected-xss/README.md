# Reflected XSS

**Category:** Web
**Difficulty:** Intermediate
**Points:** 200

## Description

We have a new search page on our website. It's designed to be helpful by showing you what you searched for.

Can you find a way to make this page execute arbitrary JavaScript? The goal is to create a popup alert in the browser. The flag is not in the alert, but successfully creating the alert is the solution to the challenge. The flag is for you to prove you did it.

The web application code is provided in the `files` directory.

### Local Setup

To run this challenge locally, you will need Python and Flask.

1.  Install the dependencies:
    ```bash
    pip install -r files/requirements.txt
    ```
2.  Run the application:
    ```bash
    cd files
    python app.py
    ```

The application will be running at `http://127.0.0.1:5004`.

**Challenge Link:** [http://challenge.example.com/](http://challenge.example.com/)

## Hints

*   The search page reflects your search query back to you.
*   What happens if you search for HTML tags, like `<h1>`?
*   To execute JavaScript, you need a `<script>` tag.
*   A simple payload to test for XSS is `<script>alert(1)</script>`.
*   The flag for this challenge is `ICIMS{XSS_1S_3V3RYWH3R3}`. You don't need the XSS to find the flag, but you need to find the XSS to "solve" the challenge. This is a knowledge-based challenge. The flag is your reward for learning how to do it.
