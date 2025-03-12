import brython
import browser
import random

colors = [
    "black", "white", "red", "green", "blue", "yellow", "cyan", "magenta",
    "gray", "silver", "maroon", "olive", "lime", "aqua", "fuchsia", "purple"
]

current_deg = 0

class Save_Control:
    def __init__(self):
        brython.localstorage.set_storage("BadUI1Clicker")
        self.coins_output = brython.html.getElement(".coins")
        pass

    def make_save(self):
        brython.localstorage.get_or_create("money", 0)
        brython.localstorage.get_or_create("amount", 1)

    def show_money(self):
        self.coins_output.text = f"Coins: {brython.localstorage.get_int('money')}"


save = Save_Control()
save.make_save()


@brython.timers.set_interval_decorator("seconds", 0.6)
def update_money():
    save.show_money()


@brython.bind.bind(".Clicker", "click")
def bad_clicker(event):
    brython.localstorage.set("money", brython.localstorage.get_int("money") - brython.localstorage.get_int("amount"))
    save.show_money()


@brython.timers.set_interval_decorator("seconds", 0.05)
def rotate_clicker_because_why_not():
    global current_deg
    current_deg = (current_deg + 1) % 360
    if current_deg == 0:
        brython.localstorage.set("money", brython.localstorage.get_int("money") + brython.localstorage.get_int("amount"))
    brython.html.getElement(".bad_clicker").style.transform = f"rotate({current_deg}deg)"


@brython.bind.bind(".annoying_button", "click")
def spawn_annoying_button(event):
    annoying_button = brython.html.createElement("button", "Annoying button")

    annoying_button.style.position = "absolute"
    annoying_button.style.width = "200px"
    annoying_button.style.height = "100px"

    def move_annoying_button():
        window_height = brython.brython_etc.get_window_size()[1]
        window_width = brython.brython_etc.get_window_size()[0]
        annoying_button.style.left = f"{random.randint(0, window_width - 200)}px"
        annoying_button.style.top = f"{random.randint(0, window_height - 100)}px"
        annoying_button.style.backgroundColor = random.choice(colors)

    brython.timers.set_interval_seconds(move_annoying_button, 0.03)


@brython.bind.bind(".first_bad", "click")
def Nuh_Uh(event):
    def delete_element():
        brython.html.removeElement(".first_bad_li")

    brython.html.setHTML(".first_bad_li", '<button class="first_bad">Nah, i gotta away from here</button>')
    brython.timers.set_timeout_seconds(delete_element, 2)


@brython.bind.bind(".second_bad", "click")
def Nuh_Uh(event):
    def delete_element():
        brython.html.removeElement(".second_bad_li")

    brython.html.setHTML(".second_bad_li", '<button class="second_bad">Nah, i gotta away from here</button>')
    brython.timers.set_timeout_seconds(delete_element, 2)


@brython.bind.bind(".third_bad", "click")
def Nuh_Uh(event):
    def delete_element():
        brython.html.removeElement(".third_bad_li")

    brython.html.setHTML(".third_bad_li", '<button class="third_bad">Nah, i gotta away from here</button>')
    brython.timers.set_timeout_seconds(delete_element, 2)
