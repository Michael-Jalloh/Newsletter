from re import A
from app import app, db, create_routes
from app.models import User, Subscriber
from app.commands import init_app

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Subscriber": Subscriber}

init_app(app)

create_routes()