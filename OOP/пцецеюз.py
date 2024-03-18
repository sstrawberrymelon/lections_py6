import pygame
import random 
from os import path #ос библиотека позволяет пройтись по порталам в одном и том же файле как (python.priject)
#path это путь 
#таким образом мы получим доступ к файлам 
img_dir = path.join(path.dirname(__file__), 'img)') #созадаем переменную ,это будет наша папка с изображением 
#создали переменную к кторой мы будем обращаться когда нам будет нужно изображение 
snd_dir = path.join(path.dirname(__file__, 'snd'))
WIDTH = 360
HEIGTH = 480
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (191, 63, 242)
PINK = (219, 31, 112)
colors = [WHITE, BLACK, RED, GREEN, BLUE, PINK]
pygame.init()
pygame.mixer.init() #запуск пайгэйм с миксер
screen = pygame.display.set_mode((WIDTH,HEIGTH)) #задать пропорции, сразу сохранили как кортеж
pygame.display.set_caption('Game') #назвать окошко
clock = pygame.time.Clock() #сколько кадров в сек , чистота кадров
running = True
#зарисовка игроков
player_img = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert() #изображение игрока 
meteor_img = pygame.image.load(path.join(img_dir, 'meteorBrown_ned1.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'LaserRed16.png')).convert()
meteor_images = []
meteor_list = ['meteorBrown_small1.png',
               'meteorGrey_small1.png',
               'meteorBrown_tiny1.png',
               'meteorBrown_big1.png',
               'meteorBrown_small1.png',
               ]
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
    shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav')) 
class Player (pygame.sprite.Sprite): #запуск всех функций в библиотеке пайгэйм
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(BLACK) 
        #self.image = pygame.Surface((50,40)) #выделяет поверхность для закраски типа фото втсавить с размеров 50/40
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect() #рэктэнгл присваиваю
        self.radius = 20
        pygame.draw.circle(self.image, RED , self.rect.center , self.radius) #это нужно чтобы сверху нарисовали кружочек и ударялись так 
        self.rect.centerx = WIDTH/2 # центр х ,чтоб был в центре
        self.rect.bottom = HEIGTH - 10 # ПОДНЯТЬ ЕГО НА 10 пик выше
        self.speedx = 0 #скорость по х
        self.hp = 100 #здоровье игрока 
    def update(self):
        self.speedx = 0 #
        keystate = pygame.key.get_pressed() #какая кнопка нажата
        if keystate[pygame.K_LEFT]:
            self.speedx = -8 #-8 это насколько пикселей он продвинется при нажатии кнопки лево
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x +=self.speedx
        if self.rect.right >= WIDTH: #чтобы не выходила за границы самой ширины
            self.rect.right = WIDTH  # тоже самое с высотой
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()
YELLOW = (230, 183, 16)
class Bullet (pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
class Mob(pygame.sprite.Sprite): #
    def __init__(self): #
        pygame.sprite.Sprite.__init__(self) #
        self.image_orig = random.choice(meteor_images)
        self.image.set_colorkey(PURPLE)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(WIDTH - self.rect.width) #
        self.rect.y = random.randrange(-100,-40) #
        self.speedx = random.randrange(-3,3) #
        self.speedy = random.randrange(1,8) #
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
    def rotate(self):
        self.rotate()
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top>HEIGTH+10 or self.rect.left<-25 or self.rect.right>WIDTH+20:
            #переобразовываются заново когда проходят опр точку
            self.rect.x = random.randrange(WIDTH-self.rect.width)  #
            self.rect.y = random.randrange(-100, -40)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range (8):
    for i in range(8):
     m = Mob(colors[i % 6])
    all_sprites.add(m)
    mobs.add(m)
score = 0
font_name = pygame.font.match_font('arial') #это название грифта корторый будет использовать
def draw_text(surf, text, size, x, y): #текст 
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def draw_hp(surf, x, y, pt): #pt это пойнт 
    if pt <0:
      pt =0 
    bar_length = 100
    bar_hight = 10 
    fill = (pt / 100) * bar_length
    outline_rect = pegame.Rect(x,y,bar_length, bar_height) #outline это обводка 
    fill_rect = pygame.Rect(x,y,fill, bar_height)
    pygame.draw.rect(surf, WHITE, outline_rect)# потом обводка 
    pygame.draw.rect(surf, GREEN , fill_rect) #чем зарисовывать 
#background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert() # фон будет хранить в себе изображение и через пайгайм вызываем функц для наложения изобр 
#background_rect = background.get_rect() #написали куда она пойдет в ректэнгл , загрузка изобрадения
while running:#
    clock.tick(FPS) #
    for event in pygame.event.get(): #для того чтоб код остановить когда игрок касается врага или когда на крестик нажимаешь
        if event.type == pygame.QUIT: #
            running = False #
        if event.type == pygame.KEYDOWN: # нажата кнопка 
            if event.key == pygame.K_SPACE:
                player.shoot()
            #отрисовка игроков
    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True,True) #тру тру это чтоб они оба исчезли и пулька и мобс 
    for fit in hits:
        score += 50
        m = Mob(RED)
        all_sprites.add(m)
        mobs.add(m)
    hits = pygame.sprites.spritecollide(player, mobs, True) # коллайд это пересечение каких то двух элементов, фалс что никто не исчезнет 
    for hit in hits: #если у игрока здоровье <0 он умирает 
       player.hp -= hit.rect.width / 2
       if payer.hp <= 0: 
         running = False 
    screen.fill(BLACK) #
    screen.blit(background , background_rect )#блит значит нарисовать сверху черного фона 
    all_sprites.draw(screen)
    draw_text(screen, str(score), 25, WIDTH - 50, 10)
    draw_hp(screen, 5,5, player.hp)
    pygame.display.flip() #перевернуть окошко, игрок потом задний фон
pygame.quit()
#зарисовка игроков