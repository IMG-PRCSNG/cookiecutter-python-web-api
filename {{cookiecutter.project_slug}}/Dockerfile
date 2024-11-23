FROM python:{{cookiecutter.python_version}} AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache python3 -m pip install --upgrade pip setuptools wheel && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/python3 -m pip install -r requirements.txt

FROM python:{{cookiecutter.python_version}}-slim AS deploy


ENV PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /
# Initialise the user
COPY docker/_entrypoint.sh entrypoint.sh

# Copy the files
COPY --from=tianon/gosu /gosu /usr/local/bin/
COPY --from=base --chown=nobody:nogroup /opt/venv /opt/venv

WORKDIR /app
COPY --chown=nobody:nogroup . .

ENTRYPOINT ["/bin/bash", "/entrypoint.sh" ]
CMD ["python3", "-m", "{{cookiecutter.project_slug}}",  "--help"]

