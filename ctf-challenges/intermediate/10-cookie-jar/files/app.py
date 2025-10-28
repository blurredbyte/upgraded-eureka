from flask import Flask, request, make_response, render_template_string
import base64
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Check if the user is an admin
    session_cookie = request.cookies.get('session')
    is_admin = False
    if session_cookie:
        try:
            decoded_cookie = base64.b64decode(session_cookie).decode('utf-8')
            session_data = json.loads(decoded_cookie)
            if session_data.get('isAdmin'):
                is_admin = True
        except Exception:
            # Invalid cookie, treat as non-admin
            pass

    if is_admin:
        # User is an admin, show the flag
        template = """
        <h1>Admin Panel</h1>
        <p>Welcome, admin! Here is your flag:</p>
        <p><b>ICIMS{C00K13S_SH0ULD_B3_S3CUR3}</b></p>
        """
    else:
        # User is not an admin, show a normal page
        template = """
        <h1>Welcome to our website!</h1>
        <p>This is a normal page for regular users.</p>
        <p>Only admins can see the secret flag.</p>
        """

    resp = make_response(render_template_string(template))

    # Set a default cookie if one doesn't exist
    if not session_cookie:
        default_session = {"isAdmin": False}
        encoded_session = base64.b64encode(json.dumps(default_session).encode('utf-8')).decode('utf-8')
        resp.set_cookie('session', encoded_session)

    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5002)
