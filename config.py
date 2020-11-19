class Config:
    DEBUG = True
    SECRET_KEY = "supsup"
    # mysql based configs
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "varalaxmi"
    MYSQL_DB = "tradeoff"
    SQLALCHEMY_DATABASE_URI = "mysql://root:varalaxmi@localhost/tradeoff"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
