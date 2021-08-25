import pygame
pygame.font.init()
pygame.mixer.init()

##### GAME SETUP #####

FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

##### GLOBAL VARIABLES #####

VEL = 7
monsters = pygame.sprite.Group()

##### SPRITE CLASSES #####


class Player_Sprite(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(picture_path), (128, 128))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


PINK_MONSTER = Player_Sprite(
    "C:/Users/andre/Documents/GitHub/Game-Project/Assets/1 Pink_Monster/Pink_Monster.png")

##### GAME FUNCTIONS #####


def draw_window(monsters):
    monsters.draw(WIN)

    pygame.display.update()


def movement(keys_pressed, character, up, down):  # MOVES THE CHARACTER
    if keys_pressed[up]:  # UP KEY
        character.rect.y -= VEL
    if keys_pressed[down]:  # DOWN KEY
        character.rect.y += VEL


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # IF PYGAME IS EXITED,
                run = False  # QUIT THE CODE
                pygame.quit()

        monsters.add(PINK_MONSTER)

        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, PINK_MONSTER, pygame.K_w, pygame.K_s)

        draw_window(monsters)


if __name__ == "__main__":
    main()
