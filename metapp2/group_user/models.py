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

class Group_User(SurrogatePK, Model):
    __tablename__ = 'group_users'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    group_id = ReferenceCol('groups')
    user_id = ReferenceCol('users')
    
    def __init__(self, date_created, group, user):
        db.Model.__init__(self, date_created=date_created, group=group, user=user)

    def __repr__(self):
        return 'Group User'