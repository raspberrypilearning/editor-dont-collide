from p5 import *
from random import randint, seed

screen_size = 400
safe = Color(200, 100, 0)
player_emoji = "🤠"
crash_emoji = "💥"
obstacle_emoji = "🌵"
player_y = 320
obstacle_count = 8
obstacle_speed = 2
frames_survived = 0
score = 0
game_over = False


def player_x():
    return max(20, min(mouse_x, screen_size - 40))


def draw_player(player_on_safe):
    icon = player_emoji if player_on_safe else crash_emoji
    text(icon, player_x(), player_y)


def draw_obstacles():
    seed(1234)
    for _ in range(obstacle_count):
        obstacle_x = randint(0, screen_size)
        obstacle_y = randint(0, screen_size) + frames_survived * obstacle_speed
        obstacle_y = obstacle_y % screen_size
        text(obstacle_emoji, obstacle_x, obstacle_y)


def draw_hud():
    text_size(20)
    text(f"Score: {score}", 10, 30)
    if game_over:
        text("Click to play again", 110, 60)
    text_size(40)


def reset_game():
    global frames_survived, score, game_over
    frames_survived = 0
    score = 0
    game_over = False


def mouse_pressed():
    if game_over:
        reset_game()


def setup():
    size(screen_size, screen_size)
    text_size(40)


def draw():
    global frames_survived, score, game_over

    background(safe)
    draw_obstacles()
    draw_hud()

    player_on = get(int(player_x()), player_y).hex
    player_on_safe = player_on == safe.hex

    if not game_over and player_on_safe:
        draw_player(True)
        frames_survived += 1
        score = frames_survived // 10
    else:
        game_over = True
        draw_player(False)
        text("Game over", 120, 130)


run()
