## Examples

**Example 1**

- **Input:** `Salary = [[1,1,9000,"2017/03/31"],[2,2,6000,"2017/03/31"],[3,3,10000,"2017/03/31"],[4,1,7000,"2017/02/28"],[5,2,6000,"2017/02/28"],[6,3,8000,"2017/02/28"]], Employee = [[1,1],[2,2],[3,2]]`

Salary:

| id | employee_id | amount | pay_date |
|---:|---:|---:|---|
| 1 | 1 | 9000 | 2017/03/31 |
| 2 | 2 | 6000 | 2017/03/31 |
| 3 | 3 | 10000 | 2017/03/31 |
| 4 | 1 | 7000 | 2017/02/28 |
| 5 | 2 | 6000 | 2017/02/28 |
| 6 | 3 | 8000 | 2017/02/28 |

Employee:

| employee_id | department_id |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 2 |

- **Output:** `[["2017-02",1,"same"],["2017-03",1,"higher"],["2017-02",2,"same"],["2017-03",2,"lower"]]`

| pay_month | department_id | comparison |
|---|---:|---|
| 2017-02 | 1 | same |
| 2017-03 | 1 | higher |
| 2017-02 | 2 | same |
| 2017-03 | 2 | lower |

- **Explanation:** In March, the company average is $(9000+6000+10000)/3=8333.33\ldots$. Department 1 has one payment of `9000`, so it is `higher`; department 2 averages $(6000+10000)/2=8000$, so it is `lower`. In February, the company average is `7000`, department 1's average is `7000`, and department 2 averages $(6000+8000)/2=7000`, so both departments are `same`.
