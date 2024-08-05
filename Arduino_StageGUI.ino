#include "CytronMotorDriver.h"

// Define motor objects for each direction
CytronMD motorX(PWM_DIR, 3, 5);  // Motor for X direction
CytronMD motorY(PWM_DIR, 6, 9);  // Motor for Y direction
CytronMD motorZ(PWM_DIR, 10, 11); // Motor for Z direction

int steps_per_rotation = 200;   // Assuming 200 steps per rotation

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char direction = Serial.read();  // Read the direction identifier ('X', 'Y', 'Z')
    int distance_mm = Serial.parseInt();  // Read distance value from serial input
    int steps = distance_mm * steps_per_rotation / 2;  // Convert mm to steps (assuming 2mm per rotation)
    
    CytronMD* motor = NULL;  // Pointer to the selected motor

    switch(direction) {
      case 'X':
        motor = &motorX;
        break;
      case 'Y':
        motor = &motorY;
        break;
      case 'Z':
        motor = &motorZ;
        break;
      default:
        return;  // If the direction is invalid, do nothing
    }

    if (motor != NULL) {
      if (steps > 0) {
        motor->setSpeed(128);  // Set motor speed for clockwise rotation
      } else if (steps < 0) {
        motor->setSpeed(-128);  // Set motor speed for counterclockwise rotation
      }
      
      delay(abs(steps));  // Adjust delay based on motor speed and mechanical setup
      
      motor->setSpeed(0);  // Stop motor
    }
  }
}
