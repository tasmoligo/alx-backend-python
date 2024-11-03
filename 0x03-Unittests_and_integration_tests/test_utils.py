#!/usr/bin/env python3
"""
test_utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that the method returns what it is supposed to
        """
        self.assertEqual(test_access_nested_map(nested_map, path), expected)
