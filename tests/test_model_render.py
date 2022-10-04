from interactive_models.management.commands._render_model import render_model_file


def test_model_render_no_fields():
    rendered = render_model_file({}, "MyModel")

    assert rendered == (
        "from django.db import models\n"
        "\n"
        "\n"
        "class MyModel(models.Model):\n"
        "    pass\n"
        "\n"
        "    def __str__(self) -> str:\n"
        '        return "MyModel"\n'
    )


def test_model_renders_with_fields():
    fields = {
        "field1": "MyDBField",
    }
    rendered = render_model_file(fields, "MyModel")
    assert rendered == (
        "from django.db import models\n"
        "\n"
        "\n"
        "class MyModel(models.Model):\n"
        "    field1 = models.MyDBField()\n"
        "\n"
        "    def __str__(self) -> str:\n"
        '        return "MyModel"\n'
    )
