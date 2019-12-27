# Introduction to PostgreSQL
{::options toc_levels="2..6" /}

## Contents
{:.no_toc}

* A markdown (kramdown) generated TOC.
{:toc}

## Basic Commands

Connect to a database from the command-line use

```
$ psql --user $USER --database $YOUR_DB
```

In the `psql` shell, you have access to a series of special commands.

`\\c dbname`
: Connect to given database.

`\\l`
: List availables databases.

`\\h sql_command`
: Get help for given SQL command.
