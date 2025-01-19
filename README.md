# pico-gui

A micropython pico gui for use with the pico display from pimoroni

# Working setup

- [Pico 2w](https://thepihut.com/products/raspberry-pi-pico-2-w)
- [Pico display](https://thepihut.com/products/pico-display-pack)
- Working firmware: [`pico2_w-v0.0.11-pimoroni-micropython`](https://github.com/pimoroni/pimoroni-pico-rp2350/releases)

# Introduction

This library provides an easy to use grid structure for basic layout when using a raspberry pi pico and the pico display. The library uses `cells` as the main building block for a simple gui. Each `cell` can then easily be coloured and have text written in (with wrap automatically calculated).

# Getting started

## Updating dependency injection

- Create a display service for your display extending `abstract_display.py` as a base
- Override all methods to your display's specific implementation
- Update the dependency injection to utilise your newly created display service

## Working with the display

To get started with the gui, instantiate the display

```python
display = PicoDisplay() # Replace with the custom display service if using a custom display service
```

The display object allows for the control of display-wide functions such as backlight and updating the screen. At the moment, no soft updates are supported so it is suggested that a hard update is always used for eink screens.

```python
display.set_backlight_percentage(0.5) # Example of updating the backlight
display.update() # Example of updating the screen
```

## Grids and cells

Every layout element is a cell. The main cell is the entire display, and can be retrieved with

```python
display_cell = display.get_cell()
```

On this, we can do basic easy functions quickly, such as:

```
display_cell.set_fill(SetFillInCellProps(Rgb(255, 0, 0)))
display_cell.set_text(SetTextInCellProps("Hello, World!"))
```
