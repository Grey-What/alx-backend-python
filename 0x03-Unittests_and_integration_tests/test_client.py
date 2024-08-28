#!/usr/bin/env python3
"""test module for client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test class for GithubOrgClient"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected: dict,
                 mocked_get_json: MagicMock) -> None:
        """test org"""
        mocked_get_json.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient(org)

        self.assertEqual(client.org(), expected)
        mocked_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))

    def test_public_repos_url(self) -> None:
        """test public_repos_url"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json: MagicMock) -> None:
        """test public_repos"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }

        mocked_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]

            self.assertEqual(GithubOrgClient("google").public_repos(), [
                "episodes.dart",
                "kratu",
            ])
            mock_public_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: dict, license_key: str,
                         expected: bool) -> None:
        """test has_license"""
        org_client = GithubOrgClient("google")
        client_has_license = org_client.has_license(repo, license_key)

        self.assertEqual(client_has_license, expected)
