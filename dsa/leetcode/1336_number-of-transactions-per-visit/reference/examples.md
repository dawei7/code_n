## Examples

**Example 1**

- **Input:** `Visits = [[1,"2020-01-01"],[2,"2020-01-02"],[12,"2020-01-01"],[19,"2020-01-03"],[1,"2020-01-02"],[2,"2020-01-03"],[1,"2020-01-04"],[7,"2020-01-11"],[9,"2020-01-25"],[8,"2020-01-28"]], Transactions = [[1,"2020-01-02",120],[2,"2020-01-03",22],[7,"2020-01-11",232],[1,"2020-01-04",7],[9,"2020-01-25",33],[9,"2020-01-25",66],[8,"2020-01-28",1],[9,"2020-01-25",99]]`

`Visits`:

| user_id | visit_date |
|---:|:---:|
| 1 | 2020-01-01 |
| 2 | 2020-01-02 |
| 12 | 2020-01-01 |
| 19 | 2020-01-03 |
| 1 | 2020-01-02 |
| 2 | 2020-01-03 |
| 1 | 2020-01-04 |
| 7 | 2020-01-11 |
| 9 | 2020-01-25 |
| 8 | 2020-01-28 |

`Transactions`:

| user_id | transaction_date | amount |
|---:|:---:|---:|
| 1 | 2020-01-02 | 120 |
| 2 | 2020-01-03 | 22 |
| 7 | 2020-01-11 | 232 |
| 1 | 2020-01-04 | 7 |
| 9 | 2020-01-25 | 33 |
| 9 | 2020-01-25 | 66 |
| 8 | 2020-01-28 | 1 |
| 9 | 2020-01-25 | 99 |

- **Output:** `[[0,4],[1,5],[2,0],[3,1]]`

Result:

| transactions_count | visits_count |
|---:|---:|
| 0 | 4 |
| 1 | 5 |
| 2 | 0 |
| 3 | 1 |

This result table is also an accessible data equivalent of the source bar chart: its four bars have heights `4`, `5`, `0`, and `1` for transaction counts `0`, `1`, `2`, and `3`, respectively.

- **Explanation:** Visits `(1,"2020-01-01")`, `(2,"2020-01-02")`, `(12,"2020-01-01")`, and `(19,"2020-01-03")` have no transactions, so bucket `0` contains four visits. Visits `(2,"2020-01-03")`, `(7,"2020-01-11")`, `(8,"2020-01-28")`, `(1,"2020-01-02")`, and `(1,"2020-01-04")` each have one transaction, so bucket `1` contains five. No visit has two transactions, but bucket `2` is still required with zero visits. Visit `(9,"2020-01-25")` has three transactions, so bucket `3` contains one. No visit has four or more transactions, so the sequence stops at `3`.
