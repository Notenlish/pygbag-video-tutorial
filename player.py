import pygame


class Player:
    def __init__(self, x, y) -> None:
        self.sprite_paths = {
            "stand": ["stand.png"],
            "walk": ["walk1.png", "walk2.png"],
            "jump": ["jump.png"],
        }

        _size = pygame.image.load(self.sprite_paths["stand"][0]).get_size()
        self.rect = pygame.Rect(x, y, _size[0], _size[1])
        self.vel = [0, 0]

        self.jump_speed = 350
        self.on_ground = False
        self.speed = 250

        self.anim_index = 0
        self.anim_timer = 0
        self.anim_name = "stand"
        self.flip_h = False

        # .waw files wont work with pygbag!
        self.jump_sound = pygame.mixer.Sound("jump.ogg")
        self.jump_sound.set_volume(0.15)

        self.load_sprites()

    def load_sprites(self):
        self.sprites = {}
        for animation_type, path_list in self.sprite_paths.items():
            self.sprites[animation_type] = []
            for path in path_list:
                img = pygame.image.load(path)
                self.sprites[animation_type].append(img)

    def update(self, pressed_keys, dt, ground):
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.on_ground:
                self.on_ground = not self.on_ground
                self.vel[1] = -self.jump_speed
                self.jump_sound.play()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.vel[0] = -self.speed
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        else:
            self.vel[0] = 0

        # anim
        if not self.on_ground:
            self.anim_name = "jump"
        elif self.vel[0] != 0:
            self.anim_name = "walk"
        else:
            self.anim_name = "stand"
            self.anim_timer = 0

        self.anim_timer += dt
        if self.anim_timer >= 0.15:
            self.anim_timer = 0
            self.anim_index += 1

        if self.vel[0] != 0:
            self.flip_h = self.vel[0] < 0
        self.anim_index %= len(self.sprites[self.anim_name])

        # jumping and collision
        self.vel[1] += 6  # gravity
        self.rect.move_ip((self.vel[0] * dt, self.vel[1] * dt))
        if self.rect.colliderect(ground.rect):
            self.on_ground = True
            self.vel[1] = 0
            self.rect.bottom = ground.rect.top

    def render(self, screen: pygame.Surface):
        sprites = self.sprites[self.anim_name]
        sprite = pygame.transform.flip(sprites[self.anim_index], self.flip_h, False)
        screen.blit(sprite, self.rect.topleft)
