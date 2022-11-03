# OpenSSH Server

## Installation
Make sure your apt package repository is up to date, then install the
ssh client and server.

```
sudo apt update
sudo apt install ssh
```

## Server Status
You can check if the SSH server is currently running and if it will
automatically starts on boot with the following command:

```
sudo systemctl status ssh
```

The server will start on boot if it is marked as `enabled` in the `Loaded:`
line of the output. It is currently running if it is marked as
`active (running)` in the `Active:` line of the output.

## Start the Server

```
sudo systemctl start ssh
```

## Stop the Server

```
sudo systemctl stop ssh
```

## Enabled / Disable Server on Boot
To start the SSH server automatically on system boot, run

```
sudo systemctl enable ssh
```

Remove the SSH service from the system startup by running
```
sudo systemctl disable ssh
```
