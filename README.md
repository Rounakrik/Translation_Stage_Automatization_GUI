# Translation_Stage_Automatization_GUI

This project provides a solution for controlling three motors connected to an Arduino to manage translation stages in X, Y, and Z directions. It includes Arduino firmware and a Python-based graphical user interface (GUI) for precise motor control.

## Components

1. **Arduino Firmware**:
   - Uses the `CytronMotorDriver` library to manage motor control.
   - Reads commands for direction and distance from the Python GUI.
   - Operates with 200 steps per rotation, equating to 2mm movement per rotation.

2. **Python GUI**:
   - Developed with `customtkinter` for a modern and user-friendly interface.
   - Allows users to input distances and control motors by sending commands via serial communication.
   - Features entry fields for distance and buttons for X, Y, and Z direction movements.

## Installation

1. **Arduino Setup**:
   - Upload the provided Arduino code to your board.
   - Connect the motors and motor drivers to the specified pins.

2. **Python Setup**:
   - Install required Python packages:
     ```bash
     pip install customtkinter pyserial
     ```
   - Modify the `arduino_port` variable in the Python script to match your Arduino’s serial port.

## Usage

1. Run the Python GUI script.
2. Enter the desired distance (in mm) for X, Y, and Z directions.
3. Click the corresponding button to move the motors.

## Acknowledgments

Thanks to `CytronMotorDriver` and `customtkinter` for their valuable libraries.
