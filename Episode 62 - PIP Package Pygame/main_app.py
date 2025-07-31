import pygame

'''
Struktur program yang harus ada ketika membuat game:
1. init = untuk inisialisasi, bisa dikatakan proses pembuatan world game
2. User input, database input = program untuk mengambil input dari user(interaksi user ke program)
3. Update asset = untuk memproses dari hasil inputan dari user terhadap game nya
4. Render ke display = memvisualisasikan dari program sebelumnya
'''
# init
pygame.init()   # Start game program

# Memuat object
## Ukuran obejct
object_panjang = 20
object_lebar = 20

## Posisi start object
object_position_x = 400
object_position_y = 250

## Kecepatan gerak posisi
speed = 10

## Color Palette
red = pygame.Color(225,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)

# membuat display surface object
window_panjang = 800
window_lebar = 500
window = pygame.display.set_mode((window_panjang,window_lebar)) # Nilai nya (x,y)

isRun = True    # variable dummy default nilainya True

while isRun:     # Untuk melooping game program supaya tidak berhenti
    pygame.time.delay(10)
    # proses input dan database input yang sudah dibuat
    for event in pygame.event.get():    # mengambil semua kejadian dari program yang berjalan
        if event.type == pygame.QUIT:   # mengaktifkan dan merecord interaksi ketika mengklik close button
            isRun = False       # Jika nilainya False akan ke fungsi while, ketika di click close windownya akan bernilai false
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and object_position_x > 0:
        object_position_x -= speed
    
    if keys[pygame.K_RIGHT] and object_position_x < window_panjang-object_panjang:
        object_position_x += speed

    if keys[pygame.K_DOWN] and object_position_y < window_lebar-object_lebar:
        object_position_y += speed

    if keys[pygame.K_UP] and object_position_y > 0:
        object_position_y -= speed


    window.fill(white)

    pygame.draw.rect(window,green,(object_position_x,object_position_y,object_panjang,object_lebar))
    
    pygame.display.update()

pygame.quit()

