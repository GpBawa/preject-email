#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_email
----------------------------------

Tests for `email` module.
"""

import unittest

import email


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(email.__version__)

    def tearDown(self):
        pass
