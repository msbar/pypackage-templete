import argparse

from package.core.management.commands.crypton import Crypt
from package.core.management.commands.run import Run
from package.core.management.commands.start_project import StartProject


class Cli:
    """Clase para o comando cli."""

    def __init__(self):
        """Inicializa a classe."""
        start_project = StartProject()
        start_project.handle()
        
        self.commands = [StartProject, Run, Crypt]

    def get_parser(self):
        """Retorna o parser."""
        parser = argparse.ArgumentParser(prog="CLI", description="Comandos de terminal.")
        subparsers = parser.add_subparsers(dest="command")

        for command in self.commands:
            cmd = command()
            command_parser = subparsers.add_parser(
                cmd.__class__.__name__.lower(),
                help=cmd.help(),
                description=cmd.help(),
            )
            command_parser.set_defaults(command=cmd)
            cmd.add_arguments(command_parser)

        return parser

    def run(self):
        """Executa o comando."""
        parser = self.get_parser()
        args = parser.parse_args()

        if not args.command:
            parser.print_help()
        else:
            args.command.handle(args)


def main():
    """Executa o comando."""
    Cli().run()


if __name__ == "__main__":
    main()
