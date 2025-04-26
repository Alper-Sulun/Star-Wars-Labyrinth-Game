import pygame
from classes import Character, Location, Stormtrooper, LukeSkywalker, MasterYoda, Stormtrooper, KyloRen, DarthVader
from collections import deque

# Pygame başlat
pygame.init()
pygame.mixer.init() 

# Müzik dosyasını yükle ve çalmaya başla
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 0.0)  # Döngüsel müzik
damage_sound = pygame.mixer.Sound('damage_sound.mp3')
wall_destruction = pygame.mixer.Sound('wall_destruction.mp3')

start_time = None  # draw_timer fonksyionu için şimdilik None olarak atandı

# Ekran boyutları
TILE_SIZE = 50  # Her karenin boyutu 

# Haritayı dosyadan oku
def load_map(file_name):
    with open(file_name, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

MAP = load_map('map.txt')

# Ekranı oluştur
WIDTH = len(MAP[0]) * TILE_SIZE
HEIGHT = (len(MAP) * TILE_SIZE) + 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Tile Map")

# Renkler
YELLOW = (255,255,0)
BLUE = (0 , 0, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
TEXT_COLOR = (0, 0, 255)  # Mavi renk
GREY = (128 ,128 ,128)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

# Player bilgileri
player_location = Location(6, 5)

#Düşman bilgileri
stormtrooper_location = Location(12,0)
stormtrooper = Stormtrooper("Stormtrooper","Kötü",stormtrooper_location)

kylo_ren_location = Location(4,10)
kyloRen = KyloRen("Kylor Ren","Kötü",kylo_ren_location)

darth_vader_location = Location(13,5)
darth_vader = DarthVader("Darth Vader","Kötü",darth_vader_location)

#Düşmanlar için görselleri yükleme ve boyularını ayarlama
stormtrooper_image = pygame.image.load('stormtrooper.png')
stormtrooper_image = pygame.transform.scale(stormtrooper_image,(TILE_SIZE - 10, TILE_SIZE))

kylo_ren_image = pygame.image.load('kylo_ren_image.png')
kylo_ren_image = pygame.transform.scale(kylo_ren_image,(TILE_SIZE - 10, TILE_SIZE))

darth_vader_image = pygame.image.load('darth_vader_image.png')
darth_vader_image = pygame.transform.scale(darth_vader_image, (TILE_SIZE - 10, TILE_SIZE))

# Oyuncu için görselleri yükle ve boyutlarını ayarla
player_images = [
    pygame.image.load('luke.png'),  # Karakter 1
    pygame.image.load('yoda.png')   # Karakter 2
]
# Yazı fontu
font = pygame.font.SysFont("Century Gothic", 35) 
# Kalp görselleri
left_heart = pygame.image.load('left_heart.png')
right_heart = pygame.image.load('right_heart.png')

# Görsellerin boyutları
left_heart = pygame.transform.scale(left_heart, (TILE_SIZE, TILE_SIZE))
right_heart = pygame.transform.scale(right_heart, (TILE_SIZE, TILE_SIZE))

hearts_count = 6

# Kalp çizme fonksiyonu
def draw_hearts():
    global hearts_count
    for i in range(hearts_count):
        # Sol yarım kalp
        screen.blit(left_heart, (4 * TILE_SIZE, 11 * TILE_SIZE))   # (4,11) konumuna sol yarım kalp
        screen.blit(right_heart, (5 * TILE_SIZE, 11 * TILE_SIZE))  # (5,11) konumuna sağ yarım kalp
        screen.blit(left_heart, (6 * TILE_SIZE, 11 * TILE_SIZE))   # (6,11) konumuna sol yarım kalp
        screen.blit(right_heart, (7 * TILE_SIZE, 11 * TILE_SIZE))  # (7,11) konumuna sağ yarım kalp
        screen.blit(left_heart, (8 * TILE_SIZE, 11 * TILE_SIZE))   # (8,11) konumuna sol yarım kalp
        screen.blit(right_heart, (9 * TILE_SIZE, 11 * TILE_SIZE))  # (9,11) konumuna sağ yarım kalp

trophy = pygame.image.load('trophy.png')
trophy = pygame.transform.scale(trophy, (TILE_SIZE, TILE_SIZE))  # Kupayı hücre boyutuna ölçeklendir

# Haritayı çiz
def draw_board():
    for row in range(len(MAP)):
        for col in range(len(MAP[0])):
            # 6. satır 5. sütun için sarı renk
            if row == 5 and col == 6:
                color = (255, 255, 0)  # Sarı             
            else:
                color = BLACK if MAP[row][col] == 1 else GREY
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (200, 200, 200), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)  # Kılavuz çizgileri
    #Kupa görseli
    screen.blit(trophy, (13 * TILE_SIZE, 9 * TILE_SIZE))   

    draw_hearts()

    # Düşmanların Giriş kapıları: 
    text_A = font.render("A", True, TEXT_COLOR)
    screen.blit(text_A, (0 * TILE_SIZE + TILE_SIZE // 4, (5 * TILE_SIZE + TILE_SIZE // 4) - 10))  # Küçük yerleştirme için TILE_SIZE/4 ekledik
    text_B = font.render("B", True, TEXT_COLOR)
    screen.blit(text_B, (4 * TILE_SIZE + TILE_SIZE // 4, (0 * TILE_SIZE + TILE_SIZE // 4) - 10))
    text_C = font.render("C", True, TEXT_COLOR)
    screen.blit(text_C, (12 * TILE_SIZE + TILE_SIZE // 4, (0 * TILE_SIZE + TILE_SIZE // 4) - 10))
    text_D = font.render("D", True, TEXT_COLOR)
    screen.blit(text_D, (13 * TILE_SIZE + TILE_SIZE // 4, (5 * TILE_SIZE + TILE_SIZE // 4) - 10))
    text_E = font.render("E", True, TEXT_COLOR)
    screen.blit(text_E, (4 * TILE_SIZE + TILE_SIZE // 4, (10 * TILE_SIZE + TILE_SIZE // 4) - 10))
    

# Karakter Seçimi İçin Görseller ve Seçim Fonksiyonu
def draw_character_selection():
    screen.fill(BLUE)
    
    # Başlık yazısı
    title_text = font.render('BİR KARAKTER SEÇ', True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))
    
    # Karakterleri çizme
    for i, img in enumerate(player_images):
        x = ((WIDTH // 4) + 50) * (i + 1) - img.get_width() // 2
        y = HEIGHT // 2 - img.get_height() // 2
        screen.blit(img, (x, y))
    
    pygame.display.flip()

def get_character_selection():
    global selected_character
    selected_character = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i, img in enumerate(player_images):
                    char_rect = pygame.Rect(((WIDTH // 4) + 50) * (i + 1) - img.get_width() // 2, HEIGHT // 2 - img.get_height() // 2, img.get_width(), img.get_height())
                    if char_rect.collidepoint(x, y):
                        selected_character = i  # Seçilen karakterin indeksini al
                        running = False
        # Ekranı güncelle
        draw_character_selection()

    return selected_character

def draw_timer():
    global start_time
    
    if selected_character is not None:
        # Eğer start_time henüz başlatılmadıysa, şu anki zamanı kaydet
        if start_time is None:
            start_time = pygame.time.get_ticks()
        
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Milisaniyeyi saniyeye çevir
        timer_text = font.render(f"Geçen Zaman: {elapsed_time}s", True, WHITE)
        screen.blit(timer_text, (10, HEIGHT - 90))  # Süreyi ekrana çiz

for i in range(len(player_images)):
    player_images[i] = pygame.transform.scale(player_images[i], (TILE_SIZE * 3, TILE_SIZE * 3))

# Seçilen karakterin bilgileri
selected_character_index = get_character_selection()
if selected_character_index == 0:
    Luke = LukeSkywalker("Luke Skywalker", "Good", player_location, hearts_count)
    luke_image = pygame.image.load('luke.png')
    luke_image = pygame.transform.scale(luke_image, (TILE_SIZE - 10, TILE_SIZE))
elif selected_character_index == 1:
    Luke = MasterYoda("Yoda", "Good", player_location, hearts_count)
    luke_image = pygame.image.load('yoda.png')
    luke_image = pygame.transform.scale(luke_image, (TILE_SIZE + 10, TILE_SIZE))

# Karakterleri çiz
def draw_player():    
    screen.blit(luke_image, (player_location.x * TILE_SIZE, player_location.y * TILE_SIZE))
    screen.blit(stormtrooper_image,(stormtrooper_location.x * TILE_SIZE,stormtrooper_location.y * TILE_SIZE))
    screen.blit(kylo_ren_image,(kylo_ren_location.x * TILE_SIZE,kylo_ren_location.y * TILE_SIZE))
    screen.blit(darth_vader_image,(darth_vader_location.x * TILE_SIZE,darth_vader_location.y * TILE_SIZE))

def victory(current_time):

    global game_over_text
    # Mevcut müziği durdur
    pygame.mixer.music.stop()

    # Yeni müziği yükle ve çalmaya başla
    pygame.mixer.music.load('victory_music.mp3')  # Game over müziğinizin dosya yolu
    pygame.mixer.music.play(1, 0.0)
    screen.fill(BLUE)  # Arka plan
    # "Game Over" yazısını çiz
    game_over_text = font.render("KAZANDIN! İMPARATORLUK YENİLDİ!", True, GREEN)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    
    # Geçen süreyi hesapla
    rank = None
    elapsed_time = (current_time - start_time) / 1000  # Geçen zamanı saniye olarak hesapla
    time_text = font.render(f"Geçen Süre: {elapsed_time:.2f} saniye", True, WHITE)
    
    # Geçen zamana göre rank belirleme
    if elapsed_time < 5:
        rank = "S"
    elif elapsed_time >= 5 and elapsed_time < 10:
        rank = "A"
    elif elapsed_time >= 10 and elapsed_time < 15:
        rank = "B"
    elif elapsed_time >= 15 and elapsed_time < 20:
        rank = "C"
    elif elapsed_time >= 20 and elapsed_time < 25:
        rank = "D"
    elif elapsed_time >= 25:
        rank = "E"
    
    rank_text = font.render(f"Rank: {rank}","TRUE",ORANGE)
    screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2))
    screen.blit(rank_text, (WIDTH // 2 - rank_text.get_width() // 2, (HEIGHT // 2) + 50))

    pygame.display.flip()  # Ekranı güncelle

    # Game Over ekranında tuşa basılana kadar bekle
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False  # Pencereyi kapatmak için çıkış yap

def you_lose(current_time):

    global game_over_text
    # Mevcut müziği durdur
    pygame.mixer.music.stop()

    # Yeni müziği yükle ve çalmaya başla
    pygame.mixer.music.load('game_over_music.mp3')  # Game over müziğinizin dosya yolu
    pygame.mixer.music.play(1, 0.0)
    screen.fill(BLUE)  # Arka plan
    # "Game Over" yazısını çiz
    game_over_text = font.render("KAYBETTİN! İMPARATORLUK KAZANDI!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, (HEIGHT // 3) + 50))
    
    # Geçen süreyi hesapla
    rank = None
    elapsed_time = (current_time - start_time) / 1000  # Geçen zamanı saniye olarak hesapla
    time_text = font.render(f"Geçen Süre: {elapsed_time:.2f} saniye", True, WHITE)
    
    screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()  # Ekranı güncelle

    # Game Over ekranında tuşa basılana kadar bekle
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False  # Pencereyi kapatmak için çıkış yap

#Düşmanların hareket hızı
stormtrooper_move_speed = 350 
kylo_ren_move_speed = 350
darth_vader_move_speed = 350

#Son hareket zamanları
last_stormtrooper_move_time = pygame.time.get_ticks() 
last_kylo_ren_move_time = pygame.time.get_ticks()
last_darth_vader_move_time = pygame.time.get_ticks()
global choose #Karaktere göre can azaltma 

def move_stormtrooper(grid, current_time):
    global last_stormtrooper_move_time, hearts_count
    # BFS ile en kısa yolu bul
    path = Stormtrooper.bfs(stormtrooper_location, player_location, grid)

    if path and current_time - last_stormtrooper_move_time > stormtrooper_move_speed:
        # Eğer yol varsa, ilk adımdan birini al ve Stormtrooper'ı o yönde hareket ettir
        next_x, next_y = path[0]
        stormtrooper_location.x = next_x
        stormtrooper_location.y = next_y

        if stormtrooper_location.x == player_location.x and stormtrooper_location.y == player_location.y:
            # Aynı lokasyona gelindiğinde kalp sayısını ve görseli azalt
            if hearts_count > 0:
                hearts_count -= choose
                damage_sound.play(maxtime=0)
                
        #Son hareket zamanını güncelle
        last_stormtrooper_move_time = current_time

def move_kylo_ren(grid, current_time):
    global last_kylo_ren_move_time, hearts_count
    # BFS ile en kısa yolu bul
    path = KyloRen.bfs(kylo_ren_location, player_location, grid)

    if path and current_time - last_kylo_ren_move_time > kylo_ren_move_speed:
        # Eğer en az iki adım varsa, ikinci adıma git, yoksa sadece ilk adımı al
        if len(path) >= 2:
            next_x, next_y = path[1]  # İkinci adıma git
        else:
            next_x, next_y = path[0]  # Sadece bir adım varsa onu al
        
        kylo_ren_location.x = next_x
        kylo_ren_location.y = next_y

        if kylo_ren_location.x == player_location.x and kylo_ren_location.y == player_location.y:
            # Aynı lokasyona gelindiğinde kalp sayısını ve görseli azalt
            if hearts_count > 0:
                hearts_count -= choose
                damage_sound.play(maxtime=0)
                
        # Son hareket zamanını güncelle
        last_kylo_ren_move_time = current_time

def move_darth_vader(grid, current_time):
    global last_darth_vader_move_time, hearts_count
    # BFS ile en kısa yolu bul
    path = DarthVader.bfs(darth_vader_location, player_location, grid)

    if path and current_time - last_darth_vader_move_time > darth_vader_move_speed:
        # Eğer yol varsa, ilk adımdan birini al ve Darth Vader'ı o yönde hareket ettir
        next_x, next_y = path[0]

        # Eğer bir duvarı yıkıyorsa, yalnızca o karede yıkım uygula
        if grid[next_y][next_x] == 0:
            grid[next_y][next_x] = 1  # Duvarı yık
            wall_destruction.play(maxtime=0)

        darth_vader_location.x = next_x
        darth_vader_location.y = next_y

        if darth_vader_location.x == player_location.x and darth_vader_location.y == player_location.y:
            # Aynı lokasyona gelindiğinde kalp sayısını ve görseli azalt
            if hearts_count > 0:
                hearts_count -= choose
                damage_sound.play(maxtime=0)
                
        #Son hareket zamanını güncelle
        last_darth_vader_move_time = current_time

# Ana döngü
running = True
clock = pygame.time.Clock()  # FPS kontrolü için saat
player_move_speed = 140  # Hareket arası bekleme süresi (milisaniye cinsinden)
last_move_time = pygame.time.get_ticks()  # Son hareket zamanını kaydet
game_timer_start = None

while running:
    screen.fill(BLUE)  # Arka plan
    draw_board()

    # Tuşlara basılma olaylarını alma
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tuşları alma
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    # Hız kontrolü: Eğer move_speed kadar zaman geçtiyse, hareketi gerçekleştir
    if current_time - last_move_time > player_move_speed:
        new_x, new_y = player_location.x, player_location.y  # Doğrudan x ve y'yi al

        if keys[pygame.K_LEFT]:
            new_x -= 1
        if keys[pygame.K_RIGHT]:
            new_x += 1
        if keys[pygame.K_UP]:
            new_y -= 1
        if keys[pygame.K_DOWN]:
            new_y += 1

        # Yeni konum 1 mi kontrol et
        if 0 <= new_x < len(MAP[0]) and 0 <= new_y < len(MAP):
            if MAP[new_y][new_x] == 1:
                player_location.x = new_x  # x'i doğrudan atama yap
                player_location.y = new_y  # y'yi doğrudan atama yap

                # Oyunun sonlanması için gereken koşul
                if new_x == 13 and new_y == 9:
                    victory(current_time)  # Game Over ekranını göster
                    running = False  # Bu satırı sadece "Game Over" sonrasında beklemesi için kaldırıyoruz.

        last_move_time = current_time  # Son hareket zamanını güncelle

    if selected_character_index == 0: #Luke için olan kalp götürme sistemi
        choose = 2
        if hearts_count == 4:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            
        if hearts_count == 2:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (7 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (6 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))       

        if hearts_count == 0:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (7 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (6 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (5 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (4 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))      

    if selected_character_index == 1: # Yoda için olan kalp götürme sistemi
        choose = 1
        if hearts_count == 5:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        if hearts_count == 4:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))            
        if hearts_count == 3:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (7 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        if hearts_count == 2:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (7 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (6 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        if hearts_count == 1:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (7 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (6 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (5 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        if hearts_count == 0:
            pygame.draw.rect(screen, GREY, (9 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (8 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (7 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (6 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (5 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GREY, (4 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE))  

    if hearts_count <= 0:
        running = False
        you_lose(pygame.time.get_ticks())

    move_stormtrooper(MAP,current_time)

    move_kylo_ren(MAP, current_time)

    move_darth_vader(MAP, current_time)

    draw_player()  # Karakteri çiz

    draw_timer()  

    pygame.display.flip()  # Ekranı güncelle

    clock.tick(60)  # FPS ayarı 

pygame.quit()