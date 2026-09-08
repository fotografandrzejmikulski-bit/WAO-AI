FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY pyproject.toml README.md ./
COPY wao ./wao
COPY run_mcp.py ./
RUN pip install --no-cache-dir .

EXPOSE 8000
CMD ["uvicorn", "wao.interfaces.http:app", "--host", "0.0.0.0", "--port", "8000"]
