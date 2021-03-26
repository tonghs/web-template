import random
from typing import List

from models.redis import get_sms_auth_code, save_sms_auth_code


def generate_auth_code(phone: str, length: int = 4) -> str:
    seeds: str = "0123456789"
    codes: List[str] = []

    for i in range(4):
        codes.append(random.choice(seeds))

    auth_code: str = ''.join(codes)
    save_sms_auth_code(phone=phone, auth_code=auth_code)

    return auth_code


def verify_auth_code(phone: str, auth_code: str) -> bool:
    _auth_code: str = get_sms_auth_code(phone=phone)

    return auth_code == _auth_code
