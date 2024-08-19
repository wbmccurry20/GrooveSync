from flask import Flask, redirect, request

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    @app.before_request
    def before_request():
        if request.is_secure is False:
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

    # Initialize routes
    init_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    print("Flask app initialized")
    app.run(debug=True)