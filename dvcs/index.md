# Distributed Version Control with Git

## Installation
Using a Debian-based Linux distribution, type

```
sudo apt install git git-gui git-cola
```

to install git and two different GUI frontends. If you're on Windows,
download `git` from [git-scm.com](https://git-scm.com/download/win) (a
portable edition is available).

## Selected Commands

| Command | Explanation |
| ------- | ---------------------------------|
| `init` | create an empty Git repository or reinitialize an existing one |
| `status` | Show the working tree status |
| `add` | Add file contents to the index |
| `commit` | Record changes to the repository |
| `push` | Update remote refs along with associated objects |
| `diff` | Show changes between commits, commit and working tree, etc |
| `log` | Show commit logs |
| `pull` | Fetch from and integrate with another repository or a local branch |
| `clone` | Clone a repository into a new directory |

An excellent overview over the available git commands is available as
[git cheatsheet](https://ndpsoftware.com/git-cheatsheet.html).

## Generate and Upload SSH-key

`ssh-keygen -t ed25519  # omitting the type leads an RSA key being generated`

Navigate to `~/.ssh/` (on Linux) resp. `/cygdrive/c/Users/[USERNAME]/.ssh`
(on Windows).

`cat id_rsa.pub`

Copy the key and paste it in your
GitHub (Settings → SSH and GPG keys → New SSH key) or
GitLab (Preferences → SSH Keys) profile.


## Branching Models
Which branching models is to be preferred depends on the needs of an
organization or of a development team. I genereally recommend to keep things
simple. Here are some of the most prevalent models:

* [GitHub flow](https://guides.github.com/introduction/flow/)
* [GitLab flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html)
* [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
