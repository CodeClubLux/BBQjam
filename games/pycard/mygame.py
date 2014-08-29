# In order to use system packages inside a virtualenv
# virtualenv --system-site-packages

import os, random
import pygame
from pygame.locals import *

def main():
	random.seed()
	pygame.init()
	pygame.display.set_caption('minimal program')
	
	clock = pygame.time.Clock()

	# Set up screen
	screen_width = 800
	screen_height = 600
	screen = pygame.display.set_mode((screen_width,screen_height))
	screen.fill((100,100,0))

	# Set up an image
	image = pygame.image.load(os.path.join('img','image.png'))
	image = pygame.transform.scale(image, (200, 200))

	#image.set_colorkey((255,255,255))	# set a color to be transparent
	#image.set_alpha(128)			# Set image opacity

	screen.blit(image, (0,0))

	# Draw screen
	pygame.display.flip()

	#xpos = 50
	#ypos = 50

	pycard = image.get_rect()
	#pygame.draw.rect(screen, (255,0,0), pycard, 2)

	xpos = pycard.x
	ypos = pycard.y

	print(pycard.x, pycard.y, pycard.left, pycard.right)
	step_x = 10
	step_y = 10

	running = True
	while running:
		# Limit to 50 fps
		time_passed = clock.tick(30)

		# For our epileptic friends ;)
		#background = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		background = (0,0,0)
		screen.fill(background)
		
		# Move the captain!
		if pycard.right > screen_width or pycard.left < 0:
			step_x = -step_x
		if pycard.bottom > screen_height or pycard.top < 0:
			step_y = -step_y

		pycard.x += step_x
		pycard.y += step_y

		# Hmm.. this makes him go off-screen
		#image = pygame.transform.rotate(image, random.randint(0,10))

		screen.blit(image, pycard)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				print('Mouse down!')
				mousex, mousey = pygame.mouse.get_pos()
				if pycard.left < mousex and pycard.right > mousex and pycard.top < mousey and pycard.bottom > mousey:
					screen.fill((255,0,0))
					pygame.display.flip()
					print('We\'ve been hit, captain!')
			if event.type == pygame.QUIT:
				running = False

if __name__ == '__main__':
	main()
