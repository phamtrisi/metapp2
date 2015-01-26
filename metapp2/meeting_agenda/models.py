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

class Meeting_Agenda(SurrogatePK, Model):
    __tablename__ = 'meeting_agendas'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    status = Column(db.String(50), nullable=True)
    meeting_id = ReferenceCol('meetings')
    
    def __init__(self, date_created, status, meeting):
        db.Model.__init__(self, date_created=date_created, status=status, meeting=meeting)

    def __repr__(self):
        return 'Meeting Agenda'