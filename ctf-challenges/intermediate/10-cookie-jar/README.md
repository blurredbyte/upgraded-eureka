# Cookie Jar

**Category:** Web
**Difficulty:** Intermediate
**Points:** 150

## Description

We have a new admin panel, but it's not quite ready for production yet. The developers have hidden it behind a feature flag, which is controlled by a cookie.

Can you find a way to access the admin panel and get the flag?

The web application code is provided in the `files` directory.

### Local Setup

To run this challenge locally, you will need Python and Flask.

1.  Install the dependencies:
    ```bash
    pip install -r files/requirements.txt
    ```
2.  Run the application:
    ```bash
    python app.py
    ```

The application will be running at `http://127.0.0.1:5002`.

**Challenge Link:** [http://challenge.example.com/](http://challenge.example.com/)

## Hints

*   Look at the cookies that are set by the website. You can use your browser's developer tools (F12) to see them.
*   There is a cookie that looks interesting. What happens if you change its value?
*   The cookie might be encoded. Try to decode it.
*   The cookie is a simple base64 encoded string. The decoded value is a JSON object. You need to change a value in the JSON object and then re-encode it.
