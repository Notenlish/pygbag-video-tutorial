import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()


from player import Player
from ground import Ground


class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((960, 540))
        
        self.clock = pygame.time.Clock()
        self.player = Player(0,0)
        self.ground = Ground(self.screen.get_height() - 128, self.screen.get_width())
        
        self.font = pygame.Font("Renogare-Regular.otf", size=24)
        
        self.time_elapsed = 0
        self.dt = 16 / 1000  # 16 ms
    
    def update(self):
        self.player.update(pygame.key.get_pressed(), self.dt, self.ground)
    
    def render(self):
        self.screen.fill("#C7D0F2")
        self.player.render(self.screen)
        self.ground.render(self.screen)
        
        surf = self.font.render(f"{self.time_elapsed:.2f}", antialias=True, color="black")
        self.screen.blit(surf, (0,0))
    
    def run(self):
        while True:
            pygame.display.set_caption(f"FPS:{self.clock.get_fps():.0f} dt:{self.dt:.2f}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return SystemExit
            
            self.update()
            
            self.render()
            
            self.dt = self.clock.tick(60) / 1000  # convert from ms to seconds
            self.dt = min(self.dt, 1)  # keep dt from getting really big if the window isnt active 
            self.time_elapsed += self.dt
            
            pygame.display.flip()
    
if __name__ == '__main__':
    app = App()
    app.run()