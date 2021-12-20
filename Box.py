import constant

class box:
	
	def __init__(self,length,width,height):
		self.length = length
		self.width = width
		self.height = height


	def isValid(self):
		return self.__check_dimensions()


	def getVolume(self):

		return self.height * self.width * self.length


	def getArea(self):

		return	(2 * self.height * self.width) + \
				(2 * self.height * self.length) + \
				(2 * self.width * self.length)


	def getSmallestSideArea(self):

		smallestSides = self.__get_two_smallest_sides()
		return smallestSides[0] * smallestSides[1]


	def getSmallestCircumference(self):

		smallestSides = self.__get_two_smallest_sides()
		return (2 * smallestSides[0]) + (2 * smallestSides[1])
		
	def __get_two_smallest_sides(self):

		sort_side_sizes = sorted([self.height, self.length, self.width])
		smallest = sort_side_sizes[0]
		next_smallest = sort_side_sizes[1]
		return smallest, next_smallest


	def __check_dimensions(self):

		if not(isinstance(self.length,int)) or not(isinstance(self.width,int)) or not(isinstance(self.height,int)):
			return constant.BOX_ERROR_NON_INTEGER	

		elif self.length == 0 or self.width == 0 or self.height == 0:
			return constant.BOX_ERROR_ZERO_VALUE

		return constant.BOX_DIMENSIONS_OK
