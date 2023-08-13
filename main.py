##
# File name: main.py
# @author: Hadi Shaheryar
# @desc: Simple GUI program that acts as a self-serve kiosk for McMaster
##

#imports kivy for GUI, this allows the app to be ported to Windows, MacOS, Android, IOS and Linux Systems
from threading import Thread
import kivy
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.config import Config

#Disables multi-touch/right-click
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#Set window size
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')

#ScreenManager in order to switch pages
class MyScreenManager(ScreenManager):
    pass

class MainMenu(Screen):
    pass

# Containing all the functions for the buttons
class OrderMenu(Screen):

    def waterMore(self):
        quantity = int(self.ids.water_quantity.text) + 1
        price = 2.00 * quantity
        self.ids.water_quantity.text = f'{quantity}'
        self.ids.water_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def waterLess(self):
        quantity = int(self.ids.water_quantity.text) - 1 if (int(self.ids.water_quantity.text) != 0) else 0
        price = 2.00 * quantity
        self.ids.water_quantity.text = f'{quantity}'
        self.ids.water_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def coffeeMore(self):
        quantity = int(self.ids.coffee_quantity.text) + 1
        price = 2.50 * quantity
        self.ids.coffee_quantity.text = f'{quantity}'
        self.ids.coffee_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def coffeeLess(self):
        quantity = int(self.ids.coffee_quantity.text) - 1 if (int(self.ids.coffee_quantity.text) != 0) else 0
        price = 2.50 * quantity
        self.ids.coffee_quantity.text = f'{quantity}'
        self.ids.coffee_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def mangoMore(self):
        quantity = int(self.ids.mango_quantity.text) + 1
        price = 2.75 * quantity
        self.ids.mango_quantity.text = f'{quantity}'
        self.ids.mango_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def mangoLess(self):
        quantity = int(self.ids.mango_quantity.text) - 1 if (int(self.ids.mango_quantity.text) != 0) else 0
        price = 2.75 * quantity
        self.ids.mango_quantity.text = f'{quantity}'
        self.ids.mango_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def creamMore(self):
        quantity = int(self.ids.cream_quantity.text) + 1
        price = 5.50 * quantity
        self.ids.cream_quantity.text = f'{quantity}'
        self.ids.cream_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def creamLess(self):
        quantity = int(self.ids.cream_quantity.text) - 1 if (int(self.ids.cream_quantity.text) != 0) else 0
        price = 5.50 * quantity
        self.ids.cream_quantity.text = f'{quantity}'
        self.ids.cream_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def ccakeMore(self):
        quantity = int(self.ids.ccake_quantity.text) + 1
        price = 4.50 * quantity
        self.ids.ccake_quantity.text = f'{quantity}'
        self.ids.ccake_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def ccakeLess(self):
        quantity = int(self.ids.ccake_quantity.text) - 1 if (int(self.ids.ccake_quantity.text) != 0) else 0
        price = 4.50 * quantity
        self.ids.ccake_quantity.text = f'{quantity}'
        self.ids.ccake_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def chcakeMore(self):
        quantity = int(self.ids.chcake_quantity.text) + 1
        price = 7.00 * quantity
        self.ids.chcake_quantity.text = f'{quantity}'
        self.ids.chcake_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def chcakeLess(self):
        quantity = int(self.ids.chcake_quantity.text) - 1 if (int(self.ids.chcake_quantity.text) != 0) else 0
        price = 7.00 * quantity
        self.ids.chcake_quantity.text = f'{quantity}'
        self.ids.chcake_price.text = "$%.2f" % price
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_ =  burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def finalBill(self):
        #Determines final bill
        burger_price = float((self.ids.burger_price.text).replace("$", ""))
        pizza_price = float((self.ids.pizza_price.text).replace("$", ""))
        fries_price = float((self.ids.fries_price.text).replace("$", ""))
        water_price = float((self.ids.water_price.text).replace("$", ""))
        coffee_price = float((self.ids.coffee_price.text).replace("$", ""))
        mango_price = float((self.ids.mango_price.text).replace("$", ""))
        cream_price = float((self.ids.cream_price.text).replace("$", ""))
        ccake_price = float((self.ids.ccake_price.text).replace("$", ""))
        chcake_price = float((self.ids.chcake_price.text).replace("$", ""))
        subtotal_price = burger_price + pizza_price + fries_price + water_price + coffee_price + mango_price + cream_price + ccake_price + chcake_price
        tax_price = subtotal_price * 0.13
        total_price = subtotal_price * 1.13
        self.manager.get_screen('finalu').ids.subtotal.text = "$%.2f" % subtotal_price
        self.manager.get_screen('finalu').ids.tax.text = "$%.2f" % tax_price
        self.manager.get_screen('finalu').ids.total.text = "$%.2f" % total_price

class OrderMeals(Screen):
    def burgerMore(self):
        quantity = int(self.ids.burger_quantity.text)+1
        price = 5.00*quantity
        self.ids.burger_quantity.text = f'{quantity}'
        burger_price = price
        shawarma_price = 10.00*int(self.ids.shawarma_quantity.text)
        fries_price = 5.50*int(self.ids.fries_quantity.text)
        salad_price = 7.50*int(self.ids.salad_quantity.text)
        # water_price = 3.50*int(self.ids.water_quantity.text)
        # milkshake_price = 6.00*int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20*int(self.ids.oj_quantity.text)
        # soda_price = 2.00*int(self.ids.soda_quantity.text)
        # cream_price = 4.50*int(self.ids.cream_quantity.text)
        # cake_price = 6.30*int(self.ids.cake_quantity.text)
        # cookies_price = 1.50*int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20*int(self.ids.macaron_quantity.text)
        # subtotal_ =  burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def burgerLess(self):
        quantity = int(self.ids.burger_quantity.text) - 1 if(int(self.ids.burger_quantity.text) != 0) else 0
        price = 5.00 * quantity
        self.ids.burger_quantity.text = f'{quantity}'
        burger_price = price
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def friesMore(self):
        quantity = int(self.ids.fries_quantity.text) + 1
        price = 5.50 * quantity
        self.ids.fries_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def friesLess(self):
        quantity = int(self.ids.fries_quantity.text) - 1 if (int(self.ids.fries_quantity.text) != 0) else 0
        price = 5.50 * quantity
        self.ids.fries_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def shawarmaMore(self):
        quantity = int(self.ids.shawarma_quantity.text) + 1
        price = 10.00 * quantity
        self.ids.shawarma_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def shawarmaLess(self):
        quantity = int(self.ids.shawarma_quantity.text) - 1 if (int(self.ids.shawarma_quantity.text) != 0) else 0
        price = 10.00 * quantity
        self.ids.shawarma_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def saladMore(self):
        quantity = int(self.ids.salad_quantity.text) + 1
        price = 7.50 * quantity
        self.ids.salad_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
    def saladLess(self):
        quantity = int(self.ids.salad_quantity.text) - 1 if (int(self.ids.salad_quantity.text) != 0) else 0
        price = 7.50 * quantity
        self.ids.salad_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        # water_price = 3.50 * int(self.ids.water_quantity.text)
        # milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        # oj_price = 5.20 * int(self.ids.oj_quantity.text)
        # soda_price = 2.00 * int(self.ids.soda_quantity.text)
        # cream_price = 4.50 * int(self.ids.cream_quantity.text)
        # cake_price = 6.30 * int(self.ids.cake_quantity.text)
        # cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        # macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        # subtotal_ = burger_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        # self.ids.totalplace.text = "Total: $%.2f" % subtotal_
class OrderDrinks(Screen):
    pass
class OrderDesserts(Screen):
    pass
class FinalMenu(Screen):
    #Indicates completion of order
    def finishBill(self):
        self.ids.status.text = "Completed.Thank you." if(self.ids.total.text != "$0.00") else "Incomplete"

kv = Builder.load_file("mcmaster.kv")
class McMasterApp(App):
    def build(self):
        self.icon="img/maclogo.png"
        self.title = "McMaster Self-Service Meal Kiosk"
        return kv

if __name__ == "__main__":
    McMasterApp().run()
