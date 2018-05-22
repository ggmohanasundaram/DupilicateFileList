import unittest
from unittest import mock
from src.main.au.com.cba.redundantFiles import scanFolders



def mock_open(file,mode="rb"):
    if 'abc' in file:
        content = b'some abc data'
    elif 'bcc' in file:
        content = b'some bcc data'
    return mock.mock_open(read_data=content).return_value


class RedundantFileTest(unittest.TestCase):

    def mock_checkSum(filename):
        if filename == 'abc.txt':
            return '1e50210a0202497fb79bc38b6ade6c34'
        elif filename == 'bcc.txt':
            return 'c472c594e26b766387b8e33ccfe83f9b'

    def test_scanFolders_shouldReturn_Dulicate_files_fornames(self):
        expected_out = {'1e50210a0202497fb79bc38b6ade6c34': ['/root/mohan/abc.txt', '/root/mohan/abc.txt']}
        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [
                ('/root', ('mohan', 'sundar'), ()),
                ('/root/mohan', (), ('abc.txt', 'abc.txt')),
            ]
            with mock.patch('builtins.open', mock.mock_open(read_data=b'some data')):
                actual_output = scanFolders('/root')
                self.assertEqual(expected_out, actual_output)

    def test_scanFolders_shouldReturn_Dulicate_files_forSize(self):
        expected_out = {'1e50210a0202497fb79bc38b6ade6c34': ['/root/mohan/abc.txt', '/root/mohan/ddd.txt']}
        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [
                ('/root', ('mohan', 'sundar'), ()),
                ('/root/mohan', (), ('abc.txt', 'ddd.txt'))

            ]
            with mock.patch('builtins.open', mock.mock_open(read_data=b'some data')):
                actual_output = scanFolders('/root')
                self.assertEqual(expected_out, actual_output)

    def test_scanFolders_shouldReturn_Dulicate_files_differnt_folders(self):
        expected_out = {'f3071c146fa17e18edaf2ee230ee5076': ['/root/mohan/abc.txt', '/root/sundar/abc.txt'],
                        'cca77da1d129bc3f9f3150cea78253b9': ['/root/mohan/bcc.txt', '/root/sundar/bcc.txt']}

        with mock.patch('os.walk') as mockwalk:
            mockwalk.return_value = [
                ('/root', ('mohan', 'sundar'), ()),
                ('/root/mohan', (), ('abc.txt', 'bcc.txt')),
                ('/root/sundar', (), ('abc.txt', 'bcc.txt'))

            ]
            with mock.patch('builtins.open', side_effect=mock_open):
                    actual_output = scanFolders('/root')
                    self.assertEqual(expected_out, actual_output)


