# Sort Checker

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SRTCHK |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [SRTCHK](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/SRTCHK) |

---

## Problem Statement

## Sort Checker

You are given an array $A$ and an array $B$ of the same size. You have to print **yes** if $B$ is the sorted version of $A$ and **no** otherwise.

### Input
- First line contains a single integer $T$, the number of testcases.
- The first line of each testcase contains a single integer $n$, the number of elements in the arrays.
- The second line of each testcase contains $n$ space separated integers denoting the array $A$.
- The third line of each testcase contains $n$ space separated integers denoting the array $B$.

### Output

Print one line for each testcase, **yes** or **no**.

### Constraints

- $1 \leq T \leq 10^5$
- $1 \le n \le 10^5$
- The sum of $n$ over all test cases does not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 3 2 2
1 2 3 4
4
1 3 2 2
1 2 3 2
4
1 3 2 2
1 2 2 3
```

**Output**

```text
no
no
yes
```

**Explanation**

All three testcases have the same array $A$, and the sorted version of $A$ is $\{1, 2, 2, 3\}$.

Therefore only the third testcase contains **yes**, rest contain **no**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 3 2 2
1 2 3 4
```

**Output for this case**

```text
no
```



#### Test case 2

**Input for this case**

```text
4
1 3 2 2
1 2 3 2
```

**Output for this case**

```text
no
```



#### Test case 3

**Input for this case**

```text
4
1 3 2 2
1 2 2 3
```

**Output for this case**

```text
yes
```


