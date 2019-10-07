# Introduction to KDE Neon (Linux) and Bash

## Installing Software
You can use either of the graphical package managers. Depending on the configuration of your Debian-based Linux system, there may be `muon`, `plasma-discover`, `synaptic` or any other GUI tool installed. On the command-line you can use `apt` - the advanced package tool. In order to be able to change the system, you need to run the command as `root` user. In order to do so, preprend your installation commands with `sudo`.

If you want to install all the mentioned GUI package managers with a shell command, type

```
sudo apt install muon plasma-discover synaptic
```

To install an excellent integrated development environment as well as its Python language support, run

```
sudo apt install kdevelop kdevelop-python
```

Installing a Python package with the python installer pip (pip installs
python)

```
sudo pip3 install packagename
```

## Selected Commands

| Command | Explanation |
| ------- | ---------------------------------|
| `cd [dir]` | change the current directory to `dir` (defaults to `$HOME`) |
| `cd -` | change to previous directory |
| `cp` | copy files and directories |
| `chmod` | change permissions of a file |
| `dolphin` | file manager |
| `konsole` | terminal emulator |
| `less` | opposite of more; read text files |
| `ln -s` | make (soft) links between files |
| `ls -lahR` | list directory contents |
| `man` | an interface to the on-line reference manuals |
| `rm -r` | (recursively) remove files or directories |
| `tar zcf archive.tar.gz [file...]` | create gzip compressed archive |
| `whatis` | display one-line manual page descriptions |
| `mv` | move (rename) files |
| `pwd` | print name of current/working directory |
| `echo` | display a line of text |
| `cat` | concatenate files and print on the standard output |
| `grep -rin` | print lines matching a pattern |
| `clear` | clear the terminal screen |
| `date` | print or set the system date and time |
| `df -h` | report file system disk space usage |
| `du -h` | estimate file space usage |
| `hostname` | show or set the system's host name |
| `whoami` | print effective userid |
| `` |  |

## Shell Variables
Examples include `$HOME`, `$HOSTNAME` and `$USER`.

## Shortcuts

### Global

Shortcut | Action
--- | ---
`Ctrl+Alt+t` | open konsole (terminal emulator)

### Dolphin File Manager

Shortcut | Action
--- | ---
`F4` | show konsole (terminal emulator)
`Shift+F4` | open konsole (terminal emulator)

### Shell
Shortcut | Action
--- | ---
`↑` | move up in history
`↓` | move down in history
`Ctrl+d` | end of input
`Ctrl+r` | reverse incremental search through history
`Esc-.`, `Alt+.` | recall the last argument of the previous command
`Ctrl+l` | clear the terminal screen

## Configuration
To define an alias use the `alias` command. For example, to create an alias called `i` that runs the `ipython3` shell, run

```
alias i=ipython3
```

In order to persist this change, either put it into your `~/.profile` which
is executed upon login or in your `~/.bashrc` which is executed when any
new shell is started. If it is in your `~/.profile`, you either have to log
in again or source the file via
```
. ~/.profile
```

## Python
Create an empty python file

```
touch filename.py
```

Edit the file with `kate`

```
kate filename.py
```

### Make Python Program Executable
Insert

```
#!/usr/bin/env python3
```

to the top of th file. Then run

```
chmod u+x filename.py
```

Execute the file via

```
./filename.py
```

### Run Script from Anywhere
In order to be able to run your scripts from anywhere in the file system, make
sure to have a `~/bin` directory.

```
mkdir -p ~/bin
```

Then, create a link to your script there

```
cd ~/bin
ln -s /path/to/your/script/filename.py
```
