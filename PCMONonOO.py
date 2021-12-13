###################################################################
# AUTHOR:          PAUL DAVID CLARK
#
# PROGRAM NAME:    PCMONonOO.py
# 
# PROGRAM DETAILS: Met Office Coding Test
#                  Shielding and Wiring Required for a Satellite
#
# PURPOSE:         To calculate total area required for
#                  Shielding and Slack for satellites
#                  Plus length of wiring needed for each box
# DOCS:            As specified in: 
#                  https://github.com/mo-rjr/shielding-and-wiring 
#
# DATE:            18 October 2021 
# 
# VERSION:         1.0
#
# INPUT FILES:     example1.txt, example2.txt and example3.txt
# OUTPUT FILE:     results.md
# TEST FILE:       TestShieldingandWiringData.py
#
#################################################################

### Initialise Variables ########################################

length = 0
width = 0
height = 0
individual_area = 0
all_total_areas = 0
input_file_list = []
newerline_sorted = []
input_file_name = ''
res_line = ''

### define output file varaiables ###########################

col1_spaces = 12
col2_spaces = 9
col3_spaces = 6
output_file_name = 'results.md'

### Define input files ############################################

input_file_list = ['example1.txt','example2.txt','example3.txt']
	
#### Produce Sorted Data #################

def sort_dataline(newline):	
	global newline_sorted

	list_of_integers = [int(i) for i in newline]
	newline_sorted = sorted(list_of_integers)
	
	return newline_sorted
	
### Get dimensions for shielding cube ###########################

def get_dimensions(newline):
	global length
	global width
	global height

	length = int(newline[0])
	width = int(newline[1])
	height = int(newline[2])
	
	return length,width,height

### Calculate side areas and total area ###########################

def calc_shielding(length, width, height):
	global individual_total_area
	
	individual_area = 0
	slack = 0
	left_side_area = 0
	top_side_area = 0
	front_side_area = 0
	
	left_side_area = length * width
	top_side_area = width * height
	front_side_area = length * height	

	individual_area = (2*left_side_area) + (2*top_side_area) + (2*front_side_area)
	
### Find Slack Provision for Shielding ###############################

	list_of_areas = []
	list_of_areas = [int(left_side_area),int(top_side_area),int(front_side_area)]
	list_of_areas_sorted = sorted(list_of_areas)
	
	slack = list_of_areas_sorted[0]
		
	individual_total_area = individual_area + slack
		
	return individual_total_area

### Calculate volumes and slack for wiring length ####################

def calc_wiring(length, width, height):
	global individual_total_wiring_length
	individual_vol = 0
	wiring_slack = 0
	smallest_side = 0
	second_smallest_side = 0
	
	individual_vol = length * width * height
					
### Find wiring Slack and wiring length ##############################

	smallest_side = int(newline_sorted[0])
	second_smallest_side = int(newline_sorted[1])

	wiring_slack = (2*smallest_side) + (2*second_smallest_side)
	
	individual_total_wiring_length = individual_vol + wiring_slack
		
	return individual_total_wiring_length


### MAIN BODY #####################################################

try:
	
### Write header to output file ###################################

	with open(output_file_name,'w') as f:
		f.write('My results for example files: \n')
		f.write('\n')	
		f.write('| file         | shielding | wiring | \n')	
		f.write('| ------------ | --------- | ------ | \n')		
	
### Read Input file ###################################

	for input_file_name in input_file_list:
		with open(input_file_name) as f:
			textlines = f.readlines()	

### Process each line in Input file #################################

		all_total_areas = 0
		all_total_wiring_lengths = 0

		for textline in textlines:	

### cut out spaces and delimiters ###################################

			newline = textline.rstrip('\n')
			newline = newline.rstrip(' ')
			newline = newline.lstrip(' ')
			newline = newline.split('x')
				
			sort_dataline(newline)

### check for wrong data or data types then do calculations ##########
			
			get_dimensions(newline)
			if length == 0 or width == 0 or height == 0:
				individual_total_area = 0
				individual_total_wiring_length = 0				
			elif not(isinstance(length,int) or isinstance(width,int) or isinstance(height,int)):
				individual_total_area = 0
				individual_total_wiring_length = 0	
			else:
				calc_shielding(length,width,height)
				all_total_areas = all_total_areas + individual_total_area
				calc_wiring(length,width,height)
				all_total_wiring_lengths = all_total_wiring_lengths + individual_total_wiring_length

### Format output results and write to file ############################

		wire_str = str(all_total_wiring_lengths)
		shield_str = str(all_total_areas)
		res_line = ''
		res_line = ('| ' + input_file_name.ljust(col1_spaces) + ' | ' + shield_str.ljust(col2_spaces) + ' | ' + wire_str.ljust(col3_spaces) + ' | ' + '\n')

		with open(output_file_name,'a') as f:
			f.write(res_line)
	
### Exception Handling ############################################

except Exception as e:
	if IOError:
		print("Error reading or writing files")
		print("Check input and output file names are correct")
		print('Also please check that all input data is the correct type of data')
		print('In Input file each line should have format intxintxint')
	elif ValueError:
		print('A wrong data type has been found in the program')
	else:
		print("Error - ", e.__class__, " has occurred. \n")
	
	print("The program will now finish")
	print("Press Return to continue")
	input('')
	
#### end of program - check all files closed ########################		

finally:
	f.close()
	print('Program finished ')
	

		

