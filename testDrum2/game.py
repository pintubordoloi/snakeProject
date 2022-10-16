import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from mosquito import Mosquito
from bee import Bee
import cv2
import ui
from test import *

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        # Load camera
        self.cap = cv2.VideoCapture(0)


    def reset(self): # reset all the needed variables
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        self.hand.draw(self.surface)


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        #self.draw()
        runEverything(self.surface)
        
        (x, y) = self.hand_tracking.get_hand_center()
        (a, b) = self.hand_tracking.get_hand_point()
        self.hand.rect.center = (x, y)
        finger = pygame.draw.rect(self.surface,(255, 255, 0), pygame.Rect(a, b, 20, 20))
        player1 = pygame.draw.rect(self.surface,(255, 255, 199), player)
        collision_tolerance = 10
        if player.rect.colliderect(finger):
        	print("touched")
        	if abs(player1.top - finger.bottom) < collision_tolerance:
        		player.move(0,10)
        	if abs(player1.bottom - finger.top) < collision_tolerance:
        		player.move(0,-10)
        	if abs(player1.right - finger.left) < collision_tolerance:
        		player.move(-10,0)
        	if abs(player1.left - finger.right) < collision_tolerance:
        		player.move(10,0)
        self.hand.left_click = self.hand_tracking.hand_closed
        print("Hand closed", self.hand.left_click)
        if self.hand.left_click:
            print("hello")
        else:
            self.hand.image = self.hand.orig_image.copy()
            
            
            #self.score = self.hand.kill_insects(self.insects, self.score, self.sounds)
            #for insect in self.insects:
             #   insect.move()



        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
