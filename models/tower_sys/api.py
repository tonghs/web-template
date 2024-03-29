from typing import Dict

from config import HOST
from models.init_db import tower_client


def get_access_token_by_auth_code(auth_code: str, user_id: int) -> Dict:
    """
    获取 tower access token
    :param auth_code:
    :return:
        {
            "access_token": "d4e949df783404f22e882430158f3b0440b608709d833f9b981e9a96b850f05c",
            "token_type": "bearer",
            "expires_in": 7199,
            "refresh_token": "c426d5ab6a211310df088c77b36b38592f6752d5238f291b79174d93f7dc2ed5",
            "created_at": 1523420694,
            "email": "tower@tower.im"
        }
    """
    redirect_uri = f"{HOST}/tower/oauth_callback?user_id={user_id}"
    return tower_client.get_access_token_by_auth_code(auth_code=auth_code, redirect_uri=redirect_uri)


def refresh_access_token(access_token: str, refresh_token: str, user_id: int):
    """
    刷新 access_token
    :param access_token:
    :param refresh_token:
    :param user_id:
    :return:
    """
    redirect_uri = f"{HOST}/tower/oauth_callback?user_id={user_id}"
    return tower_client.refresh_access_token(
        access_token=access_token, refresh_token=refresh_token,
        redirect_uri=redirect_uri
    )


def get_auth_url(user_id: int) -> str:
    """
    oauth 跳转授权 URL
    :param user_id:
    :return:
    """
    return f"{tower_client.auth_code_url}?client_id={tower_client.client_id}&redirect_uri={HOST}/tower/oauth_callback?user_id={user_id}&response_type=code"


def get_todo(todo_id: str, access_token: str):
    """
    获取任务信息
    :param todo_id:
    :param access_token:
    :return:
    """
    return tower_client.get_todo(todo_id=todo_id, access_token=access_token)
