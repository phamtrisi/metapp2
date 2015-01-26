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

class Meeting_Action_Item_User(SurrogatePK, Model):
    __tablename__ = 'groups'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    meeting_action_item_id = ReferenceCol('meeting_action_items')
    user_id = ReferenceCol('users')
    
    def __init__(self, date_created, meeting_action_item, user):
        db.Model.__init__(self, date_created=date_created, meeting_action_item=meeting_action_item, user=user)

    def __repr__(self):
        return 'Meeting Action Item User'