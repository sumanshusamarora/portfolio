"""
Config load
"""
import ast
import os

import yaml

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(THIS_DIR, "..", "..", "config")

for filename in os.listdir(CONFIG_DIR):
    if ".local" in filename:
        config_filename = filename
        break
    else:
        config_filename = filename

CONFIG_FILE = os.path.join(CONFIG_DIR, config_filename)

with open(CONFIG_FILE, "r") as configfile:
    config = yaml.safe_load(configfile)

def try_environ_else_config(
    environ_key, config_key=None, default=None, convert_to_if_environ=None
):
    """

    :param environ_key:
    :param config_key:
    :param default:
    :param convert_to_if_environ: A conversion method
    :return:
    """
    if config_key is None:
        config_key = environ_key

    return_value = None

    if os.environ.get(environ_key):
        return_value = os.environ.get(environ_key)
        if convert_to_if_environ is not None:
            return_value = convert_to_if_environ(return_value)

    if return_value is None:
        return_value = config.get(config_key)

    if return_value is None and default is not None:
        return_value = default

    return return_value

# Secret Key
config["SECRET_KEY"] = try_environ_else_config(environ_key="SECRET_KEY")

# DEBUG
if os.environ.get("DEBUG"):
    config["DEBUG"] = ast.literal_eval(os.environ.get("DEBUG"))
if config.get("DEBUG") is None:
    if "insecure" in config["SECRET_KEY"]:
        config["DEBUG"] = True
    else:
        config["DEBUG"] = False


# DATABASES
if not config.get("DATABASES"):
    config["DATABASES"] = {
        "default": {"ENGINE": "django.db.backends.postgresql_psycopg2"}
    }

if os.environ.get("DB_NAME"):
    config["DATABASES"]["default"]["NAME"] = os.environ.get("DB_NAME").strip()

if os.environ.get("DB_PASSWORD"):
    config["DATABASES"]["default"]["PASSWORD"] = os.environ.get("DB_PASSWORD").strip()

if os.environ.get("DB_HOST"):
    config["DATABASES"]["default"]["HOST"] = os.environ.get("DB_HOST").strip()

if os.environ.get("DB_USER"):
    config["DATABASES"]["default"]["USER"] = os.environ.get("DB_USER").strip()

if os.environ.get("DB_PORT"):
    config["DATABASES"]["default"]["PORT"] = os.environ.get("DB_PORT").strip()

if os.environ.get("DB_SCHEMA"):
    config["DATABASES"]["default"]["OPTIONS"] = {
        "options": f"-c search_path={os.environ.get('DB_SCHEMA')}"
    }
