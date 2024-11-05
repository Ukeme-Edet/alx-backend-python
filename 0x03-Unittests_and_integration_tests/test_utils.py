#!/usr/bin/env python3
"""
Test cases for utils.py
"""
from unittest import TestCase
import unittest
from utils import access_nested_map, memoize
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


class TestGetJson(TestCase):
    """Test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests):
        """Test get_json"""
        mock_requests.return_value = Mock(ok=True)
        mock_requests.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(TestCase):
    """Test memoize"""

    def test_memoize(self):
        """Test memoize"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        self.assertEqual(test_instance.a_property, 42)
        with patch.object(test_instance, "a_method") as mock_method:
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_not_called()


if __name__ == "__main__":
    unittest.main()
