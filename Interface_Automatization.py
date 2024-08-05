import customtkinter
import tkinter as tk
import serial

# Configure appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Set up the serial connection to Arduino
arduino_port = 'COM3'  # Adjust this based on your Arduino's serial port
arduino_baud = 9600
arduino_serial = serial.Serial(arduino_port, arduino_baud, timeout=1)

def move_motor(direction):
    # Retrieve the distance value from the appropriate entry widget
    distance = float(entries[direction].get())
    # Send direction and distance to Arduino
    arduino_serial.write(f"{direction}{distance}\n".encode())

# Initialize the GUI window
root = customtkinter.CTk()
root.title("Motor Control GUI")

# Create the main frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Title label
label = customtkinter.CTkLabel(master=frame, text="Movement Controller of Translation Stages")
label.pack(pady=12, padx=10)

# Create and pack entry widgets and buttons for X, Y, and Z directions
entries = {}  # Dictionary to hold entry widgets for X, Y, and Z directions

for direction in ['X', 'Y', 'Z']:
    entry = customtkinter.CTkEntry(master=frame, placeholder_text=f"Distance Along {direction}")
    entry.pack(pady=12, padx=200)
    entries[direction] = entry
    
    button = customtkinter.CTkButton(master=frame, text=f"Move in {direction} Direction", command=lambda d=direction: move_motor(d))
    button.pack(pady=12, padx=200)

# Start the GUI event loop
root.mainloop()



