import pygame#遊戲模組 載入pygame module

pygame.init()#遊戲模組啟動
WINDOW_WIDTH,WINDOW_HEIGHT=800,600
displayscreen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))#產生畫布
pygame.display.set_caption("Blitting Image!")

bird_topleft=pygame.image.load("angrybird.png")#載入圖案
bird_topleft_rect=bird_topleft.get_rect()#取得圖案大小放在變數中
bird_topleft_rect.topleft=(0,0)#設定圖案出現位置

bird_topright=pygame.image.load("angrybird.png")#載入圖案
bird_topright_rect=bird_topright.get_rect()#取得圖案大小放在變數中
bird_topright_rect.topright=(WINDOW_WIDTH,0)#設定圖案出現位置

mickey_topleft=pygame.image.load("mickey.png")
mickey_topleft_rect=mickey_topleft.get_rect()
mickey_topleft_rect.topleft=(0,WINDOW_HEIGHT-64)

winnie_topright=pygame.image.load("winnie.png")
winnie_topright_rect=winnie_topright.get_rect()
winnie_topright_rect.topright=(WINDOW_WIDTH,WINDOW_HEIGHT-64)

WHITE=(255,255,255)
GREEN=(0,255,0)
DARKGREEN=(10,50,10)

#fonts=pygame.font.get_fonts() //取得PYGAME內建字形
system_font=pygame.font.SysFont("century",64)
custom_font=pygame.font.Font("AbstractGroovy.ttf",30) #載入外部字形

#define Text
show_text_1=system_font.render("Angry Bird Game:",True,GREEN,DARKGREEN)
show_text_1_rect=show_text_1.get_rect()#產生字體方框
show_text_1_rect.center=(WINDOW_WIDTH//2,30)

show_text_2=custom_font.render("Move angry bird soon!",True,GREEN)
show_text_2_rect=show_text_2.get_rect()
show_text_2_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+100)

#音效
sound_1=pygame.mixer.Sound("sound_1.wav")
sound_2=pygame.mixer.Sound("sound_2.wav")

sound_1.play()
pygame.time.delay(2000) #2000毫秒=2秒
sound_2.play()
pygame.time.delay(2000)

sound_2.set_volume(0.1) # 設音量 0.1~1.0
sound_2.play()          #播放

#背景音樂:
pygame.mixer.music.load("music.wav") #-1重複播放，從頭撥放
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(10000)
pygame.mixer.music.stop()
    



running=True
while running:
    for event in pygame.event.get():#抓取畫布上所有的指令
        
        if event.type==pygame.QUIT:
            running=False
            
    pygame.draw.line(displayscreen,WHITE,(0,75),(WINDOW_WIDTH,75),5)
    
    displayscreen.blit(bird_topleft,bird_topleft_rect)
    displayscreen.blit(bird_topright,bird_topright_rect)
    displayscreen.blit(mickey_topleft,mickey_topleft_rect)
    displayscreen.blit(winnie_topright,winnie_topright_rect)
    displayscreen.blit(show_text_1,show_text_1_rect)
    displayscreen.blit(show_text_2,show_text_2_rect)
   
    pygame.display.update()


pygame.quit()