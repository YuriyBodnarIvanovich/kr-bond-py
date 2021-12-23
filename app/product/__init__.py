from flask import Blueprint

product_bp = Blueprint('product_bp_in', __name__, template_folder="templates/product")

from . import view