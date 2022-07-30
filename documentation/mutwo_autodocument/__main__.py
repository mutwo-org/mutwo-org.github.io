import os
import shutil


def remove(path: str):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except IsADirectoryError:
        shutil.rmtree(path)


def create_api_documentation():
    from mutwo_autodocument import AutoDocumentedPackage
    import mutwo

    AutoDocumentedPackage(mutwo).export(API_DOCUMENTATION_PATH)


DOCUMENTATION_PATH = f"{os.path.abspath('./')}"
SPHINX_OUTPUT_PATH = "{DOCUMENTATION_PATH}/_build"
API_DOCUMENTATION_PATH = f"{DOCUMENTATION_PATH}/api"
API_DOCUMENTATION_TREE_NAME = "api_documentation"


def main():
    remove(API_DOCUMENTATION_PATH)
    os.mkdir(API_DOCUMENTATION_PATH)
    create_api_documentation()
