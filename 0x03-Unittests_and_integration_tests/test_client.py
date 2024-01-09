#!/usr/bin/env python3
"""github orgs client"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """github test case"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, orgs: str, mock_request: patch):
        """Test that the method org returns the required result"""

        url = f"https://api.github.com/orgs/{orgs}"
        mock_request.return_value = {"key": "value"}

        instance = GithubOrgClient(orgs)

        result: Dict = instance.org
        self.assertEqual(result, {"key": "value"})
        mock_request.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Used to unit-test the GithubOrgsClient._public_repos_url property"""
        with patch.object(GithubOrgClient, 'org') as git:
            git.return_value = {'key': 'value'}
            instance = GithubOrgClient('google')
            result: str = instance._public_repos_url

            self.assertEqual(result, git['key'])
