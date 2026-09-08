# ChatGPT integration

WAO is exposed to ChatGPT through a remote MCP endpoint. OpenAI documents MCP as the integration
standard for tools/context and the Apps SDK as the route for apps that run inside ChatGPT. New
MCP integrations should prefer Streamable HTTP over legacy SSE. See the official documentation:
https://help.openai.com/en/articles/12515353-build-with-the-apps-sdk
https://openai.github.io/openai-agents-python/mcp/

## 1. Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
# set WAO_OPENAI_API_KEY
python run_mcp.py
```

The MCP server listens on the port provided by the MCP SDK. For local testing, expose the
MCP endpoint over a temporary HTTPS tunnel such as ngrok:

```bash
ngrok http 8000
```

Use the tunnel's `/mcp` endpoint when adding the connector in ChatGPT Developer Mode.

## 2. Production

Deploy the service behind HTTPS with:

- a stable DNS name;
- TLS termination;
- authentication at the edge;
- least-privilege outbound credentials;
- request logging without secrets or user content unless explicitly required;
- rate limiting and abuse controls;
- separate development and production credentials.

## 3. ChatGPT setup

Open ChatGPT web and use Developer Mode / custom MCP app configuration available to the
workspace. Add the WAO HTTPS MCP endpoint. Then add the WAO app to a conversation and invoke
it through the `wao_run` tool.

Availability of Developer Mode, full MCP actions and custom apps depends on the ChatGPT plan
and workspace configuration. OpenAI currently documents these capabilities for Business and
Enterprise/Edu workspaces, with rollout and UI details subject to change.

## 4. Tool contract

`wao_run` accepts:

- `task`: required natural-language task;
- `context`: optional JSON object;
- `constraints`: optional list;
- `output_format`: `auto`, `text`, `json` or `markdown`.

The response includes a request ID, execution status, normalized plan, response text and
verification/audit metadata.
