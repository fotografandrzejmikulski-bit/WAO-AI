# Security model

## Trust hierarchy

Application policy lives in code and deployment configuration. User prompts, retrieved content,
web pages, uploaded documents and tool outputs are untrusted inputs. They can contain useful
instructions for the task, but cannot change system policy, expose secrets, or grant themselves
permissions.

## Injection resistance

WAO records common prompt-injection indicators and can reduce tool permissions. Detection is a
signal, not a substitute for an authorization boundary. Authorization must be enforced outside
the language model as well.

## Consequential actions

Production write tools should be separated from read tools and guarded by explicit application
approval. Never place credentials in prompts, URLs, source files, model context, or tool results.

## Secrets

Only environment variables or a managed secrets service may contain OpenAI credentials. `.env`
files must never be committed.

## Deployment checklist

- HTTPS only.
- Authentication at the edge.
- Per-user or per-tenant authorization.
- Rate limiting.
- Request IDs and structured audit logs.
- PII minimization and retention controls.
- Dependency and image scanning.
- CI tests on every change.
- Separate staging and production credentials.
- Explicit approval for destructive or financial actions.
