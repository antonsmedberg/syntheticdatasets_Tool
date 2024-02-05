from waitress import serve
from app import app  # Import your Flask app instance

if __name__ == '__main__':
    serve(app)



