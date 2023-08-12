##
# File name: main.py
# @author: Hadi Shaheryar
# @desc: Simple GUI program that acts as a self-serve kiosk for McMaster
##

#imports kivy for GUI, this allows the app to be ported to Windows, MacOS, Android, IOS and Linux Systems
import kivy
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.config import Config

#Disables multi-touch/right-click
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

#ScreenManager in order to switch pages
class MyScreenManager(ScreenManager):
    pass

class MainMenu(Screen):
    pass

# Containing all the functions for the buttons
class OrderMenu(Screen):
    def burgerMore(self):
        quantity = int(self.ids.burger_quantity.text)+1
        price = 5.00*quantity
        self.ids.burger_quantity.text = f'{quantity}'
        self.ids.burger_price.text = "$%.2f" % price
    def burgerLess(self):
        quantity = int(self.ids.burger_quantity.text) - 1 if(int(self.ids.burger_quantity.text) != 0) else 0
        price = 5.00 * quantity
        self.ids.burger_quantity.text = f'{quantity}'
        self.ids.burger_price.text = "$%.2f" % price
    def pizzaMore(self):
        quantity = int(self.ids.pizza_quantity.text) + 1
        price = 3.50 * quantity
        self.ids.pizza_quantity.text = f'{quantity}'
        self.ids.pizza_price.text = "$%.2f" % price
    def pizzaLess(self):
        quantity = int(self.ids.pizza_quantity.text) - 1 if (int(self.ids.pizza_quantity.text) != 0) else 0
        price = 3.50 * quantity
        self.ids.pizza_quantity.text = f'{quantity}'
        self.ids.pizza_price.text = "$%.2f" % price
    def friesMore(self):
        quantity = int(self.ids.fries_quantity.text) + 1
        price = 4.00 * quantity
        self.ids.fries_quantity.text = f'{quantity}'
        self.ids.fries_price.text = "$%.2f" % price
    def friesLess(self):
        quantity = int(self.ids.fries_quantity.text) - 1 if (int(self.ids.fries_quantity.text) != 0) else 0
        price = 4.00 * quantity
        self.ids.fries_quantity.text = f'{quantity}'
        self.ids.fries_price.text = "$%.2f" % price
    def waterMore(self):
        quantity = int(self.ids.water_quantity.text) + 1
        price = 2.00 * quantity
        self.ids.water_quantity.text = f'{quantity}'
        self.ids.water_price.text = "$%.2f" % price
    def waterLess(self):
        quantity = int(self.ids.water_quantity.text) - 1 if (int(self.ids.water_quantity.text) != 0) else 0
        price = 2.00 * quantity
        self.ids.water_quantity.text = f'{quantity}'
        self.ids.water_price.text = "$%.2f" % price
    def coffeeMore(self):
        quantity = int(self.ids.coffee_quantity.text) + 1
        price = 2.50 * quantity
        self.ids.coffee_quantity.text = f'{quantity}'
        self.ids.coffee_price.text = "$%.2f" % price
    def coffeeLess(self):
        quantity = int(self.ids.coffee_quantity.text) - 1 if (int(self.ids.coffee_quantity.text) != 0) else 0
        price = 2.50 * quantity
        self.ids.coffee_quantity.text = f'{quantity}'
        self.ids.coffee_price.text = "$%.2f" % price
    def mangoMore(self):
        quantity = int(self.ids.mango_quantity.text) + 1
        price = 2.75 * quantity
        self.ids.mango_quantity.text = f'{quantity}'
        self.ids.mango_price.text = "$%.2f" % price
    def mangoLess(self):
        quantity = int(self.ids.mango_quantity.text) - 1 if (int(self.ids.mango_quantity.text) != 0) else 0
        price = 2.75 * quantity
        self.ids.mango_quantity.text = f'{quantity}'
        self.ids.mango_price.text = "$%.2f" % price
    def creamMore(self):
        quantity = int(self.ids.cream_quantity.text) + 1
        price = 5.50 * quantity
        self.ids.cream_quantity.text = f'{quantity}'
        self.ids.cream_price.text = "$%.2f" % price
    def creamLess(self):
        quantity = int(self.ids.cream_quantity.text) - 1 if (int(self.ids.cream_quantity.text) != 0) else 0
        price = 5.50 * quantity
        self.ids.cream_quantity.text = f'{quantity}'
        self.ids.cream_price.text = "$%.2f" % price
    def ccakeMore(self):
        quantity = int(self.ids.ccake_quantity.text) + 1
        price = 4.50 * quantity
        self.ids.ccake_quantity.text = f'{quantity}'
        self.ids.ccake_price.text = "$%.2f" % price
    def ccakeLess(self):
        quantity = int(self.ids.ccake_quantity.text) - 1 if (int(self.ids.ccake_quantity.text) != 0) else 0
        price = 4.50 * quantity
        self.ids.ccake_quantity.text = f'{quantity}'
        self.ids.ccake_price.text = "$%.2f" % price
    def chcakeMore(self):
        quantity = int(self.ids.chcake_quantity.text) + 1
        price = 7.00 * quantity
        self.ids.chcake_quantity.text = f'{quantity}'
        self.ids.chcake_price.text = "$%.2f" % price
    def chcakeLess(self):
        quantity = int(self.ids.chcake_quantity.text) - 1 if (int(self.ids.chcake_quantity.text) != 0) else 0
        price = 7.00 * quantity
        self.ids.chcake_quantity.text = f'{quantity}'
        self.ids.chcake_price.text = "$%.2f" % price
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

class FinalMenu(Screen):
    #Indicates completion of order
    def finishBill(self):
        self.ids.status.text = "Completed. Thank you." if(self.ids.total.text != "$0.00") else "Incomplete"

kv = Builder.load_file("mcmaster.kv")
class McMasterApp(App):
    def build(self):
        self.icon="img/maclogo.png"
        self.title = "McMaster Self-Service Meal Kiosk"
        return kv

if __name__ == "__main__":
    McMasterApp().run()
