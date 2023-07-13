import unittest
from main import bubble_sort

class SortedTestCase(unittest.TestCase):
  """Tests for 'main.py'"""

  def test_empty_list(self):
    """Test sorting an empty list"""
    input_list = []
    expected_list = []
    self.assertEqual(bubble_sort(input_list), expected_list)

  def test_sorted_list(self):
    """Test sorting a pre-sorted list"""
    input_list = [2, 6, 8, 13, 18, 19]
    expected_list = [2, 6, 8, 13, 18, 19]
    self.assertEqual(bubble_sort(input_list), expected_list)

  def test_unsorted_list(self):
    """Test sorting an unsorted list"""
    input_list = [19, 13, 6, 2, 18, 8]
    expected_list = [2, 6, 8, 13, 18, 19]
    self.assertEqual(bubble_sort(input_list), expected_list)

  def test_list_with_duplicates(self):
    """Test sorting a list with duplicate numbers"""
    input_list = [19, 13, 19, 6, 2, 18, 13, 8]
    expected_list = [2, 6, 8, 13, 13, 18, 19, 19]
    self.assertEqual(bubble_sort(input_list), expected_list)

if __name__ == '__main__':
  unittest.main()
