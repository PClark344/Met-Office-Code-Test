#testing code
# unittest

import unittest
import PaulClarkMetOfficeShieldingAndWiringExercise as CalcSat

class TestData(unittest.TestCase):

### regular tests #########################################

    def test_shielding(self):
        self.assertEqual(CalcSat.calc_shielding(2,3,4),58)
        
    def test_wiring(self):
        self.assertEqual(CalcSat.calc_wiring(2,3,4),68)
 
        
if __name__ == '__main__':
    unittest.main()
