# Maximum Subset Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXSUBSUM |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Introducing Intuition for dynamic programming |
| Official Link | [MXSUBSUM](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA01/problems/MXSUBSUM) |

---

## Problem Statement

So let's try to solve a very basic problem first.

Given $N$ integers, you have to select a subset of these integers such that the sum of the subset is the largest compared to all other subsets.

Note that you might select an empty subset as well.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains $N$ - the number of integers
    - The next line contains $N$ space separated integers, $i^{th}$ integer being $A_i$

---

## Output Format

For each test case, output on a new line the largest subset sum of the $N$ integers.

---

## Constraints

- $1 \leq T \leq 5 \cdot 10^{4}$
- $1 \leq N \leq 10^{5}$
- $ -10^{4} \leq A_i \leq 10^{4}$
- Sum of $N$ over test cases do not exceed $10^{5}$

---

## Examples

**Example 1**

**Input**

```text
2
5
3 -2 1 3 0
4
-2 -3 -4 -1
```

**Output**

```text
7
0
```

**Explanation**

**Test Case 1** - Select the elements 3, 1 and 3, so the total score would be 7.

**Test Case 2** - Select no elements, so the total score would be 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
3 -2 1 3 0
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
4
-2 -3 -4 -1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Maximum Subset Sum in Dynamic programming](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA01/problems/MXSUBSUM)

### [](#problem-statement-1)Problem Statement:

Given N integers, you have to select a subset of these integers such that the sum of the subset is the largest compared to all other subsets.

**Note**: You might select an empty subset as well.

### [](#approach-2)Approach:

- Iterate through the array.

- Accumulate the sum of all positive integers. Ignore negative integers and zeros.

- If all integers are negative, the maximum sum should be 0, as an empty subset provides the highest possible sum in such a case.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` Traversing the array once.

- **Space Complexity:** `O(1)` No extra space required.

</details>
