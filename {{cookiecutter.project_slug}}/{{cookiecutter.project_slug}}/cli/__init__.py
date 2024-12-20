import logging
import typer

app = typer.Typer()
app_state = {"verbose": True}
logger = logging.getLogger()


@app.callback()
def base(verbose: bool = False):
    """
    APP CLI
    TODO: Fill this
    """
    app_state["verbose"] = verbose
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s (%(threadName)s): %(name)s - %(levelname)s - %(message)s",
    )
    global logger
    logger = logging.getLogger()


@app.command()
def run():
    from {{cookiecutter.project_slug}}.config import AppConfig
    from {{cookiecutter.project_slug}}.db import create_db_and_tables
    from {{cookiecutter.project_slug}}.db.models import Dummy

    from sqlmodel import Session

    config = AppConfig()
    engine = create_db_and_tables(config.database_url)

    with Session(engine) as session:
        dummy = Dummy(
            name="dummy"
        )
        session.add(dummy)
        session.commit()

        session.refresh(dummy)

        print("Created Dummy:", dummy)
    pass

@app.command()
def inference():
    from {{cookiecutter.project_slug}}.inference import load
    from {{cookiecutter.project_slug}}.config import AppConfig

    import numpy as np

    config = AppConfig()
    manager = load(config.inference)
    #manager.start()

    client = manager.get('ExampleModel')
    print(client)
    output = client.infer_sample(
        np.arange(10, dtype=np.float32),
        np.arange(10, dtype=np.float32)
    )
    print(output)
    client.close()
    manager.stop()
    pass

if __name__ == "__main__":
    app()
