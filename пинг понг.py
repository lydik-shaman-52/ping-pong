import pygame

pygame.init()
pygame.mixer.init()

win_width = 700
win_height = 500
display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Пинг понг")


class GameSprite():
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed


class Player(GameSprite):
    def update1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - self.rect.height - 5:
            self.rect.y += self.speed

    def update2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - self.rect.height - 5:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(display, (255, 255, 255), self.rect)
        pygame.draw.rect(display, (0, 0, 0), self.rect, 4)


class Ball(GameSprite):
    def __init__(self, x, y, radius, speed):
        super().__init__(x, y, radius * 2, radius * 2, speed)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(display, (200, 255, 0), self.rect.center, self.radius)
        pygame.draw.circle(display, (0, 0, 0), self.rect.center, self.radius, 2)


racket1 = Player(30, 200, 25, 120, 5)
racket2 = Player(win_width - 55, 200, 25, 120, 5)
ball = Ball(350, 250, 15, 4)

font = pygame.font.SysFont("Arial", 40, bold=True)
lose1 = font.render('игрок 1 проиграл', True, (200, 0, 0))
lose2 = font.render('игрок 2 проиграл', True, (200, 0, 0))

game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

speed_x = 4
speed_y = 4

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False


    if not finish:
        display.fill((200, 255, 255))
        racket1.update1()
        racket2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.top <= 0 or ball.rect.bottom >= win_height:
        speed_y *= -1

    if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        display.blit(lose1, (200, 220))
    if ball.rect.x > win_width:
        finish = True
        display.blit(lose2, (200, 220))
    racket1.draw()
    racket2.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(FPS)

