# Solution: Path Traversal

This challenge involves a Path Traversal (also known as Directory Traversal) vulnerability. The application allows users to specify a filename to be read from the filesystem, but it doesn't properly sanitize the input, allowing an attacker to read files outside of the intended directory.

## Understanding the Vulnerability

The vulnerability is in the `app.py` file:

```python
@app.route('/view')
def view_file():
    filename = request.args.get('filename')
    if not filename:
        return "Please provide a filename."

    # Vulnerable code: filename is not sanitized
    file_path = os.path.join('public', filename)

    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
```

The application takes a `filename` from the user and joins it with the `public` directory. However, if the `filename` contains `../` sequences, it can be used to navigate up the directory tree. For example, if a user provides `../app.py` as the filename, `os.path.join('public', '../app.py')` will resolve to `app.py`, allowing the user to read the source code.

A secure implementation would sanitize the input, for example by using `os.path.abspath` and checking if the resolved path is still within the intended directory.

## Steps to Solve

1.  **Explore the Application:**
    The application allows you to view files like `?filename=image1.jpg`. The `README` mentions that the flag is in `app.py`.

2.  **Attempt Path Traversal:**
    To read `app.py`, we need to traverse out of the `public` directory. We can do this with `../`.
    The path we want to construct is `public/../app.py`, which simplifies to `app.py`.

3.  **Form the Payload:**
    The payload for the `filename` parameter will be `../app.py`.
    The full URL will be `http://127.0.0.1:5003/view?filename=../app.py`.

4.  **Get the Flag:**
    Making a request to this URL will return the contents of `app.py`. The flag is hidden in a comment in the code:
    ```python
    # The flag is ICIMS{P4TH_TR4V3RS4L_1S_D4NG3R0US}
    ```

5.  **URL Encoding (If Needed):**
    Some browsers or web servers might block `../`. In such cases, URL encoding the payload can bypass filters. `../` becomes `%2E%2E%2F`.
    The URL would be: `http://127.0.0.1:5003/view?filename=%2E%2E%2Fapp.py`

## Organizer Notes

*   **Hosting:** To run this challenge, navigate to the `files` directory and run `python app.py`. The application requires Flask. Ensure dependencies are installed using `pip install -r requirements.txt`. The app will run on `http://127.0.0.1:5003`.
*   **Flag:** `ICIMS{P4TH_TR4V3RS4L_1S_D4NG3R0US}`
*   **Vulnerability:** The application is vulnerable to Path Traversal because it doesn't sanitize user input for directory traversal sequences (`../`).
