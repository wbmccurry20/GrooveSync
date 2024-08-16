from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Initialize routes
    init_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    print("Flask app initialized")
    app.run(debug=True)