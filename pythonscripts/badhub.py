import browser
import random
import sys
sys.path.append('pythonscripts')  # Add parent directory to path
from brython_easier import *

annoying_button = html.getElement(".annoying_button")
colors = [
    "black", "white", "red", "green", "blue", "yellow", "cyan", "magenta",
    "gray", "silver", "maroon", "olive", "lime", "aqua", "fuchsia", "purple"
]

@timers.set_interval_decorator("seconds", 0.5)
def annoying_button_func():
    annoying_button.style.top = f"{random.randint(0, brython_etc.get_window_size()[1] - 100)}px"
    annoying_button.style.left = f"{random.randint(0, brython_etc.get_window_size()[0] - 100)}px"
    annoying_button.style.backgroundColor = random.choice(colors)


@bind.bind('.annoying_button', "click")
def annoying_click(event):
    annoying_button_func()

@bind.bind(".first_bad", "click")
def first_bad_click(event):
    brython_etc.redirect("badUI1.html")