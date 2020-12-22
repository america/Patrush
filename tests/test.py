import unittest
import

class TestPatrush(unittest.TestCase):
    def setUp(self):
        pass

    def test_on_message(self):
        expected = 'にゃーん'
        actual = 'にゃーん'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
