# -*- coding:utf-8 -*-
## encoding = utf-8


import unittest
import random


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

if __name__ == '__main__':
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    #将多个测试类加载到测试套件中
    suite = unittest.TestSuite([testCase1,testCase2])
    unittest.TextTestRunner(verbosity=2).run(suite)