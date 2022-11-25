
import unittest
from einfochips.core.conditions import pass_condition
from einfochips.core.cli_parser import *
from einfochips.core.console import prompt, prompt_overwrite, prompt_value

#
# Test methods for einfochips/core
#
class TesteinfoCore(unittest.TestCase):

    ########################################
    # cli_parser.py
    ########################################

    def test_argument_parser(self):
        test_arguments = einfochipsArgumentParser()
        assert (test_arguments.parser._subparsers.title == 'The provider you want to run einfo against')
        assert (test_arguments.subparsers._choices_actions[0].help == 'Run einfo against an Amazon Web Services account')
        assert (test_arguments.subparsers._choices_actions[1].help == 'Run einfo against a Google Cloud Platform account')
        assert (test_arguments.subparsers._choices_actions[2].help == 'Run einfo against a Microsoft Azure account')
        assert (test_arguments.subparsers._choices_actions[3].help == 'Run einfo against an Alibaba Cloud account')
        assert (test_arguments.subparsers._choices_actions[4].help == 'Run einfo against an Oracle Cloud Infrastructure account')

    ########################################
    # console.py
    ########################################

    def test_prompt(self):
        assert (prompt('test') == 'test')
        assert (prompt(['test']) == 'test')

    def test_prompt_overwrite(self):
        assert (prompt_overwrite('', True, None))

    def test_prompt_value(self):
        assert (prompt_value(question='', max_laps=1, test_input='test', is_question=True, choices=['test']) is None)
        assert (prompt_value(question='', max_laps=1, test_input='test', is_question=True, choices=['test'], no_confirm=True) == 'test')
