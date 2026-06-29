# First and Last Digit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW004 |
| Difficulty Rating | 461 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FLOW004](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW004) |

---

## Problem Statement

Given an integer **N** . Write a program to obtain the sum of the first and last digits of this number.

---

## Input Format

The first line contains an integer **T**, the total number of test cases. Then follow **T** lines, each line contains an integer **N**.

---

## Output Format

For each test case, display the sum of first and last digits of **N** in a new line.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000000$

---

## Examples

**Example 1**

**Input**

```text
3 
1234
124894
242323
```

**Output**

```text
5
5
5
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1234
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
124894
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
242323
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [First and Last Digit Practice Problem in 500 difficulty rating](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW004)

### [](#problem-statement-1)Problem Statement:

Given an integer **N** . Write a program to obtain the sum of the first and last digits of this number.

### [](#approach-2)Approach:

- **Extracting the Last Digit:** The last digit of `N` can be found using the modulus operation: `last_digit = N % 10`.

- **Extracting the First Digit:** To find the first digit, divide `N` by `10` repeatedly until `N` becomes less than `10`. The remaining value is the first digit.

- **Calculating the Sum:** Calculate the sum of the first and last digits and print the result for each test case.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(log N)` represents the number of divisions needed to extract the first digit.

- **Space Complexity**: `O(1)`, as we are only using basic variables for calculations.

</details>
