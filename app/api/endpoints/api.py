from fastapi import APIRouter, Depends

from app.schemas.atoi import AtoiInput
from app.core.utility import atoi_parser
from app.core.response import send_success_response
from app.api import deps
from app.core.cache import check_cache
from app import crud


router = APIRouter()


@router.post("/atoi")
@check_cache
def atoi(*, data: AtoiInput, redis_conn = Depends(deps.get_redis_connection)):
    result = atoi_parser(data.input_str)
    crud.atoi.set_item(redis_conn, data.input_str, result)
    return send_success_response({'result': result})
