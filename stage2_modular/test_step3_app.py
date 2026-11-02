# STEP 3: the shop is built from the two domains and the old layer files are gone.
# Fails at the start, because app.py still uses business.py, persistence.py and presentation.py.
# Passes when app.py uses catalog/ and orders/ and the three old files are deleted.
# test_shop_behaviour.py must still pass: the shop does exactly the same as before.

from pathlib import Path

from layer_rules import imports_in

HERE = Path(__file__).parent


def test_app_is_built_from_the_domains():
    imports = imports_in("app.py")

    assert any("catalog" in line for line in imports)
    assert any("orders" in line for line in imports)


def test_the_old_layer_files_are_gone():
    for name in ["business.py", "persistence.py", "presentation.py"]:
        assert not (HERE / name).exists(), f"{name} has been replaced by the domains: delete it"
