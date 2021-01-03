#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import MagicMock
from patrush import *
import asyncio

class TestPatrush(unittest.TestCase):
    def setUp(self):
        pass

    # ケース１　BOTなら無視する
    # returnでNoneが返却されることを確認する
    def test_on_message_case01(self):
        case01Mock = MagicMock()
        case01Mock.author.bot = True
        loop = asyncio.get_event_loop()
        actual = loop.run_until_complete(on_message(case01Mock))
        print("☆☆☆ on_messageの戻り値 ☆☆☆")
        print(actual)
        print("☆☆☆☆☆☆")
        
        expected = None

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
