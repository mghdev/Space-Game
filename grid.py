#-------------------------
#		Grid
#-------------------------

import drawing
from constants import *
from math import *

def worldPositionOfGridTile(index,grid_dimensions,tile_size):
	grid_x = index % grid_dimensions[0]
	grid_y = (index - grid_x) / grid_dimensions[0]
	return (grid_x*tile_size[0],grid_y*tile_size[1])


def visibleTiles(camera_pos,grid_size,tile_size,display_size=(DISPLAY_WIDTH,DISPLAY_HEIGHT)):
	grid_x = floor(camera_pos[0] / tile_size[0])
	grid_y = floor(camera_pos[1] / tile_size[1])

	center_tile_x = grid_x * tile_size[0]
	center_tile_y = grid_y * tile_size[1]

	space_left = display_size[0]/2 - (camera_pos[0] - center_tile_x)
	space_right = display_size[0]/2 - (tile_size[0] - camera_pos[0] + center_tile_x)
	space_above = display_size[1]/2 - (camera_pos[1] - center_tile_y)
	space_below = display_size[1]/2 - (tile_size[1] - camera_pos[1] + center_tile_y)
	
	if space_above < 0:
		space_above = 0
	if space_below < 0:
		space_below = 0
	if space_left < 0:
		space_left = 0
	if space_right < 0:
		space_right = 0
	
	tiles_left = int(ceil(space_left / float(tile_size[0])))
	tiles_right = int(ceil(space_right / float(tile_size[0])))
	tiles_above = int(ceil(space_above / float(tile_size[1])))
	tiles_below = int(ceil(space_below / float(tile_size[1])))
	
	start_x = grid_x - tiles_left
	end_x = grid_x + tiles_right
	start_y = grid_y - tiles_above
	end_y = grid_y + tiles_below
	
	if start_x < 0:
		start_x = 0
	if start_y < 0:
		start_y = 0
	if end_x > grid_size[0]:
		end_x = grid_size[0]
	if end_y > grid_size[1]:
		end_y = grid_size[1]

	result = []
	for i in range(tiles_above+tiles_below+1):
		for j in range(tiles_left+tiles_right+1):
			index = int(start_x+j + (start_y+i)*grid_size[0])
			if index >= 0 and index < grid_size[0]*grid_size[1]:
				result.append(index)
	return result

class TexturedGrid(drawing.Drawable):
	wrapping_grid_exists = False
	def __init__(self,grid_dimensions,tile_size,scaling=(1,1),texture_files=[],texture_map=[],wrapping=False):
		self.grid_dimensions = tuple(grid_dimensions)
		self.texture_files = list(texture_files)
		self.textures = []
		self.texture_map = list(texture_map)

		self.scaling = tuple(scaling)

		self.tile_size = tuple(tile_size)
		self.wrapping = wrapping

		if self.wrapping:
			self.wrapping_grid_exists = True

		self.loadTextures()

	def loadTextures(self):
		self.textures = []
		for file_name in self.texture_files:
			self.textures.append(pygame.image.load(file_name))

	def screenPositionOfTile(self,index,camera_pos,display_size=(DISPLAY_WIDTH,DISPLAY_HEIGHT)):
		world_pos = worldPositionOfGridTile(index,self.grid_dimensions,self.tile_size)
		space_left_of_tile = (display_size[0]/2 - (camera_pos[0] - world_pos[0]))
		space_above_tile = (display_size[1]/2 - (camera_pos[1] - world_pos[1]))
		return (int(space_left_of_tile),int(space_above_tile))

	def draw(self,surface,position):
		#This may be modified when I fully implement wrapping/repeating grids
		position_in_grid = position

		visible_tiles = visibleTiles(position_in_grid,self.grid_dimensions,self.tile_size,(DISPLAY_WIDTH,DISPLAY_HEIGHT))
		for tile_index in visible_tiles:
			if self.texture_files[self.texture_map[tile_index]] == "":
				pass
			else:
				surface.blit(self.textures[self.texture_map[tile_index]],self.screenPositionOfTile(tile_index,position_in_grid))



