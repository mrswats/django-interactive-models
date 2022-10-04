from typing import Dict, Optional

db_fields = {
    "auto": "AutoField",
    "bigauto": "BigAutoField",
    "bigint": "BigIntegerField",
    "binary": "BinaryField",
    "bool": "BooleanField",
    "char": "CharField",
    "date": "DateField",
    "datetime": "DateTimeField",
    "decimal": "DecimalField",
    "duration": "DurationField",
    "email": "EmailField",
    "file": "FileField",
    "filepath": "FilePathField",
    "float": "FloatField",
    "genericip": "GenericIPAddressField",
    "image": "ImageField",
    "int": "IntegerField",
    "nullbool": "NullBooleanField",
    "positiveint": "PositiveIntegerField",
    "positivesmallint": "PositiveSmallIntegerField",
    "slug": "SlugField",
    "smallint": "SmallIntegerField",
    "text": "TextField",
    "time": "TimeField",
    "url": "URLField",
    "uuid": "UUIDField",
}


def parse_fields(raw_fields: str) -> Dict[str, Optional[str]]:
    fields_dict = dict(field.split(":") for field in raw_fields)
    return {
        field_name.strip(): db_fields.get(db_field.strip())
        for field_name, db_field in fields_dict.items()
    }
