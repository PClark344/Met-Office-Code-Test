##################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    Shielding.py
# 
# PROGRAM DETAILS: Met Office Coding Test
#                  Shielding Required for a Satellite
#
# PURPOSE:         To calculate total area required for
#                  Shielding and Slack for satellites
#                  as described in
#                  https://github.com/mo-rjr/shielding-and-wiring 
#
# DATE:            08 December 2021 
# 
# VERSION:         1.0
################################################################## 

import Box

class shielding:
	
	def __init__(self, box):
		self.box = box

	def calc_shielding(self):

		areaOfBox = self.box.getArea()
		slack = self.box.getSmallestSideArea()
		return areaOfBox + slack


