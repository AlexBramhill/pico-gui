# pico-gui

A micropython pico gui for use with the pico display from pimoroni

# Working setup

- [Pico 2w](https://thepihut.com/products/raspberry-pi-pico-2-w)
- [Pico display](https://thepihut.com/products/pico-display-pack)
- Working firmware: [`pico2_w-v0.0.11-pimoroni-micropython`](https://github.com/pimoroni/pimoroni-pico-rp2350/releases)

# Underlying concepts

This library provides an easy to use grid structure for basic layout when using a raspberry pi pico and the pico display. The library uses `cells` as the main building block for a simple gui. Each `cell` can then easily be coloured and have text written in (with wrap automatically calculated).
