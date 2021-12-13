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

class shielding:
	
	def __init__(self,length,width,height):
		self.length = length
		self.width = width
		self.height = height
		self.shielding_cube_area = 0
		self.shielding_cube_left_side_area = 0
		self.shielding_cube_top_side_area = 0
		self.shielding_cube_front_side_area = 0
		self.total_shielding = 0

	def calc_shielding(self):

		# check for zeroes
		if self.length == 0 or self.width == 0 or self.height == 0:
			self.total_shielding = 0
		# check for non integers				
		elif not(isinstance(self.length,int)) or not(isinstance(self.width,int)) or not(isinstance(self.height,int)):
			self.total_shielding = 0	
		# if all integers calculate shielding
		else:
			self.shielding_cube_left_side_area = self.length * self.width
			self.shielding_cube_top_side_area = self.width * self.height
			self.shielding_cube_front_side_area = self.length * self.height	
			self.shielding_cube_area = (2*self.shielding_cube_left_side_area) + (2*self.shielding_cube_top_side_area) + (2*self.shielding_cube_front_side_area)

			list_of_shielding_cube_areas = []
			list_of_shielding_cube_areas = [int(self.shielding_cube_left_side_area),int(self.shielding_cube_top_side_area),int(self.shielding_cube_front_side_area)]
			list_of_shielding_cube_areas_sorted = sorted(list_of_shielding_cube_areas)
			wiring_slack = list_of_shielding_cube_areas_sorted[0]
			
			self.total_shielding = self.shielding_cube_area + wiring_slack		
		
		return self.total_shielding


