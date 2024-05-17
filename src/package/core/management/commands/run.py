from package.core.management.base import BaseCommand
from package.core.management.commands.start_project import StartProject
from package.main import main


class Run(BaseCommand):
    """Executa o programa principal do projeto."""

    def help(self):
        """Retorna a descrição do comando."""
        return "Executa o programa principal do projeto."

    def add_arguments(self, parser):
        """Adiciona argumentos ao comando."""
        pass

    def handle(self, *args):
        """Executa o comando."""
        StartProject().handle()
        main(args)
