import concurrent.futures
import os
import shutil
import subprocess
import venv


def remove(path: str):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except IsADirectoryError:
        shutil.rmtree(path)


def setup_venv():
    envelope_builder = venv.EnvBuilder(system_site_packages=False, with_pip=True)
    envelope_builder.create(VENV_PATH)


def install_package(package_name: str):
    subprocess.call([PIP_PATH, "install", package_name])


def install_package_tuple(package_tuple: tuple[str, ...]):
    thread_pool = concurrent.futures.ThreadPoolExecutor()
    for package in package_tuple:
        thread_pool.submit(lambda: install_package(package))
    thread_pool.shutdown(wait=True)


def create_api_documentation():
    remove(API_DOCUMENTATION_PATH)
    subprocess.call(
        [
            SPHINX_APIDOC_PATH,
            "--tocfile",
            API_DOCUMENTATION_TREE_NAME,
            "-M",
            "-d",
            "2",
            "--implicit-namespaces",
            "-E",
            "-o",
            API_DOCUMENTATION_PATH,
            MUTWO_PATH,
        ]
    )


SPHINX_VERSION = "4.5.0"

VENV_PATH = "virtualenv"
BIN_PATH = f"{VENV_PATH}/bin"
PIP_PATH = f"{BIN_PATH}/pip3"
SPHINX_APIDOC_PATH = f"{BIN_PATH}/sphinx-apidoc"
SPHINX_BUILD_PATH = f"{BIN_PATH}/sphinx-build"
SITE_PACKAGES_PATH = f"{VENV_PATH}/lib/python3.9/site-packages"
MUTWO_PATH = f"{SITE_PACKAGES_PATH}/mutwo"

DOCUMENTATION_PATH = "."
SPHINX_OUTPUT_PATH = "{DOCUMENTATION_PATH}/_build"
API_DOCUMENTATION_PATH = f"{DOCUMENTATION_PATH}/api"
API_DOCUMENTATION_TREE_NAME = "api_documentation"

# List of all acceptable mutwo packages
MUTWO_PACKAGE_TUPLE = (
    "mutwo.ext-core",
    "mutwo.ext-music",
    "mutwo.ext-common-generators",
    "mutwo.ext-mbrola",
    "mutwo.ext-csound",
    "mutwo.ext-reaper",
    "mutwo.ext-midi",
    "mutwo.ext-isis",
    "mutwo.ext-abjad",
    "mutwo.ext-ekmelily",
)

SPHINX_PACKAGE_TUPLE = (
    f"sphinx=={SPHINX_VERSION}",
    "sphinx-autodoc-annotation==1.0-1",
    "autodocsumm==0.2.4",
    "insipid-sphinx-theme==0.2.8",
)

setup_venv()
install_package_tuple(MUTWO_PACKAGE_TUPLE + SPHINX_PACKAGE_TUPLE)
subprocess.call([PIP_PATH, '-r', 'requirements.txt'])
create_api_documentation()
