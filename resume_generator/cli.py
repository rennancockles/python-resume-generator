import json
from pathlib import Path

import typer

from resume_generator.entities.resume import Resume


def main(filepath: Path) -> None:
    if not filepath.exists() or not filepath.is_file():
        raise FileNotFoundError(f"File {filepath} does not exist.")

    if filepath.suffix != ".json":
        raise ValueError(f"File {filepath} is not a JSON file.")

    data = json.load(filepath.open())

    try:
        resume = Resume(**data)
    except Exception as e:
        raise ValueError(f"Format of file {filepath} is not valid.") from e

    print(resume.model_dump_json(indent=4))


if __name__ == "__main__":
    typer.run(main)
