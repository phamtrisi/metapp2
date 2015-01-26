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

class Meeting_Note(SurrogatePK, Model):
    __tablename__ = 'meeting_notes'
    content = Column(db.Integer, nullable=False)
    is_important = Column(db.Integer, nullable=False)
    is_question = Column(db.Integer, nullable=False)
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    meeting_id = ReferenceCol('meetings')
    user_id = ReferenceCol('users')
    
    def __init__(self, content, is_important, is_question, date_created, meeting, user):
        db.Model.__init__(self, content=content, is_important=is_important, is_question=is_question, date_created=date_created, user=user, meeting=meeting)

    def __repr__(self):
        return 'Meeting Note'