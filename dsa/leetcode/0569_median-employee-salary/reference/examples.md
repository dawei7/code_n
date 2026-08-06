## Examples

**Example 1**

- **Input:** `Employee = [[1,"A",2341],[2,"A",341],[3,"A",15],[4,"A",15314],[5,"A",451],[6,"A",513],[7,"B",15],[8,"B",13],[9,"B",1154],[10,"B",1345],[11,"B",1221],[12,"B",234],[13,"C",2345],[14,"C",2645],[15,"C",2645],[16,"C",2652],[17,"C",65]]`

| id | company | salary |
|---:|---|---:|
| 1 | A | 2341 |
| 2 | A | 341 |
| 3 | A | 15 |
| 4 | A | 15314 |
| 5 | A | 451 |
| 6 | A | 513 |
| 7 | B | 15 |
| 8 | B | 13 |
| 9 | B | 1154 |
| 10 | B | 1345 |
| 11 | B | 1221 |
| 12 | B | 234 |
| 13 | C | 2345 |
| 14 | C | 2645 |
| 15 | C | 2645 |
| 16 | C | 2652 |
| 17 | C | 65 |

- **Output:** `[[5,"A",451],[6,"A",513],[12,"B",234],[9,"B",1154],[14,"C",2645]]`

| id | company | salary |
|---:|---|---:|
| 5 | A | 451 |
| 6 | A | 513 |
| 12 | B | 234 |
| 9 | B | 1154 |
| 14 | C | 2645 |

- **Explanation:** Company A has six employees, so its third and fourth rows after sorting are both selected:

| id | company | salary |
|---:|---|---:|
| 3 | A | 15 |
| 2 | A | 341 |
| **5** | **A** | **451** |
| **6** | **A** | **513** |
| 1 | A | 2341 |
| 4 | A | 15314 |

The source's company-B walkthrough is displayed in the following row order and marks its third and fourth displayed rows:

| id | company | salary |
|---:|---|---:|
| 8 | B | 13 |
| 7 | B | 15 |
| **12** | **B** | **234** |
| **11** | **B** | **1221** |
| 9 | B | 1154 |
| 10 | B | 1345 |

That displayed walkthrough has an internal ordering inconsistency: `1154` must precede `1221` under the stated ascending-salary rule. Correctly ordered, the third and fourth rows are employee `12` at salary `234` and employee `9` at salary `1154`, which are the two company-B rows in the official output.

Company C has five employees. Its third row is employee `14`; employee `15` has the same salary but follows it because ties are broken by `id`:

| id | company | salary |
|---:|---|---:|
| 17 | C | 65 |
| 13 | C | 2345 |
| **14** | **C** | **2645** |
| 15 | C | 2645 |
| 16 | C | 2652 |
