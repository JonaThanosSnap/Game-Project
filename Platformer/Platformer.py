import pygame
pygame.font.init()
pygame.mixer.init()

##### GAME SETUP #####

FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

##### GLOBAL VARIABLES #####

VEL = 4
monsters = pygame.sprite.Group()

##### SPRITE CLASSES #####

class Player_Sprite(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (128,128))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0

    def load_images(self):
        self.idle_frame = self.image
        self.walking_frames = [pygame.transform.scale(pygame.image.load("Assets/1 Pink_Monster/Walk Frames/pink_1.png"), (81,128)),
                                pygame.transform.scale(pygame.image.load("Assets/1 Pink_Monster/Walk Frames/pink_2.png"), (81,128)),
                               pygame.transform.scale(pygame.image.load("Assets/1 Pink_Monster/Walk Frames/pink_4.png"), (81,128)), 
                               pygame.transform.scale(pygame.image.load("Assets/1 Pink_Monster/Walk Frames/pink_5.png"), (81,128)), 
                               pygame.transform.scale(pygame.image.load("Assets/1 Pink_Monster/Walk Frames/pink_6.png"), (81,128))]

    def animate(self):
        now = pygame.time.get_ticks()

        if self.walking == True:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % 5
                self.image = self.walking_frames[self.current_frame]
        

##### INITIALIZING SPRITES #####

PINK_MONSTER = Player_Sprite(
    "Assets/1 Pink_Monster/Pink_Monster.png")

PINK_MONSTER.load_images()

BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/RLGMLA.png"), (1260,1000))

##### GAME FUNCTIONS #####

def draw_window(monsters):
    WIN.blit(BACKGROUND, (0,0))
    monsters.draw(WIN)

    pygame.display.update()


def movement(keys_pressed, character, up, down, left, right):  # MOVES THE CHARACTER
    if keys_pressed[up]:  # UP KEY
        character.rect.y -= VEL
        character.jumping = True
    if keys_pressed[down]:  # DOWN KEY
        character.rect.y += VEL
    if keys_pressed[left]: # LEFT KEY
        character.rect.x -= VEL
        character.walking = True
    if keys_pressed[right]: # RIGHT KEY
        character.rect.x += VEL
        character.walking = True
    else:
        character.walking = False
        character.jumping = False
        character.image = character.idle_frame
    
    character.animate()


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
        movement(keys_pressed, PINK_MONSTER, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

        draw_window(monsters)


if __name__ == "__main__":
    main()
