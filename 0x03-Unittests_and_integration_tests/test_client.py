#!/usr/bin/env python3
"""github orgs client"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """github test case"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, orgs, mock_request):
        """Test that the method org returns the required result"""

        mock_request.return_value = {"key": "value"}

        instance = GithubOrgClient(orgs)

        result = instance.org
        self.assertEqual(result, {"key": "value"})
        mock_request.assert_called_once_with(f"\
            https://api.github.com/orgs/{orgs}")
