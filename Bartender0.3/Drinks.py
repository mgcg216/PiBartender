import RPi.GPIO as GPIO
import time
import pygame
# Types of drinks
#water = 21 # Channel Pin 21
"""
test = 24
whiskey = 21
coke = 7
"""
#Hards
"""
hard = [["vodka", "gin", "rum", "tequila", "curcao", "whiskey", "bourbon"],[21, 20, 16, 12, 7, 8, 25]]
chase = [["sour_mix", "coke", "sprite", "red_bull", "simple_syrup", "oj"], [24, 0, 0, 0, 0, 0]]
"""
#I cannot think of a way for the having an array will be any easier than just listing below

vodka = 25
#gin = pass
#rum = pass
#tequila = pass
#curacao = pass
whiskey = 7
#jagermeister = pass
#Chasers
#sour_mix = pass #lime juice
coke = 24
sprite = 21
#red_bull = pass


#Cocktail Array

drinks_arr = ["AMF", "Whiskey and Coke", "Vodka Coke", "Gin Coke", "Whiskey Sprite", "Vodka Sprite", "Gin and Sprite",
              "Moscow Mule", "Kentucky Mule", "Gin Gin Mule", "Mexican Mule", "Vodka Redbull", "Long Island", "Old Fashion", "test"]
drinks_dic = dict({"AMF":1000, "Whiskey and Coke":1001, "Vodka Coke":1002, "Gin Coke":1003, "Whiskey Sprite":1004, "Vodka Sprite":1005, "Gin and Sprite":1006,
              "Moscow Mule":1007, "Kentucky Mule":1008, "Gin Gin Mule":1009, "Mexican Mule":1010, "Vodka Redbull":1011, "Long Island":1012, "Old Fashion":1013, "test":999})
#I need a normal array because drinks_dic.keys() does not have indexing
#Doesn't work cant index below array either
"""
drinks_arr = []
for drinks, num in drinks_dic.items():
    drinks_arr.append(drinks)"""
#print(drinks_arr(0))
#drinks_arr = drinks_dic.keys()

# Time per size
clear = 10
ounce = 3*8.5 # check this
shot = ounce/(1.5)
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
    #each cocktail is associated with a number (not the necessary the position in the array)
    #the number will be lock into the cocktail so if i were to decide to switch the order or add more
    #items in the array I will not have to change drink options too much or at all
    #if the order is change no change is need in drink options
    def drink_option(self, num):
        if num == 999: #test
            self.test()
        if num == 1000: #AMF
            self.AMF()
        if num == 1001: #Whiskey and Coke
            self.hard_chaser(whiskey, coke)
        if num == 1002: #Vodka Coke
            self.hard_chaser(vodka, coke)
        if num == 1003: #Gin Coke
            self.hard_chaser(gin, coke)
        if num == 1004: #Whiskey Sprite
            self.hard_chaser(whiskey, sprite)
        if num == 1005: #Vodka Sprite
            self.hard_chaser(vodka, sprite)
        if num == 1006: #Gin and Sprite
            self.hard_chaser(gin, sprite)
        if num == 1007: #Moscow Mule
            self.mule(vodka)
        if num == 1008: #Kentucky Mule
            self.mule(whiskey)
        if num == 1009: #Gin Gin Mule
            self.mule(gin)
        if num == 1010: #Mexican Mule
            self.mule(tequila)
        if num == 1011: #Vodka Redbull
            pass
        if num == 1012: #Long Island
            self.longIsland()
        if num == 1013: #Old Fashion
            self.oldFashion()
        else:
            print("Error no dictionary number")
    def pump_off(self, pin):
        GPIO.output(pin, GPIO.HIGH)
        
    def pump_on(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def pour(self, liquid, t):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(liquid, GPIO.OUT)
            self.pump_on(liquid)
            time.sleep(t)
            self.pump_off(liquid)
        except KeyboardInterrupt:
            print("Hmm")
        finally:
            GPIO.cleanup()
            
    def pour_wait(self, liquid, t): #keyboardinterrupt might not be working correctly
        try:
            self.pump_on(liquid)
            time.sleep()
        except KeyboardInterrupt:
            self.pump_off(liquid)
            time.sleep(1)
            GPIO.cleanup()
            
    def start_up_pump(self):
        try:
            #pump all liquids
            self.pour()
        except KeyboardInterrupt:
            GPIO.cleanup()
            
    def setup(self):
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
    def AMF(self):
        """
        self.pour(vodka,.75*ounce)
        self.pour(gin,.75*ounce)
        self.pour(rum,.75*ounce)
        self.pour(curacao,.75*ounce)
        self.pour(sour_mix,2*ounce)
        self.pour(sprite,.5*ounce)
        """
        try:
            self.pump_on(vodka)
            self.pump_on(gin)
            self.pump_on(rum)
            self.pump_on(curacao)
            self.pump_on(sour_mix)
            self.pump_on(sprite)
            """
            #carbinated drinks tend to pour half as slow so the code will need to change
            time.sleep(.5*ounce)
            time.sleep(.25*ounce)
            time.sleep(1.25*ounce)
            """
            time.sleep(.75*ounce)
            self.pump_off(vodka)
            self.pump_off(gin)
            self.pump_off(rum)
            self.pump_off(curacao)
            time.sleep(.25*ounce)
            self.pump_off(sprite)
            time.sleep(1*ounce)
            self.pump_off(sour_mix)
            time.sleep(1)
        except KeyboardInterrupt:
            print("What happened")
            time.sleep(0.01)
            self.pump_off(vodka)
            self.pump_off(gin)
            self.pump_off(rum)
            self.pump_off(curacao)
            self.pump_off(sprite)
            self.pump_off(sour_mix)
            time.sleep(1)
        #finally:
            #GPIO.cleanup()
    """
    vodka + coke jack + coke etc
    change hard and chase
    whiskey_coke
    2 ounces Jack Daniels
    10 ounces Coke
    """
    def hard_chaser(self, hard, chaser):
        """
        self.pour(hard, 2*ounce)
        self.pour(chaser, 10*ounce)
        """
        try:
            self.pump_on(hard)
            self.pump_on(chaser)
            time.sleep(2*ounce)
            self.pump_off(hard)
            time.sleep(8*ounce)
            self.pump_off(chaser)
            time.sleep(1)
        except KeyboardInterrupt:
            print("hmm")
            time.sleep(0.01)
            self.pump_off(hard)
            self.pump_off(chaser)
            time.sleep(1)
        finally:
            GPIO.cleanup(hard, chaser)
        
        
    """
    Mules
    Moscow Mule
    1 1/2 Vodka
    1/2 lime juice
    1/2 cup Ginger beer
    """

    def mule(self, hard):
        """
        self.pour(hard, 2*ounce)
        self.pour(sour_mix, 0.5*ounce)
        self.pour(ging, 5*ounce)
        """
        self.pump_on(hard)
        self.pump_on(sour_mix)
        self.pump_on(ging)
        time.sleep(0.5*ounce)
        self.pump_off(sour_mix)
        time.sleep(1.5*ounce)
        self.pump_off(hard)
        time.sleep(8*ounce) #self.sleep(3*ounce)
        self.pump_off(ging)
        time.sleep(1)
        GPIO.cleanup()
        

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
    
    def longIsland(self):
        """
        self.pour(gin, 3/4*ounce)
        self.pour(rum, 3/4*ounce)
        self.pour(tequila, 3/4*ounce)
        self.pour(vodka, 3/4*ounce)
        self.pour(curacao, 3/4*ounce)
        self.pour(simple_syrup, 3/4*ounce)
        self.pour(sour_mix, 3/4*ounce)
        self.pour(sprite, 2*ounce)
        """
        self.pump_on(gin)
        self.pump_on(rum)
        self.pump_on(tequila)
        self.pump_on(vodka)
        self.pump_on(curacao)
        self.pump_on(simple_syrup)
        self.pump_on(sour_mix)
        self.pump_on(sprite)
        time.sleep(.75*ounce)
        self.pump_off(gin)
        self.pump_off(rum)
        self.pump_off(tequila)
        self.pump_off(vodka)
        self.pump_off(curacao)
        self.pump_off(simple_syrup)
        self.pump_off(sour_mix)
        time.sleep(3.25*ounce) #time.sleep(1.25*ounce)
        self.pump_off(sprite)
        time.sleep(1)
        GPIO.cleanup()
        
    """
    1 teaspoon simple syrup
    2 dashes angostura bitters
    2 ounces of bourbon
    """
    def oldFashion(self):
        self.pour(simple_syrup, 1/8*ounce)
        self.pour(bourbon, 2*ounces)
        
    """
    Manhattan
    2 ounces rye whiskey
    1 ounce Carpano Antica Formula or other sweet vermouth
    2 dashes of Angostura bitter
    """
    def manhattan(self):
        pass
    """
    7 random shot combination
    """
    def sevenSeas(self):
        pass
        #self.pour(pass, shot)
    
    def test(self):
        try:
            self.pump_on(coke)
            time.sleep(1)
            self.pump_off(coke)
        except:
            pass
        finally:
            GPIO.cleanup(coke)
    
#d = Drinks()
#d.test()
#GPIO.setmode(GPIO.BCM)
#d.pour(whiskey, shot)
#d.pour(coke, shot)
#d.drink_option(1001)
"""

#water test
d = Drinks()

#Setup
GPIO.setmode(GPIO.BCM)
#GPIO.setup(whiskey, GPIO.OUT)
#GPIO.setup(coke, GPIO.OUT)
#d.pour(whiskey, shot)
#d.pour(coke, 10*ounce)
#GPIO.cleanup()

#d.pour(water, ounce)
#GPIO.setup(test, GPIO.OUT)
d.pour(test, clear)
        

"""