from waitress import serve
from app import app

prt = '8111'

if __name__ == "__main__":
    print('Server Started On ' + prt)
    serve(app, host='0.0.0.0', port=prt)
