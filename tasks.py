from invoke import task
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parent / "problems"


@task
def test(ctx):
    ctx.run(f"pipenv run python -m pytest -vv {SRC_PATH}")


@task(name="format")
def format_(ctx):
    ctx.run(f"pipenv run python -m black -l 80 {SRC_PATH}")


@task()
def lint(ctx):
    ctx.run(f"pipenv run python -m flake8 {SRC_PATH}")
