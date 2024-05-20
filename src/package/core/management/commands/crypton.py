from package.conf.settings import CRYPTON_TOKEN_PATH
from package.core.management.base import BaseCommand
from package.services.criptografia.crypton import Crypton


class Crypt(BaseCommand):
    """Executa o crypton."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gerenate_key()
        self.crypton = Crypton(Crypton.read_token_file(CRYPTON_TOKEN_PATH))

    def gerenate_key(self):
        if not (CRYPTON_TOKEN_PATH).exists():
            Crypton.gen_key(to_file=CRYPTON_TOKEN_PATH)

    def help(self):
        """Retorna a descrição do comando."""
        return "Executa o crypton."

    def add_arguments(self, parser):
        """Adiciona argumentos ao comando."""
        parser.add_argument("--encrypt_file", help="Encripta o arquivo passado por argumento.")
        parser.add_argument("--decrypt_file", help="Decripta o arquivo passado por argumento.")
        parser.add_argument("--encrypt_content", help="Encripta o arquivo passado por argumento.")
        parser.add_argument("--decrypt_content", help="Decripta o arquivo passado por argumento.")
        parser.add_argument("--genkey", action="store_true", help="Gera chave aleatória")

    def handle(self, *args):
        """Executa o comando."""
        args = args[0]

        if args.encrypt_file:
            self.crypton.encrypt_file(args.encrypt_file)
        elif args.decrypt_file:
            self.crypton.decrypt_file(args.decrypt_file)
        elif args.encrypt_content:
            print(self.crypton.encrypt_content(args.encrypt_content))
        elif args.decrypt_content:
            print(self.crypton.decrypt_content(args.decrypt_content))
        elif args.genkey:
            Crypton.gen_key(to_file=CRYPTON_TOKEN_PATH)
        else:
            self._logger.info(f"Este comando não é um comando do Crypon.")
