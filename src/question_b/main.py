#add import


import unittest

from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

        def test_get_person_category(self):
            self.assertEqual("child", test_get_person_category(2))
            self.assertEqual("teenager", test_get_person_category(14))
            self.assertEqual("adult",test_get_person_category(20))
            self.assertEqual("infant", test_get_person_category(1))