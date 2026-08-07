[TOC]

# Solution

---

## pandas

### Approach: Sort and Drop Duplicates

#### Algorithm
Because the salary for each employee is assumed to be increasing every year, we can first sorted the values based on `salary` using descending order. The pandas code and the sample result for this step is shown as follows.

```python
df = salary.sort_values(by = 'salary', ascending = False)
```

| emp_id | firstname | lastname | salary  | department_id |
|--------|-----------|----------|---------|---------------|
| 4      | Patricia  | Powell   | 170000  | D1004         |
| 4      | Patricia  | Powell   | 162825  | D1004         |
| 2      | Justin    | Simon    | 130000  | D1005         |
| 2      | Justin    | Simon    | 128922  | D1005         |
| 1      | Todd      | Wilson   | 110000  | D1006         |
| 1      | Todd      | Wilson   | 106119  | D1006         |
| 6      | Natasha   | Swanson  | 90000   | D1005         |
| 6      | Natasha   | Swanson  | 79632   | D1005         |
| 5      | Sherry    | Golden   | 44101   | D1002         |
| 3      | Kelly     | Rosario  | 42689   | D1002         |

<br>

After this step, we can see that, if we go from the first line and drop the duplicates if the $\text{emp}_{id}$ is already seen, then will keep only one record for each employee and the salary is guarantee to be the highest (because we already sort the data based on salary).

```python
df = df.drop_duplicates(subset = 'emp_id')
```

| emp_id | firstname | lastname | salary  | department_id |
|--------|-----------|----------|---------|---------------|
| 4      | Patricia  | Powell   | 170000  | D1004         |
| 2      | Justin    | Simon    | 130000  | D1005         |
| 1      | Todd      | Wilson   | 110000  | D1006         |
| 6      | Natasha   | Swanson  | 90000   | D1005         |
| 5      | Sherry    | Golden   | 44101   | D1002         |
| 3      | Kelly     | Rosario  | 42689   | D1002         |

<br>

Finally, we sort the data frame based on $\text{emp}_{id}$ and return it.

#### Implementation

```python
def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    df = salary.sort_values(by = 'salary', ascending = False)
    df = df.drop_duplicates(subset = 'emp_id')
    return df.sort_values(by = 'emp_id')
```

<br>
------

## Database

### Approach: Group By and use MAX function

#### Algorithm
In SQL, we can group the data using `group by` based on $\text{emp}_{id}$ clause and use `MAX` aggregate function to find the latest salary.

In addition, because we need to return the result in ascending order of $\text{emp}_{id}$, we also use the `order by` clause for the $\text{emp}_{id}$ column. Note that the `order by` sorts the values in ascending order by default, which is exactly what we want.

#### Implementation

###### MySQL

```mysql []
SELECT
  emp_id,
  firstname,
  lastname,
  MAX(salary) AS salary,
  department_id
FROM
  Salary
GROUP BY
  emp_id
ORDER BY
  emp_id;
```

###### PostgreSQL

```sql
SELECT
  emp_id,
  firstname,
  lastname,
  MAX(salary) AS salary,
  department_id
FROM
  Salary
GROUP BY
  emp_id,
  firstname,
  lastname,
  department_id
ORDER BY
  emp_id;
```