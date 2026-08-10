<!-- Don't delete this -->

# Solution

---

## pandas

### Approach: Group By and Count Distinct

#### Intuition

In pandas, we can use the groupby function on the $'\text{teacher}_{id}'$ column and then count the unique $'\text{subject}_{id}'$ per teacher using the `.nunique()` function.

#### Algorithm

To calculate the number of unique subjects each teacher teaches in the university, we first need to group by $'\text{teacher}_{id}'$ and then count the number of unique $'\text{subject}_{id}'$. The renaming of the column is done for the output to match the required format (similar to the `AS` keyword in SQL).
Note that we need to specify `axis=1` for it, as we are renaming a column and not a row.

Here is an example to help solidify the intuition behind the algorithm:

The original table `teacher`:

<table>
    <tr>
        <th>teacher_id</th>
        <th>subject_id</th>
        <th>dept_id</th>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>2</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>3</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
        <td>1</td>
    </tr>
</table>

<br>

The table after grouping by $\text{teacher}_{id}$ and counting distinct $\text{subject}_{id}$:

<table>
    <tr>
        <th>teacher_id</th>
        <th>cnt</th>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
    </tr>
</table>

#### Implementation

```python
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(["teacher_id"])["subject_id"].nunique().reset_index()
    df = df.rename({'subject_id': "cnt"}, axis=1)
    return df
```

<br>

---

## Database

### Approach: Group By and Count Distinct

#### Intuition

In SQL, the query to count the number of unique subjects each teacher teaches involves grouping by the $\text{teacher}_{id}$ and then counting the distinct $\text{subject}_{id}$.

#### Algorithm

This task requires counting the number of unique subjects each teacher teaches in the university. This implies that we have to group by the teacher_id and then count the distinct subject_id.

Here is an example to help solidify the intuition behind the algorithm:

The original table `teacher`:

<table>
    <tr>
        <th>teacher_id</th>
        <th>subject_id</th>
        <th>dept_id</th>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>2</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>3</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
        <td>1</td>
    </tr>
</table>

<br>

The table after grouping by $\text{teacher}_{id}$ and counting distinct $\text{subject}_{id}$:

<table>
    <tr>
        <th>teacher_id</th>
        <th>cnt</th>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
    </tr>
</table>

#### Implementation

```sql
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```