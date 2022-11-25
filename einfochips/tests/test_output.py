import unittest
from einfochips.output.html import *
from einfochips.output.utils import *

#
# Test methods for einfochips/output
#
class TesteinfoOutput(unittest.TestCase):

    ########################################
    # html.py
    ########################################

    def test_html_report(self):
        test_html = HTMLReport(report_name='test')
        assert (test_html.report_name == 'test')
        assert ('json' in test_html.get_content_from_folder(templates_type='conditionals'))
        assert ('json' in test_html.get_content_from_file(filename='/json_format.html'))

    def test_get_filename(self):
        assert ('einfochips-report/report.html' in get_filename("REPORT"))
        assert ('einfochips-report/einfochips-results/einfochips_results.js' in get_filename("RESULTS"))
        assert ('einfochips-results/einfochips_results.js' in get_filename("RESULTS", relative_path=True))
        assert ('einfochips-report/einfochips-results/einfochips_exceptions.js' in get_filename("EXCEPTIONS"))
        assert ('einfochips-results/einfochips_exceptions.js' in get_filename("EXCEPTIONS", relative_path=True))
        assert ('einfochips-report/einfochips-results/einfochips_errors.json' in get_filename("ERRORS"))
        assert ('einfochips-results/einfochips_errors.json' in get_filename("ERRORS", relative_path=True))
