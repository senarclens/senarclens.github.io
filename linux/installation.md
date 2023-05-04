# [WIP] Installing Linux

You can install Linux to run directly on your computer hardware or
on virtual hardware inside an existing operating system. When installing on
hardware, you may install it side-by-side with other operating systems.
Using virtual hardware to run Linux on top of an existing operating system
requires virtual machine (VM) host software.

Both options have advantages and disadvantages. Direct installation has a
performance benefit that is especially important on old hardware.
Installation on a VM host is safer as you generally cannot damage your existing
operating system.

## VM Host Software
There are numerous VM hosts available. Some of them are open source software
(eg. KVM + Virtual Machine Manager, Xen, VirtualBox, Proxmox, UTM, ...)
while others are proprietary.

For installing Linux on an existing Windows or pre-M2 MacOS host,
[VirtualBox](https://www.virtualbox.org/wiki/Downloads)
is a rather easy choice.

For installing Linux on top of an M2 MacOS host,
[UTM](https://github.com/utmapp/UTM) is likely the best choice.

## Download an ISO Image
There are many great Linux distributions. To get started, I recommend
[Debian](https://www.debian.org/CD/live/)
for installation in a virtual environment.
