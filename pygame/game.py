import pygame
import sys

# تعریف رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# تعریف اندازه صفحه
WIDTH, HEIGHT = 800, 600

# تعریف کلاس شخصیت
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        # مکان شخصیت را به موقعیت موس می‌بریم
        self.rect.center = pygame.mouse.get_pos()

# شروع بازی
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Game")
clock = pygame.time.Clock()

# تعریف گروه اجسام
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# حلقه اصلی بازی
running = True
while running:
    # حلقه ورودی کاربر
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # ایجاد یک تیر و اضافه کردن آن به گروه اجسام
            pass  # این قسمت را شما می‌توانید پیاده‌سازی کنید

    # آپدیت و رسم تمام اجسام
    all_sprites.update()

    # پاک کردن صفحه
    screen.fill(BLACK)
    
    # رسم تمام اجسام
    all_sprites.draw(screen)

    # نمایش صفحه
    pygame.display.flip()

    # تنظیم FPS
    clock.tick(60)

# خروج از بازی
pygame.quit()
sys.exit()
