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

class Meeting_Action_Item(SurrogatePK, Model):
    __tablename__ = 'meeting_action_items'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = Column(db.String(255), nullable=False)
    deadline = Column(db.DateTime, nullable=True)
    is_complete = Column(db.Integer, nullable=False, default=False)
    meeting = ReferenceCol('meetings')
    
    def __init__(self, date_created, content, deadline, is_complete, meeting):
        db.Model.__init__(self, date_created=date_created, content=content, deadline=deadline, is_complete=is_complete, meeting=meeting)

    def __repr__(self):
        return 'Meeting Action Item'