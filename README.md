# Roboptimus Prime


Roboptimus prime is a robot which is able to complete a maze, utilising a set of ultrasonic sensors, colour sensors, servos, and a oled screen. It's purpose is to be able to safely navigate a maze without crashing, and also to stop, wait a few seconds and continue its loop, when the colour green has been detected.

## Description
Roboptimus prime is a microcontroller-based robot utilising Raspberry Pi Pico. It is equipped with **Ultrasonic Sensors** to detect distance from the front and side, **Servo motors** for directional movement, a **Colour sensor** to detect the colour green, and an **OLED display** for visual feedback. The overall use of the robot is for autonomous navigation environments, like a maze-solving competition.

## Getting Started

### Dependencies

* Raspberry Pi Pico with MicroPython
* Host machine
* PiicoDev Python Libraries
* Servo-Control Library for PWM actuation
* USB-A to Micro-USB cable

### Installing

* Export Files onto System
* Open in VS Code
* Upload project to Pi Pico

### Executing program

* Ensure MicroPython Board connection is established
* Right click on a file and press run current file on Pico to run a file
* Right click on a file and press upload project to Pico in order to upload files onto Pico
* if there is a specific file you want to test change main.py line 7 into the name of code you want executed on Pico.
* Magic

## Help

* Ensure the correct **drives** are installed.
* Ensure MicroPython board is **connected**
* Ensure there is power throughout your system
* Ensure wires are **not** broken/disconnected
* Ensure sensors **are** working

## Authors

kelvin Aung
[@kelvin.aung@education.nsw.gov.au](https://github.com/TheFileExplorer)

## Version History

* 0.1
    * movement class created & unit tests added
    * Distance reading function implemented
    * mered updates from main branch
    * Start UltrasonicSensor class
    * update ultrasonic.py
* 0.2
    * Add UltraSonic method
    * Minor fixes
    * Cleanup code
* 0.3
    * introduce MS_Unit_TEST and CLS_Unit_Test
* 0.4
    * Add colour sensor class & unit tests
    * update CLS module
    * Fixed bugs in ColourSensor class
* 0.5
    * Change colour sensor to return HSV instead of RGB
    * Update roboptimus print logic
    * Fixed colour sensor bugs
* 0.6
    * Start display code
    * Ultrasonic class placeholder
* 0.7
    * Draft controller for Roboptimus
    * Updates
    * Update README.md
    * last-minute corrections
    * **Final Commit**
* 0.8
    * UPDATE README
     

## License

This project is licensed under the [GPL-3.0] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Github md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [TempeHS MicroPython template](https://github.com/TempeHS/TempeHS_MicroPython_DevContainer)
