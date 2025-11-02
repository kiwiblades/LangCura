from flask import Blueprint

bp = Blueprint("translate", __name__, url_prefix="/translate", template_folder="templates")

from . import routes