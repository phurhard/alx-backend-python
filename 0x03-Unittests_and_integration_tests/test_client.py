#!/usr/bin/env python3
"""github orgs client"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from typing import Dict, List


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

    @patch('client.get_json')
    def test_public_repos(self, mock_request):
        """Unit test public repos
        which is to return a list of repositories"""
        mock_request.return_value = [{'name': 'value1'}, {'name': 'value2'}]
        with patch.object(GithubOrgClient, '_public_repos_url') as git:
            git.return_value = 'url/json'
            instance = GithubOrgClient('google')
            result: List = instance.public_repos()
            self.assertEqual(result, ['value1', 'value2'])
            mock_request.assert_called_once()
            # git.assert_called_once()

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, key, expected):
        """Unit test has license"""
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)


@parameterized_class
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDown()
