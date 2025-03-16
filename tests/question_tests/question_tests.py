#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

        def test_get_person_category(self):
            self.assertEqual("child", test_get_person_category(5))
            self.assertEqual("teenager", test_get_person_category(15))
            self.assertEqual("adult",test_get_person_category(38))
            self.assertEqual(infant, test_get_person_category(.5))



            

