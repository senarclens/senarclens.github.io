# Git-based Programming Assignments

When accepting a programming assignment, the following workflow is required:

* copy the download URL of your assignment on your repository homepage
  (it resembles something like
  `git@github.com:HTL-Bulme/assignment-name-yourname.git`)
* clone the repository to your computer (you might have to set up
  [ssh authentication](/linux/ssh-pka.md) first and upload your public key
  to the classroom platform)  
  `git clone $YOUR_REPO_URL`
* after the above succeeds, you'll have a new directory that you have to
  enter; in this directory, you can complete the assignment
* whenever you finished coding, add your changes to the index; to see which
  files are changed, use `git status`; to add them to the index use
  `git add [...]`
* make a snapshot of your current status quo using
  `git commit -m '$YOUR_COMMIT_MESSAGE'`
* upload your new change snapshots (commits) to the classroom platform
  `git push`

For further information on using distributed version control with git, see the
[overview page on DVCs](./) or the
[git cheat sheet](https://ndpsoftware.com/git-cheatsheet.html).
