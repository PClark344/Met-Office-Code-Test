##################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    Wiring.py
# 
# PROGRAM DETAILS: Met Office Coding Test
#                  Calculation of Wiring Required for a Satellite
#
# PURPOSE:         To calculate total required for
#                  Wiring and Wiring Slack for satellites
#                  as described in
#                  https://github.com/mo-rjr/shielding-and-wiring 
#
# DATE:            13 December 2021 
# 
# VERSION:         1.0
################################################################## 

import Box

class wiring:
	
	def __init__(self, box):
		self.box = box
		
	def calc_wiring(self):		

		volumeOfBox = self.box.getVolume()
		slack = self.box.getSmallestCircumference()
		return volumeOfBox + slack