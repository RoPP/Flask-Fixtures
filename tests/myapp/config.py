# myapp/config.py


class TestConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    testing = True
    debug = True


class DefaultConfig(object):
    # FIXTURES_DIRS = ['datas', '/opt/datas']
    pass
