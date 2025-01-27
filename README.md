# pico-gui

An in development micropython gui and general pico helper

# Working setup

## Hardware

- [Pico 2w](https://thepihut.com/products/raspberry-pi-pico-2-w)
- [Pico display](https://thepihut.com/products/pico-display-pack)
- [LiPo SHIM for Pico](https://thepihut.com/products/lipo-shim-for-pico)
- [1200mAh 3.7V LiPo Battery](https://thepihut.com/products/1200mah-3-7v-lipo-battery)

## Firmware

- Working firmware: [`pico2_w-v0.0.11-pimoroni-micropython`](https://github.com/pimoroni/pimoroni-pico-rp2350/releases)

# Introduction

This library provides various easy to use services to aid Pico development. To get started, fill in the `secrets.py` with valid values using `secrets_example.py` as a base, and have a look around.

## Services

### Battery

Aids in reading of battery charging and discharging status, includes ability to get voltage/percentage charge. Has error raising to avoid getting incorrect values when charging.

### Wifi

Wifi interface that streamlines the connection to wifi, combining multiple connection steps at once to make calls more efficient for battery use.

### Spatial

Spatial layout helper that creates a grid structure for basic layout when using micro controllers and a display.

The service uses `cells` as the main building block for a simple gui.

#### Grids and cells

Every layout element is a cell. The main cell is the entire display, and can be retrieved with

`````python
display = PicoGraphics(display=DISPLAY_INKY_PACK, pen_type=PEN_1BIT)
width, height = display.get_bounds()

display_cell = CellCreator.create_cell_from_display_dimensions(
    width, height)
```

On this, we can do basic easy functions quickly, such as:

````python
subgrid = Grid.create_cell_grid_in_cell(display_cell, props=GridProps(
spacing_type='percentage_summation', x_spacing_values=[0.25, 0.5, 0.75], y_spacing_values=[0], margin=2)) # Note a 0 will not subdivide that axis
`````

We can then further subdivide the cells in the returned array, or render graphics to them for instance:

```python
for row in subgrid:
    for cell in row:
        display.rectangle(cell.left_bounds, cell.top_bounds,
                          cell.width, cell.height)
```

# Todo

The work in progress goal of this project is to create an easy to use and assemble gui for specifically a pico 2w and display, including interaction via buttons.

- [ ] LED service to turn off lipo shim LEDs
- [ ] API access to set time (for battery tests)
- [ ] Uasyncio functionality
- [ ] Screen handler
- [ ] Program handler
- [ ] Display service integration with cells/grids to allow for ease of writing text etc
