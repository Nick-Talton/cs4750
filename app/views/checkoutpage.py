# checkoutpage.py
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

checkoutpage = Blueprint('checkoutpage', __name__, template_folder='templates')

@checkoutpage.route("/checkout")
# def profile(username):
def checkout():
    # Render the profile.html template with the username variable
    # return render_template("profile.html", title='Profile', username=username)
    return render_template("checkout.html", title='Checkout')

