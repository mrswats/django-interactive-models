# Django Interactive Models

This app provides a CLI through the `manage.py` script to create models from the command line.

## Usage:

Install the package into the virtualenv:

```
pip install django-interactive-models
```

Then, add the app to the INSTALLED_APPS in settings:

```python
INSTALLED_APPS = [
    ...
    "interactive_models",
    ...
]
```

Then, you can finally run the `models` command like:

```console
./manage.py models <app_name> <model_name> <field_name>:<field_type> ...
```

Check the usage by using the `-h` flag.

For example, this command:

```console
./manage.py models my_app MyModel number:int text:text page_url:url creation_date:datetime
```

Will create a `models.py` file inside my_app with the fields
`number, text, page_url, creation_date` with their corresponding django database fields.

### Field types available:

This is the current list of accepted types and their mappings

- auto -> AutoField,
- bool -> BooleanField,
- char -> CharField,
- date -> DateField,
- datetime -> DateTimeField,
- email -> EmailField,
- float -> FloatField,
- int -> IntegerField,
- slug -> SlugField,
- text -> TextField,
- time -> TimeField,
- url -> URLField,
- uuid -> UUIDField,
- bigauto -> BigAutoField,
- bigint -> BigIntegerField,
- binary -> BinaryField,
- decimal -> DecimalField,
- duration -> DurationField,
- genericip -> GenericIPAddressField,
- image -> ImageField,
- nullbool -> NullBooleanField,
- positiveint -> PositiveIntegerField,
- positivesmallint -> PositiveSmallIntegerField,
- smallint -> SmallIntegerField,