# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("group_user", __name__, url_prefix='/group_users',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("group_user/list.html")
