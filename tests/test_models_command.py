import pytest
from django.core.management import call_command
from django.core.management.base import CommandError

test_fields = "body:text number_of_pages:int book_url:url"


@pytest.fixture
def model_command_run():
    def _(*args, **options):
        call_command("models", *args, **options)

    return _


def test_model_command_creates_file(tmp_dir, model_command_run, capsys):
    model_command_run(tmp_dir, "MyModel", test_fields)
    out, err = capsys.readouterr()
    assert out == f"Generated {tmp_dir}/models.py!\n"
    assert err == ""


def test_models_command_outputs_message_to_sdtoud_on_success(tmp_dir, model_command_run):
    model_command_run(tmp_dir, "MyModel", test_fields)
    models_file = tmp_dir / "models.py"
    assert models_file.exists()


def test_models_does_not_override_existing_models_file(tmp_path, model_command_run):
    models_file = tmp_path / "models.py"
    models_file.touch()
    with open(models_file, "w") as fileobj:
        fileobj.write("from django.db import models\n\n\nclass MyModel(models.Model):\n    pass")
    models_file
    error_message = (
        r"Not overriding '.+/models.py'[\S\s]+use `--override` to override this behavior"
    )
    with pytest.raises(CommandError, match=error_message):
        model_command_run(tmp_path, "MYModel", "name:int", override=False)


def test_models_does_override_existing_models_file_if_file_contains_no_models(
    tmp_path, model_command_run, capsys
):
    models_file = tmp_path / "models.py"
    models_file.touch()
    model_command_run(tmp_path, "MYModel", "name:int", override=False)
    out, err = capsys.readouterr()
    assert out == f"Generated {tmp_path}/models.py!\n"
    assert err == ""


def test_models_overrides_file_when_flag_is_passed(tmp_path, model_command_run, capsys):
    models_file = tmp_path / "models.py"
    models_file.touch()
    model_command_run(tmp_path, "MYModel", "name:int", override=True)
    out, err = capsys.readouterr()
    assert out == f"Generated {tmp_path}/models.py!\n"
    assert err == ""


def test_models_does_not_create_models_file_on_unexisting_app(model_command_run):
    error_message = (
        r"'\w+' does not exist![\S\s]+"
        r"Create a new app by running[\S\s]+\$ ./manage.py startapp \w+"
    )
    with pytest.raises(CommandError, match=error_message):
        model_command_run("my_app", "MYModel", "")
