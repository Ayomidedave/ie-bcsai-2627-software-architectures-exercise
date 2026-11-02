# STEP 3: the presentation layer only receives requests, calls the business layer
# and turns errors into status codes. It does not store data or apply shop rules.
#     presentation  ->  business  ->  persistence
# Fails at the start, because presentation.py still does everything by itself.

from pathlib import Path

CODE = (Path(__file__).parent / "presentation.py").read_text()
IMPORTS = [line for line in CODE.splitlines() if line.startswith(("import ", "from "))]


def test_presentation_uses_the_business_layer():
    assert any("business" in line for line in IMPORTS), "presentation.py must call business.py"


def test_presentation_does_not_use_the_persistence_layer():
    assert not any("persistence" in line for line in IMPORTS), "presentation.py must not skip the business layer"


def test_presentation_has_no_shop_rules():
    assert "5000" not in CODE and "499" not in CODE, "the shipping rule belongs to business.py"


def test_presentation_stores_no_data():
    assert "self.books" not in CODE and "self.orders" not in CODE, "storing data belongs to persistence.py"
