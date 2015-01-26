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

class Meeting_Agenda_Item(SurrogatePK, Model):
    __tablename__ = 'meeting_agenda_items'
    date_created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    content = Column(db.String(500), nullable=False)
    meeting_agenda_id = ReferenceCol('meeting_agendas')
    
    def __init__(self, date_created, content, meeting_agenda):
        db.Model.__init__(self, date_created=date_created, content=content, meeting_agenda=meeting_agenda)

    def __repr__(self):
        return 'Meeting Agenda Item'