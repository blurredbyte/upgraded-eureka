from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Search Page</h1>
    <form action="/search" method="GET">
        <input type="text" name="q" placeholder="Enter your search query">
        <input type="submit" value="Search">
    </form>
    """

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # This is the vulnerable line.
    # The query parameter is reflected without any escaping.
    return f"<h1>Search Results</h1><p>You searched for: {query}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5004)
