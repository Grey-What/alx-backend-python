#!/usr/bin/env python3
"""module contains test case for utils.access_nested_map"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """test cases for utils.access_nested_map"""
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test access_nested_map exception"""
        with self.assertRaises(KeyError) as context_manager:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test cases for utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json method returns the expected result"""
        mock_reponse = Mock()
        mock_reponse.json.return_value = test_payload

        with patch("requests.get", return_value=mock_reponse):
            result = get_json(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """test cases for memoize decorator"""
    def test_memoize(self):
        """test memoize decorator"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_object = TestClass()

        with patch.object(test_object, 'a_method') as mock_method:
            mock_method.return_value = 42

            first = test_object.a_property
            second = test_object.a_property

            mock_method.assert_called_once()
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
