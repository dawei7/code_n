### 1. Description

You are given a **0-indexed** 2D integer array `questions` where $\text{questions}[i] = [\text{points}_{i}, \text{brainpower}_{i}]$.

The array describes the questions of an exam, where you have to process the questions **in order** (i.e., starting from question `0`) and make a decision whether to **solve** or **skip** each question. Solving question `i` will **earn** you $\text{points}_{i}$ points but you will be **unable** to solve each of the next $\text{brainpower}_{i}$ questions. If you skip question `i`, you get to make the decision on the next question.

- For example, given $questions = [[3, 2], [4, 3], [4, 4], [2, 5]]$:

		- If question `0` is solved, you will earn `3` points but you will be unable to solve questions `1` and `2`.

- If instead, question `0` is skipped and question `1` is solved, you will earn `4` points but you will be unable to solve questions `2` and `3`.

Return *the **maximum** points you can earn for the exam*.

### 2. Function Contract

**Inputs**

- `questions`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $questions = [[3,2],[4,3],[4,4],[2,5]]$
- **Output:** `5`
- **Explanation:** The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

#### Example 2

- **Input:** $questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]$
- **Output:** `7`
- **Explanation:** The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.

### 4. Constraints

- $1 \le \text{questions.length} \le 10^{5}$

- $\text{questions}[i].length = 2$

- $1 \le \text{points}_{i}, \text{brainpower}_{i} \le 10^{5}$
