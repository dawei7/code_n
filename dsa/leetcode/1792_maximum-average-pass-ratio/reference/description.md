### 1. Description

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where $\text{classes}[i] = [\text{pass}_{i}, \text{total}_{i}]$. You know beforehand that in the $$i^{\text{th}}$$ class, there are $\text{total}_{i}$ total students, but only $\text{pass}_{i}$ number of students will pass the exam.

You are also given an integer `extraStudents`. There are another `extraStudents` brilliant students that are **guaranteed** to pass the exam of any class they are assigned to. You want to assign each of the `extraStudents` students to a class in a way that **maximizes** the **average** pass ratio across **all** the classes.

The **pass ratio** of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The **average pass ratio** is the sum of pass ratios of all the classes divided by the number of the classes.

Return *the **maximum** possible average pass ratio after assigning the *`extraStudents`* students. *Answers within $10^{-5}$ of the actual answer will be accepted.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $classes = [[1,2],[3,5],[2,2]], extraStudents = 2$
- **Output:** `0.78333`
- **Explanation:** You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
#### Example 2

- **Input:** $classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4$
- **Output:** `0.53485`

### 4. Constraints

- $1 \le \text{classes.length} \le 10^{5}$

- $\text{classes}[i].length = 2$

- $1 \le \text{pass}_{i} \le \text{total}_{i} \le 10^{5}$

- $1 \le extraStudents \le 10^{5}$