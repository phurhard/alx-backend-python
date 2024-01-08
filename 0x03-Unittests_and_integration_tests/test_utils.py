#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Base class for utilsnestedmap testing"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
         ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Method to test the nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Returns a KeyError because the keys path is not  available"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        exception = context.exception
        self.assertEqual(exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """Get JSON parameterization"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, url, test_payload, mock_request):
        """JSON Mocking"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_request.return_value = mock_response
        result = get_json(url)

        self.assertEqual(result, test_payload)
        mock_request.assert_called_once_with(url)
