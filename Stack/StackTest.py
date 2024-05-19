import unittest
from Stack import evalRPN
class TestStack(unittest.TestCase):
    def test_eval_RPN(self):
        self.assertEqual(evalRPN(["2","1","+","3","*"]),9)
        self.assertEqual(evalRPN(["4","13","5","/","+"]),6)

unittest.main()