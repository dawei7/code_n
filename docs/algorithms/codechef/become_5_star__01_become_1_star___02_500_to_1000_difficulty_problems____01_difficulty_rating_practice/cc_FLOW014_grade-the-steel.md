# Grade The Steel

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW014 |
| Difficulty Rating | 838 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [FLOW014](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FLOW014) |

---

## Problem Statement

A certain type of steel is graded according to the following conditions.

1. **Hardness** of the steel must be greater than 50
2. **Carbon content** of the steel must be less than 0.7
3. **Tensile strength** must be greater than 5600

The grades awarded are as follows:
- Grade is 10 if all three conditions are met
- Grade is 9 if conditions (1) and (2) are met
- Grade is 8 if conditions (2) and (3) are met
- Grade is 7 if conditions (1) and (3) are met
- Grade is 6 if only one condition is met
- Grade is 5 if none of the three conditions are met

Write a program to display the grade of the steel, based on the values of hardness, carbon content and tensile strength of the steel, given by the user.

---

## Input Format

The first line contains an integer **T**, total number of testcases. Then follow **T** lines, each line contains three numbers **hardness**, **carbon content** and **tensile strength** of the steel.

---

## Output Format

For each test case, print Grade of the steel depending on Conditions, in a new line.

---

## Constraints

- 1 **≤** **T** **≤** 1000
- 0 **≤** **hardness, carbon content, tensile strength** **≤** 10000

---

## Examples

**Example 1**

**Input**

```text
3 
53 0.6 5602
45 0 4500
0 0 0
```

**Output**

```text
10
6
6
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
53 0.6 5602
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
45 0 4500
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
0 0 0
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Grade The Steel Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FLOW014)

### [](#problem-statement-1)Problem Statement:

We are given the following conditions to grade the steel:

- **Hardness** of the steel must be greater than 50.

- **Carbon content** of the steel must be less than 0.7.

- **Tensile strength** must be greater than 5600.

Based on the above conditions, the grades are assigned as follows:

- **Grade 10**: If all three conditions are met.

- **Grade 9**: If conditions (1) and (2) are met.

- **Grade 8**: If conditions (2) and (3) are met.

- **Grade 7**: If conditions (1) and (3) are met.

- **Grade 6**: If only one condition is met.

- **Grade 5**: If none of the conditions are met.

### [](#approach-2)Approach:

- **Evaluating Conditions**: We will directly check each of the conditions using `if-else` statements for each test case:

- If all three conditions are met, print `10`.

- If only two conditions are met, we check for each possible combination of conditions and assign the corresponding grade (9, 8, or 7).

- If only one condition is met, assign grade `6`.

- If no conditions are met, assign grade `5`.

- **Using `if-else` Ladder**: The conditions are evaluated in a sequence where:

- The highest grade is checked first (Grade 10 for all three conditions).

- Then, the remaining combinations of two conditions are checked (Grade 9, 8, or 7).

- If only one condition is met, grade `6` is assigned.

- Finally, if none of the conditions are met, grade `5` is assigned.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(1)` the conditions are checked using a constant number of operations.

- **Space Complexity:**  `O(1)` No extra space is used.

</details>
