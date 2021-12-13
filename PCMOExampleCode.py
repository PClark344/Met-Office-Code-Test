##################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    PCMOExampleCode.py
# 
# PROGRAM DETAILS: Met Office Coding Test
#                  Shielding and Wiring Required for a Satellite
#				   Object Orientated Program
#
# PURPOSE:         To calculate total area required for
#                  Shielding and Slack for satellites
#                  Plus length of wiring needed for each box
# DOCS:            As specified in: 
#                  https://github.com/mo-rjr/shielding-and-wiring 
#
# DATE:            06 December 2021 
# 
# VERSION:         1.1
# NEW:             Calculations for shielding and wiring 
#                  In the modules Wiring.py and Shielding.py
#
# INPUT FILES:     example1.txt, example2.txt and example3.txt
# OUTPUT FILE:     results.md
# TEST FILE:       TestShieldingandWiringData.py
#
#################################################################

# import code

from os import path
from sys import exit
import Shielding
import Wiring

# Constants

col1_spaces = 12
col2_spaces = 9
col3_spaces = 6
		
output_file_name = 'results.md'
input_file_list = ['example1.txt','example2.txt','example3.txt']

# check input files exist

for input_file_name in input_file_list:
	if path.exists(input_file_name):
		pass
	else:
		print('Input file ',input_file_name,' does not exist')
		exit()

# write output file hdr

with open(output_file_name,'w') as f:
	f.write('My results for example files: \n')
	f.write('\n')	
	f.write('| file         | shielding | wiring | \n')	
	f.write('| ------------ | --------- | ------ | \n')				
		
# process input files data

for input_file_name in input_file_list:

	with open(input_file_name) as f:
		shield_area_grand_total = 0
		wire_length_grand_total = 0
		
		textlines = f.readlines()

		for textline in textlines:	
			shield_area= 0
			wire_vol= 0			
			data_line = textline.rstrip('\n')
			data_line = data_line.rstrip(' ')
			data_line = data_line.lstrip(' ')
			data_line = data_line.split('x')				
	
			length = int(data_line[0])
			width = int(data_line[1])
			height = int(data_line[2])
			#print(length,width,height)

			shield = Shielding.shielding(length,width,height)
			shield_area_total = shield.calc_shielding()
			shield_area_grand_total = shield_area_grand_total + shield_area_total

			wire = Wiring.wiring(length,width,height)
			wire_length_total = wire.calc_wiring()
			wire_length_grand_total = wire_length_grand_total + wire_length_total	

		# write out file data
		wire_str = str(wire_length_grand_total)
		shield_str = str(shield_area_grand_total)

		res_line = ''
		res_line = ('| ' + input_file_name.ljust(col1_spaces) + ' | ' + shield_str.ljust(col2_spaces) + ' | ' + wire_str.ljust(col3_spaces) + ' | ' + '\n')

		with open(output_file_name,'a') as f:
			f.write(res_line)		
