import pygame 

pygame.init()
win = pygame.display.set_mode((600, 800))

pygame.display.set_caption("naval battle")

run = True

bg = pygame.image.load('images/background.png')
paper = pygame.image.load('images/paper.png')

def drawWindow():
	win.blit(bg, (0, 0))
	win.blit(paper, (20, 10))

	pygame.draw.rect(win, (0,0,0), (94,124, 3, 232))
	pygame.draw.rect(win, (0,0,0), (325,124, 3, 232))
	pygame.draw.rect(win, (0,0,0), (94,124, 232, 3))
	pygame.draw.rect(win, (0,0,0), (94,354, 232, 3))

	pygame.draw.rect(win, (0,0,0), (256,469, 3, 232))
	pygame.draw.rect(win, (0,0,0), (485,469, 3, 232))
	pygame.draw.rect(win, (0,0,0), (256,469, 232, 3))
	pygame.draw.rect(win, (0,0,0), (256,700, 232, 3))

	pygame.display.update()

	#цвет фона win.fill((0,0,88))

while run:
	pygame.time.delay(100)
	drawWindow()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False