from blockchain_app.settings import YAML_CONFIGS_DIR
from . utils import EnvParser


usdt_polygon = EnvParser(f"{YAML_CONFIGS_DIR}/usdt_polygon.yaml")
