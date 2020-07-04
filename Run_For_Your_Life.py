import pygame
import random
from pygame import mixer


def game_loop():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 600))

    mixer.music.load('./res/game_music.wav')
    mixer.music.play(-1)

    background = pygame.image.load('./res/dark_forest_background.png')
    bg = pygame.transform.scale(background, (800, 600))

    icon = pygame.image.load('./res/ghost_icon.png')
    pygame.display.set_icon(icon)

    pygame.display.set_caption("Run For Your Life")

    coin = pygame.image.load('./res/coin.png')
    coinX = random.randint(100, 700)
    coinY = random.randint(100, 400)

    ghost = []
    ghostx = []
    ghosty = []
    ghostx_change = []
    ghosty_change = []
    num_of_ghosts = 2

    for i in range(num_of_ghosts):
        ghost.append(pygame.image.load('./res/ghost.png'))
        ghostx.append(random.randint(100, 700))
        ghosty.append(random.randint(100, 400))
        ghostx_change.append(7)
        ghosty_change.append(7)

    def print_ghost(x, y, i):
        screen.blit(ghost[i], (x, y))

    emoji = pygame.image.load('./res/emoji.png')
    emojiX = 380
    emojiY = 480
    emojiX_change = 0
    emojiY_change = 0

    def print_emoji():
        screen.blit(emoji, (emojiX, emojiY))

    def print_coin():
        screen.blit(coin, (coinX, coinY))

    score = 0
    score_font = pygame.font.Font('./res/font.ttf', 32)
    textX = 10
    textY = 10

    def print_score(x, y):
        score_print = score_font.render("Score:" + str(score), True, (255, 255, 255))
        screen.blit(score_print, (x, y))

    game_over = pygame.font.Font('./res/heading_font.ttf', 49)
    fontX = 5
    fontY = 270

    hiscore_font = pygame.font.Font('./res/font.ttf', 32)
    hiscore_fontX = 610
    hiscore_fontY = 10

    def print_hiscore():
        hiscore_render = hiscore_font.render("Hiscore: " + str(hiscore), True, (255, 255, 255))
        screen.blit(hiscore_render, (hiscore_fontX, hiscore_fontY))

    def print_game_over():
        game_over_ = game_over.render("GAME OVER! Press Enter to restart", True, (255, 255, 255))
        screen.blit(game_over_, (fontX, fontY))

    with open("./res/Hiscore_Manager_game.txt", "r") as f:
        hiscore = f.read()
    running = True
    game__over = False

    while running:
        if game__over:
            with open("./res/Hiscore_Manager_game.txt", "w") as f:
                f.write(str(hiscore))
            screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            print_game_over()
            print_hiscore()
            print_score(textX, textY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        emojiY_change = 0
                        emojiX_change = -4
                    if event.key == pygame.K_RIGHT:
                        emojiY_change = 0
                        emojiX_change = 4
                    if event.key == pygame.K_UP:
                        emojiX_change = 0
                        emojiY_change = -4
                    if event.key == pygame.K_DOWN:
                        emojiX_change = 0
                        emojiY_change = 4

            if abs(emojiX - coinX) < 35 and abs(emojiY - coinY) < 35:
                score += 1
                coinX = random.randint(100, 700)
                coinY = random.randint(100, 400)

            for i in range(num_of_ghosts):
                if abs(emojiX - ghostx[i]) < 30 and abs(emojiY - ghosty[i]) < 30:
                    scared = mixer.Sound('./res/scary_sound.wav')
                    scared.play()
                    game__over = True

                if ghosty[i] >= 536:
                    ghosty[i] = 536
                    ghosty_change[i] = -7
                if ghostx[i] >= 736:
                    ghostx[i] = 736
                    ghostx_change[i] = -7
                if ghosty[i] <= 0:
                    ghosty[i] = 0
                    ghosty_change[i] = 7
                if ghostx[i] <= 0:
                    ghostx[i] = 0
                    ghostx_change[i] = 7
                ghostx[i] += ghostx_change[i]
                ghosty[i] += ghosty_change[i]
                print_ghost(ghostx[i], ghosty[i], i)
            if emojiX >= 736:
                emojiX = 736
            if emojiX <= 0:
                emojiX = 0
            if emojiY >= 536:
                emojiY = 536
            if emojiY <= 0:
                emojiY = 0
            if score > int(hiscore):
                hiscore = score
            print_coin()
            print_emoji()
            print_coin()
            print_hiscore()
            print_score(textX, textY)
            emojiX += emojiX_change
            emojiY += emojiY_change
        pygame.display.update()
        clock.tick(100)


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

mixer.music.load('./res/game_music.wav')
mixer.music.play(-1)

pygame.display.set_caption("Run For Your Life")

background = pygame.image.load('./res/dark_forest_background.png')
bg = pygame.transform.scale(background, (800, 600))

icon = pygame.image.load('./res/ghost_icon.png')
pygame.display.set_icon(icon)

game_start = pygame.font.Font('freesansbold.ttf', 64)
fontX = 100
fontY = 270


def print_game_start():
    game_start_ = game_start.render("Press Enter to start", True, (255, 255, 255))
    screen.blit(game_start_, (fontX, fontY))


game_name = pygame.font.Font('./res/font.ttf', 45)
game_name_fontX = 240
game_name_fontY = 100


def print_game_name():
    game_name_ = game_name.render("Run For Your Life", True, (255, 255, 255))
    screen.blit(game_name_, (game_name_fontX, game_name_fontY))


running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    print_game_name()
    print_game_start()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_loop()
    pygame.display.update()
    clock.tick(60)
