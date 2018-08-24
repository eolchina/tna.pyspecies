from flask import Flask
from flask_bootstrap import Bootstrap
# from flask.ext.mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from config import config
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# 导入模型定义
from app.models import User, Role, TaxonomicTerm, IucnCategory


# 注册蓝本
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


if __name__ == '__main__':
    app.run()
