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

class wiring:
	
	def __init__(self,length,width,height):
		self.length = length
		self.width = width
		self.height = height
		self.vol = 0
		self.wiring_slack = 0
		self.total_wiring = 0
		
	def calc_wiring(self):		
		# check for zeroes
		if self.length == 0 or self.width == 0 or self.height == 0:
			self.total_wiring = 0				
			self.total_shielding = 0
		# check for non integers				
		elif not(isinstance(self.length,int)) or not(isinstance(self.width,int)) or not(isinstance(self.height,int)):
			self.total_wiring = 0	
		# if all integers calculate Wiring
		else:
			self.wiring_cube_side_sizes = [self.length,self.width,self.height]
			self.sort_wiring_cube_side_sizes = sorted(self.wiring_cube_side_sizes)
			self.wiring_cube_smallest_side = self.sort_wiring_cube_side_sizes[0]
			self.wiring_cube_second_smallest_side = self.sort_wiring_cube_side_sizes[1]
			
			self.vol = self.length * self.width * self.height
			self.wiring_slack = (2*self.wiring_cube_smallest_side) + (2*self.wiring_cube_second_smallest_side)
			self.total_wiring = self.vol + self.wiring_slack
			
		return self.total_wiring
