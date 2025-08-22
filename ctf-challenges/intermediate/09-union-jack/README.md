# Union Jack

**Category:** Web
**Difficulty:** Intermediate
**Points:** 150

## Description

We have a new e-commerce site that lets you search for products. The lead developer is very proud of the "feature" that lets you search for products by their ID.

He said, "It's super secure, I'm using a parameterized query... I think."

Can you find a way to extract information from the database that you are not supposed to see? The flag is in the `flags` table.

The web application code is provided in the `files` directory.

### Local Setup

To run this challenge locally, you will need Python and Flask.

1.  Install the dependencies:
    ```bash
    pip install -r files/requirements.txt
    ```
2.  Initialize the database:
    ```bash
    cd files
    python -c 'from app import init_db; init_db()'
    ```
3.  Run the application:
    ```bash
    python app.py
    ```

The application will be running at `http://127.0.0.1:5001`.

**Challenge Link:** [http://challenge.example.com/](http://challenge.example.com/)

## Hints

*   The challenge name "Union Jack" is a clue. What SQL operator does it refer to?
*   You need to find the number of columns in the original `SELECT` query before you can use a `UNION` statement. How can you do that? (Hint: `ORDER BY`)
*   The application is written in Python using Flask and SQLite. The source code might give you some clues about the database schema.
*   You are looking for a table named `flags`. What would you select from it? Probably a column named `flag`.
