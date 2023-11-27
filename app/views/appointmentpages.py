# appointmentpage.py
from flask import Blueprint, render_template, request
from jinja2 import TemplateNotFound

appointmentpages = Blueprint('appointmentpages', __name__, template_folder='../templates')

@appointmentpages.route("/appointment", methods=["GET", "POST"])
def appointment():
    # If the request method is POST, get the form data and redirect to the confirmation page
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("time")
        # You can add your own logic to save the appointment data here
        return redirect(url_for("confirmation", name=name, date=date, time=time))
    # If the request method is GET, render the appointment.html template
    return render_template("appointment.html", title='Create Appointment')

@appointmentpages.route("/appointment/confirmation/<name>/<date>/<time>")
def confirmation(name, date, time):
    # Render the confirmation.html template with the name, date, and time variables
    return render_template("confirmation.html", name=name, date=date, time=time, title='Confirmation')

if __name__ == '__main__':
    app.run(debug=True)