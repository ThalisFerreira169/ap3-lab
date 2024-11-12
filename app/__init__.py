from flask import Flask
from .routes import main_bp

def create_app():
  app = Flask(__name__)
  app.config.from_object('instance.config.Config')

  app.register_blueprint(main_bp)

  return app
