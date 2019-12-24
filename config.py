import redis


class Config:
    DEBUG = True
    SECRET_KEY = "jherwqjweioghwriogjwe21312"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test1:test1@localhost:3306/test1"
    SQLALCHEMY_ECHO = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 隐藏sessionid
    PERMANENT_SESSION_LIFETIME = 24 * 3600


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    pass


config_map = {
    "dev": DevConfig,
    "prod": ProdConfig
}
