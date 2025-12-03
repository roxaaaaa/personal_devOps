import unittest
from unittest.mock import patch
import sys

import main


class TestAgeGuessingGame(unittest.TestCase):

    def test_all_incorrect_guesses(self):
        inputs = ["10", "20", "5"]

        with patch("builtins.input", side_effect=inputs):
            
            try:
                main.start_game(19, 3)
            except SystemExit:
                self.fail("start_game() should not exit on failure.")


    def test_invalid_input(self):
        inputs = ["abc", "abc", "o"]

        with patch("builtins.input", side_effect=inputs):
            try:
                main.start_game(19, 3)
            except SystemExit:
                self.fail("SystemExit should not be raised for invalid input.")


if __name__ == "__main__":
    unittest.main()
