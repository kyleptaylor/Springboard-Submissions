from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import string

class FlaskTests(TestCase):
    def setUp(self):
        """Set up test client and configure app for testing."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        app.config['SECRET_KEY'] = 'testkey'
    
    def test_render_board(self):
        """Test if the boggle board is generated and stored in session."""
        with self.client:
            # Test initial board generation
            response = self.client.get('/boggle')
            self.assertIn(b'<div class="boggle-board">', response.data)
            self.assertIn('board', session)
            self.assertEqual(len(session['board']), 5)
            self.assertEqual(len(session['board'][0]), 5)

            # Test if board is not regenerated when already in session
            old_board = session['board']
            response = self.client.get('/boggle')
            self.assertEqual(session['board'], old_board)

            # Test if the board is regenerated with the restart flag
            response = self.client.get('/boggle?restart=true')
            self.assertNotEqual(session['board'], old_board)
            self.assertEqual(len(session['board']), 5)
            self.assertEqual(len(session['board'][0]), 5)
            json_response = response.get_json()
            self.assertIn('board', json_response)

    def test_answer(self):
        """Test the answer validation and scoring."""
        with self.client:
            # Generate a board and store in session
            response = self.client.get('/boggle')
            session['board'] = [['T', 'E', 'S', 'T'],
                                ['A', 'B', 'C', 'D'],
                                ['E', 'F', 'G', 'H'],
                                ['I', 'J', 'K', 'L']]

            # Test a valid word
            response = self.client.post('/answer', json={
                'word': 'test',
                'words': [],
            })
            json_response = response.get_json()
            self.assertEqual(json_response['result'], 'ok')
            self.assertEqual(json_response['word'], 'test')
            self.assertEqual(json_response['points'], 4)

            # Test a word not on the board
            response = self.client.post('/answer', json={
                'word': 'wrong',
                'words': [],
            })
            json_response = response.get_json()
            self.assertEqual(json_response['result'], 'not-on-board')

            # Test an invalid word
            response = self.client.post('/answer', json={
                'word': 'invalidword',
                'words': [],
            })
            json_response = response.get_json()
            self.assertEqual(json_response['result'], 'not-on-board')

            # Test error when board is not in session
            session.pop('board', None)  # Clear the board from session
            response = self.client.post('/answer', json={
                'word': 'test',
                'words': [],
            })
            self.assertEqual(response.status_code, 400)
            json_response = response.get_json()
            self.assertEqual(json_response['error'], 'Board not found in session')

