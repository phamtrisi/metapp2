import os
import sys
import subprocess
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand

from metapp2.app import create_app, register_blueprints, register_errorhandlers, register_extensions
from metapp2.user.models import User
from metapp2.settings import DevConfig, ProdConfig
from metapp2.database import db

if os.environ.get("METAPP2_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

register_blueprints(app)
register_errorhandlers(app)
register_extensions(app)

import metapp2.views