from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:root@localhost/flask_migrate"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    return app
