#!/usr/bin/env python3
"""Utils function to test patch, memoize, and parameterize"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """This class defines the memoize usage
    memoize is used as a caching system.
    it is the storing of values/result from a function operation so that
    that result can be reused if the function is called multiple times with
    the same arguments."""
    def test_memoize(self):
        """Test for the memoize decorator"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """A method to return a value 42"""
                return 42

            @memoize
            def a_property(self):
                """The memoize method"""
                return self.a_method()

        @patch('test_utils.TestMemoize.test_memoize.TestClass.a_method')
        def test_function(self, mock_a_method):
            """The test function"""
            # Set up the mock_a_method return value
            mock_a_method.return_value = 42

            # Create an instance of TestClass
            test_instance = TestClass()

            # Call a_property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that a_method was only called once
            mock_a_method.assert_called_once_with(test_instance)

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
