import pygame
import sys
import math
from pygame.locals import *

#Settings
#Game Option/Settings
TITLE = "Bartender"
FPS = 10
WIDTH = 800
HEIGHT = 480
FONT_NAME = 'helvetica'

#Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Spacing and Buffers
NUMBER_OF_COLUMNS = 3
wbuff = WIDTH/6.5
hbuff = HEIGHT/10

#DRINKS
drinks_arr = ["AAAAAAAAAAAAAAA", "AMF", "Long Island", "Old Fashion", "Bloody Mary", "ABCDEFGHIJKLMN", "Manhatton"] #Place Holder

class Bar:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Bartender")
        self.clock = pygame.time.Clock()
        self.running = True
        self.color = True
        self.last_update = 0
        self.position = 0
        #pygame.draw.rect(self.screen, BLACK,[50,50,100,200], 3)
        self.font_name = pygame.font.match_font(FONT_NAME)
        
    def update(self):
        # Game Loop - Update
        self.blink()
        print(self.position)
        
    def draw(self):
        # Game Loop - draw
        self.screen.fill(WHITE)
        # *after* drawing everything, flip
        #pygame.display.flip() #Do I need this? 
        
    def run(self):
        # main game loop
        self.clock.tick(FPS)
        self.menu()
        self.event()
        self.update()
        self.draw()
        
        
    def event(self):
        # event game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            #selector
            const = NUMBER_OF_COLUMNS
            pos = self.position
            """
            example
            0 1 2
            3 4 5
            6 7 8
            3 colums
            to move to the right add 1
            to move to the left sub 1
            to move up and down add or subtract the number of columns
            """
            #moving left
            if self.position <= len(drinks_arr):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.position = self.position + 1
            #moving down
            if self.position + const <= len(drinks_arr)+1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.position = self.position + const
            if self.position > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.position = self.position - 1
            if self.position - const >= 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.position = self.position - const
        
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
                
    def menu(self):
        if not self.running:
            return
        #self.screen.fill(WHITE)
        #self.draw_text("Bartender", 48, BLACK, WIDTH/2, HEIGHT/4)
        #pygame.draw.rect(self.screen, BLACK, [50, 50, 100, 200], 2)
        self.drinks()
        x = WIDTH*((self.position%NUMBER_OF_COLUMNS+1)*2-1)/(2*NUMBER_OF_COLUMNS)-wbuff
        y = hbuff*(self.position//NUMBER_OF_COLUMNS+1)
        print(x)
        print(y)
        if self.color == True:
            pygame.draw.rect(self.screen, WHITE, [x,y,WIDTH/NUMBER_OF_COLUMNS, hbuff], 5)
        if self.color == False:
            pygame.draw.rect(self.screen, BLACK, [x,y,WIDTH/NUMBER_OF_COLUMNS, hbuff], 5)
        pygame.display.flip()
        
        
        
    def blink(self):
        now = pygame.time.get_ticks()
        blink_time = 800 # time in milseconds to alternate colors
        if self.color == True and now - self.last_update > blink_time:
            self.color = False
            self.last_update = now
        if self.color == False and now - self.last_update > blink_time:
            self.color = True
            self.last_update = now
    
    def drinks(self):
        #Max Char 15
        #drinks_arr = ["AAAAAAAAAAAAAAA", "AMF", "Long Island", "Old Fashion", "Bloody Mary", "ABCDEFGHIJKLMN", "Manhatton"]
        #number of columns
        n_cols = NUMBER_OF_COLUMNS
        rows = math.ceil(len(drinks_arr)/n_cols) #ex number of drinks is 4, 4/3 cieling is 2
        n = 0
        for j in range(1, rows+1):
            #if #colums/#row has a remainder add a for loop
            for i in range(1, n_cols+1): 
                self.draw_text(drinks_arr[n], 24, BLACK, WIDTH*((i*2-1)/(2*n_cols)),hbuff*j)
                if n == len(drinks_arr)-1:
                    break
                else:
                    n = n + 1
            
    
b = Bar()
while b.running:
    b.run()
    #b.menu()
    
pygame.quit()
sys.exit()
    
    
        
