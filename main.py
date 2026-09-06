import pygame
import random

pygame.init()
pygame.mixer.init()

# -------------------- Window & Fonts --------------------
font = pygame.font.SysFont("Open Sans", 30)
screen = pygame.display.set_mode((1100, 700))
clock = pygame.time.Clock()
FPS = 60

# -------------------- Sounds --------------------
pygame.mixer.music.load("./sounds/edm-gaming-music-335408.mp3")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

car_window_sound = pygame.mixer.Sound("./sounds/Car-Window-Smash.mp3")
car_window_sound.set_volume(0.5)

car_crash_sound = pygame.mixer.Sound("./sounds/car_crash_sound.mp3")
car_crash_sound.set_volume(0.5)

# -------------------- Start / End Images --------------------
background_1 = pygame.image.load("./image/photo-output.jpeg")
background_1 = pygame.transform.scale(background_1, (600, 600))
background_x = 250
background_y = 100

game_over = pygame.image.load("./image/photo-output3.jpeg")
game_over = pygame.transform.scale(game_over, (600, 600))
game_over_x = 250
game_over_y = 0

wone_player = pygame.image.load("./image/6.jpeg")
wone_player = pygame.transform.scale(wone_player, (600, 600))
wone_player_x = 250
wone_player_y = 100


# -------------------- Start Screen --------------------
def start():
    new_font = pygame.font.SysFont("Impact", 50, italic=True)
    start_button = pygame.Rect(450, 370, 200, 90)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(background_1, (background_x, background_y))
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            start_button,
            border_radius=20,
            width=10,
        )

        txt = new_font.render("START", True, (61, 107, 255))
        screen.blit(txt, (start_button.x + 35, start_button.y + 10))
        pygame.display.update()
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if e.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(e.pos):
                    return


# -------------------- Game Over Screen --------------------
def draw_game_over_screen(score, game_time):
    new_font = pygame.font.SysFont("Impact", 40, italic=True)
    restart_button = pygame.Rect(450, 370, 200, 90)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(game_over, (game_over_x, game_over_y))

        score_txt = new_font.render(f"Score: {score}", True, (255, 255, 255))
        time_text = font.render(f"Time : {game_time}", True, (255, 255, 255))

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            restart_button,
            border_radius=20,
            width=10,
        )

        restart_txt = new_font.render("RESTART", True, (253, 0, 0))

        screen.blit(score_txt, (480, 470))
        screen.blit(time_text, (500, 600))
        screen.blit(restart_txt, (restart_button.x + 27, restart_button.y + 18))
        pygame.display.update()
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if e.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(e.pos):
                    return "restart"

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return "restart"
                if e.key == pygame.K_ESCAPE:
                    return "quit"


# -------------------- Window Setup --------------------
pygame.display.set_caption("....speed racers....")
icon = pygame.image.load("./image/speed_racers.png")
pygame.display.set_icon(icon)

# -------------------- Game Background --------------------
background = pygame.image.load("./image/speed_racers_background.jpg")
background = pygame.transform.scale(background, (1200, 800))
background_y = 0
background_speed = 420  # pixels per second

# -------------------- Player Car --------------------
car_yellow_img = pygame.image.load("./image/yellow_car.png")
car_yellow_img = pygame.transform.scale(car_yellow_img, (50, 100))
car_yellow_x = 600
car_yellow_y = 650
car_yellow_speed = 300  # pixels per second

# -------------------- Enemy Cars --------------------
car1_img = pygame.image.load("./image/car1.png")
car1_img = pygame.transform.scale(car1_img, (50, 90))
car1_x = random.randint(390, 770)
car1_y = -100
car1_go = True

car2_img = pygame.image.load("./image/car2.png")
car2_img = pygame.transform.scale(car2_img, (50, 90))
car2_x = random.randint(390, 770)
car2_y = -100
car2_go = False

car3_img = pygame.image.load("./image/car3.png")
car3_img = pygame.transform.scale(car3_img, (50, 90))
car3_x = random.randint(390, 770)
car3_y = -100
car3_go = False

car4_img = pygame.image.load("./image/car4.png")
car4_img = pygame.transform.scale(car4_img, (50, 90))
car4_x = random.randint(390, 770)
car4_y = -100
car4_go = False

enemy_car_speed = 96  # pixels per second

# -------------------- Ball --------------------
ball_img = pygame.image.load("./image/football.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))
ball_x = -20
ball_y = -20
ball_speed = 600  # pixels per second
ball_active = True

# -------------------- Score & Health --------------------
score = 0
health = 100
max_health = 100
damage_per_crash = 10


def draw_txt_box(
    txt,
    txt_x,
    txt_y,
    bg_color,
    txt_color,
    border_color,
    border_radius=10,
    padding=10,
    border_width=3,
):
    txt_style = font.render(txt, True, txt_color)
    txt_rect = txt_style.get_rect()
    box_rect = pygame.Rect(
        txt_x,
        txt_y,
        txt_rect.width + padding * 2,
        txt_rect.height + padding * 2,
    )

    pygame.draw.rect(screen, bg_color, box_rect, border_radius=border_radius)
    pygame.draw.rect(
        screen,
        border_color,
        box_rect,
        border_width,
        border_radius=border_radius,
    )
    screen.blit(txt_style, (txt_x + padding, txt_y + padding))


def reset_game():
    """Reset all game values so the player can start again."""
    global score, health
    global car_yellow_x, car_yellow_y
    global car1_x, car2_x, car3_x, car4_x
    global car1_y, car2_y, car3_y, car4_y
    global car1_go, car2_go, car3_go, car4_go
    global ball_active, ball_x, ball_y, background_y, start_time

    score = 0
    health = max_health

    car_yellow_x, car_yellow_y = 600, 650

    car1_x = random.randint(390, 770)
    car2_x = random.randint(390, 770)
    car3_x = random.randint(390, 770)
    car4_x = random.randint(390, 770)

    car1_y = car2_y = car3_y = car4_y = -100
    car1_go, car2_go, car3_go, car4_go = True, False, False, False

    ball_active = True
    ball_x, ball_y = -20, -20
    background_y = 0
    start_time = pygame.time.get_ticks()


# -------------------- Main Game --------------------
start()
start_time = pygame.time.get_ticks()
running = True

while running:
    # Delta time makes movement independent of computer speed.
    dt = clock.tick(FPS) / 1000.0
    shoot_requested = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            shoot_requested = True

    # -------------------- Time --------------------
    ticks = pygame.time.get_ticks() - start_time
    seconds_total = ticks // 1000
    minutes = seconds_total // 60
    seconds = seconds_total % 60
    out = f"{minutes:02d}:{seconds:02d}"

    # -------------------- Win Condition --------------------
    # Win when the player reaches 10 points within 1 minute.
    if seconds_total >= 60 and score >= 10:
        pygame.mixer.music.stop()
        screen.fill((0, 0, 0))
        screen.blit(wone_player, (wone_player_x, wone_player_y))
        pygame.display.update()
        pygame.time.delay(4000)
        running = False
        continue

    # -------------------- Health / Game Over --------------------
    if health <= 0:
        pygame.mixer.music.stop()
        result = draw_game_over_screen(score, out)

        if result == "restart":
            reset_game()
            pygame.mixer.music.play(-1)
            continue

        running = False
        continue

    # -------------------- Background Movement --------------------
    background_y += background_speed * dt
    if background_y >= 800:
        background_y = 0

    # -------------------- Player Controls --------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        car_yellow_x -= car_yellow_speed * dt

    if keys[pygame.K_RIGHT]:
        car_yellow_x += car_yellow_speed * dt

    if keys[pygame.K_UP]:
        car_yellow_y -= car_yellow_speed * dt
        if car_yellow_y <= 0:
            car_yellow_y = 650

    # Keep the player's car inside the road boundaries.
    car_yellow_x = max(390, min(770, car_yellow_x))

    # -------------------- Ball Shooting --------------------
    # Only shoot once per SPACE press and only when no ball is already active.
    if shoot_requested and ball_active:
        ball_x = car_yellow_x + 15
        ball_y = car_yellow_y
        ball_active = False

    # -------------------- Enemy Car Movement --------------------
    if car1_go:
        car1_y += enemy_car_speed * dt
        if car1_y > 800:
            car1_y = -100
            car1_go = False
            car2_go = True

    elif car2_go:
        car2_y += enemy_car_speed * dt
        if car2_y > 800:
            car2_y = -100
            car2_go = False
            car3_go = True

    elif car3_go:
        car3_y += enemy_car_speed * dt
        if car3_y > 800:
            car3_y = -100
            car3_go = False
            car4_go = True

    elif car4_go:
        car4_y += enemy_car_speed * dt
        if car4_y > 800:
            car4_y = -100
            car4_go = False
            car1_go = True

    # -------------------- Collision Rectangles --------------------
    car1_rect = car1_img.get_rect(topleft=(car1_x, car1_y))
    car2_rect = car2_img.get_rect(topleft=(car2_x, car2_y))
    car3_rect = car3_img.get_rect(topleft=(car3_x, car3_y))
    car4_rect = car4_img.get_rect(topleft=(car4_x, car4_y))

    # -------------------- Ball Movement & Collision --------------------
    if not ball_active:
        ball_y -= ball_speed * dt

        if ball_y < -20:
            ball_active = True
            ball_x, ball_y = -20, -20
        else:
            ball_rect = ball_img.get_rect(topleft=(ball_x, ball_y))
            enemy_cars = [car1_rect, car2_rect, car3_rect, car4_rect]

            for i, car_rect in enumerate(enemy_cars):
                if ball_rect.colliderect(car_rect):
                    car_window_sound.play()

                    if i == 0:
                        car1_x = random.randint(375, 650)
                        car1_y = -100
                        car1_go, car2_go = False, True
                    elif i == 1:
                        car2_x = random.randint(375, 650)
                        car2_y = -100
                        car2_go, car3_go = False, True
                    elif i == 2:
                        car3_x = random.randint(375, 650)
                        car3_y = -100
                        car3_go, car4_go = False, True
                    elif i == 3:
                        car4_x = random.randint(375, 650)
                        car4_y = -100
                        car4_go, car1_go = False, True

                    ball_active = True
                    ball_x, ball_y = -20, -20
                    score += 1
                    break

    # -------------------- Player Collision --------------------
    car_yellow_rect = car_yellow_img.get_rect(
        topleft=(car_yellow_x, car_yellow_y)
    )

    enemy_cars = [car1_rect, car2_rect, car3_rect, car4_rect]

    for i, car_rect in enumerate(enemy_cars):
        if car_yellow_rect.colliderect(car_rect):
            car_crash_sound.play()

            if i == 0:
                car1_x = random.randint(350, 650)
                car1_y = -100
                car1_go, car2_go = False, True
            elif i == 1:
                car2_x = random.randint(350, 650)
                car2_y = -100
                car2_go, car3_go = False, True
            elif i == 2:
                car3_x = random.randint(350, 650)
                car3_y = -100
                car3_go, car4_go = False, True
            elif i == 3:
                car4_x = random.randint(350, 650)
                car4_y = -100
                car4_go, car1_go = False, True

            ball_active = True
            ball_x, ball_y = -20, -20
            score -= 1
            health = max(0, health - damage_per_crash)
            break

    # -------------------- Drawing --------------------
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - 800))

    screen.blit(car_yellow_img, (car_yellow_x, car_yellow_y))
    screen.blit(car1_img, (car1_x, car1_y))
    screen.blit(car2_img, (car2_x, car2_y))
    screen.blit(car3_img, (car3_x, car3_y))
    screen.blit(car4_img, (car4_x, car4_y))
    screen.blit(ball_img, (ball_x, ball_y))

    draw_txt_box(
        f"Score : {score}",
        900,
        10,
        bg_color=(25, 25, 25),
        txt_color=(255, 255, 255),
        border_color=(255, 215, 0),
        border_radius=12,
        padding=8,
        border_width=3,
    )

    draw_txt_box(
        f"Time : {out}",
        900,
        60,
        bg_color=(25, 25, 25),
        txt_color=(255, 255, 255),
        border_color=(0, 191, 255),
        border_radius=12,
        padding=8,
        border_width=3,
    )

    # -------------------- Health Bar --------------------
    health_bar_border = pygame.Rect(50, 10, 200, 20)
    health_width = int(200 * (health / max_health))
    health_bar_fill = pygame.Rect(50, 10, health_width, 20)

    pygame.draw.rect(screen, (255, 0, 0), health_bar_fill)
    pygame.draw.rect(screen, (255, 255, 255), health_bar_border, 2)

    pygame.display.update()

pygame.quit()





