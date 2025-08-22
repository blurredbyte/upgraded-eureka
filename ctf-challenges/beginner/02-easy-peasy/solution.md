# Solution: Easy Peasy Lemon Squeezy

This challenge introduces the concept of `robots.txt`, a file used by websites to communicate with web crawlers and other automated bots.

## Steps to Solve

1.  The challenge description mentions that developers were trying to hide files from web crawlers. This is a strong hint to look for a `robots.txt` file.
2.  The `robots.txt` file is always located at the root of a website (e.g., `http://example.com/robots.txt`).
3.  In the provided `files` directory, there is a `robots.txt` file.
4.  Open the `robots.txt` file. The content will be something like:

    ```
    User-agent: *
    Disallow: /admin/
    Disallow: /tmp/
    # The flag is ICIMS{R0B0T5_C4N7_K33P_S3CR3T5}
    ```

5.  The flag is found in a comment within the `robots.txt` file.

This challenge highlights that `robots.txt` is not a security mechanism. It's a public file that anyone can view. It's used to manage crawler traffic, not to secure sensitive information.

## Organizer Notes

*   **Hosting:** The files in the `files` directory (`index.html` and `robots.txt`) should be hosted on a web server. The `robots.txt` file must be accessible at the root of the server (e.g., `http://challenge-url/robots.txt`).
*   **Flag:** `ICIMS{R0B0T5_C4N7_K33P_S3CR3T5}`
