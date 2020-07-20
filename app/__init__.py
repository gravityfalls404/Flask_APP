from flask import Flask

app = Flask(__name__)
if app.config["ENV"] == "production":
  app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
  app.config.from_object("config.DevelopmentConfig")
else:
  app.config.from_object("config.TestingConfig")




from app import views
from app import  adminViews
from app import error_handlers
from app import ex1