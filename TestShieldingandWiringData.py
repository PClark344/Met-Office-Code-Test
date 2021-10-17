#testing code
# unittest

import unittest
import PaulClarkMetOfficeShieldingAndWiringExercise as CalcSat

class TestData(unittest.TestCase):

    def test_shielding(self):
        self.assertEqual(CalcSat.calc_shielding(2,3,4),58)
        
    #def test_rectangle(self):
        #self.assertEqual(shape_area.rectangle(6,7),42)
        
    #def test_square(self):
       #self.assertEqual(shape_area.square(7),49)
        
if __name__ == '__main__':
    unittest.main()
