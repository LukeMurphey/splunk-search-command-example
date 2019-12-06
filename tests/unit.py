
import unittest
import errno
import sys
import os
import re

sys.path.append( os.path.join("..", "src", "bin") )
sys.path.append( os.path.join("..", "src", "bin", "search_command_example_app") )

from search_command_example_app.search_command import SearchCommand

class TestSearchCommand(unittest.TestCase):
    """
    Test the ability to construct the search command.
    """

    def test_construct(self):
        """
        Make sure the search command can be constructed.
        """
        search_command = SearchCommand()
        self.assertIsNotNone(search_command)

if __name__ == "__main__":
    unittest.main()
