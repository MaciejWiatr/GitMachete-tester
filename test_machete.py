import unittest
import filecmp
import os
import sandboxsetup
import time

Setup = sandboxsetup.SandboxSetup()


class MacheteTester(unittest.TestCase):

    def test_machete(self):
        self.file_directory = os.path.dirname(os.path.abspath(__file__))
        self.correct_output = os.path.join(
            self.file_directory, 'data/correct_output.txt')
        with open(self.correct_output) as f:
            self.content = f.read()
        self.assertEqual(Setup.setupSandbox(), self.content)


if __name__ == '__main__':
    unittest.main()
