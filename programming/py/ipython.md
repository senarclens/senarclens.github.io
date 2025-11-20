# IPython

## Enabling `autoreload` in IPython
To make working with IPython easier, you may configure it so that imported
modules are automatically reloaded whenever they change. This is extremely
handy when you're testing Python modules in `ipython` while
still modifying them in your editor.

Check if an `ipython` config file already exists:

```shell
ipython profile list
```

If no profiles exist, create one:

```shell
ipython profile create
```

Open the config file in your favorite editor:

```py
$EDITOR ~/.ipython/profile_default/ipython_config.py
```

Find the following lines. They might not yet exist. In this case, add them.

```py
c.InteractiveShellApp.extensions = []
c.InteractiveShellApp.exec_lines = []
```

Change the two lines to:

```py
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
```

