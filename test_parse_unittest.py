import unittest
from logparser_bit import string_parse
from hypothesis import given
from hypothesis.strategies import text


class TestParser(unittest.TestCase):
    def test_correct_equal_sign(self):
        self.assertEqual(string_parse(r'a|b b|cc|d d d|e|f|g| key1=value1 key2=valu  \=  e2   key3=value3 keyN=valueN')
                         , {'key2': 'valu  =  e2  ',
                            'param4': 'd d d',
                            'param7': 'g',
                            'key1': 'value1',
                            'param2': 'b b',
                            'param3': 'cc',
                            'param6': 'f',
                            'param1': 'a',
                            'param5': 'e',
                            'keyN': 'valueN',
                            'key3': 'value3'}, "Something Wrong")

    def test_without_pairs(self):
        self.assertEqual(string_parse(r'a|b b|cc|d d d|e|f|g|'), {'param5': 'e',
                                                                  'param4': 'd d d',
                                                                  'param2': 'b b',
                                                                  'param1': 'a',
                                                                  'param3': 'cc',
                                                                  'param6': 'f',
                                                                  'param7': 'g'}, "Something Wrong")

    def test_blank(self):
        self.assertEqual(string_parse(''), '', "Your function is wrong")

    def test_only_pipes(self):
        self.assertEqual(string_parse("|||||||"), {'param2': '',
                                                   'param1': '',
                                                   'param4': '',
                                                   'param7': '',
                                                   'param3': '',
                                                   'param6': '',
                                                   'param5': ''}, "Your function is wrong")

    def test_correct_pipes(self):
        self.assertEqual(string_parse(r'\|\|\|aa|b b b|c|d\| \| |vvvvv|g||'), {'param2': 'b b b',
                                                                               'param3': 'c',
                                                                               'param7': '',
                                                                               'param6': 'g',
                                                                               'param1': '|||aa',
                                                                               'param4': 'd| | ',
                                                                               'param5': 'vvvvv'},
                         "Your function is wrong")

    def test_wrong_string(self):
        self.assertEqual(r'a|b b|cc|d d d|e|f|g| key1=value1 ke=y2=value2 key3=value3 keyN=valueN',
                         r'a|b b|cc|d d d|e|f|g| key1=value1 ke=y2=value2 key3=value3 keyN=valueN',
                         "Your function don't work correct")

    def test_also_wrong_string(self):
        self.assertEqual(r'a|b | b|cc|d d d|e|f|g| key1=value1 key2=value2 key3=value3 keyN=valueN',
                         r'a|b | b|cc|d d d|e|f|g| key1=value1 key2=value2 key3=value3 keyN=valueN',
                         "Your function don't work correct")

    @given(text())
    def some_sort_of_random_data(self,s):
        self.assertEqual(string_parse(s), s, "Ooopss")


if __name__ == '__main__':
    unittest.main()
