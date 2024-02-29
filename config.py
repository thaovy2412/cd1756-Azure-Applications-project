import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'https://vytt1storageaccount.blob.core.windows.net/images'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or '98NkLG1V6ohBDzkQezwj2vlrbtCcXa0+Vgox1QjbrFGBQmlTFhuv0nb8FSvB40V59/8R/jDgwysV+AStg4WvJQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'vytt1-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'vytt1-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Rebound@991224'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + '/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "suF8Q~DSzTCkzxKnMtNhjzRpr4v.lXZN5QtqccVa"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/common"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "bcb905cd-80ff-46a7-9e75-c49a2a0f5579"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/home"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
