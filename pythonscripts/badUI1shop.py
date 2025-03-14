from brython_easier import *

colors = [
    "black", "white", "red", "green", "blue", "yellow", "cyan", "magenta",
    "gray", "silver", "maroon", "olive", "lime", "aqua", "fuchsia", "purple"
]

localstorage.set_storage("BadUI1Clicker")

@bind.bind(".Get_Back", "click")
def get_back_to_game(event):
    brython_etc.redirect("badUI1.html")


@bind.bind(".first_bad", "click")
def Nuh_Uh(event):
    def delete_element():
        html.removeElement(".first_bad")

    html.setHTML(".first_bad", 'Nah, i gotta away from here')
    timers.set_timeout_seconds(delete_element, 2)

@bind.bind(".first_buy_button", "click")
def buy_amount_lol(event):
    kamar = random.randint(0, 10)
    def update_render():
        html.setText(".button_cost", f"Cost: {localstorage.get_int("cost_amount")} coins")
    if localstorage.get_int("money") >= localstorage.get_int("cost_amount"):
        localstorage.set("money", localstorage.get_int("money") - localstorage.get_int("cost_amount"))
        localstorage.set("amount", localstorage.get_int("amount") + kamar)
        localstorage.set("cost_amount", localstorage.get_int("cost_amount") * 1.1)
        html.setText(".button_cost", f"You got {kamar} multipler!")
        timers.set_timeout_seconds(update_render, 1)
    else:
        html.setHTML(".button_cost", "Not enough money")
        timers.set_timeout_seconds(update_render, 2)

@bind.bind(".Annoying_button", "click")
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

@bind.bind(".second_bad", "click")
def Nuh_Uh(event):
    def delete_element():
        html.removeElement(".second_bad")

    html.setHTML(".second_bad", 'Nah, i gotta away from here')
    timers.set_timeout_seconds(delete_element, 2)
