# Joins

## Self Joins
Reasons for joining a table onto itself include
* a table includes a hierarchy (eg. employees reporting to other employees)
* finding similarities in a column (eg. employees with the same birthday)

## Using
The `USING` keyword allows to join two tables on a set of columns that share the
exact same names. It is used as a shorthand notation for the slightly more
verbose and flexible `ON`.

The syntax is
```sql
-- ...
JOIN other_table USING (col1)
```
where `col1` is the column on which you want to join.

## Natural
The `NATURAL` keyword is essentially a shorthand for `USING`. It joins two
subsequent tables together on all the columns which have the same names in
both tables. Hence
* order matters
* be careful if multiple column names are identical

The syntax is
```sql
-- ...
NATURAL JOIN other_table
```
