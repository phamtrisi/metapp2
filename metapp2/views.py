# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session, g)
from flask.ext.login import current_user, login_user, login_required, logout_user

from metapp2.extensions import login_manager
from metapp2.user.models import User
from metapp2.forms import LoginForm
from metapp2.user.forms import RegisterForm
from metapp2.utils import flash_errors
from metapp2.database import db
from metapp2 import app

@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))

@app.before_request
def load_app_context():
    if current_user and current_user.is_authenticated():
        g.user = current_user
    else:
        g.user = None

"""
We require that user is logged in on every pages
except for these page:
- Landing (promo)
- Contact
- About us
- Login/Register
"""

@app.route("/", methods=["GET", "POST"])
def landing():
    if g.user and g.user.is_authenticated():
        return redirect(url_for("home"))
    register_form = RegisterForm(request.form, csrf_enabled=False)
    login_form = LoginForm(request.form)
    return render_template("public/landing.html", 
                           login_form=login_form,
                           register_form=register_form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    g.user = None
    print current_user
    print g.user
    flash('You are logged out.', 'info')
    return redirect(url_for('home'))

@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User.create(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        active=True)
        flash("Thank you for registering. You can now log in.", 'success')
        return redirect(url_for('home'))
    else:
        flash_errors(form)
        return redirect(url_for('landing'))

@app.route("/login/", methods=["POST"])
def login():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(url_for("home"))
        else:
            flash_errors(form)

    return redirect(url_for("landing"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
@app.errorhandler(401)
def not_allowed(e):
    return redirect(url_for("landing"))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    if not (g.user and g.user.is_authenticated()):
        return redirect(url_for("landing"))
    return render_template("layout.html")

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     login_form = LoginForm(request.form)
#     return render_template("layout.html")
