import requests as req
from icecream import ic

URL = 'http://localhost:7100'
AUTH = {'user': 'root', 'pass': '1234'}

session = req.Session()

auth = session.post(f'{URL}/auth', headers = AUTH).json()

if auth['status'] == 1:
    raise Exception(auth['msj'])

if not auth['auth']:
    raise Exception('No autorizado')

