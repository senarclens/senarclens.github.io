# Open Source Software License Management

When using free / open source software (FOSS) libraries it is important to
understand their terms and conditions. The same holds true when publishing
your own software using a FOSS license.

There are a great many different open source software licenses. I recommend
to use one of the licenses that is approved by either
[Free Software Foundation (FSF)](https://www.fsf.org/) or
[Open Source Initiative (OSI)](https://opensource.org/).

The term free refers to freedom, not price. Free software licenses
grant four essential freedoms: the freedom use, the freedom to study,
the freedom to share and the freedom to improve free software.
An excellent summary of these freedoms is available by the
the [Free Software Foundation Europe (FSFE)](https://fsfe.org/freesoftware/freesoftware.html).

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

## Tools for Managing Licenses of Open Source Dependencies

### License Finder
[License Finder](https://github.com/pivotal/LicenseFinder)
detects the licenses of the packages your software depends. It works with
package managers (like `pip` or `npm`) to find your dependencies. When
integrated in your CI process, it can ensure upon every `push` that all
dependencies have licenses that are accepted by your policies.

For this to work, your policy has to be defined in configurable list of
permitted licenses. For example, your `.dependency_decisions.yml` could
include

```yaml
---
- - :permit
  - Apache-2.0
  - :who: Gerald Senarclens de Grancy
    :why: Permissive OSI approved license w/out conflicts for us
    :versions: []
    :when: 2021-10-01 18:07:00.097448338 Z
- - :permit
  - MIT
  - :who: Gerald Senarclens de Grancy
    :why: Permissive OSI approved license w/out conflicts for us
    :versions: []
    :when: 2021-10-01 18:14:08.047430689 Z

```

To install `license_finder`, type
```
sudo gem install license_finder
```
If you prefer to install `license_finder` in your home directory, type
```
gem install --user-install license_finder
```
instead.

After installing all of your dependencies, launch `license_finder` with
```
license_finder --python-version=3 --decisions-file=.dependency_decisions.yml
```

`license_finder` can easily be included in the free tier of Gitlab's CI/CD
pipelines (.gitlab-ci.yml) as well as GitHub's actions (.github/workflows).

## FOSSology
Another great tool is [FOSSology](https://www.fossology.org/).
It is an open source license compliance software system and toolkit.
It can run license, copyright and export control scans from the command line.
In contrast to License Finder, it also offers a complete compliance workflow
based upon a database and web UI.

The workflow allows to generate an SPDX file, or a README with the copyrights
notices from your software.

## Proprietary Solutions
There are many proprietary solutions that offer scanning for
open source license compliance. They usually also include scanning for
security vulnerabilities, but come with a considerable price tag.
The first prominent one was
[Black Duck](https://www.synopsys.com/software-integrity/security-testing/software-composition-analysis.html), however meanwhile there are many
alternatives. One of them is the most expensive tier of
[GitLab](https://about.gitlab.com/pricing/).

