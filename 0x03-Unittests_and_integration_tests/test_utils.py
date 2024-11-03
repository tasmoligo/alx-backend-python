#!/usr/bin/env python3
"""
test_utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


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
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), keyError),
        ({"a": 1}, ("a", "b"), keyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that a KeyError is raised for the above inputs
        """
        with self.assertRises(expected) as output:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Inherits from unittest.TestCase
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """
        Test that utils.get_json returns the expected result.
        """
        mockOutput = Mock()
        mockOutput.json.return_value = expected
        with patch('requests.get', return_value=mockOutput):
            response = get_json(url)
            self.assertEqual(response, expected)


class TestMemoize(unittest.TestCase):
    """
    Memoization test class
    """
    def test_memoize(self):
        """
        Method for testing memoization
        """
        class TestClass:
            """ Class in method """
            def a_method(self):
                """ A test method """
                return 42

            @memoize
            def a_property(self):
                """ A test method """
                return self.a_method()

        testObj = TestClass()
        with patch.object(testObj, 'a_method') as mockMethod:
            mockMethod.return_value = 42
            first = testObj.a_property
            second = testObj.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mockMethod.assert_called_once()
