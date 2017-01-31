#-------------------------
#		Game Input
#-------------------------

import pygame, sys


from constants import *
from math import *
from region import Region
from game.state import Game

KEYS = {
	'esc': 27,
	'a': 97,
	'w': 119,
	'q': 113,
	's': 115,
	'd': 100
}

current_player_movement = [0,0,0]
movement_key_state = {
	"left": False,
	"right": False,
	"up": False,
	"down": False
	}

def handleKeydown(key):
	if key == KEYS['esc']:
		pygame.quit()
		sys.exit()
	if key == KEYS['w']:
		movement_key_state["up"] = True
	if key == KEYS['a']:
		movement_key_state["left"] = True
	if key == KEYS['s']:
		movement_key_state["down"] = True
	if key == KEYS['d']:
		movement_key_state["right"] = True

def handleKeyup(key):
	if key == KEYS['w']:
		movement_key_state["up"] = False
	if key == KEYS['a']:
		movement_key_state["left"] = False
	if key == KEYS['s']:
		movement_key_state["down"] = False
	if key == KEYS['d']:
		movement_key_state["right"] = False


def move(transform,moves,bounds=None):
	transform[0] += moves[0]
	transform[1] += moves[1]
	transform[2] += moves[2]
	
	if bounds == None:
		return

	if transform[1] < bounds["top"]:
		transform[1] = bounds["top"]
	if transform[1] > bounds["bottom"]:
		transform[1] = bounds["bottom"]
	if transform[0] < bounds["left"]:
		transform[0] = bounds["left"]
	if transform[0] > bounds["right"]:
		transform[0] = bounds["right"]


def updatePlayerMovement(angle):
	current_player_movement[2] = 0
	if movement_key_state["left"]:
		current_player_movement[2] = ROTATION_SPEED
	if movement_key_state["right"]:
		current_player_movement[2] = -ROTATION_SPEED
	if movement_key_state["up"]:
		current_player_movement[1] -= MOVE_ACCELERATION*cos(radians(angle))
		current_player_movement[0] -= MOVE_ACCELERATION*sin(radians(angle))
		speed = sqrt(pow(current_player_movement[0],2) + pow(current_player_movement[1],2))
		if speed >= MAX_PLAYER_SPEED:
			ratio = speed/MAX_PLAYER_SPEED
			current_player_movement[0] = current_player_movement[0]/ratio
			current_player_movement[1] = current_player_movement[1]/ratio
	if movement_key_state["down"]:
		speed = sqrt(pow(current_player_movement[0],2) + pow(current_player_movement[1],2))
		if fabs(current_player_movement[0]) < MOVE_ACCELERATION:
			current_player_movement[0] = 0
		else:
			current_player_movement[0] -= MOVE_ACCELERATION*current_player_movement[0]/speed
		if fabs(current_player_movement[1]) < MOVE_ACCELERATION:
			current_player_movement[1] = 0
		else :
			current_player_movement[1] -= MOVE_ACCELERATION*current_player_movement[1]/speed
		
	return current_player_movement











