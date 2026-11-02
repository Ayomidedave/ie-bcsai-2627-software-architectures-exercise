# Helper for the step tests: reads the import lines of a file. Not part of the shop.

from pathlib import Path

HERE = Path(__file__).parent


def imports_in(path):
    lines = (HERE / path).read_text().splitlines()
    return [line.strip() for line in lines if line.strip().startswith(("import ", "from "))]


def check_layers(domain):
    """Inside a domain: presentation -> business -> persistence."""
    for line in imports_in(f"{domain}/presentation.py"):
        assert "persistence" not in line, f"{domain}/presentation.py must not use persistence: {line}"
    for line in imports_in(f"{domain}/business.py"):
        assert "presentation" not in line, f"{domain}/business.py must not use presentation: {line}"
    for line in imports_in(f"{domain}/persistence.py"):
        assert "business" not in line and "presentation" not in line, f"{domain}/persistence.py: {line}"
