# Distributed Version Control

{% include list.liquid %}

To seriously get into git, I recommend working through the
"[git book](https://git-scm.com/book/en/v2)".

## Installation
Using a Debian-based Linux distribution, type

```
sudo apt install git git-gui git-cola
```

to install git and two different GUI front-ends. If you're on Windows,
download `git` from [git-scm.com](https://git-scm.com/download/win) (a
portable edition is available).

## Basic Configuration
```shell
git config --global user.name "Your Name"
git config --global user.email "you@your.provider.eu"
git config --global core.editor $YOUR_FAVORITE_EDITOR
git config --global -e  # show/ edit config file if desired
```

## Selected Commands

| Command | Explanation |
| ------- | ---------------------------------|
| `clone` | Clone a repository into a new directory |
| `status` | Show the working tree status |
| `add` | Add file contents to the index |
| `commit` | Record changes to the repository |
| `push` | Update remote refs along with associated objects |
| `diff` | Show changes between commits, commit and working tree, etc |
| `log [-p]` | Show commit logs |
| `pull` | Fetch from and integrate with another repository or a local branch |
| `init` | Create a new local Git repository |
| `blame` | Show what revision and author last modified each line of a file |

## Git Cheat Sheet
A great overview of the structure of git workflows and their associated
commands is available as
[cheat sheet](https://ndpsoftware.com/git-cheatsheet.html).

To understand and practice branching with git,
[https://learngitbranching.js.org/](https://learngitbranching.js.org/)
offers an interactive tutorial.

## Generate and Upload SSH-key

`ssh-keygen -t ed25519  # omitting the type would generate an RSA key`

When being prompted for the filename, leave the default value.
Navigate to `~/.ssh/` (on Linux) resp. `/cygdrive/c/Users/[USERNAME]/.ssh`
(on Windows). Print the key to standard output via

`cat id_ed25519.pub`

Copy the key and paste it in your
GitHub (Settings → SSH and GPG keys → New SSH key) or
GitLab (Preferences → SSH Keys) profile.

## Git Hosting Platforms

* [GitHub](https://github.com)
* [GitLab](https://gitlab.com/)

## Branching Models
Which branching models is to be preferred depends on the needs of an
organization or of a development team. I generally recommend to keep things
simple. Here are some of the most prevalent models:

* [GitHub flow](https://guides.github.com/introduction/flow/)
* [GitLab flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html)
* [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
