#!/usr/bin/env python
import unittest
from mounttab import parse_mounts

class TestMount(unittest.TestCase):
    """
    Our basic test class
    """

    def test_parsemount(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = parse_mounts()
        self.assertIsInstance(result, list)
        #self.assertIsInstance(result[0], tuple)


if __name__ == '__main__':
    unittest.main()