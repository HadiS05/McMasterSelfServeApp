##
# File name: main.py
# @author: Hadi Shaheryar
# @desc: Simple GUI program that acts as a self-serve kiosk for McMaster
##

#imports kivy for GUI, this allows the app to be ported to Windows, MacOS, Android, IOS and Linux Systems
from threading import Thread
import kivy
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.config import Config
from datetime import date
#Disables multi-touch/right-click
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#Set window size
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')

#ScreenManager in order to switch pages


class MyScreenManager(ScreenManager):
    subtotalprice = StringProperty("Total: $0.00")
    subtotal = StringProperty("$0.00")
    taxtotal = StringProperty("$0.00")
    total = StringProperty("$0.00")
    date = StringProperty("MM, dd, YYYY")
class MainMenu(Screen):
    pass


class OrderMeals(Screen):
    def burgerMore(self):
        quantity = int(self.ids.burger_quantity.text)+1
        price = 5.00*quantity
        self.ids.burger_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00*int(self.ids.shawarma_quantity.text)
        fries_price = 5.50*int(self.ids.fries_quantity.text)
        salad_price = 7.50*int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def burgerLess(self):
        quantity = int(self.ids.burger_quantity.text) - 1 if(int(self.ids.burger_quantity.text) != 0) else 0
        price = 5.00 * quantity
        self.ids.burger_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def friesMore(self):
        quantity = int(self.ids.fries_quantity.text) + 1
        price = 5.50 * quantity
        self.ids.fries_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def friesLess(self):
        quantity = int(self.ids.fries_quantity.text) - 1 if (int(self.ids.fries_quantity.text) != 0) else 0
        price = 5.50 * quantity
        self.ids.fries_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def shawarmaMore(self):
        quantity = int(self.ids.shawarma_quantity.text) + 1
        price = 10.00 * quantity
        self.ids.shawarma_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def shawarmaLess(self):
        quantity = int(self.ids.shawarma_quantity.text) - 1 if (int(self.ids.shawarma_quantity.text) != 0) else 0
        price = 10.00 * quantity
        self.ids.shawarma_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def saladMore(self):
        quantity = int(self.ids.salad_quantity.text) + 1
        price = 7.50 * quantity
        self.ids.salad_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def saladLess(self):
        quantity = int(self.ids.salad_quantity.text) - 1 if (int(self.ids.salad_quantity.text) != 0) else 0
        price = 7.50 * quantity
        self.ids.salad_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.ids.fries_quantity.text)
        salad_price = 7.50 * int(self.ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def finish(self):
        taxtotal= float(self.ids.totalplace.text.replace("Total: $", ""))*0.13
        total = float(self.ids.totalplace.text.replace("Total: $", "")) * 1.13
        today = date.today().strftime("%B %d, %Y")
        self.manager.date = today
        self.manager.subtotal = self.ids.totalplace.text.replace("Total: ", "")
        self.manager.taxtotal = "$%.2f"%taxtotal
        self.manager.total = "$%.2f"%total

class OrderDrinks(Screen):
    def waterMore(self):
        quantity = int(self.ids.water_quantity.text)+1
        price = 3.50*quantity
        self.ids.water_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50*int(self.ids.water_quantity.text)
        milkshake_price = 6.00*int(self.ids.milkshake_quantity.text)
        oj_price = 5.20*int(self.ids.oj_quantity.text)
        soda_price = 2.00*int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def waterLess(self):
        quantity = int(self.ids.water_quantity.text) - 1 if (int(self.ids.water_quantity.text) != 0) else 0
        price = 7.50 * quantity
        self.ids.water_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.ids.oj_quantity.text)
        soda_price = 2.00 * int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def milkshakeMore(self):
        quantity = int(self.ids.milkshake_quantity.text)+1
        price = 6.00*quantity
        self.ids.milkshake_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50*int(self.ids.water_quantity.text)
        milkshake_price = 6.00*int(self.ids.milkshake_quantity.text)
        oj_price = 5.20*int(self.ids.oj_quantity.text)
        soda_price = 2.00*int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def milkshakeLess(self):
        quantity = int(self.ids.milkshake_quantity.text) - 1 if (int(self.ids.milkshake_quantity.text) != 0) else 0
        price = 6.00 * quantity
        self.ids.milkshake_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.ids.oj_quantity.text)
        soda_price = 2.00 * int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def ojMore(self):
        quantity = int(self.ids.oj_quantity.text)+1
        price = 5.20*quantity
        self.ids.oj_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50*int(self.ids.water_quantity.text)
        milkshake_price = 6.00*int(self.ids.milkshake_quantity.text)
        oj_price = 5.20*int(self.ids.oj_quantity.text)
        soda_price = 2.00*int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def ojLess(self):
        quantity = int(self.ids.oj_quantity.text) - 1 if (int(self.ids.oj_quantity.text) != 0) else 0
        price = 5.20 * quantity
        self.ids.oj_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.ids.oj_quantity.text)
        soda_price = 2.00 * int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def sodaMore(self):
        quantity = int(self.ids.soda_quantity.text)+1
        price = 2.00*quantity
        self.ids.soda_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50*int(self.ids.water_quantity.text)
        milkshake_price = 6.00*int(self.ids.milkshake_quantity.text)
        oj_price = 5.20*int(self.ids.oj_quantity.text)
        soda_price = 2.00*int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + fries_price + shawarma_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def sodaLess(self):
        quantity = int(self.ids.soda_quantity.text) - 1 if (int(self.ids.soda_quantity.text) != 0) else 0
        price = 2.00 * quantity
        self.ids.soda_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.ids.oj_quantity.text)
        soda_price = 2.00 * int(self.ids.soda_quantity.text)
        cream_price = 4.50 * int(self.manager.get_screen('orderde').ids.cream_quantity.text)
        cake_price = 6.30 * int(self.manager.get_screen('orderde').ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.manager.get_screen('orderde').ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.manager.get_screen('orderde').ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def finish(self):
        taxtotal= float(self.ids.totalplace.text.replace("Total: $", ""))*0.13
        total = float(self.ids.totalplace.text.replace("Total: $", "")) * 1.13
        today = date.today().strftime("%B %d, %Y")
        self.manager.date = today
        self.manager.subtotal = self.ids.totalplace.text.replace("Total: ", "")
        self.manager.taxtotal = "$%.2f"%taxtotal
        self.manager.total = "$%.2f"%total
class OrderDesserts(Screen):
    def creamMore(self):
        quantity = int(self.ids.cream_quantity.text)+1
        price = 4.50*quantity
        self.ids.cream_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50*int(self.ids.cream_quantity.text)
        cake_price = 6.30*int(self.ids.cake_quantity.text)
        cookies_price = 1.50*int(self.ids.cookies_quantity.text)
        macaron_price = 5.20*int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def creamLess(self):
        quantity = int(self.ids.cream_quantity.text) - 1 if (int(self.ids.cream_quantity.text) != 0) else 0
        price = 4.50 * quantity
        self.ids.cream_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.ids.cream_quantity.text)
        cake_price = 6.30 * int(self.ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def cakeMore(self):
        quantity = int(self.ids.cake_quantity.text)+1
        price = 6.30*quantity
        self.ids.cake_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50*int(self.ids.cream_quantity.text)
        cake_price = 6.30*int(self.ids.cake_quantity.text)
        cookies_price = 1.50*int(self.ids.cookies_quantity.text)
        macaron_price = 5.20*int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + fries_price + shawarma_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def cakeLess(self):
        quantity = int(self.ids.cake_quantity.text) - 1 if (int(self.ids.cake_quantity.text) != 0) else 0
        price = 6.30 * quantity
        self.ids.cake_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.ids.cream_quantity.text)
        cake_price = 6.30 * int(self.ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def cookiesMore(self):
        quantity = int(self.ids.cookies_quantity.text)+1
        price = 1.50*quantity
        self.ids.cookies_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50*int(self.ids.cream_quantity.text)
        cake_price = 6.30*int(self.ids.cake_quantity.text)
        cookies_price = 1.50*int(self.ids.cookies_quantity.text)
        macaron_price = 5.20*int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + fries_price + shawarma_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def cookiesLess(self):
        quantity = int(self.ids.cookies_quantity.text) - 1 if (int(self.ids.cookies_quantity.text) != 0) else 0
        price = 1.50 * quantity
        self.ids.cookies_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.ids.cream_quantity.text)
        cake_price = 6.30 * int(self.ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def macaronMore(self):
        quantity = int(self.ids.macaron_quantity.text)+1
        price = 5.20*quantity
        self.ids.macaron_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50*int(self.ids.cream_quantity.text)
        cake_price = 6.30*int(self.ids.cake_quantity.text)
        cookies_price = 1.50*int(self.ids.cookies_quantity.text)
        macaron_price = 5.20*int(self.ids.macaron_quantity.text)
        subtotal_ =  burger_price + fries_price + shawarma_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def macaronLess(self):
        quantity = int(self.ids.macaron_quantity.text) - 1 if (int(self.ids.macaron_quantity.text) != 0) else 0
        price = 5.20 * quantity
        self.ids.macaron_quantity.text = f'{quantity}'
        burger_price = 5.00 * int(self.manager.get_screen('orderm').ids.burger_quantity.text)
        shawarma_price = 10.00 * int(self.manager.get_screen('orderm').ids.shawarma_quantity.text)
        fries_price = 5.50 * int(self.manager.get_screen('orderm').ids.fries_quantity.text)
        salad_price = 7.50 * int(self.manager.get_screen('orderm').ids.salad_quantity.text)
        water_price = 3.50 * int(self.manager.get_screen('orderdr').ids.water_quantity.text)
        milkshake_price = 6.00 * int(self.manager.get_screen('orderdr').ids.milkshake_quantity.text)
        oj_price = 5.20 * int(self.manager.get_screen('orderdr').ids.oj_quantity.text)
        soda_price = 2.00 * int(self.manager.get_screen('orderdr').ids.soda_quantity.text)
        cream_price = 4.50 * int(self.ids.cream_quantity.text)
        cake_price = 6.30 * int(self.ids.cake_quantity.text)
        cookies_price = 1.50 * int(self.ids.cookies_quantity.text)
        macaron_price = 5.20 * int(self.ids.macaron_quantity.text)
        subtotal_ = burger_price + shawarma_price + fries_price + salad_price + water_price + milkshake_price + oj_price + soda_price + cream_price + cake_price + cookies_price + macaron_price
        self.manager.subtotalprice = "Total: $%.2f" % subtotal_
    def finish(self):
        taxtotal= float(self.ids.totalplace.text.replace("Total: $", ""))*0.13
        total = float(self.ids.totalplace.text.replace("Total: $", "")) * 1.13
        today = date.today().strftime("%B %d, %Y")
        self.manager.date = today
        self.manager.subtotal = self.ids.totalplace.text.replace("Total: ", "")
        self.manager.taxtotal = "$%.2f"%taxtotal
        self.manager.total = "$%.2f"%total
class FinalMenu(Screen):
    #Indicates completion of order
    def finishBill(self):
        self.ids.status.text = "Completed.Thank you." if(self.ids.total.text != "$0.00") else "Incomplete"


class endMenu(Screen):
    def on_enter(self):
        Clock.schedule_once(App().get_running_app().stop, 2)


kv = Builder.load_file("mcmaster.kv")


class McMasterApp(App):
    def build(self):
        self.icon="img/maclogo.png"
        self.title = "McMaster Self-Service Meal Kiosk"
        return kv


if __name__ == "__main__":
    McMasterApp().run()
