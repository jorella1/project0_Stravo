from flask import Flask, render_template, request, url_for, redirect, abort
from controller.pace_controller import get_pace_page, get_results
from controller.registration_controller import get_registration_page, register_user
from controller.pr_controller import add_new_pr, get_pr_page
from controller.account_controller import get_account_page, delete_user_account
from repo.login_dao import insert_user, select_user
from models.login_dto import Login
from controller.login_controller import *


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()

@app.route('/login/input', methods=["POST"])
def user_login():
    user = check_user_login(request.form)
    if user is not None:
        return redirect(url_for('account_page', user=user))
    else:
        abort(401)

@app.route('/registration')
def registration_page():
    return get_registration_page()

@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)

@app.route('/pace', methods=["GET"])
def pace_page():
    return get_pace_page()

@app.route('/pace/results', methods=["GET", "POST"])
def results_page():
    return get_results(request.form)

@app.route('/account/<user>', methods=["GET", "POST"])
def account_page(user):
    return get_account_page(user)

@app.route('/account/<user>/PR', methods=["GET"])
def pr_page(user):
    return get_pr_page(user)

@app.route('/account/<user>/PR/submit', methods=["GET", "POST"])
def pr_page_submit(user):
    return add_new_pr(user, request.form)

@app.route('/account/<user>/delete_account', methods=["GET", "POST"])
def delete_account(user):
    return delete_user_account(user)

if __name__== "__main__":
    app.run()