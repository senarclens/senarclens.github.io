# Documentation Generation

Documentation can be automatically generated from source code comments. This
is similiar to docstrings in Python. To distinguish between regular comments
and documentation comments for C and C++,
[special comment blocks][special_comments] (`/**`, `/*!`, `///` or `//!`)
have to be used.

These special comments will then be consumed by a documentation generation
tool. For C and C++, the most renowned tool is [Doxygen][doxygen]. It
generate's the complete source code documentation as website or pdf file
automatically including links and generating diagrams.
[Sphinx][sphinx] offers a viable, more modern alternative.

## Doxygen
Creating the complete documentation is as easy as calling

```shell
doxygen Doxyfile
```

This requires to have a configuration file in place - for an example see
one of my prior project's
[`Doxyfile`][doxyfile]. This file can be written manually or created via a
GUI tool called
`doxywizard` (usually installed with doxygen).



[doxyfile]: https://raw.githubusercontent.com/senarclens/cvrptwms/refs/heads/master/Doxyfile
[doxygen]: https://www.doxygen.nl/
[special_comments]: https://www.doxygen.nl/manual/docblocks.html#specialblock
[sphinx]: https://www.sphinx-doc.org
