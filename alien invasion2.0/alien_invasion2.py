import pygame

class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600,300))
		pygame.display.set_caption("AlienInvasion")
		self.bg_color = (0, 0, 225)

	def run_game(self):
		while True:
			for event in pygame.event.get()
				if event.type == pygame.QUIT:
					sys.exit()
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()