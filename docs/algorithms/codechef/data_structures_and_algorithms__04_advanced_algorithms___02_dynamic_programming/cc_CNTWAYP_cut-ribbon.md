# Cut Ribbon

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTWAYP |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Different types of dynamic programming problems |
| Official Link | [CNTWAYP](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA06/problems/CNTWAYP) |

---

## Problem Statement

Given a ribbon of length **N** units. It needs to be cut into parts such that the length of each part is even and each part is atmost **L** units. How many ways are there to cut the ribbon? Two ways are different if and only if

- Number of cuts are different (OR)

- Number of cuts are same and there is some i such that the i-th part from the left is of different lengths in each of the two ways

If there is no way to cut it such that all parts are even, print 0.

---

## Input Format

- The first line of the input contains an integer **T** denoting the number of test cases.

- The first and the only line of each test case contains two space separated integers **N** and **L**.

---

## Output Format

For each test case, output a single line containing the answer. Since,
 the answer can be pretty large, print it modulo **109 + 7**

---

## Constraints

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N** ≤ **103**

- **1** ≤ **L** ≤ **N**

---

## Examples

**Example 1**

**Input**

```text
3
6 4
4 2
2 2
```

**Output**

```text
3
1
1
```

**Explanation**

**Example case 1.** Ribbon of length 6 units needs to be cut into parts having length at most 4 units. You can cut this into pieces in following 3 ways.

- Way 1: 2 units + 2 units + 2 units

- Way 2: 4 units + 2 units

- Way 3: 2 units + 4 units

**Example case 2.**
Ribbon of length 4 units needs to be cut into parts having length at most 2 units. You can cut this into pieces in following way.

- Way 1: 2 units + 2 units

**Example case 3.**
Ribbon of length 2 units needs to be cut into parts having length at most 2 units. You: can cut this into pieces in only oe way, and that is by not cutting at all

- Way 1: 2 units

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 4
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2 2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Cut Ribbon in Dynamic programming](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA06/problems/CNTWAYP)

### [](#problem-statement-1)Problem Statement:

Given a ribbon of length N units. It needs to be cut into parts such that the length of each part is even and each part is atmost L units. How many ways are there to cut the ribbon? Two ways are different if and only if

- Number of cuts are different (OR)

- Number of cuts are same and there is some i such that the i-th part from the left is of different lengths in each of the two ways

If there is no way to cut it such that all parts are even, print 0.

### [](#approach-2)Approach:

- Start by initializing the `DP` array to size N to accommodate all lengths up to N.

- Set `DP[0] = 1`, which signifies that there is one way to have a ribbon of length 0 (by not cutting it at all).

- Initialize the `DP` with except `DP[0]`. Iterate through possible lengths of the last cut from i−1 down to 1. The inner loop checks:

- The length of the last piece being considered is i−j+1 (where j is the length before the last cut).

- Only consider the last piece if it is even and does not exceed L (`i - j + 1 <= L`).

- If valid, add the number of ways to cut the previous ribbon length j−1 to `DP[i]`

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N^2)` For outer loop `O(N)`, the inner loop takes till `O(N)` in the worst case.

- **Space Complexity:** `O(N)` for `DP` array.

</details>
