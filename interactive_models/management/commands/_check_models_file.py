import ast
import os


def _file_exists(path: str) -> bool:
    return os.path.exists(path)


def _file_does_not_contain_models(path: str) -> bool:
    with open(path) as fileobj:
        file_contents = fileobj.read()

    models_ast = ast.parse(file_contents)

    return any(
        type(statement) not in (ast.Import, ast.ImportFrom) for statement in models_ast.body
    )


def check_models_file(path: str) -> bool:
    return _file_exists(path) and _file_does_not_contain_models(path)
