import redis
from config import (
    MYSQL_DB,
    MYSQL_HOST,
    MYSQL_PASSWD,
    MYSQL_PORT,
    MYSQL_USER,
    NOTION_DATABASE_ID,
    NOTION_TOKEN,
    QCLOUD_CC_COS_BUCKET,
    QCLOUD_CC_COS_REGION,
    QCLOUD_SECRET_ID,
    QCLOUD_SECRET_KEY,
    REDIS_URL,
    TOWER_CLIENT_ID,
    TOWER_SECRET_KEY,
    WXAPP_ID,
    WXAPP_SECRET,
)
from libs.notion import NotionClient
from libs.qcloud import QCloudCOSClient
from libs.tower import TowerClient
from playhouse.pool import PooledMySQLDatabase
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatWxa


db = PooledMySQLDatabase(MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWD,
                         host=MYSQL_HOST, port=MYSQL_PORT)

wxapp_client = WeChatWxa(WeChatClient(WXAPP_ID, WXAPP_SECRET))

# 存储用户单据
qcloud_cos_client = QCloudCOSClient(secret_id=QCLOUD_SECRET_ID,
                                    secret_key=QCLOUD_SECRET_KEY,
                                    bucket=QCLOUD_CC_COS_BUCKET,
                                    region=QCLOUD_CC_COS_REGION,
                                    allow_prefix='*')

# redis
redis_conn = redis.Redis.from_url(REDIS_URL, decode_responses=True)  # 存binary 数据，不需要 decode response

# tower client
tower_client = TowerClient(client_id=TOWER_CLIENT_ID, secret_key=TOWER_SECRET_KEY)

# notion client
notion_client = NotionClient(token=NOTION_TOKEN, database_id=NOTION_DATABASE_ID)
