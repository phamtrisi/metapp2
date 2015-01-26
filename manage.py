#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand

from metapp2.app import create_app

from metapp2.user.models import User
from metapp2.meeting.models import Meeting
from metapp2.meeting_user.models import Meeting_User
from metapp2.meeting_user_type.models import Meeting_User_Type
from metapp2.meeting_purpose.models import Meeting_Purpose
from metapp2.meeting_note.models import Meeting_Note
from metapp2.meeting_material.models import Meeting_Material
from metapp2.meeting_decision.models import Meeting_Decision
from metapp2.meeting_agenda.models import Meeting_Agenda
from metapp2.meeting_agenda_item.models import Meeting_Agenda_Item
from metapp2.meeting_agenda_item_user.models import Meeting_Agenda_Item_User
from metapp2.meeting_action_item.models import Meeting_Action_Item
from metapp2.meeting_action_item_user.models import Meeting_Action_Item_User
from metapp2.group.models import Group
from metapp2.group_user.models import Group_User

from metapp2.settings import DevConfig, ProdConfig
from metapp2.database import db
from metapp2 import app

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)

def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User, 'Meeting': Meeting, 'Meeting_Purpose': Meeting_Purpose, 'Meeting_Note': Meeting_Note, 'Meeting_Material': Meeting_Material, 'Meeting_Decision': Meeting_Decision,'Meeting_Action_Item': Meeting_Action_Item, 'Group': Group, 'Group_User': Group_User, 'Meeting_User': Meeting_User, 'Meeting_User_Type': Meeting_User_Type, 'Meeting_Action_Item_User': Meeting_Action_Item_User, 'Meeting_Agenda': Meeting_Agenda, 'Meeting_Agenda_Item': Meeting_Agenda_Item, 'Meeting_Agenda_Item_User': Meeting_Agenda_Item_User}

@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def run():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
