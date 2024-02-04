#!/usr/bin/env python3
"""this is utils test module"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    '''test object for access nested map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
                            self, nested_map: Mapping,
                            path: Sequence,
                            expected_result: Any) -> None:
        '''this is access nestd map test'''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected_exception_msg: str) -> None:
        '''Test that KeyError is raised with expected message'''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        expected_repr = f"'{expected_exception_msg}'"
        actual_repr = str(context.exception)
        self.assertEqual(expected_repr, actual_repr)


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test that utils.get_json returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """ Testing Memoize object instance"""

    def test_memoize(self):
        """test memoize"""

        class TestClass:
            """ Test object instance for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
