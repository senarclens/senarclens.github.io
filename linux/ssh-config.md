# SSH Client Configuration

When logging in to a server, one has to provide the (username unless the
username on the server is the same as on the current system). In addition,
the fully qualified domain name has to be provided. In order to simplify
the process of logging in, it is possible to write a configuration.

For example, it is possible log in to `sandbox` via

```shell
ssh sandbox
```

instead of the much more verbose

```shell
ssh firstname.lastname@sandbox.bulme.at
```

To set this up, edit (create if it doesn't exist) the file
`~/.ssh/config` and append the following

```ssh-config
Host sandbox
  HostName sandbox.bulme.at
  User firstname.lastname
```

Right after saving the file it will be possible to use

```shell
ssh sandbox
```

to log in to the newly configured server. It is possible to configure many
additional parameters and multiple servers in this configuration file.
See `man ssh_config` for more information.
