from flask import Flask, request, g, render_template_string
import sqlite3
import time

app = Flask(__name__)
DATABASE = 'database.db'

# SQLite doesn't have a sleep function, so we create a custom one.
def sleep(seconds):
    time.sleep(seconds)
    return 1

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Register the custom sleep function
        db.create_function("sleep", 1, sleep)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def index():
    return """
    <form action="/login" method="POST">
      <h1>Login</h1>
      <input type="text" name="username" placeholder="Username">
      <input type="password" name="password" placeholder="Password">
      <input type="submit" value="Login">
    </form>
    """

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Intentionally vulnerable to SQL injection
    query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'"

    try:
        db = get_db()
        cursor = db.execute(query)
        result = cursor.fetchone()

        if result:
            return "Login successful!"
        else:
            # Even on failure, we don't give a specific error.
            # This makes it a "blind" vulnerability.
            return "Login failed."
    except Exception as e:
        # In a real scenario, you wouldn't show the error to the user.
        # But for this challenge, we'll keep it simple and just return a generic message.
        return "An error occurred."

def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run(debug=False, port=5005)
