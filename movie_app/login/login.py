from flask import Blueprint, render_template, request

login_blueprint = Blueprint(
    'login_bp', __name__)


@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')
