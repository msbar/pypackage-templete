import logging
from logging.handlers import RotatingFileHandler

from package.conf.settings import (
    CRYPTON_TOKEN_PATH,
    DATAFILES_PATH,
    DOTENV_PATH,
    LOGS_PATH,
)
from package.conf.templates.dotenv_template import DOTENV_TEMPLATE
from package.core.management.base import BaseCommand
from package.services.criptografia.crypton import Crypton


class StartProject(BaseCommand):
    """Cria a estrutura inicial do projeto."""

    def setup_logger(self):
        """Cria um logger para o projeto."""
        handler_formatter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        # Adiciona um stream handler para logar no console.
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter(handler_formatter))

        # Adiciona um rotating file handler para logar em arquivo.
        file_handler = RotatingFileHandler(LOGS_PATH / "package.log", maxBytes=10 * 1024 * 1024, backupCount=5)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(handler_formatter))

        # Configura o logging básico
        logging.basicConfig(level=logging.INFO, encoding="utf-8", handlers=[stream_handler, file_handler])

    def create_token_crypton(self):
        """Cria o token do crypton."""
        if not (CRYPTON_TOKEN_PATH).exists():
            Crypton.gen_key(to_file=CRYPTON_TOKEN_PATH)

    def create_dot_env(self):
        """Cria o arquivo .env."""
        if DOTENV_PATH.exists():
            return
        with open(DOTENV_PATH, "w") as f:
            f.write(DOTENV_TEMPLATE.strip())

    def create_datafiles(self):
        """Cria a pasta datafiles."""
        if not DATAFILES_PATH.exists():
            DATAFILES_PATH.mkdir()

    def create_logs(self):
        """Cria a pasta logs."""
        if not LOGS_PATH.exists():
            LOGS_PATH.mkdir()

    def help(self):
        """Retorna a descrição do comando."""
        return "Cria a estrutura inicial do projeto."

    def add_arguments(self, parser):
        """Adiciona argumentos ao comando."""
        pass

    def handle(self, *args):
        """Executa o comando."""
        self.create_token_crypton()
        self.setup_logger()
        self.create_dot_env()
        self.create_datafiles()
        self.create_logs()
