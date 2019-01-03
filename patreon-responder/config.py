import os


def _get_config_env(key):
    """
    Check the environment variables for the key.
    """
    return os.getenv(key)


def _get_config_env_file(key):
    """
    Check the environment variables for the key with the
    suffix of "_file" and if it is set then read the file.
    """
    filename = os.getenv(key + "_file")
    if not filename:
        return None
    with open(filename) as file:
        return file.read()


SECRET_LOCATIONS = [
    "/run/secrets/",
    "/var/openfaas/secrets/",
]


def _get_config_secret_locations(key):
    """
    Check the folders listed in SECRET_LOCATIONS for a file
    named the same as the key and return its contents.
    """
    for prefix in SECRET_LOCATIONS:
        filename = prefix+key
        if os.path.isfile(filename):
            with open(filename) as file:
                return file.read()
    return None


AVAILABLE_LOOKUPS = [
    _get_config_env,
    _get_config_env_file,
    _get_config_secret_locations,
]


def get_config(key, default=None):
    for lookup in AVAILABLE_LOOKUPS:
        ret = lookup(key)
        if ret is not None:
            return ret
    return default
