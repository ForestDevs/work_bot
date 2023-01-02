from dotenv import dotenv_values

config = dotenv_values('.env')


def get_config() -> dict[str, str | None]:

    for key, value in config.items():
        if value == "":
            exception = "%s is empty!" % key
            raise Exception(exception)

    return config
