# Linux (KDE Neon)
{::options toc_levels="2..6" /}

## Contents
{:.no_toc}

* A markdown (kramdown) generated TOC.
{:toc}

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

## Selected Shell Commands

| Command | Explanation |
| ------- | ---------------------------------|
| `cat` | concatenate files and print on the standard output |
| `cd [dir]` | change the current directory to `dir` (defaults to `$HOME`) |
| `cd -` | change to previous directory |
| `clear` | clear the terminal screen |
| `cp` | copy files and directories |
| `chmod` | change permissions of a file |
| `date` | print or set the system date and time |
| `echo` | display a line of text |
| `df -h` | report file system disk space usage |
| `du -h` | estimate file space usage |
| `dolphin` | file manager |
| `grep -rin` | print lines matching a pattern |
| `hostname` | show or set the system's host name |
| `konsole` | terminal emulator |
| `less` | opposite of more; read text files |
| `ln -s` | make (soft) links between files |
| `ls -lahR` | list directory contents |
| `man` | an interface to the on-line reference manuals |
| `mkdir [dir]` | make directories |
| `mv` | move (rename) files |
| `pwd` | print name of current/working directory |
| `rm -r` | (recursively) remove files or directories |
| `tar zcf archive.tar.gz [file...]` | create gzip compressed archive |
| `whatis` | display one-line manual page descriptions |
| `whoami` | print effective userid |

An excellent tool for explaining complex linux commands is 
[explainshell.com](https://explainshell.com/).

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
`Ctrl+l` | clear the terminal screen
`Ctrl+r` | reverse incremental search through history
`Esc-.`, `Alt+.` | recall the last argument of the previous command

## Configuration
To define an alias use the `alias` command. For example, to create an alias called `i` that runs the `ipython3` shell, run

```
alias i=ipython3
```

In order to persist this change, put it into your `~/.profile` which
is executed upon login. Alternatively, you could add that line to
your `~/.bashrc` which is executed when a new bash
new shell is started. To add the line to your `~/.profile`, edit it
with your favorite text editor, for example with
```
kate ~/.profile
```
To make the change available without logging in, you need to source the
file via
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
In case the directory did not exist, you will have add it to your executabe
`$PATH`.
```
PATH=~/bin:"${PATH}"
```

Then, create a link to your script

```
cd ~/bin
ln -s /path/to/your/script/filename.py
```
Finally, you'll be able to run your script as executable program from anywhere
in your filesystem.

## Video Tutorial
Finally, there exists a (somewhat outdated) video tutorial covering most of the content of this session: [Introduction to Linux for Beginning Software Development](https://www.youtube.com/watch?v=4cdRApK7RTQ).
