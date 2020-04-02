from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()  # overwrite from original make_special_dish in class Chef
myChineseChef.make_chicken()  # Inherit from Chef
