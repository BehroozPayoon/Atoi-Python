from fastapi import APIRouter

from app.schemas.atoi import AtoiInput
from app.core.utility import atoi_parser
from app.core.response import send_success_response

router = APIRouter()


@router.post("/atoi")
def atoi(data: AtoiInput):
    result = atoi_parser(data.input_str)
    return send_success_response({'result': result})
