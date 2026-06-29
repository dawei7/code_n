# Small Factorial

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW018 |
| Difficulty Rating | 760 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FLOW018](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW018) |

---

## Problem Statement

Write a program to find the factorial value of any number entered by the user.

---

## Input Format

The first line contains an integer **T**, the total number of testcases. Then **T** lines follow, each line contains an integer **N**.

---

## Output Format

For each test case, display the factorial of the given number **N** in a new line.

---

## Constraints

- 1 **≤** **T** **≤** 1000
- 0 **≤** **N** **≤** 20

---

## Examples

**Example 1**

**Input**

```text
3 
3 
4
5
```

**Output**

```text
6
24
120
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
24
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
120
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Small Factorial Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW018)

### [](#problem-statement-1)Problem Statement:

Write a program to find the factorial value of any number entered by the user.

### [](#approach-2)Approach:

Since N can range from 0 to 20, we need a straightforward way to compute the factorial for each N in a single test case. Here’s how we can approach the problem:

- **Iterative Computation**:

- Use a loop to compute the factorial iteratively. Initialize the result as 1 and multiply it by each integer from 1 to N.

- **Handling Special Cases**:

- 0! is defined as 1. This needs to be considered as a special case to avoid errors in computation.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(N)` for each computation of `N!`.

- **Space Complexity**: `O(1)` No additional space other than variables used for computation.

</details>
