import unittest
from pydicttoxml import dict2xml


class TestDictToXML(unittest.TestCase):

    def test_dict2xml(self):
        d = {
            'student': {
                'name': 'Shera',
                'age': 25,
                'address': {
                    'pin': 500082,
                    'city': 'Hyderabad',
                    'state': 'telangana',
                    'country': 'India'
                }
            }
        }
        xml = dict2xml(d, root_tag_name="data")
        exp_data = "<?xml version='1.0' encoding='utf-8'?><data><student><name>Shera</name><address><pin>500082</pin><state>telangana</state><city>Hyderabad</city><country>India</country></address><age>25</age></student></data>"


if __name__ == '__main__':
    unittest.main()
