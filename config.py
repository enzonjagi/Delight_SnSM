import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to get string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	DELIGHT_SNSM_SUBJECT_PREFIX = '[Delight_SnSM]'
	DELIGHT_SNSM_MAIL_SENDER= 'Delight_SNSM Admin <Delight_SnSM@example.com>'
	[DELIGHT_SNSM_ADMIN = os.environ.get('DELIGHT_SNSM_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PASSWORD = 587
	MAIL_USE_TLS= True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///'  + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///'  + os.path.join(basedir, 'data.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,

	'default' : DevelopmentConfig
}