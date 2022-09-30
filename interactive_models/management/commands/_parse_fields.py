from typing import Dict, Optional

db_fields = {
    "auto": "AutoField",
    "bool": "BooleanField",
    "char": "CharField",
    "date": "DateField",
    "datetime": "DateTimeField",
    "email": "EmailField",
    "float": "FloatField",
    "int": "IntegerField",
    "slug": "SlugField",
    "text": "TextField",
    "time": "TimeField",
    "url": "URLField",
    "uuid": "UUIDField",
}


def parse_fields(raw_fields: str) -> Dict[str, Optional[str]]:
    fields_dict = dict(field.split(":") for field in raw_fields)
    return {field_name: db_fields.get(db_field) for field_name, db_field in fields_dict.items()}
