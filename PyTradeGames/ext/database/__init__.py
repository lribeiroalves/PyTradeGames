"""SQLAlchemy Database Factory."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(lambda exc: db.session.close())