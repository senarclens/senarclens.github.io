# Open Source Software License Management

When using free / open source software (FOSS) libraries it is important to
understand their terms and conditions. The same holds true when publishing
your own software using a FOSS license.

There are a great many different open source software licenses. I recommend
to use one of the licenses that is approved by either
[Free Software Foundation (FSF)](https://www.fsf.org/) or
[Open Source Initiative (OSI)](https://opensource.org/).

The Software Package Data Exchange (SPDX) provides an excellent overview
in their [SPDX License List](https://spdx.org/licenses/). The site provides
each of the licenses' full name, identifier, full text and whether or not they
are approved by any of the above organisations.

## Publish Your Own Code as FOSS
When publishing your own code as FOSS, you need to decide which license to
use. For this purpose, start by consulting
[choose an open source license](https://choosealicense.com/).

After chosing an appropriate license, add it to your project by commiting
a `LICENSE.txt` file. You should also add it to your project's package
description file if applicable (eg. `package.json` for node projects or
Python's `setup.py`).

Ideally, also add a license headers in each source file stating the
copyright holder(s), year and the license's short name. You may even want to
mention the license in the project's `README.md`.

## Tools for Managing Open Source Dependencies
