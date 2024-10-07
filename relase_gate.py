import unittest
from ReadNetList import *

class MyTestCase(unittest.TestCase):
    def test_class_gate(self):
        logic_gate = Gates("AND", [1,2],3)
        self.assertEqual(logic_gate.gate_type, "AND")  # add assertion here

    def test_sim(self):
        sim = Simulator("s27.txt", "0001010")
        sim.Run()

if __name__ == '__main__':
    unittest.main()
