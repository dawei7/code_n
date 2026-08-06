## Examples

**Example 1**

- **Input:** `Salaries = [[1,1,"Tony",2000],[1,2,"Pronub",21300],[1,3,"Tyrrox",10800],[2,1,"Pam",300],[2,7,"Bassem",450],[2,9,"Hermione",700],[3,7,"Bocaben",100],[3,2,"Ognjen",2200],[3,13,"Nyancat",3300],[3,15,"Morninngcat",7777]]`

| company_id | employee_id | employee_name | salary |
|---:|---:|---|---:|
| 1 | 1 | `Tony` | 2000 |
| 1 | 2 | `Pronub` | 21300 |
| 1 | 3 | `Tyrrox` | 10800 |
| 2 | 1 | `Pam` | 300 |
| 2 | 7 | `Bassem` | 450 |
| 2 | 9 | `Hermione` | 700 |
| 3 | 7 | `Bocaben` | 100 |
| 3 | 2 | `Ognjen` | 2200 |
| 3 | 13 | `Nyancat` | 3300 |
| 3 | 15 | `Morninngcat` | 7777 |

- **Output:** `[[1,1,"Tony",1020],[1,2,"Pronub",10863],[1,3,"Tyrrox",5508],[2,1,"Pam",300],[2,7,"Bassem",450],[2,9,"Hermione",700],[3,7,"Bocaben",76],[3,2,"Ognjen",1672],[3,13,"Nyancat",2508],[3,15,"Morninngcat",5911]]`

| company_id | employee_id | employee_name | salary |
|---:|---:|---|---:|
| 1 | 1 | `Tony` | 1020 |
| 1 | 2 | `Pronub` | 10863 |
| 1 | 3 | `Tyrrox` | 5508 |
| 2 | 1 | `Pam` | 300 |
| 2 | 7 | `Bassem` | 450 |
| 2 | 9 | `Hermione` | 700 |
| 3 | 7 | `Bocaben` | 76 |
| 3 | 2 | `Ognjen` | 1672 |
| 3 | 13 | `Nyancat` | 2508 |
| 3 | 15 | `Morninngcat` | 5911 |

- **Explanation:** Company `1` has maximum salary `21300`, so all its employees
  are taxed at $49\%$. Company `2` has maximum salary `700`, so its tax rate is
  $0\%$. Company `3` has maximum salary `7777`, placing all its employees in
  the $24\%$ bracket. In general, the adjusted salary is the original salary
  minus the selected percentage of that salary. For example, Morninngcat's
  result is $7777-7777\cdot(24/100)=5910.52$, which rounds to $5911$.
