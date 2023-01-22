# Using SSH to Work With Remote Files

Files can be copied securely back and forth between computers using the `scp`
command.

```
scp source ... target
```

Both the `source` and the `target` can be local or remote. It is hence possible
to copy files
* from your computer to a remote computer
* from a remote computer to your computer or
* directly between two remote computers.

For remote files, the hostname and location on the filesystem are separated
by appending a colon (`:`) after the hostname. To copy, for example, the
file `a_file` from the current directory to the directory
`/home/user/location/a_file`, one needs to issue

```bash
scp a_file user@host.example.com:/home/user/location/a_file
```

If the path on a remote system is omitted, the file will be copied to the
user's home directory. For example, to copy `a_file` to the user's home
directory on the remote host, type

```bash
scp a_file user@host.example.com:
```

To copy an entire directory from the current computer, the `-r` flag is
required. To copy the local folder `images/` to the existing folder
`~/public_html/` on the remote host, type

```bash
scp -r images user@host.example.com:public_html
```

## SSHFS
SSHFS allows to mount a remote filesystem using SSH's SFTP subsystem.
This means you can access the files the same way you can access local files.

```
sshfs [user@]host:[dir] mountpoint [options]
```

This way, remote files can be edited with any editor or IDE on your local
computer. However, compile the files only remotely via SSH to avoid a lot of
unnecessary network traffic.

The desired mountpoint must be an existing directory. To mount, for example,
your entire home directory from `sandbox.bulme.at` to the local directory
`sandbox`, type
```
mkdir sandbox
sshfs user@sandbox.bulme.at: sandbox
```

After a remote filesystem has been mounted, it can be unmounted using the
`umount` command (note the missing `n` after the `u`). To unmount the 
connection to sandbox created above, type
```
umount sandbox
```
