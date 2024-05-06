# Create, read, update and delete

Create, read, update, and delete (CRUD) are the four basic operations of
persistent storage. The major operations which are implemented by databases
are also referred to as CRUD. Each letter in the acronym can be mapped to a
standard SQL statement.

| CRUD   | MariaDB SQL     | PostgreSQL       | SQLite          | REST API |
| ------ | --------------- | ---------------- | --------------- | -------- |
| create | [`insert`][m_i] | [`insert`][pg_i] | [`insert`][l_i] | `post`   |
| read   | [`select`][m_s] | [`select`][pg_s] | [`select`][l_s] | `get`    |
| update | [`update`][m_u] | [`update`][pg_u] | [`update`][l_u] | `put`    |
| delete | [`delete`][m_d] | [`delete`][pg_d] | [`delete`][l_d] | `delete` |


[m_i]: https://mariadb.com/kb/en/insert/
[m_s]: https://mariadb.com/kb/en/select/ 
[m_u]: https://mariadb.com/kb/en/update/
[m_d]: https://mariadb.com/kb/en/delete/ 
[pg_i]: https://www.postgresql.org/docs/current/sql-insert.html
[pg_s]: https://www.postgresql.org/docs/current/sql-select.html
[pg_u]: https://www.postgresql.org/docs/current/sql-update.html
[pg_d]: https://www.postgresql.org/docs/current/sql-delete.html
[l_i]: https://www.sqlite.org/lang_insert.html
[l_s]: https://www.sqlite.org/lang_select.html
[l_u]: https://www.sqlite.org/lang_update.html
[l_d]: https://www.sqlite.org/lang_delete.html
