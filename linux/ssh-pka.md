# SSH Public Key Authentication

Public key authentication (PKA) is a mechanism that provides

1. improved security via two factor authentication and
2. better ease of use

when logging tools like `ssh`, `scp` and `sftp`. Security is improved as
PKA requires you to both own the correct private key (1st factor) and the
private key's password. Usability is better as it is possible to set up
`ssh-agent` to hold private keys used for PKA.

## Creating a Public/Private Key Pair

To create a new (ed25519) key, type

```shell
ssh-keygen -t ed25519
```

During the creation, you will be asked to enter a password for the key.
Note that when you type this password, nothing will be echoed to `stdout`
for security reasons (no asterisk characters). The output you'll see is
similar to the following if successful.

```
Enter file in which to save the key (/home/$USER/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/$USER/.ssh/id_ed25519
Your public key has been saved in /home/$USER/id_ed25519.pub
The key fingerprint is:
SHA256:Od8mqEP/E/2NYkqtXsGfsCdUFNA8YBE7KB7HIoooEYI $USER@$HOST
The key's randomart image is:
+--[ED25519 256]--+
|+           *Bo. |
|E.       . o o+  |
|.     . + + o .. |
| o . . o * . o   |
|o . .   S  .=    |
|.     .  +.+.= . |
|     . .. +.B.+o |
|      .....=ooo .|
|      .. o=+ .   |
+----[SHA256]-----+
```

Once the keypair is created, you can start using it.

## Installing a Public Key on a Server
To move your public key to an ssh server, use the `ssh-copy-id` tool. For
example, after having [configured your connection](ssh-config.md), type

```shell
ssh-copy-id sandbox
```

You'll have to enter your user's password on the target server. After this
step, you will be able to log in to the server using PKA. As soon as you
type

```shell
ssh sandbox
```
you'll have to enter your key's password instead of your user password.
This improved overall security, but didn't make logging in easier.

## Using `ssh-agent`
The `ssh-agent` tool holds your private keys. You can store
your ssh identities in this authentication agent to avoid having to type
they key password upon every remote login. When using an X window session,
it is usually enough to issue

```shell
ssh-add
```

This will prompt for your private key's password. Afterwards, you'll be
able to use that private key without entering any password. You can hence
log in to or use `scp` and `sshfs` as you desire without entering a password.
This will work for all servers having received your public key via
`ssh-copy-id` as outlined above.

### Using `ssh-agent` on a Server
On Linux clients with a desktop environment, `ssh-agent` is usually
automatically started when the user logs in. This happens eg. in
`/etc/X11/Xsession.d/90x11-common_ssh-agent` or a similar script.

On systems without X11, the agent is usually not automatically started when
logging in. In such cases, the user can start the agent via

```shell
eval `ssh-agent`
```

Make sure to run the command exactly as above so that the output will be
executed as well. This is done to export required environment variables.

After the agent has been started with the above command, `ssh-add` should
work as expected.

Finally, make sure to terminate the agent when you log out:

```shell
kill $SSH_AGENT_PID
```

To avoid forgetting this, you can add this command to your shell's logout
script (eg. `.bash_logout` when using the bash shell).
