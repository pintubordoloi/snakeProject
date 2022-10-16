import os
import sys
import random
import pygame
from hand import Hand
from hand_tracking import HandTracking
import cv2
import ui
from background import Background


#Class for the orange dude
class Player(object):
	def __init__(self):
		self.rect = pygame.Rect(400, 400, 16, 16)
	
	def move(self, dx, dy):
		#move each axis separately. Note that this checks for collisions both times.
		if dx != 0:
			self.move_single_axis(dx, 0)
		if dy != 0:
			self.move_single_axis(0, dy)
	
	def move_single_axis(self, dx, dy):
		#move the rect
		self.rect.x += dx
		self.rect.y += dy
		
		#if you collide with a wall, move out based on velocity
		for wall in walls:
			if self.rect.colliderect(wall.rect):
				if dx > 0: #moving right; Hit the left side of the wall
					self.rect.right = wall.rect.left
				if dx < 0:
					self.rect.left = wall.rect.right
				if dy > 0:
					self.rect.bottom = wall.rect.top
				if dy < 0:
					self.rect.top = wall.rect.bottom

class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 20, 20)

#os.environ["SDL_VIDEO_CENTERED"] = "1"
#pygame.init()

#Set up teh display
#pygame.display.set_caption("Get the red Square!")
#screen = pygame.display.set_mode((1200, 700))

clock = pygame.time.Clock()
walls = []
player = Player()
#hand = Hand()
#hand_tracking = HandTracking()

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                              W",
    "W         WWWWWW                                               W",
    "W   WWWW       W                                               W",
    "W   W        WWWW                                              W",
    "W WWW  WWWW                                                    W",
    "W   W     W W                                                  W",
    "W   W     W   WWW W                                            W",
    "W   WWW WWW   W W                                              W",
    "W     W   W   W W                                              W",
    "WWW   W   WWWWW W                                              W",
    "W W      WW                                                    W",
    "W W   WWWW   WWW                                               W",
    "W     W    E   W                                               W",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

#Parse the level string above, W = wall, E = exit
x = y = 0
for row in level:
	for col in row:
		if col == "W":
			Wall((x, y))
		if col == "E":
			end_rect = pygame.Rect(x, y, 16, 16)
		x += 20
	y += 20
	x = 0
running = True

def runEverything(screen):
	#Move the player if an arrow key is pressed
	#pygame.draw.rect(screen, (255,255,255), player)
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		player.move(-10, 0)
	if key[pygame.K_RIGHT]:
		player.move(10, 0)
	if key[pygame.K_UP]:
		player.move(0, -10)
	if key[pygame.K_DOWN]:
		player.move(0, 10)
	
	#Just added this to make it slighty fun
	if player.rect.colliderect(end_rect):
		pygame.quit()
		sys.exit()
	
	#Draw the scene
	screen.fill((0, 0, 0))
	for wall in walls:
		pygame.draw.rect(screen, (255, 255, 255), wall.rect)
	pygame.draw.rect(screen, (255, 0, 0), end_rect)
	pygame.draw.rect(screen, (255, 200, 0), player.rect)
	
	pygame.display.flip()
	clock.tick(360)

pygame.quit()


