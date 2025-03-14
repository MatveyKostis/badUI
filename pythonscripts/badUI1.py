import sys
sys.path.append('pythonscripts')  # Add parent directory to path
from brython_easier import *
import browser
import random

colors = [
    "black", "white", "red", "green", "blue", "yellow", "cyan", "magenta",
    "gray", "silver", "maroon", "olive", "lime", "aqua", "fuchsia", "purple"
]

current_deg = 0

class Save_Control:
    def __init__(self):
        localstorage.set_storage("BadUI1Clicker")
        self.coins_output = html.getElement(".coins")
        pass

    def make_save(self):
        localstorage.get_or_create("money", 0)
        localstorage.get_or_create("amount", 1)
        localstorage.get_or_create("cost_amount", 1000)

    def show_money(self):
        self.coins_output.text = f"Coins: {localstorage.get_int('money')}"


save = Save_Control()
save.make_save()

@timers.set_interval_decorator("seconds", 0.6)
def update_money():
    save.show_money()


@bind.bind(".Clicker", "click")
def bad_clicker(event):
    html.setText(".coins", "Do not press!")


@timers.set_interval_decorator("seconds", 0.04)
def rotate_clicker_because_why_not():
    global current_deg
    current_deg = (current_deg + 1) % 360
    if current_deg == 0:
        localstorage.set("money", localstorage.get_int("money") + localstorage.get_int("amount"))
        update_money()
    html.getElement(".bad_clicker").style.transform = f"rotate({current_deg}deg)"


@bind.bind(".annoying_button", "click")
def spawn_annoying_button(event):
    annoying_button = html.createElement("button", "Annoying button")

    annoying_button.style.position = "absolute"
    annoying_button.style.width = "100px"
    annoying_button.style.height = "100px"

    x = 0
    y = 0
    dx = 4
    dy = 4

    def move_annoying_button():
        nonlocal x, y, dx, dy
        window_height = brython_etc.get_window_size()[1]
        window_width = brython_etc.get_window_size()[0]

        x += dx
        y += dy

        if x <= 0 or x + 100 >= window_width:
            annoying_button.style.backgroundColor = random.choice(colors)
            dx = -dx
        if y <= 0 or y + 100 >= window_height:
            annoying_button.style.backgroundColor = random.choice(colors)
            dy = -dy

        annoying_button.style.left = f"{x}px"
        annoying_button.style.top = f"{y}px"

    timers.set_interval_seconds(move_annoying_button, 0)


@bind.bind(".first_bad", "click")
def Nuh_Uh(event):
    def delete_element():
        html.removeElement(".first_bad")

    html.setHTML(".first_bad", 'Nah, i gotta away from here')
    timers.set_timeout_seconds(delete_element, 2)


@bind.bind(".second_bad", "click")
def Nuh_Uh(event):
    brython_etc.redirect("index.html")


@bind.bind(".third_bad", "click")
def Nuh_Uh(event):
    brython_etc.redirect("badUI1shop.html")