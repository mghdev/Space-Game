#-------------------------
#		Game Objects
#-------------------------

from constants import *
from drawing import Drawable, Sprite

# WorldObject
#	What does every object in a grid need to be able to do?
#		draw
#		position (move)
#
#

class WorldObject(Drawable):
	def __init__(self):
		super(WorldObject,self).__init__()
		self._transform = [0,0,0]
		self._size = [0,0]

	@property
	def transform(self):
	    return self._transform

	@transform.setter
	def transform(self,value):
	    self._transform = list(value[:3])
	
	@property
	def pos(self):
	    return self.transform[:2]

	@pos.setter
	def pos(self,value):
		self._transform[:2] = value[:2]

	@property
	def rotation(self):
	    return self.transform[2]

	@rotation.setter
	def rotation(self,value):
	    self._transform[2] = value
 	
	@property
	def size(self):
	    return self._size

	@size.setter
	def size(self,value):
		self._size = list(value[:2])

	@property
	def width(self):
	    return self.size[0]
	@width.setter
	def width(self,value):
		self._size[0] = value
	@property
	def height(self):
	    return self.size[1]
	@height.setter
	def height(self,value):
		self._size[1] = value
	
	def rotate(self,angle):
		self._transform[2] += angle

	def translate(self,translation):
		self._transform[0] += translation[0]
		self._transform[1] += translation[1]

	def screenPos(self,camera_pos):
		return (self.pos[0]-camera_pos[0]+DISPLAY_HALF_WIDTH,self.pos[1]-camera_pos[1]+DISPLAY_HALF_HEIGHT)
	

class Ship(WorldObject):
	def __init__(self,image_path):
		super(Ship,self).__init__()
		self._sprite = Sprite(image_path,self)
		self.addDrawable(self._sprite)

