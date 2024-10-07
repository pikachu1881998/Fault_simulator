import unittest
from ReadNetList import *

class MyTestCase(unittest.TestCase):
    def test_class_gate(self):
        logic_gate = Gates("AND", [1,2],3)
        self.assertEqual(logic_gate.gate_type, "AND")  # add assertion here

    def test_sim_s27(self):
        input_Str = ["0001010","0001010","1010101","0110111","1010001"]
        for i in input_Str:
            sim = Simulator("s27.txt", i)
            sim.Run()

    def test_sim_s298f_2(self):
        input_Str = ["10101010101010101",
                    "01011110000000111",
                    "11111000001111000",
                    "11100001110001100",
                    "01111011110000000"]
        for i in input_Str:
            sim = Simulator("s298f_2.txt", i)
            sim.Run()

    def test_sim_s344f_2(self):
        input_Str = ["101010101010101011111111",
                    "010111100000001110000000",
                    "111110000011110001111111",
                    "111000011100011000000000",
                    "011110111100000001111111"]
        for i in input_Str:
            sim = Simulator("s344f_2.txt", i)
            sim.Run()

    def test_sim_s349f_2(self):
        input_Str = ["101010101010101011111111",
                    "010111100000001110000000",
                    "111110000011110001111111",
                    "111000011100011000000000",
                    "011110111100000001111111"]
        for i in input_Str:
            sim = Simulator("s349f_2.txt", i)
            sim.Run()


if __name__ == '__main__':
    unittest.main()
