from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)
if app.config["ENV"] == "production":
  app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
  app.config.from_object("config.DevelopmentConfig")
else:
  app.config.from_object("config.TestingConfig")

r = redis.Redis()
q = Queue(connection=r)


# from app import views
from app import adminViews
from app import error_handlers
# from app import ex1
from app import myCalc
from app import tasks
from app import views_2