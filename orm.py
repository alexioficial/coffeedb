from flask import Flask, request, session
from flask_session import Session
from uuid import uuid4

app = Flask(__name__)

llave = uuid4().hex

app.config.from_mapping(
    SECRET_KEY = llave,
    SESSION_TYPE = 'filesystem',
    SESSION_PERMANENT = True
)

Session(app)

@app.post('/')
def index():
    pass