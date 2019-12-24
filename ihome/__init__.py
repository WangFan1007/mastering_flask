from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()
redis_store = None

logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
filelog_handler = RotatingFileHandler('logs/log',maxBytes=1024*1024*100,backupCount=10)
filelog_handler.setFormatter(formatter)
logging.getLogger().addHandler(filelog_handler)

def create_app(config_name):
    """
    创建flaskapp应用对象
    :param config_name:str ("dev","prod")
    :return:
    """
    app = Flask(__name__)
    conf = config_map.get(config_name)
    app.config.from_object(conf)
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=conf.REDIS_HOST, port=conf.REDIS_PORT)
    Session(app)
    CSRFProtect(app)
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")
    return app
