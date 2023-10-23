from time import sleep
import customtkinter
import tkinter
from PIL import ImageGrab
import numpy as np
import pyautogui
from screeninfo import get_monitors

# Configuration

# Target color
cs2_color = (54, 183, 82)
dota2_color = (69, 111, 89)

# Monitor
for monitor in get_monitors():
    if monitor.is_primary:
        primary_monitor = monitor

if primary_monitor is None:
    raise Exception("No primary monitor found")

# Region
left = primary_monitor.width / 2  # Replace with the left coordinate of your region
top = primary_monitor.height / 3  # Replace with the top coordinate of your region
right = primary_monitor.width / 2 + 1  # Replace with the right coordinate of your region
bottom = primary_monitor.height - primary_monitor.height / 3  # Replace with the bottom coordinate of your region


def button_callback():
    global x, y, target_color, tolerance

    # Get the selected radio button
    game_mode = radio_var.get()

    # Set the target color
    if game_mode == 1:
        target_color = cs2_color
        tolerance = 20
    elif game_mode == 2:
        target_color = dota2_color
        tolerance = 3

    # Loop until the program clicks
    while True:
        sleep(3)
        # Get the screenshot
        cropped_screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

        # Convert the screenshot to numpy array
        screenshot_array = np.array(cropped_screenshot)

        # Find the coordinates and click
        match_coordinates = np.argwhere(np.all(np.abs(screenshot_array - target_color) <= tolerance, axis=-1))
        if len(match_coordinates) > 0:
            y, x = match_coordinates[0]
            pyautogui.click(left + x, top + y)
            if switch_var.get() == "on":
                app.quit()
            break


# Main
app = customtkinter.CTk()

# Window
app.geometry("400x300")
app.title("AutoAccept")
app.resizable(False, False)
app.iconbitmap("icon.ico")

# Labels
label = customtkinter.CTkLabel(app, font=("Arial", 32), text="AutoAccept", fg_color="transparent")
label.pack(padx=20, pady=20)

# Radiobutton
radio_var = tkinter.IntVar(value=1)
radiobutton_cs2 = customtkinter.CTkRadioButton(app, text="CS2", font=("Arial", 16), variable=radio_var, value=1)
radiobutton_dota2 = customtkinter.CTkRadioButton(app, text="Dota 2", font=("Arial", 16), variable=radio_var, value=2)
radiobutton_cs2.pack(padx=20, pady=10)
radiobutton_dota2.pack(padx=20, pady=10)

# Button
button = customtkinter.CTkButton(app, text="Start", font=("Arial", 16), command=button_callback)
button.pack(padx=20, pady=20)

# Switch
switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="Close after click", font=("Arial", 16),
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.pack(padx=20, pady=0)

# Run
app.mainloop()
