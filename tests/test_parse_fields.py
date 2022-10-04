import pytest
from django.db.models import fields

from interactive_models.management.commands._parse_fields import db_fields, parse_fields

test_fields = ["body:text", "number_of_pages:int", "book_url:url"]

all_raw_fields = [
    "auto : auto",
    "bigauto : bigauto",
    "bigint : bigint",
    "binary : binary",
    "bool : bool",
    "char : char",
    "date : date",
    "datetime : datetime",
    "decimal : decimal",
    "duration : duration",
    "email : email",
    "file : file",
    "filepath : filepath",
    "float : float",
    "genericip : genericip",
    "image : image",
    "int : int",
    "nullbool : nullbool",
    "positiveint : positiveint",
    "positivesmallint : positivesmallint",
    "slug : slug",
    "smallint : smallint",
    "text : text",
    "time : time",
    "url : url",
    "uuid : uuid",
]


@pytest.mark.parametrize("django_field", db_fields.values())
def test_db_fields_exist_in_django(django_field):
    assert hasattr(fields, django_field) or hasattr(fields.files, django_field)


def test_parse_fields_with_empty_input():
    raw_fields = parse_fields([])
    assert raw_fields == {}


def test_all_fields():
    raw_fields = parse_fields(all_raw_fields)
    assert raw_fields == db_fields
