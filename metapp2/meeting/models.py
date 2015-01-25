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
    SurrogatePK,
)

class Meeting(Model):
    __tablename__ = 'meetings'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    start_time = Column(db.DateTime, nullable=False)
    end_time = Column(db.DateTime, nullable=False)
    title = Column(db.String(255), nullable=False)
    meeting_purpose_id = db.Column(db.Integer, db.ForeignKey('meeting_purpose.id'))

    def __init__(self, date_created, start_time, end_time, title, meeting_purpose):
        db.Model.__init__(self, date_created=date_created, start_time=start_time, end_time=end_time, title=title, meeting_purpose=meeting_purpose)

    def __repr__(self):
        return 'Meeting'