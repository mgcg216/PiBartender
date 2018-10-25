import RPi.GPIO as GPIO
import time
import pygame
# Types of drinks
#water = 21 # Channel Pin 21
#Hards

hard = [["vodka", "gin", "rum", "tequila", "curcao", "whiskey", "bourbon"],[21, 20, 16, 12, 7, 8, 25]]
chase = [["sour_mix", "coke", "sprite", "red_bull", "simple_syrup", "oj"], [24, 0, 0, 0, 0, 0]]
'''
vodka = XX
gin = XX
rum = XX
tequila = XX
curacao = XX
whiskey = XX
jagermeister = XX
#Chasers
sour_mix = XX #lime juice
coke = XX
sprite = XX
red_bull = XX

'''

#Cocktail Array
drinks_arr = ["AMF", "Whiskey and Coke", "Vodka Coke", "Gin Coke", "Whiskey Sprite", "Vodka Sprite", "Gin and Sprite",
              "Moscow Mule", "Kentucky Mule", "Gin Gin Mule", "Mexican Mule", "Vodka Redbull", "Long Island", "Old Fashion"]

# Time per size
ounce = 3*8.5 # check this
shot_time = ounce/(1.5)
cup = 8*ounce
"""
def main():
    #Setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(water, GPIO.OUT)
    #water test
    pour(water,ounce)
"""
class Drinks:
    def pump_off(pin):
        GPIO.output(pin, GPIO.HIGH)
        
    def pump_on(pin):
        GPIO.output(pin, GPIO.LOW)

    def pour(liquid, t):
        try:
            pump_on(liquid)
            time.sleep(t)
            pump_off(liquid)
            time.sleep(1)
            GPIO.cleanup()
        except KeyboardInterrupt:
            pump_off(liquid)
            GPIO.cleanup()
            
    def pour_wait(liquid, t): #keyboardinterrupt might not be working correctly
        try:
            pump_on(liquid)
            time.sleep()
        except KeyboardInterrupt:
            pump_off(liquid)
            time.sleep(1)
            GPIO.cleanup()
            
    def start_up_pump():
        try:
            #pump all liquids
            pour()
        except KeyboardInterrupt:
            GPIO.cleanup()
            
    def setup():
        GPIO.setmode(GPIO.BCM)
        pass 
            
    #drinks
    """AMF
    3/4 ounce vodka
    3/4 ounce gin
    3/4 ounce light rum
    3/4 ounce blue curacao
    2 ounce sour mix
    1/2 7-up/sprite
    """
    def AMF():
        pour(vodka,.75*ounce)
        pour(gin,.75*ounce)
        pour(rum,.75*ounce)
        pour(curacao,.75*ounce)
        pour(sour_mix,2*ounce)
        pour(sprite,.5*ounce)
    """
    vodka + coke jack + coke etc
    change hard and chase
    whiskey_coke
    2 ounces Jack Daniels
    10 ounces Coke
    """
    def hard_chaser(hard, chaser):
        pour(hard, 2*ounce)
        pour(chaser, 10*ounce)
        
    """
    Mules
    Moscow Mule
    1 1/2 Vodka
    1/2 lime juice
    1/2 cup Ginger beer
    """

    def mule(hard, lime, ging):
        pour(hard, 2*ounce)
        pour(sour_mix, 0.5*ounce)
        pour(ging, 5*ounce)

    """
    Long Island
    3/4 oz Gin
    3/4 oz Rum
    3/4 oz Tequila
    3/4 oz Vodka
    3/4 oz Triple sec/ curacao
    3/4 oz simple syrup
    3/4 oz lemon juice/ sour_mix
    2 oz sprite #Playwith this value
    """
    
    def longIsland():
        pour(gin, 3/4*ounce)
        pour(rum, 3/4*ounce)
        pour(tequila, 3/4*ounce)
        pour(vodka, 3/4*ounce)
        pour(curacao, 3/4*ounce)
        pour(simple_syrup, 3/4*ounce)
        pour(sour_mix, 3/4*ounce)
        pour(sprite, 2*ounce)
        
        
    """
    1 teaspoon simple syrup
    2 dashes angostura bitters
    2 ounces of bourbon
    """
    def oldFashion():
        pour(simple_syrup, 1/8*ounce)
        pour(bourbon, 2*ounces)
        
    """
    Manhattan
    2 ounces rye whiskey
    1 ounce Carpano Antica Formula or other sweet vermouth
    2 dashes of Angostura bitter
    """
    def manhattan():
        pass
    
        

