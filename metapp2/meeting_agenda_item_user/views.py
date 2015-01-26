# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("meeting_agenda_item_user", __name__, url_prefix='/meeting_agenda_item_users',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("meeting_agenda_item_user/list.html")
