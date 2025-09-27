# Installing Linux

You can install Linux to run directly on your computer hardware or
on virtual hardware inside an existing operating system. When installing on
hardware, you may install it side-by-side with other operating systems.
Using virtual hardware to run Linux on top of an existing operating system
requires virtual machine (VM) host software.

Both options have advantages and disadvantages. Direct installation has a
performance benefit that is especially important on old hardware.
Installation on a VM host is safer as you generally cannot damage your existing
operating system.


## Download an ISO Image
No matter which distribution you want to install - I always recommend using
a "live" version of that distribution. A live version allows you to boot
directly intro a running system from your installation medium without
installing anything. This way, you may test if your hardware is properly
supported by the distribution upfront.

### Debian Stable
There are many great Linux distributions. To get started, I recommend the
latest stable version of
[Debian](https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/)
for installation both on hardware and in a virtual environment.

In the link above, you may choose among different desktop environments.
Personally, I like KDE best for getting started as it has excellent
integration between GUI tools and the shell. If you like to try the KDE
flavor of Debian, download the file called
`debian-live-??.?.0-amd64-kde.iso` (the question marks represent the current
version). Once downloaded, you may want to verify the file's
cryptographic hash. To do so, download
[SHA512SUMS](https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/SHA512SUMS)
to the same directory as your `.iso`. Then run

```shell
sha512sum --check SHA512SUMS
```

Note that you should receive an 'OK' only for the file you downloaded. All
other files listed in `SHA512SUMS` are expected to fail since they are
not available for checking.

### Manjaro
If you want to run Linux on very modern hardware, you may need to use the
newest Linux kernel. Manjaro is a beginner friendly alternative to Debian
that offers an easy to use tool to always run the newest Linux kernel. Be
aware that you'll have to perfom lots of updates of all installed software
since Manjaro aims to deliver new versions as soon as possible.

Download your desired flavor (I recommend KDE Plasma) from
[manjaro.org](https://manjaro.org/products/download/x86).
To verify the authenticity of your download, get the corresponding *.sig file
(available after clicking on "More") and do the following once:

```shell
wget gitlab.manjaro.org/packages/core/manjaro-keyring/-/raw/master/manjaro.gpg
gpg --import manjaro.gpg
```

For each iso image you'd like to verify, run

```shell
gpg --verify manjaro-kde-??.?-??????-linux??.iso.sig manjaro-kde-??.?-??????-linux??.iso.sig
```


## Native Installation
To install Linux on your hardware, you need installation media. Once you have
an iso image, flash the image to a USB drive. This can be done, for example,
with [Balena Etcher](https://etcher.balena.io/).

Once you have a bootable USB drive, simply plug it into your computer and
boot from it. Make sure to create proper backups of your data before
installation in case you accidentally remove an existing partition.


## VM Host Software
There are numerous VM hosts available. Some of them are open source software
(eg. KVM + Virtual Machine Manager, Xen, VirtualBox, Proxmox, UTM, ...)
while others are proprietary.

For installing Linux on an existing Windows or pre-M2 MacOS host,
[VirtualBox](https://www.virtualbox.org/wiki/Downloads)
is a rather easy choice.

For installing Linux on top of an M2 MacOS host,
[UTM](https://github.com/utmapp/UTM) is likely the best open source option.

