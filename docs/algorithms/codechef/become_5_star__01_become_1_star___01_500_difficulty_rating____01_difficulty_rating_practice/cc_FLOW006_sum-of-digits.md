# Sum of Digits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW006 |
| Difficulty Rating | 455 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FLOW006](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW006) |

---

## Problem Statement

You're given an integer **N**. Write a program to calculate the sum of all the digits of **N**.

---

## Input Format

The first line contains an integer **T**, the total number of testcases. Then follow **T** lines, each line contains an integer **N**.

---

## Output Format

For each test case, calculate the sum of digits of **N**, and display it in a new line.

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
12345
31203
2123
```

**Output**

```text
15
9
8
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
12345
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
31203
```

**Output for this case**

```text
9
```



#### Test case 3

**Input for this case**

```text
2123
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Sum of Digits Practice Problem in Basic Math](https://www.codechef.com/practice/course/basic-math/BASICMATH/problems/FLOW006)

### [](#problem-statement-1)Problem Statement:

You’re given an integer **N** . Write a program to calculate the sum of all the digits of **N**.

### [](#approach-2)Approach:

For Calculating the sum of digits, we have to extract each digit from the number and then add them up.

Steps:

- Initialize a variable to store the sum of digits (let’s call it `sum`).

- Use a loop to repeatedly extract the last digit of N using the modulus operator (`% 10`), add this digit to `sum`, and then remove the last digit by dividing N by 10 (`N = N/10`).

- Continue this process until N becomes `0`.

### [](#complexity-3)Complexity:

- **Time Complexity**: The time complexity for calculating the sum of digits for a single number `N` is `O(d)`, where `d` is the number of digits in `N`. In the worst case, since N≤1,000,000,  `d` can be at most `7`.

- **Space Complexity**: `O(1)` No extra space is required

</details>
