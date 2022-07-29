from flask import Flask

from app.blueprints.views import post_blueprint
from app.paths import PATH_CONFIG, PATH_DATA_STATIC

app = Flask(__name__, static_folder=PATH_DATA_STATIC)
app.register_blueprint(post_blueprint)

app.config.from_pyfile(PATH_CONFIG)
