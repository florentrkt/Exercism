# # Globals for the bearings
# # Change the values as you see fit
# EAST = 'EAST'
# NORTH = 'NORTH'
# WEST = 'WEST'
# SOUTH = 'SOUTH'


# class Robot(object):
#     def __init__(self, bearing=NORTH, x=0, y=0) :
#         self.coordinates = (x,y)
#         self.bearing = bearing
#     def turn_right(self) :
#     	if self.bearing == EAST : 
#     		self.bearing = SOUTH
#     		return self.bearing
#     	elif self.bearing == NORTH : 
#     		self.bearing = EAST
#     		return self.bearing
#     	elif self.bearing == WEST :
#     		self.bearing = NORTH
#     		return self.bearing
#     	elif self.bearing == SOUTH : 
#     		self.bearing = WEST
#     		return self.bearing
#     def turn_left(self) :
#     	if self.bearing == EAST : 
#     		self.bearing = NORTH
#     		return self.bearing
#     	elif self.bearing == NORTH : 
#     		self.bearing = WEST
#     		return self.bearing
#     	elif self.bearing == WEST :
#     		self.bearing = SOUTH
#     		return self.bearing
#     	elif self.bearing == SOUTH : 
#     		self.bearing = EAST
#     		return self.bearing
#     def advance(self) :
#     	if self.bearing == SOUTH : 
#     		x, y = (self.coordinates[0], self.coordinates[1]-1)
#     		self.coordinates = (x, y)
#     		return self.coordinates
#     	elif self.bearing == NORTH :
#     		x, y = (self.coordinates[0], self.coordinates[1]+1)
#     		self.coordinates = (x, y)
#     		return self.coordinates
#     	elif self.bearing == WEST : 
#     		x, y = (self.coordinates[0]-1, self.coordinates[1])
#     		self.coordinates = (x, y)
#     		return self.coordinates
#     	elif self.bearing == EAST :
#     		x, y = (self.coordinates[0]+1, self.coordinates[1])
#     		self.coordinates = (x, y)
#     		return self.coordinates
#     def simulate(self,indication):
#     	for command in indication : 
#     		if command == 'R' : 
#     			self.turn_right()
#     		elif command == 'L' : 
#     			self.turn_left()
#     		elif command == 'A' :
#     			self.advance()
#     	return self.coordinates, self.bearing




NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot(object):
    def __init__(self, bearing = NORTH, x = 0, y = 0):
        self.bearing = bearing
        self.coordinates = (x, y)
    
    def advance(self):
        cx, cy = self.coordinates
        x, y = self.bearing
        self.coordinates = (x + cx, y + cy)

    def turn_left(self):
        x, y = self.bearing
        self.bearing = (-y, x)

    def turn_right(self):
        x, y = self.bearing
        self.bearing = (y, -x)
    
    def simulate(self, program):
        for char in program:
            if char == 'L':
                self.turn_left()
            elif char == 'R':
                self.turn_right()
            elif char == 'A':
                self.advance()
            else:
                raise ValueError

