# Pygame

Pygame is a Python package designed for writing video games.
It uses the Simple DirectMedia Layer (SDL) library, which is written in
the C programming language. Pygame allows game development using the SDL
without having to use the C.

## Getting Started with pygame
You may want to start with a quick video tutorial like
[Get Started in Pygame in 10 minutes!](https://youtu.be/y9VG3Pztok8?si=88_ANgwX0u8gy-Nt&t=111)
to get a taste of what you're going to accomplish.

You may use any proper pygame tutorial, but make sure that the tutorial uses
any current version of Python (>= 3.8). I currently recommend this
[complete guide to pygame](https://coderslegacy.com/python/python-pygame-tutorial/).

## Setting up pygame
You can test if pygame is installed on your compouter by starting
python

```shell
python
```

and then importing the library

```py
import pygame
```

If you want to install it on your own computer, run the following

```
sudo apt install python3-pygame
```

If you don't have the joy of running a debian-based Linux operating system,
you may install pygame with `pip` (stands for pip installs python)

```
python -m venv pygame-venv
. pygame-venv/bin/activate
pip install -U pip
pip install pygame
```
