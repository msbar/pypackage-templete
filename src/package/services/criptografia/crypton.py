import logging
import typing
from pathlib import Path

from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)


class Crypton:
    """Classe para criptografia de arquivos e conteúdo."""

    def __init__(self, key: typing.Union[bytes, str]):
        """
        Inicializa a classe de criptografia.

        Args:
            key: Chave de criptografia.
        """
        self.key = key

    @classmethod
    def gen_key(cls, to_file: Path = None) -> bytes:
        """
        Gera uma chave de criptografia.

        Args:
            to_file: Caminho para salvar a chave.
        """
        key = Fernet.generate_key()
        if not to_file:
            return key
        Path(to_file).write_bytes(key)

    @classmethod
    def read_token_file(self, path) -> bytes:
        """
        Lê o conteúdo de um arquivo de token.

        Args:
            path: Caminho para o arquivo de token.
        """
        if isinstance(path, str):
            path = Path(path)
        return path.read_bytes()

    def path_handler(self, path, pattern=None):
        """
        Verifica se o caminho é um diretório ou arquivo.

        Args:
            path: Caminho para o arquivo ou diretório.
            pattern: Padrão de busca para diretórios.
        """
        if isinstance(path, str):
            path = Path(path)
            if path.is_dir():
                pattern = pattern if pattern else "*"
                return list(path.rglob(pattern))
            return [path]
        else:
            if isinstance(path, list):
                return [Path(p) for p in path]
            if path.is_dir():
                pattern = pattern if pattern else "*"
                return list(path.rglob(pattern))
            return [path]

    def _encrypt_file(self, file):
        """
        Encripta um arquivo.

        Args:
            file: Caminho para o arquivo.
        """
        cf = Fernet(self.key)
        file_content = file.read_bytes()
        token = cf.encrypt(file_content)
        file.write_bytes(token)
        return file

    def _decrypt_file(self, file):
        """
        Decripta um arquivo.

        Args:
            file: Caminho para o arquivo.
        """
        cf = Fernet(self.key)
        file_content = file.read_bytes()
        token = cf.decrypt(file_content)
        file.write_bytes(token)
        return file

    def encrypt_file(self, path, pattern=None):
        """
        Encripta um arquivo ou diretório.

        Args:
            path: Caminho para o arquivo ou diretório.
            pattern: Padrão de busca para diretórios.
        """
        pattern = pattern if pattern else "*"
        path_list = self.path_handler(path, pattern)
        result = []
        for path in path_list:
            result.append(self._encrypt_file(path))
        return result

    def decrypt_file(self, path, pattern=None):
        """
        Decripta um arquivo ou diretório.

        Args:
            path: Caminho para o arquivo ou diretório.
            pattern: Padrão de busca para diretórios.
        """
        pattern = pattern if pattern else "*"
        path_list = self.path_handler(path, pattern)
        result = []
        for path in path_list:
            result.append(self._decrypt_file(path))
        return result

    def encrypt_content(self, content):
        """
        Encripta conteúdo.

        Args:
            content: Conteúdo a ser encriptado.
        """
        cf = Fernet(self.key)
        token = cf.encrypt(str.encode(content))
        return token

    def decrypt_content(self, content):
        """
        Decripta conteúdo.

        Args:
            content: Conteúdo a ser decriptado.
        """
        cf = Fernet(self.key)
        decrypted_bytes = cf.decrypt(str.encode(content))
        return decrypted_bytes.decode("utf-8")
