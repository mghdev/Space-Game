#-------------------------
#		Drawing
#-------------------------

import pygame
from constants import *

class Drawable(object):
	def __init__(self):
		self.drawable_sub_objects = []

	def addDrawable(self,obj):
		self.drawable_sub_objects.append(obj);

	def draw(self,surface,camera_pos):
		for obj in self.drawable_sub_objects:
			obj.draw(surface,camera_pos)


class Sprite(Drawable):
	def __init__(self,path,game_object):
		self._image_path = str(path)
		self._image = pygame.image.load(self.image_path)
		self._game_object = game_object

	@property
	def image(self):
	    return self._image

	@property
	def image_path(self):
	    return self._image_path

	@image_path.setter
	def image_path(self,value):
		self._image_path = str(value)
		self._image = pygame.image.load(self._image_path)

	def draw(self,surface,camera_pos):
		image = pygame.transform.rotate(self._image,self._game_object.rotation)
		screen_pos = self._game_object.screenPos(camera_pos)
		if screen_pos[0]+image.get_width()/2 < 0 or screen_pos[0]-image.get_width()/2 > DISPLAY_WIDTH:
			return
		if screen_pos[1]+image.get_height()/2 < 0 or screen_pos[1]-image.get_height()/2 > DISPLAY_HEIGHT:
			return
		surface.blit(image,[screen_pos[0]-image.get_width()/2,screen_pos[1]-image.get_height()/2])




