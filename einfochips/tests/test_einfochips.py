import subprocess
import unittest
from unittest import mock

import pytest
from einfochips.__main__ import run_from_cli
from einfochips.core.console import set_logger_configuration


class TesteinfochipsClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        set_logger_configuration(is_debug=True)
        cls.has_run_einfo_chips = False

    @pytest.mark.xfail("only runs with AWS, cannot be used dynamically")
    @staticmethod
    def call_einfo_chips(args):
        args = ['./einfo.py'] + args

        args.append('aws')

        if TesteinfochipsClass.profile_name:
            args.append('--profile')
            args.append(TesteinfochipsClass.profile_name)
        # TODO: FIXME this only tests AWS

        args.append('--force')
        args.append('--debug')
        args.append('--no-browser')
        if TesteinfochipsClass.has_run_einfo_chips:
            args.append('--local')
        TesteinfochipsClass.has_run_einfo_chips = True

        sys = None
        with mock.patch.object(sys, 'argv', args):
            return run_from_cli()

    def test_einfo_chips_help(self):
        """Make sure that einfochips does not crash with --help"""
        command = './einfo.py --help'
        process = subprocess.Popen(command, shell=True, stdout=None)
        process.wait()
        assert process.returncode == 0

    @pytest.mark.xfail
    def test_einfo_chips_default_run(self):
        """Make sure that einfochips's default run does not crash"""
        rc = self.call_einfo_chips([])
        assert (rc == 0)
