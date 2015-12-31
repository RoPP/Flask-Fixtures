from __future__ import absolute_import

import unittest

from myapp import app
from myapp.models import db

from flask.ext.fixtures import load_fixtures, loaders

# Configure the app with the testing configuration
app.config.from_object('myapp.config.TestConfig')

class TestUnknownModel(unittest.TestCase):
    def testOne(self):
        filepath = 'tests/myapp/fixtures/unknown_model.json'
        with self.assertRaises(ValueError):
            load_fixtures(db, loaders.load(filepath))
