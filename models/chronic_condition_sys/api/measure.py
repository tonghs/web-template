import datetime
from typing import List

from models.chronic_condition_sys.api.metric import get_metric
from models.chronic_condition_sys.dao.metric_measure import MetricMeasureDAO
from models.chronic_condition_sys.dto.metric import MetricDTO
from models.chronic_condition_sys.dto.metric_measure import MetricMeasureDTO
from models.chronic_condition_sys.exceptions import MetricMeasureNotFoundException
from models.exceptions import AccessDeniedError


def create_metric_measure(user_id: int, metric_id: int, metric_label: str, value: float, created_at: datetime.datetime):
    metric: MetricDTO = get_metric(metric_id=metric_id)
    # TODO
    # get_metric_label()
    dao = MetricMeasureDAO.create(
        user_id=user_id,
        metric_id=metric.id,
        metric_label=metric_label,
        value=value, created_at=created_at)

    return MetricMeasureDTO.from_dao(dao)


def get_recnet_metric_measure(user_id: int, metric_id: int, limit: int = 15) -> List[MetricMeasureDTO]:
    metric: MetricDTO = get_metric(metric_id=metric_id)
    daos: List[MetricMeasureDAO] = MetricMeasureDAO.query_recent_by_metric(user_id=user_id, metric_id=metric.id, limit=limit)

    return [MetricMeasureDTO.from_dao(dao) for dao in daos]


def delete_metric_measure(metric_measure_id: int, user_id: int):
    dao = MetricMeasureDAO.get_by_id(measure_id=metric_measure_id)
    if not dao:
        raise MetricMeasureNotFoundException()

    if dao.user_id != user_id:
        raise AccessDeniedError()

    dao.delete()
