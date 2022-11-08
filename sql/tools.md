# SQL Tools

When working with PostgreSQL, [pgAdmin](https://www.pgadmin.org/) is a great
tool to interact with your database. It is free software and available
for [download](https://www.pgadmin.org/download/) on all major platforms.

For SQLite, [DB Browser for SQLite (DB4S)](https://sqlitebrowser.org/) is
a great GUI. It is free software and available for
[download](https://sqlitebrowser.org/dl/) on all major platforms, including
a portable version. In Linux, DB4S is available in the package manager
```
sudo apt install sqlitebrowser
```

For all other DBMS (including PostgreSQL and SQLite),
[DBeaver Community](https://dbeaver.io/) is an excellent choice as well.
It is free software (ALv2) and available for
[download](https://dbeaver.io/download/) on all major platforms, including
a portable version. In Linux, it can be installed via the package manager
```
curl -fsSL https://dbeaver.io/debs/dbeaver.gpg.key \
  | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/dbeaver.gpg
echo "deb https://dbeaver.io/debs/dbeaver-ce /" \
  | sudo tee /etc/apt/sources.list.d/dbeaver.list
```
