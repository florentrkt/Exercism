from isogram import*

import unittest

class TestIsogram(unittest.TestCase):
	
	def test_is_isogram(self):
		self.assertTrue(is_isogram('lumberjacks'))

	def test_is_isogram(self):
		self.assertTrue(is_isogram('background'))

	def test_is_isogram(self):
		self.assertTrue(is_isogram('downstream'))

	def test_is_not_isogram(self):
		self.assertFalse(is_isogram('isograms'))

if __name__ == '__main__':
    unittest.main()

