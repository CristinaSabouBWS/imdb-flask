# from config import ConfigurationSet, config_from_env, config_from_yaml

import os

PREFIX = "imdb_flask"


def config():
    env = os.environ.get("imdb_flask", "local")
    dict(env=env)
    # return ConfigurationSet(
    #     config_from_env(prefix=PREFIX),
    #     # config_from_yaml(f"{ROOT_PATH}/src/flashy/configuration/{env}.yml", read_from_file=True),
    # )
