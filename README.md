# McMasterSelfServeApp
## By: Hadi Shaheryar ##
This is app is a simple GUI program that shows how a self-order kiosk may look for McMaster.
It displays subtotal, tax, total and quantity information.
The program is made fully from python and utilizes the Kivy framework for portability to different devices.
Note: This application has **NOT** been optimized for all devices. The standard screen resolution this is set to run at is **700x700px**.
- - - -
# Walk-through #
The program is pretty self explanatory but there are some highlighting features.
1. The GUI system utilizes background images as a means to enhance UX. For this reason, it's recommended you keep the same screen resolution as the default.
2. The program will allow you to select your items and move to the payment section. However, in the odd case that someone does not select anything, the program will not move beyond the payment screen, it will show an "Order Empty" statement in the console.
3. Credit card is the default method for payment selected by the program, but you have free will to choose between credit card, meal card and cash.
4. Once the payment screen is validated, the program will move on to the final screen and then terminate in 2 seconds.
5. This is just a demonstration so no payment information is being asked and the order isn't sent to any clerk for handling.
