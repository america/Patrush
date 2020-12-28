import unittest
from Mock import MagicMock
import patrush


class TestPatrush(unittest.TestCase):
    def setUp(self):
        pass

    # ケース１　BOTなら無視する
    # returnでNoneが返却されることを確認する
    def test_on_message_case01(self):
        case01Mock = MagicMock()
        case01Mock.author.bot = True
        actual = patrush.on_message(case01Mock)
        expected = None

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
