# Raspberry Pi LED Display Timer

A fun project using the Raspberry Pi and Sense HAT emulator to create interactive LED display timers. This project demonstrates how to control an 8x8 LED matrix to create visual countdown effects.

## Features

- Text-based countdown timer with color transitions
    - Numbers fade from green to red as time progresses
    - Ends with a striking purple display
- Dot-based countdown timer
    - Uses individual LED pixels to show progress
    - Visual transition from green to red pixels
    - Includes a flashy ending sequence

## Setup

You'll need to install the Sense HAT emulator:

```bash
sudo apt install python3-sense-emu python-sense-emu-doc sense-emu-tools -y
```

## Quick Start

1. Launch the Sense HAT Emulator from Programming menu
2. Run the example code to display "Hello World"
3. Try out both countdown timer variations - text and dots

## Note

This project uses the Sense HAT emulator instead of physical hardware, making it accessible to anyone with a Raspberry Pi.
