from __future__ import absolute_import

from flask import Flask
from flask.ext.fixtures import Fixtures

from myapp.config import DefaultConfig

app = Flask(__name__)
app.config.from_object(DefaultConfig)
fixtures = Fixtures(app)
