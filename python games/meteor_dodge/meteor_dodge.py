import pygame, sys

class spaceship(pygame.sprite.Sprite):
	def __init__(self, path, xpos, y_pos, speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(centre = ((x_pos, y_pos))

	def update(self)
		self.rect.centre = pygame.mouse.get_pos()

pygame.init()
screen = pygame.display.set_mode((1280,720)) #create display surface
clock = pygame.time.Clock() #create clock object

spaceship = Spaceship("game_pics\spaceship.png", 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True: #Game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((15,40,75))
	spaceship_group.draw(screen)
	pygame.display.update() #draw frame
	clock.tick(120) #control framerate

