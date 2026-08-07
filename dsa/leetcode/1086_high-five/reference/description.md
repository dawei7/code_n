### 1. Description

Given a list of the scores of different students, `items`, where $\text{items}[i] = [\text{ID}_{i}, \text{score}_{i}]$ represents one score from a student with $\text{ID}_{i}$, calculate each student's **top five average**.

Return *the answer as an array of pairs *`result`*, where *$\text{result}[j] = [\text{ID}_{j}, \text{topFiveAverage}_{j}]$* represents the student with *$\text{ID}_{j}$* and their **top five average**. Sort *`result`* by *$\text{ID}_{j}$* in **increasing order**.*

A student's **top five average** is calculated by taking the sum of their top five scores and dividing it by `5` using **integer division**.

### 2. Function Contract

**Input**

- `items`: an array of pairs $[\text{student}_{id}, score]$.

Let $N$ be the number of score records and $S$ the number of distinct student identifiers. Every represented student has at least five records, and repeated score values are separate records.

**Return value**

- One row $[\text{student}_{id}, average]$ for every distinct student.
- `average` is the integer quotient obtained by summing that student's five highest scores and dividing by `5`.
- Rows are ordered by $\text{student}_{id}$ in increasing order.

### 3. Examples

#### Example 1

- **Input:** $items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]$
- **Output:** `[[1,87],[2,88]]`
- **Explanation:**
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
#### Example 2

- **Input:** $items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]$
- **Output:** `[[1,100],[7,100]]`

### 4. Constraints

- $1 \le \text{items.length} \le 1000$

- $\text{items}[i].length = 2$

- $1 \le \text{ID}_{i} \le 1000$

- $0 \le \text{score}_{i} \le 100$

- For each $\text{ID}_{i}$, there will be **at least** five scores.