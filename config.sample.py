import os


DEBUG = bool(os.environ.get('DEBUG', False))

# MySQL
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db')
MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
MYSQL_USER = os.environ.get('MYSQL_USER', 'tonghs')
MYSQL_PASSWD = os.environ.get('MYSQL_PASSWD', 'tonghs')
MYSQL_DB = os.environ.get('MYSQL_DB', 'web-template')

# sentry
SENTRY_DSN = "https://ad8effa8e62040b6826c8a44b025ad6c@o327962.ingest.sentry.io/5624232"

LOG_PATH = os.environ.get('LOG_PATH', "/var/log/web-template")


# 微信小程序
WXAPP_ID = os.environ.get('WXAPP_ID', '')
WXAPP_SECRET = os.environ.get('WXAPP_SECRET', '')


# jwt
JWT_SECRET = os.environ.get('JWT_SECRET', 'your-secret')

# API sign secret
API_SECRET = os.environ.get('API_SECRET', 'your-secret')

# qcloud
QCLOUD_SECRET_ID = os.environ.get('QCLOUD_SECRET_ID', '')
QCLOUD_SECRET_KEY = os.environ.get('QCLOUD_SECRET_KEY', '')

# 慢病管理 bucket
QCLOUD_CC_COS_BUCKET = os.environ.get('QCLOUD_CC_COS_BUCKET', '')
QCLOUD_CC_COS_REGION = os.environ.get('QCLOUD_CC_COS_REGION', '')