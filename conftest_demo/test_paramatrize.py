#!/usr/bin/env/python
# -*-coding:utf-8-*-

import pytest


@pytest.mark.parametrize("test_input, expected", [
    ("3+5", 8),
    ("6/2", 3),
    ("6*2", 12)
])
def test_parameter(test_input, expected):
    assert eval(test_input) == expected
