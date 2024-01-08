#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


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

        #get_JSON
# class TestGetJson(unittest.TestCase):
#     """Get JSON parameterization"""
#     @patch('utils.requests')
#     def test_get_json(self, mock_request):
#         """JSON Mocking"""
#         mock_reponse = MagicMock()
#         mock_reponse.json.return_value = {}
