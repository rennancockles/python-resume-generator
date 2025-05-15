from pathlib import Path

import pytest

from resume_generator.__main__ import main


def test_file_not_exist() -> None:
    """Test if the function raises FileNotFoundError when the file does not exist."""
    with pytest.raises(FileNotFoundError):
        main(Path("non_existent_file.json"))


def test_file_not_json() -> None:
    """Test if the function raises ValueError when the file is not a JSON file."""
    with pytest.raises(ValueError):
        main(Path("tests/test_resume_generator.py"))


def test_invalid_json() -> None:
    """Test if the function raises ValueError when the file is not a valid JSON file."""
    with pytest.raises(ValueError):
        main(Path("tests/inputs/invalid_schema.json"))


def test_invalid_email() -> None:
    """Test if the function raises ValueError when the email field is invalid."""
    with pytest.raises(ValueError):
        main(Path("tests/inputs/invalid_email.json"))


def test_valid_json() -> None:
    """Test if the function does not raise any exception when the file is valid."""
    main(Path("tests/inputs/valid_empty.json"))
