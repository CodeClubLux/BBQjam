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
	font = pygame.font.Font(None, 32)
	text = font.render('WTF, is this shit? We\'ve been hit!', 0, (255,255,255))

	# Set up screen
	screen_width = 800
	screen_height = 600
	screen = pygame.display.set_mode((screen_width,screen_height))
	bg = (0,0,0)
	screen.fill(bg)

	# Set up an image
	image = pygame.image.load(os.path.join('img','image.png')).convert_alpha()
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

	counter = 0
	hit = False
	running = True
	while running:
		# Limit to 50 fps
		time_passed = clock.tick(30)

		# For our epileptic friends ;)
		#background = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		screen.fill(bg)


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

		if hit:
			counter += 1
			screen.blit(text, (screen_width/3, screen_height/2))

		if counter > 20:
			counter = 0
			hit = False
		

		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				print('Mouse down!')
				mousex, mousey = pygame.mouse.get_pos()
				if pycard.left < mousex and pycard.right > mousex and pycard.top < mousey and pycard.bottom > mousey:
					screen.fill((255,0,0))
					hit = True
					pygame.draw.line(screen, (0,0,255), (400,600), (pycard.centerx, pycard.centery), 2)	
					print('We\'ve been hit, captain!')
			if event.type == pygame.QUIT:
				running = False

		pygame.display.flip()

if __name__ == '__main__':
	main()
