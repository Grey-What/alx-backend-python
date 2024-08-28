#!/usr/bin/env python3
"""test module for client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, Mock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """test class for GithubOrgClient"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected: dict, mocked_get_json: MagicMock) -> None:
        """test org"""
        mocked_get_json.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient(org)

        self.assertEqual(client.org(), expected)
        mocked_get_json.assert_called_once_with("https://api.github.com/orgs/{}".format(org))
