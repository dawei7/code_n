<!-- Don't delete this -->
[TOC]

# Solution

---

## pandas

<!-- h3 for approaches -->
### Approach: Conditional Index, .groupby().sum(), and .merge()

<!-- h4 for sections -->
#### Intuition
In this problem, we are tasked with finding the IDs of the candidates in any order given the following criteria:
- candidates who have **at least two** years of experience
- the sum of the score of candidate's interview rounds is **strictly greater than** `15`

We are given 2 DataFrames:
- `candidates` representing the interview candidates, years of experience and interview id
- `rounds` representing the interview id, interview round and score for the interview round

Here are the DataFrames with data given to us:

`candidates`:
| candidate_id | name    | years_of_exp | interview_id |
|--------------|---------|--------------|--------------|
| 11           | Atticus | 1            | 101          |
| 9            | Ruben   | 6            | 104          |
| 6            | Aliza   | 10           | 109          |
| 8            | Alfredo | 0            | 107          |
<br>

`rounds`:
| interview_id | round_id | score |
|--------------|----------|-------|
| 109          | 3        | 4     |
| 101          | 2        | 8     |
| 109          | 4        | 1     |
| 107          | 1        | 3     |
| 104          | 3        | 6     |
| 109          | 1        | 4     |
| 104          | 4        | 7     |
| 104          | 1        | 2     |
| 109          | 2        | 1     |
| 104          | 2        | 7     |
| 107          | 2        | 3     |
| 101          | 1        | 8     |
<br>

<!-- Describe your approach to solving the problem. -->
One way to solve this problem is to use a conditional index to filter candidates based on the criteria, using `.groupby().sum()` on scores in `rounds` and then joining the two tables together with an inner merge.

1. `candidates` - Conditional index given `years_of_exp` is at least 2
We will start by filtering `candidates` for candidates that have at least 2 `years_of_exp`. This will fulfill criteria number one.

```python
candidates = candidates[candidates['years_of_exp'] >= 2]
```

Here is our `candidates` dataframe after the conditional filter:

| candidate_id | name    | years_of_exp | interview_id |
|--------------|---------|--------------|--------------|
| 9            | Ruben   | 6            | 104          |
| 6            | Aliza   | 10           | 109          |
<br>

2. `rounds` - `.groupby().sum()` and conditional index
Next, we will need to aggregates the scores for each interview. To achieve this, we will utilize the `.groupby().sum()` method, grouping by $\text{interview}_{id}$. We will utilize the method $.\text{reset}_{index}()$ with `name={column name}` to rename the sized column. In this case, we will use $name='\text{total}_{score}'$.

After grouping the interviews and getting the summed scores for each, we will filter the DataFrame for $\text{total}_{score}$s that are strictly over 15. This will fulfill our second criteria.

```python
rounds = rounds.groupby('interview_id')['score'].sum().reset_index(name='total_score')
rounds = rounds[rounds['total_score'] > 15]
```

Here is the `rounds` DataFrame:

|interview_id |total_score |
|-------------|------------|
|101          |16          |
|104          |22          |
<br>

3. `result` - Inner `.merge()`
Finally, after filtering the `candidates` DataFrame and `rounds` DataFrame, we will utilize the method `.merge()`, passing in `how='inner'` as a parameter to intersect on $\text{interview}_{id}$, which will create a DataFrame containing only rows that fulfill both criteria:
- candidates who have **at least two** years of experience
- the sum of the score of candidate's interview rounds is **strictly greater than** `15`

```python
result = candidates.merge(rounds, how='inner', on='interview_id')
```

Here is the resulting DataFrame `result` and completed code:

| candidate_id |
| ------------ |
| 9            |
<br>

<!-- h4 for sections -->
#### Implementation

```python
import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    # Approach: Conditional Index, Groupby Sum, inner merge
    # Filtering candidates who have at least two YoE
    candidates = candidates[candidates['years_of_exp'] >= 2]

    # .groupby('interview_id')['score'].sum(), filter for > 15
    rounds = rounds.groupby('interview_id')['score'].sum().reset_index(name='total_score')
    rounds = rounds[rounds['total_score'] > 15]

    # Inner merge on `interview_id`, rounds onto candidates
    result = candidates.merge(rounds, how='inner', on='interview_id')

    # Return `candidate_id`
    return result[['candidate_id']]

```

<br>

---

## Database

<!-- h3 for approaches -->
### Approach: INNER JOIN, WHERE, and GROUP BY ... HAVING

<!-- h4 for sections -->
#### Intuition
We are tasked with reporting the candidates in any order given these criteria:
- candidates who have **at least two** years of experience
- the sum of the score of candidate's interview rounds is **strictly greater than** `15`

<!-- Describe your approach to solving the problem. -->
1. `INNER JOIN`
We will start our query by utilizing `INNER JOIN` to join `Rounds` onto `Candidates` given matching $\text{interview}_{id}$.

```sql
FROM
    Candidates AS c
INNER JOIN
    Rounds AS r
ON
    c.interview_id = r.interview_id
```

2. `WHERE` - filtering `years_of_exp`
Next, we will filter candidates given their `years_of_exp` by utilizing the `WHERE` clause, which will fulfill our first criteria.

```sql
WHERE
    c.years_of_exp >= 2
```

3. `GROUP BY ... HAVING`
After filtering the table for candidates with `years_of_exp` greater than or equal to 2, we will utilize the `GROUP BY ... HAVING` clause to aggregate the interviews by score. This is achieved by grouping the $\text{candidate}_{id}$s and passing `SUM(Rounds.score) > 15` into the `HAVING` clause. This will fulfill our second criteria.

```sql
GROUP BY
    c.candidate_id
HAVING
    SUM(r.score) > 15;
```

Finally, we are able to `SELECT` the $\text{candidate}_{id}$.

Here is the resulting output and completed code:

| candidate_id |
| ------------ |
| 9            |

<br>

<!-- h4 for sections -->
#### Implementation

```mysql []
SELECT
    c.candidate_id
FROM
    Candidates AS c
INNER JOIN
    Rounds AS r
ON
    c.interview_id = r.interview_id
WHERE
    c.years_of_exp >= 2
GROUP BY
    c.candidate_id
HAVING
    SUM(r.score) > 15;
```

<!-- an empty line to separate approaches -->
<br>