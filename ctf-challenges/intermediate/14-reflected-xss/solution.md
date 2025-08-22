# Solution: Reflected XSS

This challenge demonstrates a Reflected Cross-Site Scripting (XSS) vulnerability. The application takes user input from a search query and includes it in the response page without proper sanitization, allowing an attacker to inject and execute malicious JavaScript in the user's browser.

## Understanding the Vulnerability

The vulnerability is in the `app.py` file, in the `/search` route:

```python
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # The 'query' is directly embedded in the HTML without escaping.
    return f"<h1>Search Results</h1><p>You searched for: {query}</p>"
```

The `query` parameter is taken from the URL and inserted directly into the HTML response. An attacker can craft a URL with a malicious script in the `q` parameter. When a victim clicks this URL, the script will execute in their browser.

A secure implementation would use a templating engine that performs context-aware escaping (like Jinja2, which Flask uses by default, but was not used here for simplicity), or manually escape the user input using a library function like `escape()` from `markupsafe` (which is a Flask dependency).

## Steps to Solve

1.  **Identify the Reflection:**
    Navigate to the search page and enter a simple search term like "hello". The page will display "You searched for: hello". This confirms that the input is being reflected on the page.

2.  **Test for HTML Injection:**
    Try entering simple HTML tags as the search query, like `<b>test</b>`. If the word "test" appears in bold, the application is rendering the injected HTML.

3.  **Craft the XSS Payload:**
    The goal is to execute JavaScript. The most common payload for this is the `<script>` tag.
    *   Payload: `<script>alert('XSS')</script>`
    *   URL: `http://127.0.0.1:5004/search?q=<script>alert('XSS')</script>`

4.  **Execute the Payload:**
    When you visit the crafted URL, the browser will render the HTML, encounter the `<script>` tag, and execute the JavaScript inside it. This will cause an alert box to pop up with the message "XSS".

5.  **Submit the Flag:**
    The challenge `README` states that successfully triggering the alert means you have solved the challenge, and provides the flag to claim the points.
    The flag is `ICIMS{XSS_1S_3V3RYWH3R3}`.

## Organizer Notes

*   **Hosting:** To run this challenge, navigate to the `files` directory and run `python app.py`. The application requires Flask. Ensure dependencies are installed using `pip install -r requirements.txt`. The app will run on `http://127.0.0.1:5004`.
*   **Flag:** `ICIMS{XSS_1S_3V3RYWH3R3}`
*   **Vulnerability:** The application is vulnerable to Reflected XSS because it includes unescaped user input in the HTML response. This is a classic example of a reflected XSS vulnerability. The challenge is designed to be simple, with no filters to bypass.
