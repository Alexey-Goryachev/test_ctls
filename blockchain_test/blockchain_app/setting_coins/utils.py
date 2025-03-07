from yaml import safe_load

class EnvParser:

    def __init__(self, filename) -> None:
        with open(filename, 'r') as yaml_file:
            config = safe_load(yaml_file.read())
            for k, v in config.items():
                setattr(self, k, v)
