# Flask settings

FLASK_SERVER_NAME = None#'isbtranslatorapi.adversary.us'#'biggim.ncats.io'
FLASK_DEBUG = False# Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

#secrets
SECRET_DIR = '/run/secrets/'

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#Fingerprint code
FINGERPRINT_PATH = '/data-fingerprints/bin'

