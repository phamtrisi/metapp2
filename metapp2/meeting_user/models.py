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

class Meeting_User(SurrogatePK, Model):
    __tablename__ = 'meeting_users'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    meeting_id = ReferenceCol('meetings')
    user_type_id = ReferenceCol('meeting_user_types')
    user_id = ReferenceCol('users')
    
    def __init__(self, date_created, meeting, user_type, user):
        db.Model.__init__(self, date_created=date_created, meeting=meeting, user_type=user_type, user=user)

    def __repr__(self):
        return 'Meeting User'