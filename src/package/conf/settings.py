from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
CRYPTON_TOKEN_PATH = BASE_DIR / "token.crypton"
DOTENV_PATH = Path(".env")
DATAFILES_PATH = BASE_DIR / "datafiles"
LOGS_PATH = BASE_DIR / "logs"
