# Installing Python

Start by installing Python for your operating system.
Make sure that `pip` is installed as well.

## Linux
On debian-based Linux distributions, you should install the following

    sudo apt install python3-pip

Most likely, you also want install

    sudo apt install python-is-python3

This allows you to use `python` and `pip` in lieu of `python3` and `pip3`.

## Windows
On Windows, download and install Python from
[python.org](https://www.python.org/downloads/).
Make sure to select `pip` to be installed as well and that Python will be
available through your operating systems `PATH` variable. You might need to
select these from advanced options during the installation.

If you already have a working installation of Python, but still require `pip`,
follow the instructions for
<a href="https://pip.pypa.io/en/stable/installation/#python">installing pip</a>.

Usually, Python will be available as `py` in the Windows terminal. If you
do not want to add the relevant directories to your `PATH` variable, it should
be possible to run `py` whenever `python` is executed here and
`py -m name` when a Python program (like `pip`) is executed. That means,
for example, instead of writing

```
pip install --user --upgrade pip
```

you should be able to write

```
py -m pip install --user --upgrade pip
```

on Windows, even without adding the relevant directories to your `PATH`.

## Installing Packages
When installing packages, always make sure to upgrade `pip` first.

    pip install --user --upgrade pip

When `pip` is up to date, install the packages you desire (for example,
`numpy`, `pandas` and `jupyterlab`).

    pip install --user --upgrade numpy pandas jupyterlab

