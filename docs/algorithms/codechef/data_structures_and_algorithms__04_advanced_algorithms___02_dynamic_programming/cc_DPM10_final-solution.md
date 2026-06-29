# Final Solution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DPM10 |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Introducing Intuition for dynamic programming |
| Official Link | [DPM10](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA05/problems/DPM10) |

---

## Problem Statement

Ok, so armed with the knowledge of Dynamic Programming, let's try to solve this problem.

Given $N$ integers, you have to pick a valid subset with the largest sum from these integers.

A valid subset is a subset in which no two adjacent elements are picked.

*Hint - Store the result of the i-th prefix in an array as dp[i], so you might be able to use it in the future.*

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains $N$ - the number of integers
    - The next line contains $N$ space separated integers, $A_i$

---

## Output Format

For each test case, output on a new line the largest sum of any valid subset.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
2
5
3 -2 1 3 0
4
4 3 1 2
```

**Output**

```text
6
6
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
3 -2 1 3 0
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
4
4 3 1 2
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Final Solution in Dynamic programming](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA05/problems/DPM10)

### [](#problem-statement-1)Problem Statement:

Given N integers, you have to pick a valid subset with the largest sum from these integers.

A valid subset is a subset in which no two adjacent elements are picked.

### [](#approach-2)Approach:

- We will use a **DP** array where dp[i] represents the maximum sum of any valid subset that can be formed from the first i integers, respecting the rule that no two adjacent elements are picked.

- For each integer A[i], we have two options:

- Include: If we include A[i] in the subset, we cannot include A[i−1], so the total sum will be dp[i−2]+A[i];

- Exclude: If we exclude A[i], then the total sum will simply be dp[i−1].

- Therefore, the recurrence relation is dp[i]=max⁡(dp[i−1],dp[i−2]+A[i]). The idea is to make a choice at each position based on the previous computations.

- The first element’s maximum sum is either 0 (if we don’t select it) or the element itself.

- For the second element, we can either pick just the second element or stick with the first one.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` Traversing the array once for calculating dp array `O(N)` and calculating the maximum value for the answer `O(N)`. `2*O(N)->O(N)`

- **Space Complexity:** `O(N)` Assigning the dp array with `N+1`.

</details>
