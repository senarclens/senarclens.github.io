# Bug Tracker

Many large software projects use software designated to keeping track of the
problems and issues in their code. Such programs are generally referred to as
**bug trackers** or **issue trackers**. These tools are also used for
planning future features and releases. In addition, there may
even be legal requirements dictating the use of such software.

In agile software develoopment, there are also good reasons not to use
such tools as they create additional overhead. One of their key advantages
is to have information on prior issues in a single place. However,
some argue that for well written and automatically tested software,
a sprint board and a product backlog are enough to keep track of issues that
need to be solved. As of the documentation on how it was solved, version
control like git lends itself well. But this documentation is only really
relevant should a bug re-occur as a regression. However, this must be
avoided by proper automated tests written before the bugfix. So wether your
team needs issue tracking software is an individual decision.

If you need such software, evaluate carefully whether it fits your
requirements. Personally, I recommend using simple processes that are
easily matched by any product. There are a series of possible tools.


## Git Hosting Services
Git hosting services like [GitHub](https://github.com/) and
[GitLab](https://gitlab.com/) both offer issue tracking and
planning tools in their free tiers with more features in their paid tiers.


## Open Source Tools
There are very many different options when it comes to open source bug
tracking tools. A small selection is

|                      | Bugzilla | Mantis |       RT | Redmine |
| -------------------- | -------- | ------ | -------- | ------- |
| License              |
| Main Language        |     Perl |    PHP |     Perl |    Ruby |
| Professional Service |   market |    yes |      yes |      no |
| Website              | [bugzilla.org][bugzilla] | [mantisbt.org][mantis] | [requesttracker.com][rt] | [redmine.org][redmine] |
| Repository           | [bugzilla][bugzilla-repo] | [mantisbt][mantis-repo] |  [rt][rt-repo] | [redmine][redmine-repo] |


[bugzilla]: https://www.bugzilla.org/ "Bugzilla"
[bugzilla-repo]: https://github.com/bugzilla/bugzilla "Bugzilla repo"
[mantis]: https://mantisbt.org/ "MantisBT"
[mantis-repo]: https://github.com/mantisbt/mantisbt "MantisBT repo"
[rt]: https://requesttracker.com/ "Request Tracker"
[rt-repo]: https://github.com/bestpractical/rt "RT repo"
[redmine]: https://www.redmine.org/ "Redmine"
[redmine-repo]: https://github.com/redmine/redmine "Redmine repo"


## Proprietary Tools
There is also an abundance of proprietary tools. Currently, the best known
closed source bug tracker is
Jira (the name is derived from Gojira, which is Japanese for Godzilla).
Its customizability is great, but also allows to keep and represent highly
inefficient business and development processes.


## Conclusion
For many projects, issue tracking software provides a valuable service.
Wikipedia offers an excellent
[comparison of issue tracking systems][comparison].

[comparison]: https://en.wikipedia.org/wiki/Comparison_of_issue-tracking_systems
