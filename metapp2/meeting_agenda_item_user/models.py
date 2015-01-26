# -*- coding: utf-8 -*-
import datetime as dt

from flask.ext.login import UserMixin

from metapp2.extensions import bcrypt
from metapp2.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK
)

class Meeting_Agenda_Item_User(SurrogatePK, Model):
    __tablename__ = 'meeting_agenda_item_users'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    meeting_agenda_item_id = ReferenceCol('meeting_agenda_items')
    user_id = ReferenceCol('users')
    
    def __init__(self, date_created, meeting_agenda_item, user):
        db.Model.__init__(self, date_created=date_created, meeting_agenda_item=meeting_agenda_item, user=user)

    def __repr__(self):
        return 'Meeting Agenda Item User'