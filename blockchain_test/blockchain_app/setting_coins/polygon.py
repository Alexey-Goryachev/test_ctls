from blockchain_app.settings import YAML_CONFIGS_DIR
from . utils import EnvParser


polygon = EnvParser(f"{YAML_CONFIGS_DIR}/polygon.yaml")