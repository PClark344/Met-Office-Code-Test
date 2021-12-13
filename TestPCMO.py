###################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    TestPCMO.py
# 
# PROGRAM DETAILS: Met Office Coding Exercise
#                  Shielding and Wiring Required for a Satellite
# DOCS:            As specified in: 
#                  https://github.com/mo-rjr/shielding-and-wiring 
#
# PURPOSE:         To test the modules in the Program
#                  PaulClarkMetOfficeSWCEOONew.py
#
# DATE:            02 December 2021 
# 
# VERSION:         1.0
#
#################################################################

import unittest
import Shielding
import Wiring

class TestData(unittest.TestCase):

### test output of shielding and wiring functions #####################

    #@unittest.skip('Skipping Test Shielding')
    def test_shielding(self):
        shield_1 = Shielding.shielding(2,3,4)
        self.assertEqual(shield_1.calc_shielding(),58)
 
        return
        
    #@unittest.skip('Skipping Test Shielding Zero Edge Conditions')
    def test_shielding_zero_conditions(self):
        shield_1 = Shielding.shielding(2,3,0)
        self.assertEqual(shield_1.calc_shielding(),0)
        shield_1 = Shielding.shielding(2,0,4)
        self.assertEqual(shield_1.calc_shielding(),0)
        shield_1 = Shielding.shielding(0,2,4)
        self.assertEqual(shield_1.calc_shielding(),0)
               
        return
 
    #@unittest.skip('Skipping Test Shielding Non Integer Input')
    def test_shielding_non_int_conditions(self):
        shield_1 = Shielding.shielding(2,3,4.1)
        self.assertEqual(shield_1.calc_shielding(),0)
        shield_1 = Shielding.shielding(2,3.0,4)
        self.assertEqual(shield_1.calc_shielding(),0)
        shield_1 = Shielding.shielding(2.0,3,4)
        self.assertEqual(shield_1.calc_shielding(),0)
               
        return       

   #@unittest.skip('Skipping Test Shielding Non Numeric Input')
    def test_shielding_non_num_conditions(self):
        shield_1 = Shielding.shielding(2,3,'a')
        self.assertEqual(shield_1.calc_shielding(),0)
        shield_1 = Shielding.shielding(2,'a',4)
        self.assertEqual(shield_1.calc_shielding(),0)
        shield_1 = Shielding.shielding('a',3,4)
        self.assertEqual(shield_1.calc_shielding(),0)
               
        return       
 
 
    #@unittest.skip('Skipping Test Wiring')
    def test_wiring(self):
        wire_1 = Wiring.wiring(2,3,4)
        self.assertEqual(wire_1.calc_wiring(),34)
        
        return

    #@unittest.skip('Skipping Test Wiring Zero Edge Conditions')
    def test_wiring_zero_conditions(self):
        wire_1 = Wiring.wiring(2,3,0)
        self.assertEqual(wire_1.calc_wiring(),0)
        wire_1 = Wiring.wiring(2,0,4)
        self.assertEqual(wire_1.calc_wiring(),0)
        wire_1 = Wiring.wiring(0,3,4)
        self.assertEqual(wire_1.calc_wiring(),0)
               
        return
        
    #@unittest.skip('Skipping Test Wiring Non Integer Input')
    def test_wiring_non_int_conditions(self):
        shield_1 = Wiring.wiring(2,3,4.1)
        self.assertEqual(shield_1.calc_wiring(),0)
        shield_1 = Wiring.wiring(2,3.1,4)
        self.assertEqual(shield_1.calc_wiring(),0)
        shield_1 = Wiring.wiring(2.1,3,4)
        self.assertEqual(shield_1.calc_wiring(),0)
               
        return       

    #@unittest.skip('Skipping Test wiring Non Numeric Input')
    def test_wiring_non_num_conditions(self):
        shield_1 = Wiring.wiring(2,3,'a')
        self.assertEqual(shield_1.calc_wiring(),0)
        shield_1 = Wiring.wiring(2,'a',4)
        self.assertEqual(shield_1.calc_wiring(),0)
        shield_1 = Wiring.wiring('a',3,4)
        self.assertEqual(shield_1.calc_wiring(),0)
           
if __name__ == '__main__':
    unittest.main()
