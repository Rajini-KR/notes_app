from flask import Flask
from models import User, Note
from extensions import db
from config import config
import os


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config)

    # Initialize database
    db.init_app(app)

    # Create the instance folder if it doesn't exist
    os.makedirs(app.instance_path, exist_ok=True)

    # Register Blueprints
    try:
        from routes.auth import auth_bp
        from routes.notes import notes_bp
        from routes.api import api_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(notes_bp)
        app.register_blueprint(api_bp)

    except ImportError:
        pass

    # Home Route
    @app.route('/')
    def hello_world():
        return """
        <h1>Hello, World!</h1>
        <p>My Notes App</p>
        <p>Project setup done and database connected.</p>
        """

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)