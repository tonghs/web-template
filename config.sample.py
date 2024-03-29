import os


DEBUG = bool(os.environ.get('DEBUG', False))

HOST = "https://web.nps.motn.top"

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
QCLOUD_CC_COS_DOMAIN = os.environ.get('QCLOUD_CC_COS_DOMAIN', 'cc.cos.motn.top')
QCLOUD_CC_COS_URL = 'https://{}/{}{}'.format(QCLOUD_CC_COS_DOMAIN, '{}', '?imageView2/q/85')
QCLOUD_CC_COS_URL_PATTERN = 'https://{}/{}{}'.format(QCLOUD_CC_COS_DOMAIN, '{}', '?imageMogr2/crop/#width#x#height#/gravity/center/rquality/85')

# redis
REDIS_DB = os.environ.get('REDIS_DB', 'test-redis')
REDIS_URL = f'redis://{REDIS_DB}/0'

# tower
TOWER_CLIENT_ID = os.environ.get('TOWER_CLIENT_ID', 'tower-client-id')
TOWER_SECRET_KEY = os.environ.get('TOWER_SECRET_KEY', 'tower-secret-key')
TOWER_TEAM_ID = 158367

# notion
NOTION_TOKEN = os.environ.get('NOTION_TOKEN', 'notion-token')
NOTION_DATABASE_ID = os.environ.get("NOTION_DB_ID", "notion-database-id")
