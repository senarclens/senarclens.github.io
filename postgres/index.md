# Introduction to PostgreSQL
{::options toc_levels="2..6" /}

## Contents
{:.no_toc}

* A markdown (kramdown) generated TOC.
{:toc}

## psql

### Basic Commands

Connect to a database from the command-line use

```
$ psql --user $USER --database $YOUR_DB
```

In the `psql` shell, you have access to a series of special commands.

`\c dbname`
: Connect to given database.

`\d name`
Describe table, view, sequence, or index.

`\dn`
: List schemas available in current database.

`\dt schema.`
: List relations in schema.

`\h sql_command`
: Get help for given SQL command.

`\l`
: List availables databases.

`\?`
: Get help for available psql commands (`\` commands)

`\! shell_command`
: Execute the given command in the operating system's shell.

### Configuration
In order to avoid typing too many parameters when launching `psql` from the
command line, you can configure default values. By all means, I strongly
recommend not to store your password without second thoughts.
For storing defaults, there are three options.
The first is the use of environment variables.

```shell
export PGHOST=localhost
export PGPORT=5433
export PGUSER=...
export PGPASSWORD=...
export PGDATABASE=...
```

Alternatively, you could use a `.pgpass` file using the following format.

```
localhost:5433:databasename:username:password
```

Finally, you can use the `.pg_service.conf` file which uses an ini like format.

```ini
[example]
host=localhost
port=5432
dbname=...
user=...
password=...
```

## SQL

### Self Joins
Reasons for joining a table onto itself include
* a table includes a hierarchy (eg. employees reporting to other employees)
* finding similarities in a column (eg. employees with the same birthday)

### Using
The `USING` keyword allows to join two tables on a set of columns that share the
exact same names. It is used as a shorthand notation for the slightly more
verbose and flexible `ON`.

The syntax is
```sql
-- ...
JOIN other_table USING (col1)
```
where `col1` is the column on which you want to join.

### Natural
The 'NATURAL` keyword is essentially a shorthand for `USING`. It joins two
subsequent tables together on all the columns which have the same names in
both tables. Hence
* order matters
* be careful if multiple column names are identical

The syntax is
```sql
-- ...
NATURAL JOIN other_table
```
