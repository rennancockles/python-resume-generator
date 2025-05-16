import json
import shutil
from pathlib import Path

import typer
from jinja2 import Environment, FileSystemLoader
from pydantic import HttpUrl

from resume_generator.entities.resume import Resume


def build_template(resume: Resume, template_path: Path) -> None:
    def only_numbers(value: str) -> str:
        return "".join(filter(str.isdigit, value))

    def url_path(url: HttpUrl) -> str:
        return (url.path or "").strip("/")

    output_folder = Path("output")

    env = Environment(loader=FileSystemLoader(template_path))
    env.filters["only_numbers"] = only_numbers
    env.filters["url_path"] = url_path

    context = resume.model_dump()
    if not context["skills"]:
        context["skills"] = resume.get_calculated_skills()

    template = env.get_template("index.html")
    output = template.render(context)

    if output_folder.exists():
        shutil.rmtree(output_folder, ignore_errors=True)
    output_folder.mkdir(parents=True, exist_ok=True)

    for file in template_path.iterdir():
        if file.name != "index.html" and file.is_file():
            shutil.copy(file, output_folder)

    with open(output_folder / "index.html", "w") as f:
        f.write(output)


def main(filepath: Path, template: str = "basic") -> None:
    if not filepath.exists() or not filepath.is_file():
        raise FileNotFoundError(f"File {filepath} does not exist.")

    if filepath.suffix != ".json":
        raise ValueError(f"File {filepath} is not a JSON file.")

    template_path = Path("templates") / template
    if not template_path.exists() or not template_path.is_dir():
        raise NotADirectoryError(f"Template {template} does not exist.")

    data = json.load(filepath.open())

    try:
        resume = Resume(**data)
    except Exception as e:
        raise ValueError(f"Format of file {filepath} is not valid.") from e

    build_template(resume, template_path)

    print("Resume generated successfully!")


if __name__ == "__main__":
    typer.run(main)
