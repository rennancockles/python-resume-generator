import json
from pathlib import Path

from entities.resume import Resume


def main() -> None:
    data_path = Path("data")
    for file in data_path.glob("*.json"):
        print(f"Loading {file}")
        data = json.load(file.open())
        resume = Resume(**data)
        print(resume.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
