import tkinter as tk
from tkinter import ttk
import requests

ESP8266_IP = "ESP8266_IP_ADDRESS"

def send_rgb_request():
    red1 = red_scale1.get()
    green1 = green_scale1.get()
    blue1 = blue_scale1.get()
    red2 = red_scale2.get()
    green2 = green_scale2.get()
    blue2 = blue_scale2.get()
    
    payload = {
        "red1": red1,
        "green1": green1,
        "blue1": blue1,
        "red2": red2,
        "green2": green2,
        "blue2": blue2
    }
    
    try:
        requests.post(f"http://{ESP8266_IP}/rgb", data=payload)
    except requests.exceptions.RequestException as e:
        print("Failed to send request:", e)

def toggle_light1():
    if light1_var.get():
        light1_var.set(False)
        light1_button.config(text="Off")
        red_scale1.config(state="disabled")
        green_scale1.config(state="disabled")
        blue_scale1.config(state="disabled")
    else:
        light1_var.set(True)
        light1_button.config(text="On")
        red_scale1.config(state="normal")
        green_scale1.config(state="normal")
        blue_scale1.config(state="normal")

def toggle_light2():
    if light2_var.get():
        light2_var.set(False)
        light2_button.config(text="Off")
        red_scale2.config(state="disabled")
        green_scale2.config(state="disabled")
        blue_scale2.config(state="disabled")
    else:
        light2_var.set(True)
        light2_button.config(text="On")
        red_scale2.config(state="normal")
        green_scale2.config(state="normal")
        blue_scale2.config(state="normal")

root = tk.Tk()
root.title("RGB Controller")

# RGB Control for LED 1
frame1 = ttk.Frame(root, padding="10")
frame1.grid(row=0, column=0, padx=10, pady=10)
ttk.Label(frame1, text="RGB Control - LED 1").grid(row=0, column=0, columnspan=3)

red_scale1 = ttk.Scale(frame1, from_=0, to=255, length=200, orient="horizontal")
red_scale1.grid(row=1, column=0, padx=5, pady=5)
green_scale1 = ttk.Scale(frame1, from_=0, to=255, length=200, orient="horizontal")
green_scale1.grid(row=1, column=1, padx=5, pady=5)
blue_scale1 = ttk.Scale(frame1, from_=0, to=255, length=200, orient="horizontal")
blue_scale1.grid(row=1, column=2, padx=5, pady=5)

# Color indicators for LED 1
ttk.Label(frame1, text="R", foreground="red").grid(row=2, column=0)
ttk.Label(frame1, text="G", foreground="green").grid(row=2, column=1)
ttk.Label(frame1, text="B", foreground="blue").grid(row=2, column=2)

# On/Off switch for LED 1
light1_var = tk.BooleanVar(value=True)
light1_button = ttk.Button(frame1, text="On", command=toggle_light1)
light1_button.grid(row=3, column=1, pady=10)

# RGB Control for LED 2
frame2 = ttk.Frame(root, padding="10")
frame2.grid(row=1, column=0, padx=10, pady=10)
ttk.Label(frame2, text="RGB Control - LED 2").grid(row=0, column=0, columnspan=3)

red_scale2 = ttk.Scale(frame2, from_=0, to=255, length=200, orient="horizontal")
red_scale2.grid(row=1, column=0, padx=5, pady=5)
green_scale2 = ttk.Scale(frame2, from_=0, to=255, length=200, orient="horizontal")
green_scale2.grid(row=1, column=1, padx=5, pady=5)
blue_scale2 = ttk.Scale(frame2, from_=0, to=255, length=200, orient="horizontal")
blue_scale2.grid(row=1, column=2, padx=5, pady=5)

# Color indicators for LED 2
ttk.Label(frame2, text="R", foreground="red").grid(row=2, column=0)
ttk.Label(frame2, text="G", foreground="green").grid(row=2, column=1)
ttk.Label(frame2, text="B", foreground="blue").grid(row=2, column=2)

# On/Off switch for LED 2
light2_var = tk.BooleanVar(value=True)
light2_button = ttk.Button(frame2, text="On", command=toggle_light2)
light2_button.grid(row=3, column=1, pady=10)

# Send Button
send_button = ttk.Button(root, text="Send RGB", command=send_rgb_request)
send_button.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
