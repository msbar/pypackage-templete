import sys
from unittest import mock

import pytest
from package.apps.cli.cli import Cli


@pytest.fixture
def cli():
    return Cli()

def test_no_command(cli):
    with mock.patch('sys.argv', ['cli.py']):
        with mock.patch('argparse.ArgumentParser.print_help') as mock_print_help:
            cli.run()
            mock_print_help.assert_called_once()

def test_start_project_command(cli):
    with mock.patch('sys.argv', ['cli.py', 'startproject']):
        with mock.patch.object(cli.commands[0], 'handle', return_value=None) as mock_handle:
            cli.run()
            mock_handle.assert_called_once()

def test_run_command(cli):
    with mock.patch('sys.argv', ['cli.py', 'run']):
        with mock.patch.object(cli.commands[1], 'handle', return_value=None) as mock_handle:
            cli.run()
            mock_handle.assert_called_once()

def test_crypt_command(cli):
    with mock.patch('sys.argv', ['cli.py', 'crypt']):
        with mock.patch.object(cli.commands[2], 'handle', return_value=None) as mock_handle:
            cli.run()
            mock_handle.assert_called_once()
