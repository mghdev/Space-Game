
#-------------------------
#		A SPACE GAME
#		by Michael Hein
#-------------------------

#importing full modules
import pygame, sys, random, grid, region, objects
from game import inputs, state
#importing parts of other modules into local namespace
from pygame.locals import *
from math import *
from constants import *

def drawFrame(surface,camera_pos,drawables):
	surface.fill(BLACK)
	for drawable_object in drawables:
		drawable_object.draw(surface,camera_pos)

def main():
	pygame.init()
	pygame.display.set_caption(DISPLAY_TITLE)
	display_surface = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT)) #,pygame.FULLSCREEN
	fps_clock = pygame.time.Clock()
	display_surface.fill(BLACK)
	
	background_grid_dimensions = (int(ceil(float(region.Region.width*state.Game.region_grid_size[0])/BACKGROUND_IMAGE_WIDTH)),int(ceil(float(region.Region.height*state.Game.region_grid_size[1])/BACKGROUND_IMAGE_HEIGHT)))
	num_background_tiles = background_grid_dimensions[0]*background_grid_dimensions[1]

	background_grid = grid.TexturedGrid(background_grid_dimensions,(BACKGROUND_IMAGE_WIDTH,BACKGROUND_IMAGE_HEIGHT),(1,1),["Sprites/empty_space.jpg"],[0]*num_background_tiles,False)
	camera_pos = [DISPLAY_WIDTH/2,DISPLAY_HEIGHT/2]

	player_ship = objects.Ship(SHIP_IMAGE_PATH)
	player_ship.pos = [1000,1000]
	
	print("Beginning game loop.")
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				inputs.handleKeydown(event.key)
			if event.type == KEYUP:
				inputs.handleKeyup(event.key)
		
		movement = inputs.updatePlayerMovement(player_ship.rotation)
		movement_bounds = {"left":DISPLAY_HALF_WIDTH,
							"right":state.Game.region_grid_size[0]*region.Region.width - DISPLAY_HALF_WIDTH,
							"top":DISPLAY_HALF_HEIGHT,
							"bottom":state.Game.region_grid_size[1]*region.Region.height - DISPLAY_HALF_HEIGHT}
		transform = player_ship.transform
		inputs.move(transform,movement,movement_bounds)
		player_ship.transform = transform

		camera_pos = player_ship.pos
		drawFrame(display_surface,camera_pos,[background_grid,player_ship])
		
		pygame.display.update()
		fps_clock.tick(FPS)

if __name__ == '__main__':
	main()









