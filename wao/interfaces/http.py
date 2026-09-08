from fastapi import FastAPI, Header, HTTPException

from ..config import settings
from ..core import run_wao
from ..models import ExecutionResult, TaskRequest

app = FastAPI(title=settings.app_name, version='0.1.0')


def _authorize(authorization: str | None) -> None:
    if settings.auth_token and authorization != f'Bearer {settings.auth_token}':
        raise HTTPException(status_code=401, detail='Unauthorized')


@app.get('/health')
async def health() -> dict[str, str]:
    return {'status': 'ok', 'service': settings.app_name}


@app.post('/v1/run', response_model=ExecutionResult)
async def run(request: TaskRequest, authorization: str | None = Header(default=None)) -> ExecutionResult:
    _authorize(authorization)
    return await run_wao(request)
