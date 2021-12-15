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
import Box
import constant
from unittest.mock import MagicMock

class TestData(unittest.TestCase):

### test output of shielding and wiring functions #####################

    def test_box_isValid_when_all_dimensions_non_zero_returns_valid(self):
        
        # Arrange
        box = Box.box(1,2,3)

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_DIMENSIONS_OK, result)

    def test_box_isValid_when_length_zero_returns_error(self):
        
        # Arrange
        box = Box.box(0,2,3)

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_ERROR_ZERO_VALUE, result)

    def test_box_isValid_when_width_zero_returns_error(self):
        
        # Arrange
        box = Box.box(2,0,3)

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_ERROR_ZERO_VALUE, result)

    def test_box_isValid_when_height_zero_returns_error(self):

        # Arrange
        box = Box.box(2,3,0)

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_ERROR_ZERO_VALUE, result)

    def test_box_isValid_when_length_not_integer_returns_error(self):
        
        # Arrange 
        box = Box.box("a",2,3)

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_ERROR_NON_INTEGER, result)

    def test_box_isValid_when_width_not_integer_returns_error(self):
        
        # Arrange 
        box = Box.box(2,"a",3)

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_ERROR_NON_INTEGER, result)

    def test_box_isValid_when_height_not_integer_returns_error(self):

        # Arrange
        box = Box.box(2,3,"a")

        # Act
        result = box.isValid()

        # Assert
        self.assertEqual(constant.BOX_ERROR_NON_INTEGER, result)

    def test_box_getArea_returns_correct_result(self):

        # Arrange
        box1 = Box.box(2,3,4)
        box2 = Box.box(1,3,5)

        # Act
        result1 = box1.getArea()
        result2 = box2.getArea()

        # Assert
        self.assertEqual(52, result1)
        self.assertEqual(46, result2)

    def test_box_getVolume_returns_correct_result(self):

        # Arrange
        box1 = Box.box(2,3,4)
        box2 = Box.box(1,3,5)

        # Act
        result1 = box1.getVolume()
        result2 = box2.getVolume()

        # Assert
        self.assertEqual(24, result1)
        self.assertEqual(15, result2)
    
    def test_box_getSmallestSideArea_returns_correct_result(self):

        # Arrange
        box1 = Box.box(2,3,4)
        box2 = Box.box(5,3,1)

        # Act
        result1 = box1.getSmallestSideArea()
        result2 = box2.getSmallestSideArea()

        # Assert
        self.assertEqual(6, result1)
        self.assertEqual(3, result2)

    def test_box_getSmallestCircumference_returns_correct_result(self):

        # Arrange
        box1 = Box.box(2,3,4)
        box2 = Box.box(5,3,1)

        # Act
        result1 = box1.getSmallestCircumference()
        result2 = box2.getSmallestCircumference()

        # Assert
        self.assertEqual(10, result1)
        self.assertEqual(8, result2)

    def test_shielding_calc_shielding_returns_total_area_plus_smallest_side(self):

        # Arrange
        # Mock box class to control values returned
        box = Box.box(0,0,0)
        box.getArea = MagicMock(return_value=22)
        box.getSmallestSideArea = MagicMock(return_value=6)
        shielding = Shielding.shielding(box)

        # Act
        result = shielding.calc_shielding()

        # Assert
        self.assertEqual(28, result)


    def test_wiring_calc_wiring_returns_total_volume_plus_smallest_circumference(self):

        # Arrange
        # Mock box class to control values returned
        box = Box.box(0,0,0)
        box.getVolume = MagicMock(return_value=104)
        box.getSmallestCircumference = MagicMock(return_value=16)
        wiring = Wiring.wiring(box)

        # Act
        result = wiring.calc_wiring()

        # Assert
        self.assertEqual(120, result)
           
if __name__ == '__main__':
    unittest.main()
