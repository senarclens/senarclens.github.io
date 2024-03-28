# Introduction to wxWidgets
{% assign wx = "https://docs.wxwidgets.org/latest/" %}
{% assign gh = "https://github.com/wxWidgets/wxWidgets" %}

## Contents
{:.no_toc}
* A markdown (kramdown) generated TOC.
{:toc}

## Getting Started with wxWidgets
[wxWidgets](https://www.wxwidgets.org/) is a leightweight GUI toolkit that is
primarily targeted for C++
but is also available for other languages including Python. It gives
applications a truly native look by using each platform's native API. 
wxWidgets is completely open source using the
[wxWidgets licence]({{ gh }}/blob/master/docs/licence.txt) which is
a more liberal version of the LGPL (allowing distribution without the source
code). It is very
[actively developed]({{ gh }}/pulse/monthly) and maintained and has good
support for all common programming environments. The source code is available
on the project's [Github page]({{ gh }}). Reference applications built with
wxWidgets include
[Audacity](https://github.com/audacity/audacity) and
[Code::Blocks](https://www.codeblocks.org/).

To get started, install the required dependencies

```
sudo apt install libwxgtk3.2-dev
```

After the installation, follow the official
[Hello World Example]({{ wx }}overview_helloworld.html). Save your code to
`hello_wx.cpp`
To compile the example, type

```
clang++ hello_wx.cpp `wx-config --cxxflags --libs` -o hello_wx
```

Start your first GUI application by typing `./hello_wx`.

![wxWidgets hello world application](images/hello_wx.png)

## Compiling wxWidgets Programs with GNU Make
wxWidgets files can, of course, also be compiled with GNU Make. Use the
source below as an example
```make
{% include_relative Makefile %}
```
Download the above template [Makefile](Makefile).

## Compiling wxWidgets Programs with CMake
While GNU Make is a great build system for learning and understanding how
build files work, Makefiles quickly get complicated and have portability
issues between operating systems. Hence, I recommend using CMake for
generating the build files for `make` or `ninja`.

```cmake
{% include_relative CMakeLists.txt %}
```
Download the above template [CMakeLists.txt](CMakeLists.txt).

CMake allows creating out of source builds. This is usually done by your IDE.
On the command-line, within your project directory, you'd have to
type
```shell
mkdir -p build && cd build
cmake ..
make -j8  # -j defines the number of cores to use for compilation
```
You binary can then be found in the above created `build` directory.

## wxWidgets Example Programs
There are a series of high quality examples available directly in the
[wxWidgets documentation](https://docs.wxwidgets.org/3.2/page_samples.html).
These examples can be installed via

```shell
sudo apt install wx3.2-examples  # recommended way
```

or by cloning wxWidgets and entering the `samples` directory

```shell
git clone git@github.com:wxWidgets/wxWidgets.git
cd wxWidgets/samples
```

In addition, you can find tested, working example code in the
[C++ wxWidgets Examples](https://gitlab.com/htl-bulme/cpp_wx_examples/)
repository.
