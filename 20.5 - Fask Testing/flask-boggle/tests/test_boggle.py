from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import string

class TestBoggle(TestCase):

    def setUp(self):
        """Set up a Boggle instance for testing."""
        self.boggle = Boggle()
        self.test_board = [
            ['T', 'E', 'S', 'T', 'E'],
            ['A', 'B', 'C', 'D', 'F'],
            ['G', 'H', 'I', 'J', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U']
        ]

    def test_read_dict(self):
        """Test that the dictionary is read correctly."""
        words = self.boggle.read_dict("words.txt")
        self.assertIn("test", words)  # Assuming "TEST" is in the words.txt
        self.assertIn("hello", words) # Assuming "HELLO" is in the words.txt
        self.assertNotIn("XYZXYZ", words)  # Assuming "XYZXYZ" is not in words.txt

    def test_make_board(self):
        """Test that the board is generated correctly."""
        board = self.boggle.make_board()
        self.assertEqual(len(board), 5)
        self.assertEqual(len(board[0]), 5)
        for row in board:
            for letter in row:
                self.assertIn(letter, string.ascii_uppercase)

    def test_check_valid_word_ok(self):
        """Test that a valid word returns 'ok'."""
        self.boggle.words = ["TEST"]  # Simulate a dictionary with just "TEST"
        result = self.boggle.check_valid_word(self.test_board, "TEST")
        self.assertEqual(result, "ok")

    def test_check_valid_word_not_on_board(self):
        """Test that a word in the dictionary but not on the board returns 'not-on-board'."""
        self.boggle.words = ["NOTONBOARD"]
        result = self.boggle.check_valid_word(self.test_board, "NOTONBOARD")
        self.assertEqual(result, "not-on-board")

    def test_check_valid_word_not_in_dict(self):
        """Test that a word not in the dictionary returns 'not-word'."""
        self.boggle.words = ["HELLO"]
        result = self.boggle.check_valid_word(self.test_board, "TESTING")
        self.assertEqual(result, "not-word")

    def test_find_word_on_board(self):
        """Test finding a word that is on the board."""
        result = self.boggle.find(self.test_board, "TEST")
        self.assertTrue(result)

    def test_find_word_not_on_board(self):
        """Test finding a word that is not on the board."""
        result = self.boggle.find(self.test_board, "HELLO")
        self.assertFalse(result)

    def test_find_diagonal_word_on_board(self):
        """Test finding a word that is diagonally placed on the board."""
        board = [
            ['H', 'E', 'L', 'L', 'O'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'W', 'X', 'X'],
            ['X', 'X', 'X', 'O', 'X'],
            ['X', 'X', 'X', 'X', 'R']
        ]
        result = self.boggle.find(board, "HELLO")
        self.assertTrue(result)