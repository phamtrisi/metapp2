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

class Meeting_Decision(SurrogatePK, Model):
    __tablename__ = 'meeting_decisions'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = Column(db.String(500), nullable=False)
    meeting = ReferenceCol('meetings')

    def __init__(self, date_created, content, meeting):
        db.Model.__init__(self, date_created=date_created, content=content, meeting=meeting)

    def __repr__(self):
        return 'Meeting Decision'