# Solution: Cookie Jar

This challenge involves manipulating a cookie to gain elevated privileges and access an admin panel.

## Understanding the Vulnerability

The application uses a cookie to manage user sessions and permissions. The cookie, named `session`, is a Base64 encoded JSON object. The application decodes this cookie and checks a value in the JSON to determine if the user is an admin. Because the cookie is not cryptographically signed, a user can decode it, modify its contents, and re-encode it to change their privilege level.

## Steps to Solve

1.  **Find the Cookie:**
    Open the web application in your browser and use the developer tools (F12) to inspect the cookies. You will find a cookie named `session`.

2.  **Decode the Cookie:**
    The value of the cookie will be a string like `eyJpc0FkbWluIjogZmFsc2V9`. This looks like Base64. You can use an online decoder or a command-line tool to decode it.
    ```bash
    echo "eyJpc0FkbWluIjogZmFsc2V9" | base64 --decode
    ```
    Decoding this string reveals the following JSON object:
    ```json
    {"isAdmin": false}
    ```

3.  **Modify the Cookie:**
    To gain admin access, change the value of `isAdmin` from `false` to `true`:
    ```json
    {"isAdmin": true}
    ```

4.  **Re-encode the Cookie:**
    Now, you need to Base64 encode the modified JSON object.
    ```bash
    echo -n '{"isAdmin": true}' | base64
    ```
    This will give you the new cookie value: `eyJpc0FkbWluIjogdHJ1ZX0=`.

5.  **Replace the Cookie and Get the Flag:**
    Go back to your browser's developer tools, replace the old `session` cookie value with the new one (`eyJpc0FkbWluIjogdHJ1ZX0=`), and refresh the page. The application will now recognize you as an admin and display the flag.

## Organizer Notes

*   **Hosting:** To run this challenge, navigate to the `files` directory and run `python app.py`. The application requires Flask. Ensure dependencies are installed using `pip install -r requirements.txt`. The app will run on `http://127.0.0.1:5002`.
*   **Flag:** `ICIMS{C00K13S_SH0ULD_B3_S3CUR3}`
*   **Vulnerability:** The core vulnerability is the lack of a signature on the session cookie, allowing for client-side manipulation of privileges. A secure implementation would use a server-side session store or a signed cookie (e.g., using Flask's built-in session management with a secret key, or a JWT).
