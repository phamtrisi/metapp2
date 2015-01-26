# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("meeting_user_type", __name__, url_prefix='/meeting_user_types',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("meeting_user_type/list.html")
