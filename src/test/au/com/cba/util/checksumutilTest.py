import unittest

from src.main.au.com.cba.util.checksumutil import calculatechecksum


class CheckSumUtilTest(unittest.TestCase):

    def test_calculatechecksum_handleException(self):
        chceksum_value = calculatechecksum("somePath")
        self.assertEqual(None, chceksum_value)

    def test_calculatechecksum(self):
        import unittest.mock as um
        with um.patch('builtins.open', um.mock_open(read_data=b'some data')):
            chceksum_value = calculatechecksum("somePath")
            self.assertEqual("1e50210a0202497fb79bc38b6ade6c34", chceksum_value)


if __name__ == '__main__':
    unittest.main()
