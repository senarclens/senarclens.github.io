# Introduction Jupyter Notebooks
{::options toc_levels="2..6" /}

## Contents
{:.no_toc}

* A markdown (kramdown) generated TOC.
{:toc}

## Installation
Make sure to use an updated version of `pip`.

```
pip install --user --upgrade pip
```

Install `jupyterlab` which includes the kernel for running Python code.

```
pip install --user --upgrade jupyterlab
```

### Installing the C++ Kernel
In order to run C++ code, the `cling` interactive C++ interpreter must be
available. It can be downloaded from
[root.cern.ch](https://root.cern.ch/download/cling/) for selected Linux
distributions. After extracting the archive, the `PATH` variable must be
adjusted to include the path to cling's binaries.

```
export PATH=$PATH:${YOUR_CLING_ROOT}/bin
```

To make the change persistent, add the above line to your `~/.profile'.
Afterwards, prepare and install the corresponding Jupyter kernel. You may
select any of C++11, C++14 and C++17. In the instructions below, the C++17
kernel is made available.

```
cd ${YOUR_CLING_ROOT}/share/cling/Jupyter/kernel/
pip install -e .
jupyter-kernelspec install --user cling-cpp17
```

Once this is done, language support for C++ will be available in future
`jupyterlab` sessions.

## Getting Started
After completing the installation, you can either start the classic
`jupyter-notebook` or the more recent `jupyter-lab`. Once started, the
built-in help is available via the `Help` menu. While using
`jupyter-notebook`, the shortcuts can be displayed using the `h` key and an
interactive tour is available in `Help->User Interface Tour`.

## Converting Notebooks
It is possible to convert notebook files to a variety of formats.
For example, you can extract the contained python code into a proper python
script via

```
jupyter-nbconvert --to python yournotebook.ipynb
```

Multiple other formats are available as well (including $\LaTeX$). Consult

```
jupyter-nbconvert --help
```

more information.
