# MariaDB / MySQL Administration
When using MariaDB, one can use the `mariadb` command interchangably with
the `mysql` command. The latter is used to better fit into existing
scripts and infrastructure.

## Installing MariaDB

### Linux

```
sudo apt install mariadb-server
```

### Windows
On Windows, you can either download and use a standalone server
[https://mariadb.org/download](https://mariadb.org/download)
or use the
[XAMPP](https://sourceforge.net/projects/xampp/files/) package.

## Login
```
mysql [-h hostname]-u root -p
```

## Logout
```
exit;
```

## Database Administration

```
create database DB_NAME;
show databases;
drop database DB_NAME;
```
