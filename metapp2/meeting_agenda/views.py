# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("meeting_agenda", __name__, url_prefix='/meeting_agendas',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("meeting_agenda/list.html")
