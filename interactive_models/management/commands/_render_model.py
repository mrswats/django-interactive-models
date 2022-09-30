from typing import Dict, Optional

from django.template import loader

TEMPLATE_NAME = "model_template.py.template"


def render_model_file(raw_fields: Dict[str, Optional[str]], model_name: str) -> str:
    fields = ("\n" + " " * 4).join(
        f"{key} = models.{value}()" for key, value in raw_fields.items() if value is not None
    )

    ctx = {
        "fields": fields or "pass",
        "model_name": model_name,
    }

    return loader.render_to_string(TEMPLATE_NAME, context=ctx)[:-1]
