### 1. Description

Table `Variables`:

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
In SQL, name is the primary key for this table.
This table contains the stored variables and their values.
```

Table `Expressions`:

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
In SQL, (left_operand, operator, right_operand) is the primary key for this table.
This table contains a boolean expression that should be evaluated.
operator is an enum that takes one of the values ('<', '>', '=')
The values of left_operand and right_operand are guaranteed to be in the Variables table.
```

Evaluate the boolean expressions in `Expressions` table.

Return the result table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Inputs**

- `Variables(name, value)` contains one uniquely named integer variable per row;
- $Expressions(\text{left}_{operand}, operator, \text{right}_{operand})$ contains uniquely identified comparisons;
- each operand references a name present in `Variables`;
- `operator` is exactly one of `<`, `>`, or `=`.

Let $V$ be the number of rows in `Variables`, and let $E$ be the number of rows in `Expressions`.

**Return value**

Return one row per expression with columns $\text{left}_{operand}$, `operator`, $\text{right}_{operand}$, and `value`. Evaluate the relation between the two referenced integers and set `value` to exactly `true` or `false`. Output order is unrestricted.

### 3. Examples

#### Example 1

```
- **Input:** 
Variables table:
+------+-------+
| name | value |
+------+-------+
| x    | 66    |
| y    | 77    |
+------+-------+
Expressions table:
+--------------+----------+---------------+
| left_operand | operator | right_operand |
+--------------+----------+---------------+
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |
+--------------+----------+---------------+
- **Output:** 
+--------------+----------+---------------+-------+
| left_operand | operator | right_operand | value |
+--------------+----------+---------------+-------+
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
+--------------+----------+---------------+-------+
- **Explanation:** As shown, you need to find the value of each boolean expression in the table using the variables table.
```
