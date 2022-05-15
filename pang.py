import os
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

# get the path of the current file
current_path = os.path.dirname(__file__)
# get the path of the images folder
image_path = os.path.join(current_path, "img")

# create background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# create stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# create character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# direction of moving
character_to_x = 0
# speed of character
character_speed = 5

# create weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# weapon list
weapons = []
# speed of weapon
weapon_speed = 10

# create balls
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball01.png")),
    pygame.image.load(os.path.join(image_path, "ball02.png")),
    pygame.image.load(os.path.join(image_path, "ball03.png")),
    pygame.image.load(os.path.join(image_path, "ball04.png"))]
# speeds of balls
ball_speed_y = [-18, -15, -12, -9] 
# balls on the screen
balls = []
# the initial biggest ball
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y" : ball_speed_y[0]})

# variables for weapons and balls to be removed
weapon_to_remove = -1
ball_to_remove = -1

# declare the font
game_font = pygame.font.Font(None, 40)

# set times
total_time = 100
start_ticks = pygame.time.get_ticks()

# set message
game_result = "Game Over"

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

        # pressing key event
        if event.type == pygame.KEYDOWN:
            # move character to the left using the left key
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            # move character to the left using the left key
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            # fire weapon from the center of character
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        # releasing key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # reposition character
    character_x_pos += character_to_x

    # when character reaches left end
    if character_x_pos < 0:
        character_x_pos = 0
    # when character reaches right end
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # move up weapons adjusting y position
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    # save only weapons whose y position is greater than 0
    # weapon that reaches the top (y <= 0) is removed
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # position of balls
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # turn around when reaching the left and right ends
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
            
        # turn up when reaching the stage
        if ball_pos_y >= screen_height - stage_height - ball_height:  
            ball_val["to_y"] = ball_val["init_spd_y"]
        # increase speed and move down ball
        else:
            ball_val["to_y"] += 0.5
            
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # update character position
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # update ball position
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # when character and ball touch
        if character_rect.colliderect(ball_rect):
            running = False
            break

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # update weapon position    
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # when weapon and ball touch
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                # not the smallest ball
                if ball_img_idx < 3: 
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                        
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # new ball bouncing to the left
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : -3, 
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})
                        
                    # new ball bouncing to the right
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : 3, 
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) 
                break
        else:
            continue 
        break 

    # remove touched ball
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    # remove touched weapon
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # when all balls removed
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    # display images
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for inx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # caculate and display elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time  : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # when time over
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    # update screen continuously
    pygame.display.update() 

# display game result message
msg = game_font.render(game_result, True, (255, 255, 0))
mag_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, mag_rect)
pygame.display.update()

# delay 2 seconds before closing the window
pygame.time.delay(2000)

# shut down
pygame.quit()
