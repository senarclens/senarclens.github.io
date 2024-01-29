# Introduction to wxPython

Ensure you have a working
[installation of `pip`](../installation.html).
Then install the required dependencies via

```shell
sudo apt install python3-wxgtk4.0
```

If you are not using a Debian-based Linux, you may instead run

```shell
pip install --upgrade --user wxpython
```

Note that the latter option requires a series of development packages to be
present on your system in order to compile the dependencies. The required
packages are likely named `libwxgtk3.2-dev` and `libgtk-3-dev`.

From now on, you should be able to `import wx` in your python programs.
To get started with GUI programming in Python, follow the official wxPython
tutorial

[Getting started with wxPython](https://wiki.wxpython.org/Getting%20Started)
