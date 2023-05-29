import pygame
import pygame as p
from copy import deepcopy
from MazeGame import GameEngine


WIDTH = 960
HEIGHT = 640
DIMENSION_X = 16
DIMENSION_Y = 24
SQ_SIZE = HEIGHT // DIMENSION_X
MAX_FPS = 30
IMAGES_OBJ = {}
IMAGES_HEALTH = {}


def load_images():
    objs = ['p1', 'm1', 'm2', 'm3', 'w1', 'f1', 'heart1', 'heart2', 'treasure1', 'treasure2', 'b1', 'k1', 'd1', 'h1', 'c1', 'test', 'f2', 'd2']
    # p1 = player1, m1 = monster1, w1 = wall1, f1 = floor1, b1 = box1, k1 = key1, d1 = door1, h1 = healer1
    for obj in objs:
        IMAGES_OBJ[obj] = p.transform.scale(p.image.load("images/" + obj + ".png"), (SQ_SIZE, SQ_SIZE))
        IMAGES_HEALTH[obj] = p.transform.scale(p.image.load("images/" + obj + ".png"), (40, 40))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT+100))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = GameEngine.GameState()
    gs_cp = deepcopy(gs)
    load_images()
    running = True
    gameOver = False
    WHITE = (255, 255, 255)
    font = p.font.SysFont("Helvitca", 48, False, False)
    text_level = font.render('Level 1', True, WHITE)
    text_health = font.render('Health : ', True, WHITE)

    while running:
        # print(gs.time)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                if not gameOver:
                    if e.key == p.K_DOWN:
                        gs.make_move('player', (1, 0))
                    elif e.key == p.K_UP:
                        gs.make_move('player', (-1, 0))
                    elif e.key == p.K_LEFT:
                        gs.make_move('player', (0, -1))
                    elif e.key == p.K_RIGHT:
                        gs.make_move('player', (0, 1))
                if e.key == p.K_r:
                    gs = GameEngine.GameState()
                    gs_cp = deepcopy(gs)
                    gameOver = False
        if gs.game_over:
            gameOver = True
            gs.health_bar[0] = 'heart2'
            draw_health_state(screen, gs.health_bar)
            draw_text(screen, 'Game Over')

        if gs.win:
            gameOver = True
            draw_game_state(screen, gs)
            draw_text(screen, 'You Win')

        if gs.die:
            health_now = gs.health
            gs = deepcopy(gs_cp)
            gs.health = health_now - 1
            gs.health_bar[gs.health] = 'heart2'
            gs.number_of_checkpoints -= 1
            gs.die = False
            draw_game_state(screen, gs)

        if gs.save_state:
            for i in range(gs.checkpoint_control[gs.number_of_checkpoints][0], gs.checkpoint_control[gs.number_of_checkpoints][1] + 1, 1):
                gs.monster_list[i][7] = False
            gs.number_of_checkpoints += 1
            for i in range(gs.checkpoint_control[gs.number_of_checkpoints][0], gs.checkpoint_control[gs.number_of_checkpoints][1] + 1, 1):
                gs.monster_list[i][7] = True
            gs_cp = deepcopy(gs)
            gs.save_state = False


        if not gameOver:
            gs.time += 1
            monster_move(gs)
            draw_game_state(screen, gs)
            draw_health_state(screen, gs.health_bar)
            screen.blit(text_level, (0, 0))
            screen.blit(text_health, (0, 50))

        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    draw_map(screen)
    draw_object(screen, gs.map)


def draw_map(screen):
    for r in range(DIMENSION_X):
        for c in range(DIMENSION_Y):
            screen.blit(IMAGES_OBJ['f1'], p.Rect(c * SQ_SIZE, 100 + r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_object(screen, map):
    for r in range(DIMENSION_X):
        for c in range(DIMENSION_Y):
            obj = map[r][c]
            screen.blit(IMAGES_OBJ[obj], p.Rect(c*SQ_SIZE, 100+r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_health_state(screen, health_bar):
     for c in range(3):
         obj = health_bar[c]
         screen.blit(IMAGES_HEALTH[obj], p.Rect(140+c*45, 55, 40, 40))


def draw_text(screen, text):
    font = p.font.SysFont("Helvitca", 96, True, False)
    textObject = font.render(text, False, p.Color('Black'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)


def monster_move(gs):
    for monster in gs.monster_list:
        if monster[7]:
            gs.make_move(monster[0], (0, 0), monster[1])


if __name__ == "__main__" :
    main()

pygame.quit()
