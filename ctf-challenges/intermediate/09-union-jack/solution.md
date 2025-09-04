# Solution: Union Jack

This challenge involves a Union-based SQL injection vulnerability. The goal is to extract a flag from a hidden table in the database.

## Understanding the Vulnerability

First, let's look at the source code in `app.py`. The vulnerability is in the `/search` route:

```python
@app.route('/search')
def search():
    product_id = request.args.get('id')
    db = get_db()
    # This is the vulnerable line
    cursor = db.execute("SELECT name, description FROM products WHERE id = " + product_id)
    product = cursor.fetchone()
    ...
```

The `product_id` from the user input is directly concatenated into the SQL query string. This allows an attacker to inject arbitrary SQL code. A secure implementation would use a parameterized query, like this:
`cursor.execute("SELECT name, description FROM products WHERE id = ?", (product_id,))`

## Steps to Solve

1.  **Confirm the Vulnerability:**
    You can confirm the vulnerability by entering a single quote `'` in the search input (e.g., `?id=1'`). This will likely cause a database error, proving that the input is being interpreted by the SQL server.

2.  **Find the Number of Columns:**
    To use a `UNION` statement, the `SELECT` query you add must have the same number of columns as the original query. We can find this number using `ORDER BY`. We can try different numbers until we get an error.
    *   `?id=1 ORDER BY 1` - Works.
    *   `?id=1 ORDER BY 2` - Works.
    *   `?id=1 ORDER BY 3` - Fails.
    This tells us the original query has 2 columns.

3.  **Use `UNION SELECT`:**
    Now we can use `UNION SELECT` to start extracting data. We need to select 2 columns of a compatible data type.
    *   `?id=1' UNION SELECT 1,2 --`
    This should return a result, with `1` and `2` displayed on the page. The `--` is a comment in SQL, used to ignore the rest of the original query.

4.  **Find Table Names:**
    Since this is an SQLite database (as hinted in the `README` and seen in `app.py`), we can query the `sqlite_master` table to list all tables in the database.
    *   `?id=1' UNION SELECT name, sql FROM sqlite_master --`
    This might not work if the column types are not compatible. Let's try to get just the table name.
    *   `?id=1' UNION SELECT name, type FROM sqlite_master WHERE type='table' --`
    This should return a list of table names. One of them will be `flags`.

5.  **Extract the Flag:**
    Now that we know the table is named `flags`, we need to find the column names. We could guess common names like `flag` or `secret`.
    *   `?id=1' UNION SELECT flag, 1 FROM flags --`
    This query selects the `flag` column from the `flags` table. The `1` is just a placeholder for the second column.
    This will return the flag: `ICIMS{SQL_INJ3CTI0N_IS_A_T0P_VULN}`.

This challenge teaches the importance of input validation and using parameterized queries to prevent SQL injection, one of the most common and dangerous web vulnerabilities.

## Organizer Notes

*   **Hosting:** This challenge can be run locally by following the instructions in the `README.md`. Alternatively, it can be run using Docker.
*   **Flag:** `ICIMS{SQL_INJ3CTI0N_IS_A_T0P_VULN}`
*   **Vulnerability:** The application is vulnerable to SQL injection because it uses unsafe string concatenation to build an SQL query with user-provided input.

### Docker Instructions

1.  Navigate to the `files` directory for this challenge.
2.  Build the Docker image:
    ```bash
    docker build -t union-jack-challenge .
    ```
3.  Run the challenge:
    ```bash
    docker run -p 5001:5001 union-jack-challenge
    ```
4.  The application will be accessible at `http://localhost:5001`.
