from flask import Flask, request, session
from flask_session import Session
from uuid import uuid4
from icecream import ic
import tools

app = Flask(__name__)

llave = uuid4().hex

app.config.from_mapping(
    SECRET_KEY = llave,
    SESSION_TYPE = 'filesystem',
    SESSION_PERMANENT = True
)

Session(app)

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    if request.method == 'POST':
        try:
            headers = request.headers
            session['auth'] = True
            session['user'] = headers.get('user')
            session['pass'] = headers.get('pass')
            return {'status': 0, 'auth': session['auth']}
        except Exception as e:
            return {'status': 1, 'msj': str(e)}