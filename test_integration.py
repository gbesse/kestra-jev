import pathlib
import unittest
import yaml

class FlowTest(unittest.TestCase):
    def test_flow_contract(self):
        flow = yaml.safe_load(pathlib.Path('flow.yaml').read_text())
        self.assertEqual('io.kestra.plugin.scripts.python.Script',flow['tasks'][0]['type'])
        self.assertIn('JEV_API_KEY',flow['tasks'][0]['env'])
