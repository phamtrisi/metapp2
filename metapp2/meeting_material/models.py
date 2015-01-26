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

class Meeting_Material(SurrogatePK, Model):
    __tablename__ = 'meeting_materials'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    gdrive_url = Column(db.String(500), nullable=True)
    dropbox_url = Column(db.String(500), nullable=True)
    type = Column(db.String(25), nullable=True)
    meeting_id = ReferenceCol('meetings')
    user_id = ReferenceCol('users')

    def __init__(self, date_created, gdrive_url, dropbox_url, type, meeting, user):
        db.Model.__init__(self, date_created=date_created, gdrive_url=gdrive_url, dropbox_url=dropbox_url, type=type, meeting=meeting, user=user)

    def __repr__(self):
        return 'Meeting Material'