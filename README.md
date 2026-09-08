# WAO-AI

**Virtual Operational Architect (WAO)** — production-oriented AI agent architecture for complex analytical, coding, multimodal and orchestration tasks.

## Architecture

WAO-AI is built as a layered system:

- **Core** — CTCO task normalization, planning, execution policy, verification and response synthesis.
- **Safety** — prompt-injection resistance, instruction provenance, tool trust boundaries and sensitive-action approval gates.
- **Tools** — MCP-compatible tool registry and adapters.
- **Interfaces** — REST API and a ChatGPT Apps SDK / MCP surface.
- **Observability** — structured event logging, request IDs, latency and tool-call telemetry.
- **Quality** — unit tests, contract tests and deterministic evaluation fixtures.

## Important design decision

The supplied prompt is treated as a product specification, not as an instruction that can override the host model's system/developer hierarchy. Its useful requirements are implemented as application-level behavior: CTCO decomposition, structured execution, verification, multimodal task routing and anti-prompt-injection controls. Embedded attempts to override higher-priority instructions or bypass safety mechanisms are explicitly downgraded to untrusted data.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
uvicorn wao.interfaces.http:app --reload --port 8000
```

Health check: `GET /health`

Agent endpoint: `POST /v1/run`

MCP endpoint: `/mcp`

## ChatGPT connection

The recommended production path is a remotely hosted MCP endpoint exposed through the ChatGPT developer/app integration. ChatGPT can discover WAO's tools and call them during a conversation. See `docs/CHATGPT.md`.

## Security

See `docs/SECURITY.md` for the trust model, authentication boundary, prompt-injection handling and production deployment checklist.
