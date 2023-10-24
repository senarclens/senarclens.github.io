# PostgreSQL Administration
{::options toc_levels="2..6" /}

Administrative tasks in PostgreSQL are usually performed using the designated
`postgres` operating system user.

PostgreSQL provides a series of convenience
scripts written in Perl to perform the tasks directly from the operating
system shell.


## Adding and Changing Users
To create a user, use the `createuser` command.

```shell
sudo -u postgres createuser ${USER} [--pwprompt]
```

To create or change a user's password, log in to the database and execute
the sql `alter ROLE` statement. In addition, one can grant or revoke a series
of permissions on the role.

```sql
ALTER ROLE ${USER} WITH LOGIN PASSWORD ${password} NOSUPERUSER INHERIT
NOCREATEDB NOCREATEROLE NOREPLICATION VALID UNTIL 'infinity';
```

## Create a Database
To create a database, use the `createdb` command.

```shell
sudo -u postgres createdb ${DBNAME} --owner=${USER} [-E UNICODE]
```
