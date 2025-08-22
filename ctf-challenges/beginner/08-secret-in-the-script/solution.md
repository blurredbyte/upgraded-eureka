# Solution: Secret in the Script

This challenge involves finding a flag that is hardcoded in a JavaScript variable within an HTML page.

## Steps to Solve

1.  Open the `index.html` file in a web browser or a text editor.
2.  View the source code of the page. You can do this by right-clicking and selecting "View Page Source" or by using your browser's developer tools (F12).
3.  In the `<head>` section of the HTML, you will find a `<script>` tag with some JavaScript code.
    ```html
    <script>
        // Our developers love to hide secrets in the code.
        var super_secret_flag = "ICIMS{J4V4SCR1PT_1S_CL13NT_S1D3}";

        function displayMessage() {
            alert("Welcome to our page!");
        }
    </script>
    ```
4.  The flag is stored in a JavaScript variable called `super_secret_flag`.
5.  The value of this variable is `ICIMS{J4V4SCR1PT_1S_CL13NT_S1D3}`.
6.  You can also find this by opening the developer tools console in your browser and typing `super_secret_flag` to see the value of the variable.

This challenge teaches participants that any code that is sent to the client's browser (like HTML, CSS, and JavaScript) can be viewed by the user. Therefore, secrets should never be stored in client-side code.

## Organizer Notes

*   **Hosting:** The `index.html` file should be hosted on a web server.
*   **Flag:** `ICIMS{J4V4SCR1PT_1S_CL13NT_S1D3}`
*   **Vulnerability:** The flag is hardcoded in a JavaScript variable, which is visible to anyone who views the page source.
