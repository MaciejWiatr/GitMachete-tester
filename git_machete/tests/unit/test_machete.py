import unittest
import os
import MacheteSandbox.sandbox.sandboxsetup as sandboxsetup
import urllib.request

Setup = sandboxsetup.SandboxSetup()


class MacheteTester(unittest.TestCase):

    def test_machete(self):
        self.file_directory = os.path.dirname(os.path.abspath(__file__))
        self.url = 'https://gist.githubusercontent.com/MaciejWiatr/95026ffe57b5665eacc542ca6be64d61/raw/46b22f9080a7d3f1c0b6df597a2ebfe7c12db727/correct_output.txt'
        urllib.request.urlretrieve(self.url, './correct_output.txt')
        self.correct_output = os.path.join(
            self.file_directory, 'correct_output.txt')
        with open(self.correct_output) as f:
            self.content = f.read()
        self.assertEqual(Setup.setupSandbox(), self.content)


if __name__ == '__main__':
    unittest.main()
