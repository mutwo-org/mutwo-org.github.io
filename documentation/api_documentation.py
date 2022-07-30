import os

VENV_PATH = f"{os.path.abspath('./')}/virtualenv"
SITE_PACKAGES_PATH = f"{VENV_PATH}/lib/python3.9/site-packages"
MUTWO_PATH = f"{SITE_PACKAGES_PATH}/mutwo"


def make_api_documentation():
    from mutwo_autodocument import __main__
    __main__.main()
