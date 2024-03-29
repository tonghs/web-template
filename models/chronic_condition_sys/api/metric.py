from typing import List

from models.chronic_condition_sys.dao.metric import (
    MetricDAO,
    MetricLabelDAO,
    UserMetricDAO,
)
from models.chronic_condition_sys.dto.metric import (
    MetricDTO,
    MetricLabelDTO,
    UserMetricDTO,
)
from models.chronic_condition_sys.exceptions import (
    DuplicatedMetricException,
    MetricLabelNotFoundException,
    MetricNotFoundException,
)
from models.const import CommonStatus
from models.init_db import db


def create_metric(name: str, text: str, unit: str) -> MetricDTO:
    dao = MetricDAO.get_by_name(name=name)
    if dao:
        raise DuplicatedMetricException()
    dao = MetricDAO.create(name=name, text=text, unit=unit)
    return MetricDTO.from_dao(dao)


def get_metric(metric_id: int) -> MetricDTO:
    dao = MetricDAO.get_by_id(metric_id=metric_id)
    if not dao or dao.status == CommonStatus.DELETED:
        raise MetricNotFoundException()

    return MetricDTO.from_dao(dao)


def get_metric_by_name(name: str) -> MetricDTO:
    dao = MetricDAO.get_by_name(name=name)
    if not dao:
        raise MetricNotFoundException()

    return MetricDTO.from_dao(dao)


@db.atomic()
def delete_metric(metric_id: int):
    dao = MetricDAO.get_by_id(metric_id=metric_id)
    if not dao:
        raise MetricNotFoundException()

    dao.delete()

    for um_dao in UserMetricDAO.query_by_metric_id(metric_id=metric_id):
        um_dao.delete()

    for ml_dao in MetricLabelDAO.query_by_metric_id(metric_id=metric_id):
        ml_dao.delete()


def create_user_metric(user_id: int, metric_id: int) -> UserMetricDTO:
    get_metric(metric_id=metric_id)
    dao = UserMetricDAO.create(user_id=user_id, metric_id=metric_id)
    return UserMetricDTO.from_dao(dao)


def query_user_metric_by_user_id(user_id: int) -> List[UserMetricDTO]:
    daos = UserMetricDAO.query_by_user_id(user_id=user_id)
    return [UserMetricDTO.from_dao(dao) for dao in daos]


def create_metric_label(metric_id: int, name: str, text: str, order: int = 0) -> MetricLabelDTO:
    dao = get_metric(metric_id=metric_id)
    dao = MetricLabelDAO.create(metric_id=dao.id, name=name, text=text, order=order)
    return MetricLabelDTO.from_dao(dao)


def delete_metric_label(metric_label_id: int):
    dao = MetricLabelDAO.get_by_id(metric_label_id=metric_label_id)
    if not dao:
        raise MetricLabelNotFoundException()
    dao.delete()


def query_metric_label_by_metric_id(metric_id: int) -> List[MetricLabelDTO]:
    daos = MetricLabelDAO.query_by_metric_id(metric_id=metric_id)
    return [MetricLabelDTO.from_dao(dao) for dao in daos]
