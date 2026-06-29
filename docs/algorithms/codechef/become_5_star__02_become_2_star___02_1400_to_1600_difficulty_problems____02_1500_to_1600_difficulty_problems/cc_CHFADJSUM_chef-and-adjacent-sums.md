# Chef And Adjacent Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFADJSUM |
| Difficulty Rating | 1604 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [CHFADJSUM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/CHFADJSUM) |

---

## Problem Statement

You are given an array $A$ of size $N$.
Consider an array $B$ of size $N$ formed by sorting $A$ in non-decreasing order.
Let $Z = (B_N + B_{(N-1)})$.

Find whether there exists any rearrangement of the array $A$, such that, for all $(1\le i \lt N)$,
$(A_i + A_{(i+1)}) \lt Z$.
If such a rearrangement exists, print `YES`, otherwise print `NO`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a integer $N$  — the number of elements in the array.
    - The next line contains $N$ space-separated integers, denoting the elements of the array.

---

## Output Format

For each test case, output `YES`, if a rearrangement exists that satisfies the conditions. Otherwise, output `NO`.

You may print each character in uppercase or lowercase. For example, `NO`, `no`, `No`, and `nO` are all considered the same.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
3 4 4
4
1 2 3 4
2
2 2
2
1 2
```

**Output**

```text
YES
YES
NO
NO
```

**Explanation**

**Test case $1$:** Here $B = [3, 4, 4]$ and $Z = (4 + 4) = 8$.
We can rearrange the array to $[4,3,4]$ such that $(A_1 + A_2) = 7 \lt 8$ and $(A_2 + A_3) = 7 \lt 8$. Thus, the rearrangement is valid.

**Test case $2$:** Here $B = [1, 2, 3, 4]$ and $Z = (4 + 3) = 7$.
We can rearrange the array to $[4,2,3,1]$ such that $(A_1 + A_2) = 6 \lt 7$, $(A_2 + A_3) = 5 \lt 7$, and $(A_3 + A_4) = 4 \lt 7$. Thus, the rearrangement is valid.

**Test case $3$:** The exists no possible rearrangement that satisfies the conditions.

**Test case $4$:** The exists no possible rearrangement that satisfies the conditions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 4 4
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
2
2 2
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chef And Adjacent Sums Practice Coding Problem](https://www.codechef.com/problems/CHFADJSUM)

### [](#problem-statement-1)Problem Statement:

Given an array A of size N, we need to determine whether we can rearrange the elements of A such that for all adjacent pairs in the rearranged array, their sum is strictly less than Z, where: Z = B[N] + B[N−1]. Here, B is the array A sorted in non-decreasing order.

For each test case, output “YES” if such a rearrangement exists, otherwise output “NO”.

### [](#approach-2)Approach:

**Observations:**

- Z is the sum of the two largest elements in the array.

- To satisfy the condition (A[i]+A[i+1])<Z for all i, the rearrangement should avoid placing the two largest elements next to each other.

- The frequency of the largest or second-largest elements must not dominate the array, as it would force them to be adjacent.

**Special Cases:**

- If the largest element occurs too many times (more than half of N), it is impossible to avoid adjacency.

**Plan:**

- Sort the array A to compute Z.

- Check the frequency of the largest element. If it appears more than ⌈N/2⌉ times, output “NO”.

- Otherwise, check the adjacency condition using frequency analysis of the largest and second-largest elements.

### [](#complexity-3)Complexity:

- **Time Complexity:** Sorting takes `O(N log ⁡N)`. Frequency Count takes `O(N)`. Overall Complexity will come as `O(N log ⁡N)`.

- **Space Complexity:** * A `map` (or `unordered_map`) is used to store the frequency of elements. In the worst case, all elements are unique, so the map requires `O(N)` space for `N` key-value pairs.

</details>
