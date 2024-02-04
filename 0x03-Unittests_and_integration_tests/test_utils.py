#!/usr/bin/env python3
"""this is utils test module"""
import unittest
from utils import access_nested_map
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
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception(self,
                            nested_map: Mapping,
                            path: Sequence,
                            expected_exception_msg: str) -> None:
        '''Test that KeyError is raised with expected message'''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        actual_exception_msg = str(context.exception)
        self.assertEqual(actual_exception_msg, expected_exception_msg)
