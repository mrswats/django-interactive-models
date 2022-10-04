from interactive_models.management.commands._check_models_file import check_models_file


def test_check_models_non_existing_file_is_false(tmp_dir):
    assert not check_models_file(tmp_dir / "models.py")


def test_check_models_empty_file_is_false(tmp_dir):
    models_file = tmp_dir / "models.py"
    models_file.touch()

    assert not check_models_file(models_file)


def test_check_models_file_contains_django_boilerplate_is_false(tmp_dir):
    models_file = tmp_dir / "models.py"
    models_file.touch()

    with open(models_file, "w") as fileobj:
        fileobj.write("from djagno.db import models\n\n\n# put your models here")

    assert not check_models_file(models_file)


def test_check_models_file_contains_class_is_true(tmp_dir):
    models_file = tmp_dir / "models.py"
    models_file.touch()

    with open(models_file, "w") as fileobj:
        fileobj.write("from djagno.db import models\n\n\nclass MyModel(models.Model):\n    pass")

    assert check_models_file(models_file)
