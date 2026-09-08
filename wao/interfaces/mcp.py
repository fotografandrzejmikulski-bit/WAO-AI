"""Minimal MCP surface for exposing WAO to ChatGPT-compatible MCP clients.

The production deployment should put this endpoint behind TLS and an authenticated
reverse proxy. Keep the exposed tool set intentionally narrow and auditable.
"""

from mcp.server.fastmcp import FastMCP

from ..core import run_wao
from ..models import TaskRequest

mcp = FastMCP('wao-ai')


@mcp.tool(name='wao_run', description='Execute a complex task through the WAO operational agent.')
async def wao_run(
    task: str,
    context: dict | None = None,
    constraints: list[str] | None = None,
    output_format: str = 'auto',
) -> dict:
    request = TaskRequest(
        task=task,
        context=context or {},
        constraints=constraints or [],
        output_format=output_format if output_format in {'auto', 'text', 'json', 'markdown'} else 'auto',
    )
    result = await run_wao(request)
    return result.model_dump(mode='json')
