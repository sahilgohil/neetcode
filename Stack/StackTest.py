import unittest
from Stack import evalRPN,generateParenthesis,dailyTemperatures,carFleet,largestRectangleArea
class TestStack(unittest.TestCase):
    def test_eval_RPN(self):
        self.assertEqual(evalRPN(["2","1","+","3","*"]),9)
        self.assertEqual(evalRPN(["4","13","5","/","+"]),6)
    def test_generate_parenthesis(self):
        self.assertEqual(generateParenthesis(3),["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(generateParenthesis(1),["()"])
    def test_daily_temperatures(self):
        self.assertEqual(dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
        self.assertEqual(dailyTemperatures([30,40,50,60]), [1,1,1,0])
    def test_car_fleet(self):
        self.assertEqual(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]), 3)
        self.assertEqual(carFleet(10, [3], [3]),1)
    def test_largest_rectangle_area(self):
        self.assertEqual(largestRectangleArea([2,1,5,6,2,3]),10)
        self.assertEqual(largestRectangleArea([2,4]), 4)

unittest.main()