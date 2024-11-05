#!/usr/bin/env python3
"""
Test cases for utils.py
"""
from unittest import TestCase
import unittest
from utils import access_nested_map
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, path, expected):
        """Test get_json"""
        mock = Mock()
        mock.json.return_value = expected
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(path), expected)


if __name__ == "__main__":
    unittest.main()
