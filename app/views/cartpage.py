# cartpage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

cartpage = Blueprint('cartpage', __name__, template_folder='templates')

@cartpage.route('/cart')
def cart():
    # render the shopping cart template
    return render_template('cart.html', title='Shopping Cart')