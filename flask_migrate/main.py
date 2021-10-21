from app import db, migrate, create_app
from app.models.models import Users, Products

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=Users, Products=Products, migrate=migrate)
