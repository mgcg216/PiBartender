import RPi.GPIO as GPIO
from gpiozero import Button
import pygame
import sys
import math
import uinput
import os
from Drinks import *
from pygame.locals import *



#get admin access for uinput
os.system('sudo chmod 666 /dev/uinput')

#Settings
#Game Option/Settings
TITLE = "Bartender"
FPS = 30
WIDTH = 800
HEIGHT = 480
FONT_NAME = 'American Captain'

#Define Colors
WHITE = (255, 255, 255)
CLR = (200, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BGCOLOR = CLR

#Spacing and Buffers
NUMBER_OF_COLUMNS = 6
wbuff = WIDTH/6.5
hbuff = HEIGHT/10

#Buttons
device = uinput.Device([uinput.KEY_SPACE,
                        uinput.KEY_BACKSPACE,
                        uinput.KEY_UP,
                        uinput.KEY_DOWN,
                        uinput.KEY_LEFT,
                        uinput.KEY_RIGHT
                        ])
button_white = Button(26)
button_black = Button(19)
button_up = Button(4)
button_down = Button(27)
button_left = Button(2)
button_right = Button(17)


#DRINKS
#drinks_arr = ["AAAAAAAAAAAAAAA", "AMF", "Long Island", "Old Fashion", "Bloody Mary", "ABCDEFGHIJKLMN", "Manhatton"] #Place Holder

class Bar:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("PiBartender")
        self.clock = pygame.time.Clock()
        self.running = True
        self.color = True
        self.last_update = 0
        self.position = 0
        self.isMenu = True
        self.pour = False
        self.temp = 0 #Im a bad coder so i need this
        #self.isDispensing = False
        self.font_name = pygame.font.match_font(FONT_NAME)
        
    def update(self):
        # Game Loop - Update
        print(self.position)
        """
        if self.isMenu == True:
            self.isDispensing = False
        if self.isDispensing == True:
            self.isMenu = False
            """
        if self.isMenu == True:# and self.isDispensing == False:
            self.menu()
            self.blink()
        if self.isMenu == False:# and self.isDispensing == True:        
            self.dispense_window()
        #print("Menu is ",self.isMenu)
        #print("Dispensing is " ,self.isDispensing)
        
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BGCOLOR)
        # *after* drawing everything, flip
        #pygame.display.flip() #Do I need this? 
        
    def run(self):
        # main game loop
        self.clock.tick(FPS)
        self.event()
        self.update()
        self.draw()
        
        
    def event(self):
        # event game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
            pause = 0
            if self.isMenu == True:
                #moving right
                if self.position < len(drinks_arr)-1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.position = self.position + 1
                            time.sleep(pause)
                #moving down
                if self.position + const <= len(drinks_arr)-1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            self.position = self.position + const
                            time.sleep(pause)
                if self.position > 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.position = self.position - 1
                            time.sleep(pause)
                #moving up
                if self.position - const >= 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.position = self.position - const
                            time.sleep(pause)
            if self.isMenu == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.isMenu = False
                        #self.isDispensings = True
            if self.isMenu == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.isMenu = True
            
                    
        
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
        
        #loading bars for drink dispensing
        #work on this
    def load_bar(self, tim):
        ld_secs = 100
        tme = tim * 1000 #converts time into seconds
        #for i in range(1, ld_secs):
        now = pygame.time.get_ticks()
        if self.temp <= ld_secs and now - self.last_update > tme/ld_secs:
            #pygame.draw.rect(self.screen, BLACK, [1/6*WIDTH, 3/4*HEIGHT, self.temp*4/6*WIDTH/ld_secs, 5], 10)
            self.temp = self.temp + 1
            self.last_update = now
            print("SELF TEMP",self.temp)
        pygame.draw.rect(self.screen, BLACK, [1/6*WIDTH, 3/4*HEIGHT, self.temp*4/6*WIDTH/ld_secs, 5], 10)
        #pygame.draw.rect(self.screen, BLACK, [1/6*WIDTH, 3/4*HEIGHT, (self.temp-1)*4/6*WIDTH/ld_secs, 5], 10)
        
                
    """Drink Menu
    all drink can be order in different amount of columns
    they can be change using the NUMBER_OF_COLUMN variable"""
    def menu(self):
        if not self.running:
            return
        self.drinks()
        w = WIDTH/NUMBER_OF_COLUMNS*.9
        x = WIDTH*((self.position%NUMBER_OF_COLUMNS+1)*2-1)/(2*NUMBER_OF_COLUMNS)-w/2
        y = hbuff*(self.position//NUMBER_OF_COLUMNS+1)-HEIGHT/32
        if self.color == True:
            pass
        if self.color == False:
            pygame.draw.rect(self.screen, BLACK, [x,y,w, hbuff], 5)
            #pygame.draw.rect(self.screen, BLACK, [x,y,WIDTH/NUMBER_OF_COLUMNS-.1*wbuff, hbuff], 5)
        self.temp = 0
        pygame.display.flip()
        
    """Dispensing Drink Window
    """
    def dispense_window(self):
        if self.running == False:
            return
        #self.isMenu = False
        #self.isDispensing = True
        self.screen.fill(BGCOLOR)
        self.draw_text(drinks_arr[self.position], 48, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("Dispensing Now", 24, BLACK, WIDTH/2, HEIGHT/4)
        self.load_bar(60)
        pygame.display.flip()
        
        
        """blinks the selector"""
    def blink(self):
        now = pygame.time.get_ticks()
        blink_time = 1000 # time in milseconds to alternate colors
        if self.color == True and now - self.last_update > .15 * blink_time: #off
            self.color = False
            self.last_update = now
        if self.color == False and now - self.last_update > blink_time: #on
            #self.color = True
            self.color = False
            self.last_update = now
    
    def drinks(self):
        #Max Char 15
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
paus = 0.2
b = Bar()
b.menu()
while b.running:
    #Buttons
    if button_white.is_pressed:
        device.emit_click(uinput.KEY_SPACE)
        time.sleep(paus)
    if button_black.is_pressed:
        device.emit_click(uinput.KEY_BACKSPACE)
        time.sleep(paus)
    if button_up.is_pressed:
        device.emit_click(uinput.KEY_UP)
        time.sleep(paus)
    if button_down.is_pressed:
        device.emit_click(uinput.KEY_DOWN)
        time.sleep(paus)
    if button_left.is_pressed:
        device.emit_click(uinput.KEY_LEFT)
        time.sleep(paus)
    if button_right.is_pressed:
        device.emit_click(uinput.KEY_RIGHT)
        print("right")
        time.sleep(paus)
    b.run()

    
pygame.quit()
sys.exit()
    
    
        

