from flask import Flask, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return """
    <h1>Product Search</h1>
    <p>Search for a product by its ID. For example, ?id=1</p>
    <form action="/search" method="GET">
        <input type="text" name="id" placeholder="Enter product ID">
        <input type="submit" value="Search">
    </form>
    """

@app.route('/search')
def search():
    product_id = request.args.get('id')
    if not product_id:
        return "Please provide a product ID."

    try:
        db = get_db()
        # This is the vulnerable line.
        # It uses string concatenation to build the query, which is unsafe.
        cursor = db.execute("SELECT name, description FROM products WHERE id = " + product_id)
        product = cursor.fetchone()

        if product:
            return f"<h2>{product[0]}</h2><p>{product[1]}</p>"
        else:
            return "Product not found."
    except Exception as e:
        return f"An error occurred: {e}"

def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    # This is just for demonstration.
    # In a real CTF, this would be run by a server like Gunicorn.
    # The database should be initialized before running the app.
    # For simplicity, we assume the db is already created.
    app.run(debug=True, port=5001)
