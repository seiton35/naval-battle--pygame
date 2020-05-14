import pygame 

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("naval battle")

run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.draw.rect(win, (0,0,255), (30, 40, 50 ,10))
	pygame.display.update()