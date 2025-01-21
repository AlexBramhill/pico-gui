# pico-gui

An in development micropython gui for use with a variety of displays

# Working setup

Currently developing on:

- [Pico 2w](https://thepihut.com/products/raspberry-pi-pico-2-w)
- [Pico display](https://thepihut.com/products/pico-display-pack)
- Working firmware: [`pico2_w-v0.0.11-pimoroni-micropython`](https://github.com/pimoroni/pimoroni-pico-rp2350/releases)

# Introduction

This library provides an easy to use grid structure for basic layout when using micro controllers and a display. The library uses `cells` as the main building block for a simple gui.

The work in progress goal of this project is to create an easy to use and assemble gui for specifically a pico 2w and display, including interaction via buttons.

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
