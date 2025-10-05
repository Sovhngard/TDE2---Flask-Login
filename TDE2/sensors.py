from flask import Blueprint, request, render_template
from flask_login import login_required 

sensors = Blueprint("sensors", __name__, template_folder="templates")

devices = {}

@sensors.route('/remove_sensors')
@login_required
def remove_sensors():
    return render_template("remove_sensors.html", devices=devices)

@sensors.route('/del_sensor', methods=['GET', 'POST'])
@login_required
def del_sensor():
    global devices
    if request.method == 'POST':
        sensor_name = request.form['sensor_name']
    else:
        sensor_name = request.args.get('sensor_name', None)

    devices.pop(sensor_name, None)

    return render_template("sensors.html", devices=devices)

@sensors.route('/register_sensors')
@login_required
def register_sensors():
    return render_template("register_sensors.html")

@sensors.route('/add_sensors', methods=['GET', 'POST'])
@login_required
def add_sensors():
    global devices
    if request.method == 'POST':
        sensor_name = request.form['sensor_name']
        sensor_type = request.form['sensor_type']
    else:
        sensor_name = request.args.get('sensor_name', None)
        sensor_type = request.args.get('sensor_type', None)

    if sensor_name and sensor_type:
        devices[sensor_name] = sensor_type

    return render_template("sensors.html", devices=devices)

@sensors.route('/list_sensors')
@login_required
def list_sensors():
    return render_template("sensors.html", devices=devices)
