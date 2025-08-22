# Solution: Git Exposed

This challenge simulates a common security misconfiguration where a `.git` directory is accidentally exposed on a web server. This allows attackers to download the entire source code history, including any secrets that were ever committed.

## Steps to Solve

1.  **Analyze the Leaked Files:**
    You are given two files: `leaked_git_log.txt` and `leaked_git_object.txt`.

2.  **Examine the Log File:**
    The `leaked_git_log.txt` file contains a simulated `git log` output:
    ```
    commit 8a7d6e5f... (HEAD -> main)
    Author: A Developer <dev@example.com>
    Date:   Mon Aug 25 10:00:00 2025 -0500

        Remove super secret API key

        This should not have been committed.

    commit 4b3c2d1a...
    Author: A Developer <dev@example.com>
    Date:   Mon Aug 25 09:55:00 2025 -0500

        Add super secret API key

    commit 1a2b3c4d...
    Author: A Developer <dev@example.com>
    Date:   Mon Aug 25 09:50:00 2025 -0500

        Initial commit
    ```
    The log clearly shows that a secret was added in commit `4b3c2d1a...` and then removed in commit `8a7d6e5f...`. The secret still exists in the git history.

3.  **Find the Secret:**
    In a real scenario, you would use git commands to check out the old commit or view the object directly using its hash. In this simplified version of the challenge, the `leaked_git_object.txt` file represents the contents of the file that was added in the "bad" commit.

4.  **Examine the Object File:**
    Opening `leaked_git_object.txt` reveals the contents of the file `config.php` from the old commit:
    ```
    <?php
    $db_host = "localhost";
    $db_user = "user";
    $db_pass = "password";
    $api_key = "ICIMS{G1T_1S_4_W0ND3RFUL_T00L_BUT_D4NG3R0US}";
    ?>
    ```
    The flag is the value of the `$api_key`.

## Organizer Notes

*   **Hosting:** This is a static challenge. The two files, `leaked_git_log.txt` and `leaked_git_object.txt`, should be provided to the participants.
*   **Flag:** `ICIMS{G1T_1S_4_W0ND3RFUL_T00L_BUT_D4NG3R0US}`
*   **Note:** This challenge is a simplified representation of a real `.git` exposure vulnerability. In a real case, an attacker would use tools like `git-dumper` to download the entire `.git` directory and then use standard git commands to explore the history. This challenge captures the essence of the vulnerability without requiring complex tooling.
