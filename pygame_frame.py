import pygame

# initialization
pygame.init()

# screen setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pang Arcade")

# create time object
clock = pygame.time.Clock()

# game running
running = True 
while running:
    # set FPS
    clock.tick(30) 
    
    # event handling
    for event in pygame.event.get(): 
        # close the window by clicking the X button of the game window
        if event.type == pygame.QUIT:
            # stop the game 
            running = False
    
    # update screen continuously
    pygame.display.update() 

# shut down
pygame.quit()
