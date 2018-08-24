#!/usr/bin/env python
#
# manage.py 用于启动程序以及其他的程序任务
import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from flask_debugtoolbar import DebugToolbarExtension


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# add flask debug toolbar
toolbar = DebugToolbarExtension(app)

if __name__ == '__main__':
    manager.run()
