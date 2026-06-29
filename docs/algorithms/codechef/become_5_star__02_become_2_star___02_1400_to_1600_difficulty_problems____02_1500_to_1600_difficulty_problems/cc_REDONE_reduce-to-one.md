# Reduce to One

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REDONE |
| Difficulty Rating | 1507 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [REDONE](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/REDONE) |

---

## Problem Statement

You have become good friends with Chef. Right now, Chef is busy in the kitchen, so he asked you to solve a problem for him.

Consider a list of integers $L$. Initially, $L$ contains the integers $1$ through $N$, each of them exactly once (but it may contain multiple copies of some integers later). The order of elements in $L$ is not important. You should perform the following operation $N-1$ times:
- Choose two elements of the list, let's denote them by $X$ and $Y$. These two elements may be equal.
- Erase the chosen elements from $L$.
- Append the number $X + Y + X \cdot Y$ to $L$.

At the end, $L$ contains exactly one integer. Find the maximum possible value of this integer. Since the answer may be large, compute it modulo $1,000,000,007$ ($10^9+7$).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

### Output
For each test case, print a single line containing one integer ― the maximum possible value of the final number in the list modulo $10^9+7$.

### Constraints
- $1 \le T \le 100,000$
- $1 \le N \le 1,000,000$

### Subtasks
**Subtask #1 (20 points):** $1 \le T, N \le 25$

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1
2
4
```

**Output**

```text
1
5
119
```

**Explanation**

**Example case 1:** $L=[1]$

**Example case 2:** $L=[1,2] \rightarrow [1 + 2 + 1 \cdot 2] $

**Example case 3:** $L=[\textbf{1},2,3,\textbf{4}] \rightarrow [\textbf{2},3,\textbf{9}] \rightarrow [3,29] \rightarrow [119] $. The chosen elements in each step are in bold.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
4
```

**Output for this case**

```text
119
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Reduce to One Practice Problem in 1400 to 1600 difficulty problems](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/REDONE)

### [](#problem-statement-1)Problem Statement:

Given a list of integers from `1` to `N`, you repeatedly perform the operation:

- Choose two elements `X` and `Y` from the list (they can be equal).

- Replace them with the number `X+Y+X⋅Y`.

The goal is to find the maximum possible final number that remains in the list after performing this operation `N−1` times, and then return the result modulo 10^9 + 7.

### [](#approach-2)Approach:

This is essentially computing: (n+1)! −1 mod (10^9 + 7)

**Precomputation of Factorials Modulo 10^9 + 7**:

- To solve this problem efficiently, instead of computing the factorial for each test case individually (which can be slow), we precompute the factorials modulo 10^9 + 7 up to a maximum number (in this case 10^6 + 1).

- This is stored in the array `preCompute`, where `preCompute[i]` holds i! mod (10^9 + 7).

**Factorial Computation**:

- We initialize the first factorial `preCompute[1] = 1` (since 1!=1).

- Then, for each number from 2 to `maxN - 1` (which is 10^6 + 1), we calculate the factorial of the current number iteratively: preCompute[i]=(preCompute[i−1]×i) mod(10^9+7)

- This ensures that all factorials up to 10^6 + 1 are computed efficiently using previously computed values.

**Handling Multiple Test Cases**:

- After precomputing the factorial values, for each test case, we directly retrieve the factorial of `n+1` from the `preCompute` array.

- The result is computed by subtracting 1 from (n+1)!mod (10^9+7), then outputting the result modulo 10^9 + 7.

### [](#complexity-3)Complexity:

- **Time Complexity:** Computing the factorial for all numbers from `1` to 10^6+1 takes `O(maxN)`, where `maxN=`10^6+2. Since each computation involves a constant number of operations (multiplication and modulo), this is efficient.

- **Space Complexity:** We use an array of size `maxN` to store the factorials. Thus, the space complexity is `O(maxN)`.

</details>
