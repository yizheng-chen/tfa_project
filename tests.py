import main
import json
import unittest


class Test(unittest.TestCase):

    def test_id(self):
        result = main.main_def()
        t_result = json.loads(s=result)
        ch = t_result["characterizations"]
        self.assertEqual(ch[3]["id"], 3)


    def test_singer(self):
        result = main.main_def()
        t_result = json.loads(s=result)
        ch = t_result["characterizations"]
        self.assertEqual(ch[3]["artist"], "Jeff Beck")

    def test_name(self):
        result = main.main_def()
        t_result = json.loads(s=result)
        ch = t_result["characterizations"]
        self.assertEqual(ch[3]["title"], "All Shook Up")
#length
    def test_length(self):
        result = main.main_def()
        t_result = json.loads(s=result)
        ch = t_result["characterizations"]
        self.assertEqual(len(ch), 1001)


if __name__ == '__main__':
    unittest.main()
