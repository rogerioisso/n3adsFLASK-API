from flask import Flask
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default
