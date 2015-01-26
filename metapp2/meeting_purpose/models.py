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

class Meeting_Purpose(SurrogatePK, Model):
    __tablename__ = 'meeting_purposes'
    type = Column(db.String(255), nullable=False)

    def __init__(self, type):
        db.Model.__init__(self, type=type)

    def __repr__(self):
        return 'Meeting Purpose'