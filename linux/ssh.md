# Connecting to Linux Using SSH

To connect to a remote Linux computer that offers an `ssh` server, use

```
ssh firstname.lastname@sandbox.bulme.at  # use your domain
```

## Downloading Data

To download files to your user account on the remote machine, one can use
the `wget` command with the url to download. For example

```
wget https://github.com/HTL-Bulme/c_free_store/archive/refs/heads/main.zip
```

To extract files, use the appropriate commands depending on the type of
archive. For example

```
unzip main.zip
tar xf main.tar.gz
```

## Editing Files

There are many text editors available on the Linux shell. These include
GNU `nano`, `vi`, `vim`, `emacs` and `jed`. To edit a file, type the name of
the editor followed by the name of the file. For example

```
nano infile.c
```
