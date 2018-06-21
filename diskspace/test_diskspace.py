
import unittest

from diskspace import diskspace

class TestDiskspaceMethods(unittest.TestCase):

    def test_subprocess_check_output(self):
        abs_directory = os.path.abspath('')
        cmd = 'du -d 1 ' + abs_directory

        result = subprocess.check_output(cmd.strip().split(' '))
        command = subprocess_check_output('du -d 1 {}'.format(abs_directory))

        self.assertEqual(command, result)

    def test_bytes_to_readable(self):
        command = bytes_to_readable(256)
        self.assertEqual(command, '128.00Kb')
        self.assertNotEqual(command, '256.00Kb')


suite = unittest.TestLoader().loadTestsFromTestCase(TestDiskspaceMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
