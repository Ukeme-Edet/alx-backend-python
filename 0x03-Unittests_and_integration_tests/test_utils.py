#!/usr/bin/env python3
"""
Test cases for utils.py
"""
from unittest import TestCase
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """Test access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([{}, ("a",)], [1, ("a", "b")])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
