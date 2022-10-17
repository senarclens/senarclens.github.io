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
Depending on the version and installation settings, logging in to the
freshly installed database server can be done with either of the following
```bash
mysql [-h hostname] -u root -p
sudo mysql  # if the above does not work
```

## Logout
```
exit;
```

## Database Administration

```sql
create database $DB_NAME;
show databases;
use $DB_NAME;  -- start working with this database
drop database $DB_NAME;
```

## User Administration
```sql
create user '$USER'@'localhost' identified by '$PASSWORD';
grant all privileges on $DB_NAME.* to '$USER'@'localhost';
```

## Table Administration
After logging in and selecting a database, one can create, change and
remove database relations (tables).

```sql
create table $TABLE_NAME (
  -- column definitions
);
show tables;
describe table $TABLE_NAME;
alter table $TABLE_NAME ...;
drop table $TABLE_NAME;
```
More information on
* [data types](https://mariadb.com/kb/en/data-types/)
* [create table](https://mariadb.com/kb/en/create-table/)
* [alter table](https://mariadb.com/kb/en/alter-table/)

A comprehensive example can be found on
[Wikiversity](https://en.wikiversity.org/wiki/Database_Examples).
