import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(SECRET_KEY=os.environ.get("SECRET_KEY", "shelf-dev-key"), SQLALCHEMY_DATABASE_URI="sqlite:///shelf.db")
    if config:
        app.config.update(config)
    db.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Войдите, чтобы продолжить."
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from .auth import bp as auth_bp
    from .books import bp as books_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)

    from .seed import seed_command

    app.cli.add_command(seed_command)
    with app.app_context():
        db.create_all()
    return app
