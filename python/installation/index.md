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
On Windows, download and install Python from https://www.python.org/downloads/
Make sure to select `pip` to be installed as well and that Python will be
available through your operating systems `PATH` variable. You might need to
select these from advanced options during the installation.

## Installing Packages
When installing packages, always make sure to upgrade `pip` first.

    pip install --user --upgrade pip

When `pip` is up to date, install the packages you desire

    pip install --user --upgrade numpy pandas jupyterlab

