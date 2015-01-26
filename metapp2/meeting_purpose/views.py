# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("meeting_purpose", __name__, url_prefix='/meeting_purposes',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("meeting_purpose/list.html")
