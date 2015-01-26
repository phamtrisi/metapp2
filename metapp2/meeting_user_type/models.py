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

class Meeting_User_Type(SurrogatePK, Model):
    __tablename__ = 'meeting_user_types'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    type = Column(db.String(255), nullable=False)
    
    def __init__(self, date_created, type):
        db.Model.__init__(self, date_created=date_created, type=type)

    def __repr__(self):
        return 'Meeting User Type'