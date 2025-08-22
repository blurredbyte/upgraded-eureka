# Path Traversal

**Category:** Developer-Friendly
**Difficulty:** Intermediate
**Points:** 200

## Description

We have a simple file viewer application that is supposed to let you view images from the `public` directory. However, we suspect there might be a vulnerability that allows you to view other files on the server.

Can you find a way to read the contents of the application's source code (`app.py`) to find a secret message? The flag is hidden in a comment in the source code.

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

The application will be running at `http://127.0.0.1:5003`.

**Challenge Link:** [http://challenge.example.com/](http://challenge.example.com/)

## Hints

*   The application lets you view files using a `filename` parameter, like `?filename=image1.jpg`.
*   What happens if you try to go "up" a directory? The `..` sequence is used for this in file systems.
*   You need to escape the `public` directory to get to the root of the application and read `app.py`.
*   You might need to use a sequence like `../../app.py`. You might need to try different numbers of `../`.
*   Web browsers sometimes block `../` in URLs. You might need to use a tool like `curl` or Burp Suite, or you can try URL encoding the characters (`.` is `%2E`, `/` is `%2F`).
