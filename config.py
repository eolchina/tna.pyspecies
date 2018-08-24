import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://umbel:umbel@localhost/qn_pyspecies_dev"


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    # DEV_DATABASE_URL = "postgresql://umbel:umbel@localhost/qn_pyspecies_dev"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # SQLALCHEMY_DATABASE_URI = "postgresql://umbel:umbel@localhost/qn_pyspecies_dev"


class TestingConfig(Config):
    TESTING = True
    # TEST_DATABASE_URL = "postgresql://umbel:umbel@localhost/qn_pyspecies_test"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
