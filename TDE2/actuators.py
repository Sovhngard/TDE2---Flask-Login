from flask import Blueprint, request, render_template
from flask_login import login_required

actuators = Blueprint("actuators", __name__, template_folder="templates")

actuators_devices = {}

@actuators.route('/register_actuators')
@login_required 
def register_actuators():
    return render_template("register_actuators.html")

@actuators.route('/add_actuators', methods=['GET', 'POST'])
@login_required 
def add_actuators():
    global actuators_devices
    if request.method == 'POST':
        actuator_name = request.form['actuator_name']
        actuator_type = request.form['actuator_type']
    else:
        actuator_name = request.args.get('actuator_name', None)
        actuator_type = request.args.get('actuator_type', None)

    if actuator_name and actuator_type:
        actuators_devices[actuator_name] = actuator_type

    return render_template("actuators.html", devices=actuators_devices)

@actuators.route('/remove_actuators')
@login_required 
def remove_actuators():
    return render_template("remove_actuators.html", devices=actuators_devices)

@actuators.route('/del_actuator', methods=['GET', 'POST'])
@login_required 
def del_actuator():
    global actuators_devices
    if request.method == 'POST':
        actuator_name = request.form['actuator_name']
    else:
        actuator_name = request.args.get('actuator_name', None)

    actuators_devices.pop(actuator_name, None)

    return render_template("actuators.html", devices=actuators_devices)

@actuators.route('/list_actuators')
@login_required 
def list_actuators():
    return render_template("actuators.html", devices=actuators_devices)
