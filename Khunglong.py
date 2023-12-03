import pygame
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas',15)

pygame.display.set_caption('Game Khung Long')

screen = pygame.display.set_mode((600,300))
nen = pygame.image.load(r'hinhanh\nen.jpg')
khunglong = pygame.image.load(r'hinhanh\khunglong.png')
vatcan = pygame.image.load(r'hinhanh\vatcan.png')
chim = pygame.image.load(r'hinhanh\chim.png')
amthanh1 = pygame.mixer.Sound(r'amthanh\tick.wav')
amthanh2 = pygame.mixer.Sound(r'amthanh\te.wav')

nen_x, nen_y = 0, 0
vatcan_x, vatcan_y = 510, 230
khunglong_x, khunglong_y = 10, 230
chim_x, chim_y = 700, 120
roi = 7
tocdogame = 5
lucnhay = 100

running = True
nhay = False
choigame = True

diem,kiluc = 0, 0

def vacham():
    if khunglong_game.colliderect(vatcan_game) or khunglong_game.colliderect(chim_game):
        pygame.mixer.Sound.play(amthanh2)
        return False
    return True



while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and choigame and khunglong_y >= 230:
                nhay=True
                pygame.mixer.Sound.play(amthanh1)
            if event.key == pygame.K_SPACE and choigame == False:
                choigame = True
    
    diem_txt = font.render(f'Điểm: {int(diem)}', True, (128,128,128))
    kiluc_txt = font.render(f'Kỉ lục: {int(kiluc)}', True, (128,128,128))
    ketthuc_txt = font.render('Kết Thúc', True, (128,128,128))
    if choigame:
        nen_game = screen.blit(nen, (nen_x, nen_y))
        nen_game_2 = screen.blit(nen, (nen_x+600, nen_y))
        nen_x -= tocdogame
        if nen_x < -599: nen_x = 0
        
        vatcan_game = screen.blit(vatcan, (vatcan_x, vatcan_y), )
        vatcan_x -= tocdogame
        if vatcan_x < -20: vatcan_x = 510
        
        khunglong_game = screen.blit(khunglong, (khunglong_x,khunglong_y))
        if khunglong_y >= lucnhay and nhay == True: 
            khunglong_y -= roi
        else:
            nhay = False
        if khunglong_y < 230 and nhay == False:
            khunglong_y += roi
        
        chim_game = screen.blit(chim, (chim_x, chim_y))
        hiendiem = screen.blit(diem_txt, (10, 10))
        hienkiluc = screen.blit(kiluc_txt, (10, 40))
        diem += 0.1    
        if diem > kiluc : kiluc = diem
        if diem > 20:
            tocdogame = 6
            roi = 8
        if diem > 40:
            tocdogame = 8
            roi = 10
            lucnhay = 30
            chim_x -= tocdogame
            if chim_x < -20: chim_x = vatcan_x + 900
        if diem > 100:
            tocdogame = 10
            roi = 12
            
        choigame = vacham()
    else:
        nen_x, nen_y = 0, 0
        vatcan_x, vatcan_y = 510, 230
        khunglong_x, khunglong_y = 10, 230
        chim_x, chim_y = 1000, 150
        nen_game = screen.blit(nen, (nen_x, nen_y))
        vatcan_game = screen.blit(vatcan, (vatcan_x, vatcan_y))
        khunglong_game = screen.blit(khunglong, (khunglong_x,khunglong_y))
        chim_game = screen.blit(chim, (chim_x, chim_y))
        hiendiem = screen.blit(diem_txt, (10, 10))
        hienkiluc = screen.blit(kiluc_txt, (10, 40))   
        hienketthuc = screen.blit(ketthuc_txt, (260, 130))      
        roi = 7
        tocdogame = 5
        lucnhay = 100
        diem = 0
    
    
    
    
    pygame.display.update()