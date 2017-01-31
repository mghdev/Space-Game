
#-------------------------
# This file contains code related to world regions
#	Regions are sections of the game world
#	A region object is responsible for collision detection and drawing objects within its limits
#-------------------------

import random
from drawing import Drawable
from math import *
from constants import *

class Region(Drawable):
	width = 10000
	height = 10000
	
	def __init__(self,region_grid,grid_dimensions,index):
		self._region_grid = region_grid
		self._index = int(index)
		self._grid_pos = (int(index%grid_dimensions[0]),int(floor(index/grid_dimensions[0])))
		self._world_pos = (self._grid_pos[0]*self.width,self._grid_pos[1]*self.height)

		self._world_objects = []

		self._adjacent_region_indices = {"N":None,"S":None,"E":None,"W":None,"NE":None,"NW":None,"SE":None,"SW":None,None:None}
		grid_size = grid_dimensions[0]*grid_dimensions[1]
		on_north_edge = False
		on_south_edge = False
		on_east_edge = False
		on_west_edge = False
		if self.index < grid_dimensions[0]:
			on_north_edge = True
		if self.index >= grid_size - grid_dimensions[0]:
			on_south_edge = True
		if self.index % grid_dimensions[0] == 0 :
			on_west_edge = True
		if self.index % grid_dimensions[0] == grid_dimensions[0]-1:
			on_east_edge = True
		if not on_north_edge:
			self._adjacent_region_indices["N"] = self.index - grid_dimensions[0]
			if not on_east_edge:
				self._adjacent_region_indices["E"] = self.index + 1
				self._adjacent_region_indices["NE"] = self.index - grid_dimensions[0] + 1
			if not on_west_edge:
				self._adjacent_region_indices["W"] = self.index - 1
				self._adjacent_region_indices["NW"] = self.index - grid_dimensions[0] - 1
		if not on_south_edge:
			self._adjacent_region_indices["S"] = self.index + grid_dimensions[0]
			if not on_east_edge:
				self._adjacent_region_indices["SE"] = self.index + grid_dimensions[0] + 1
			if not on_west_edge:
				self._adjacent_region_indices["SW"] = self.index + grid_dimensions[0] - 1

	@property
	def region_grid(self):
	    return self._region_grid
	
	@region_grid.setter
	def region_grid(self,value):
		self._region_grid = value

	@property
	def index(self):
	    return self._index
	
	@property
	def grid_pos(self):
	    return self._grid_pos

	@property
	def world_pos(self):
	    return self._world_pos
	
	@property
	def world_objects(self):
	    return self._world_objects

	def adjacentRegion(self,direction):
		return self.region_grid[self._adjacent_region_indices[direction]]
	
	def removeWorldObject(self,obj):
		self._world_objects.remove(obj)

	def addWorldObject(self,new_obj):
		self._world_objects.append(new_obj)

	def screenPosition(self,camera_pos):
		space_left_of_region = (DISPLAY_HALF_WIDTH - (camera_pos[0] - self._world_pos[0]))
		space_above_region = (DISPLAY_HALF_HEIGHT - (camera_pos[1] - self._world_pos[1]))
		return (int(space_left_of_region),int(space_above_region))

	def draw(self,surface,camera_pos):
		for obj in self.world_objects:
			obj.draw(surface,camera_pos)







