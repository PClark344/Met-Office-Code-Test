###################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    TestShieldingAndWiringData.py
# 
# PROGRAM DETAILS: Met Office Coding Exercise
#                  Shielding and Wiring Required for a Satellite
# DOCS:            As specified in: 
#                  https://github.com/mo-rjr/shielding-and-wiring 
#
# PURPOSE:         To test the modules in the Program
#                  PaulClarkMetOfficeShieldingAndWiringExercise.py
#
# DATE:            18 October 2021 
# 
# VERSION:         1.0
#
#################################################################

import unittest
import PaulClarkMetOfficeShieldingAndWiringExercise as CalcSat

class TestData(unittest.TestCase):

### test output of shielding and wiring functions #####################

    def test_shielding(self):
        self.assertEqual(CalcSat.calc_shielding(2,3,4),58)
        
    def test_wiring(self):
        self.assertEqual(CalcSat.calc_wiring(2,3,4),68)
      
if __name__ == '__main__':
    unittest.main()
