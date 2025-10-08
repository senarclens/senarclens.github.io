# Deploying Web Projects

There are very many ways of deploying web projects. One of the easiest is
to use a designated Linux-based server or virtual machine. Then, any of
the established web servers can easily be installed via `apt`. For example,
the Apache webserver is available via

```shell
sudo apt install apache2
```

Once installed, access http://localhost/ to find out more on how to configure
the server and where to deploy your files (usually `/var/www/html`).

## `mod_userdir`
The apache server allows each user on a server to host their individual web
data at, eg. https://sandbox.bulme.at/`~username`/. By
default, the data is hosted from the `public_html` subdirectory within
the user's home. If `mod_userdir` is enabled, users may deploy their content
by creating this directory and adjusting the permissions so that the web
server can access the files.

```shell
mkdir ~/public_html
chmod o+x ~
chmod 755 ~/public_html
```
For this to work, it is important that the web server can access the user's
home directory (`+x`), however, the privileges should be as limited as
possible, hence the server should only get read access (for listing files)
to `~/public_html` but not to `~`. The server must absolutely not get write
access to any files or directories within the user's home.
