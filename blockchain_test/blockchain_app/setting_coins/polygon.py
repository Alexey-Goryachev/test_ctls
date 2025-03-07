from blockchain_app.settings import YAML_CONFIGS_DIR
from setting_coins.utils import EnvParser


polygon = EnvParser(f"{YAML_CONFIGS_DIR}/polygon.yaml")