# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

*Features*

## Pre-requisites

1. docker
2. Run the following command and edit the .env file
```bash
env UID=$(id -u) GID=$(id -g) envsubst < .env.template > .env
```

## Getting Started

```bash
docker compose up # pass --build if you want to build from local
```

## Usage

```bash
docker compose run --rm {{cookiecutter.project_slug}} python3 -m {{cookiecutter.project_slug}} --help
```

## Changelog

## Contributing

## License

{{ cookiecutter.license }}

