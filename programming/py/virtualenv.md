# Virtual Environments

A Python virtual environment (venv) is an isolated Python installation that
allows you to create and manage independent Python environments for different
projects. It's essentially a self-contained directory tree that contains a copy
of the Python interpreter and various supporting files, enabling you to install
packages and manage dependencies without affecting your global Python
installation or other projects.

If you hence want to install packages limited to a particular Python project,
create a virtual environment for that project.
Note that your virtual environments won't have access to globally installed
Python packages.

## Setup, Activation and Deactivation
To create a virtual environment, you may first have to install the management
utility for virtual environments

```
sudo apt install python3-venv
```

Once this is installed, create up your virtual environment. The second `venv`
is the name of your virtual environment in the command below.

```
python -m venv venv
```

Once complete, activate your virtual environment whenever you want to work
with it

```
. venv/bin/activate
```

Note that if you want to leave your virtual environment, you'd have to type
```
deactivate
```

## Installing Packages
Once a virtual environment is activated (`. venv/bin/activate`) packages
can be installed via

```
pip install $PACKAGE_NAME
```

