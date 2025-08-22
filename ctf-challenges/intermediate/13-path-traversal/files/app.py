from flask import Flask, request, escape
import os

app = Flask(__name__)

# The flag is hidden here in a comment.
# FLAG: ICIMS{P4TH_TR4V3RS4L_1S_D4NG3R0US}

@app.route('/')
def index():
    return """
    <h1>File Viewer</h1>
    <p>Here are the available images:</p>
    <ul>
        <li><a href="/view?filename=images/image1.jpg">image1.jpg</a></li>
        <li><a href="/view?filename=images/image2.png">image2.png</a></li>
    </ul>
    <p>View the <a href="/view?filename=readme.txt">readme.txt</a></p>
    """

@app.route('/view')
def view_file():
    filename = request.args.get('filename')
    if not filename:
        return "Please provide a filename."

    # This is the vulnerable part of the code.
    # The filename is not sanitized before being used.
    file_path = os.path.join('public', filename)

    try:
        with open(file_path, 'r') as f:
            content = f.read()
        # Using escape to prevent XSS, though not the point of this challenge.
        return f"<h2>Viewing {escape(filename)}</h2><pre>{escape(content)}</pre>"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred."

def setup_challenge():
    # Create some dummy files for the challenge
    if not os.path.exists('public/images'):
        os.makedirs('public/images')
    with open('public/images/image1.jpg', 'w') as f:
        f.write('This is a dummy image file.')
    with open('public/images/image2.png', 'w') as f:
        f.write('This is another dummy image file.')
    with open('public/readme.txt', 'w') as f:
        f.write('This is the readme file. The goal is to read the main application file.')

if __name__ == '__main__':
    # Setting up the files when the app starts.
    # The app should be run from within the 'files' directory.
    setup_challenge()
    app.run(debug=True, port=5003)
