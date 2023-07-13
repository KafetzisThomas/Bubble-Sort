#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from main import bubble_sort

class ReversedTestCase(unittest.TestCase):
  """Tests for 'main.py'"""

  def test_empty_list(self):
    """Test reverse sorting an empty list"""
    input_list = []
    expected_list = []
    self.assertEqual(bubble_sort(input_list), expected_list)

  def test_reversed_sorted_list(self):
    """Test reverse sorting a pre-reverse sorted list"""
    input_list = [19, 18, 13, 8, 6, 2]
    expected_list = [19, 18, 13, 8, 6, 2]
    self.assertEqual(bubble_sort(input_list), expected_list)

  def test_reversed_unsorted_list(self):
    """Test reverse sorting an unstorted list"""
    input_list = [2, 6, 8, 13, 18, 19]
    expected_list = [19, 18, 13, 8, 6, 2]
    self.assertEqual(bubble_sort(input_list), expected_list)

  def test_list_with_duplicates(self):
    """Test reverse sorting a list with duplicate numbers"""
    input_list = [19, 13, 19, 6, 2, 18, 13, 8]
    expected_list = [19, 19, 18, 13, 13, 8, 6, 2]
    self.assertEqual(bubble_sort(input_list), expected_list)

if __name__ == '__main__':
  unittest.main()
