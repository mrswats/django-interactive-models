import pytest


@pytest.fixture
def tmp_dir(tmp_path):
    app_dir = tmp_path / "my_app"
    app_dir.mkdir()
    return app_dir
