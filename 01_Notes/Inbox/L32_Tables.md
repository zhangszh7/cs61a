# Lecture 32: Tables

## Join
Joins are expressed in SQL by separating table names by **commas** in the from clause of a select statement.

If A has m rows and B has n rows, A, B will have m*n rows.

**alias and dot expression**:
`select a.class b.name from parent as a, parent as b`

## Expression

numerical expression
string expression: string values can be combined(`select "hello," || "world"`)