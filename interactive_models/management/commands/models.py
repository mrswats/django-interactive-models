import os
from typing import Any

from django.core.management.base import BaseCommand, CommandError, CommandParser

from ._check_models_file import check_models_file
from ._parse_fields import parse_fields
from ._render_model import render_model_file


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            dest="app_name",
            help="App label where the model will be created in",
            type=str,
        )
        parser.add_argument(
            "model_name",
            help="Name of the model",
            type=str,
        )
        parser.add_argument(
            "model_fields",
            nargs="*",
            help="List of model fields with their corresponding type separated by colon.",
            type=str,
        )
        parser.add_argument(
            "--override",
            default=False,
            action="store_true",
            help="Override existing files",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        app_name = options["app_name"]
        model_name = options["model_name"]

        models_path = f"{app_name}/models.py"

        if not os.path.isdir(app_name):
            error_msg = (
                f"'{app_name}' does not exist!\n"
                "Create a new app by running:\n"
                f"  $ ./manage.py startapp {app_name}\n"
            )
            raise CommandError(error_msg)

        if not options["override"] and check_models_file(models_path):
            error_msg = (
                f"Not overriding '{models_path}'\nuse `--override` to override this behavior"
            )
            raise CommandError(error_msg)

        fields = parse_fields(options["model_fields"])
        file_contents = render_model_file(fields, model_name)

        with open(f"{app_name}/models.py", "w") as fileobj:
            fileobj.writelines(file_contents)

        self.stdout.write(f"Generated {app_name}/models.py!")
