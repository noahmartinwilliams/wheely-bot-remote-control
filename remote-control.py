#! /usr/bin/python

import pygame
from pygame.locals import *

import os 
import sys

pygame.init()

v_min=5.0
o_min=0.6

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

red=False
green=False
blue=False

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

		elif event.type==KEYDOWN:
			if event.key==K_UP:
				print "!steer "+str(v_min)+" 0.0 "

			if event.key==K_LEFT:
				print "!steer 0.0 "+str(o_min)+" "

			if event.key==K_RIGHT:
				print "!steer 0.0 "+str(-o_min)+" "

			if event.key==K_DOWN:
				print "!steer "+str(-v_min)+" 0.0 "

			if event.key==K_r:
				if red==False:
					print "!ron "
					red=True
				else:
					print "!roff "
					red=False


			if event.key==K_g:
				if green==False:
					print "!gon "
					green=True
				else:
					print "!goff "
					green=False

			if event.key==K_b:
				if blue==False:
					print "!bon "
					blue=True
				else:
					print "!boff "
					blue=False
			if event.key==K_s:
				print "!halt "

		elif event.type==KEYUP:
			print "!halt "

	sys.stdout.flush()
