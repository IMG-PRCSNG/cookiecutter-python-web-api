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
docker compose build # build the docker first

```

## Usage

```bash
# Run docker
docker compose build
docker compose run --rm -it -v $PWD:/app sample python3 -m {{cookiecutter.project_slug}} --help
docker compose run --rm -it -v $PWD:/app sample python3 -m {{cookiecutter.project_slug}} run
docker compose run --rm -it -v $PWD:/app sample python3 -m {{cookiecutter.project_slug}} inference
```

## Changelog

## Contributing

## License

{{ cookiecutter.license }}

