FROM python:3.12 AS builder

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN python -m pip install --no-cache-dir -U pip poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-cache --no-root

COPY resume_generator ./resume_generator
COPY templates ./templates


FROM python:3.12-slim AS runtime

ENV PYTHONPATH=/app

WORKDIR /app

COPY --from=builder /app /app

ENTRYPOINT ["/app/.venv/bin/python", "resume_generator"]
