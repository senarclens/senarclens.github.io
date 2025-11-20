### Configure autoreload in IPython
If you want to make working with IPython much easier, you can configure it so that imported modules are automatically reloaded whenever they change. This is extremely handy when you're testing locally written Python code in IPython while editing the same code in a second window (e.g., your editor).

Check if a config file for IPython already exists:
```
ls ~/.ipython/profile_default/ipython_config.py
```

If it doesn't, create it:
```
ipython profile create
```

Open the config file in your favorite editor:
```
$EDITOR ~/.ipython/profile_default/ipython_config.py
```

Find the following lines. They might not yet exist. In this case, add them.
```
c.InteractiveShellApp.extensions = []
c.InteractiveShellApp.exec_lines = []
```

Change the two lines to:
```
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
```
