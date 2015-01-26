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

class Group(SurrogatePK, Model):
    __tablename__ = 'groups'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    name = Column(db.String(255), nullable=False)
    owner_id = ReferenceCol('users')
    
    def __init__(self, date_created, name, owner):
        db.Model.__init__(self, date_created=date_created, name=name, owner=owner)

    def __repr__(self):
        return 'Group'