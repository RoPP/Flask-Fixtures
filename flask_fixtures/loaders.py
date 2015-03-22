"""
    flask.ext.fixtures.loaders
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Classes for loading serialized fixtures data.

    :copyright: (c) 2015 Christopher Roach <ask.croach@gmail.com>.
    :license: MIT, see LICENSE for more details.
"""

import abc
import os
import logging

log = logging.getLogger(__name__)

try:
    import simplejson as json
except ImportError:
    import json

try:
    import yaml
except ImportError:
    def load(self, filename):
        raise Exception("Could not load fixture '{0}'. Make sure you have PyYAML installed.".format(filename))
    yaml = type('FakeYaml', (object,), {
        'load': load
    })()


class FixtureLoader(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self):
        pass


class JSONLoader(FixtureLoader):

    extensions = ('.json', '.js')

    def load(self, filename):
        with open(filename) as fin:
            return json.load(fin)


class YAMLLoader(FixtureLoader):

    extensions = ('.yaml', '.yml')

    def load(self, filename):
        with open(filename) as fin:
            return yaml.load(fin)


def load(filename):
    name, extension = os.path.splitext(filename)

    for cls in FixtureLoader.__subclasses__():
        # If a loader class has no extenions, log a warning so the developer knows
        # that it will never be used anyhwhere
        if not hasattr(cls, 'extensions'):
            log.warn("The loader '{0}' is missing extensions and will not be used.".format(cls.__name__))
            continue

        # Otherwise, check if the file's extension matches a loader extension
        for ext in cls.extensions:
            if extension == ext:
                return cls().load(filename)

    # None of the loaders matched, so raise an exception
    raise Exception("Could not load fixture '{0}'. Unsupported file format.".format(filename))


def extensions():
    return [ext for c in FixtureLoader.__subclasses__() for ext in c.extensions]
