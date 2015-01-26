# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("meeting_action_item", __name__, url_prefix='/meeting_action_items',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("meeting_action_item/list.html")
