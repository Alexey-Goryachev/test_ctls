from blockchain_app.settings import YAML_CONFIGS_DIR
from . utils import EnvParser


tron = EnvParser(f"{YAML_CONFIGS_DIR}/tron.yaml")