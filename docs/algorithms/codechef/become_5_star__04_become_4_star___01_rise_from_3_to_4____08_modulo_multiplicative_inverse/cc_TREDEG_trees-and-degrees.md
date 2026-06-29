# Trees and Degrees

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREDEG |
| Difficulty Rating | 2783 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [TREDEG](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/TREDEG) |

---

## Problem Statement

Vivek is quite fond of expected values. One day, he stumbled upon the following problem. He cannot solve it, so he is asking you for help.

Consider all trees with $N$ vertices (numbered $1$ through $N$); two trees are different if there is a pair of vertices $u$ and $v$ such that there is an edge between vertices $u$ and $v$ in exactly one of these trees.

For a uniformly randomly chosen tree $T$, let's denote the degrees of vertices $1$ through $N$ in this tree by $d_1, d_2, \ldots, d_N$. Then, let's denote $A = (d_1 \cdot d_2 \cdot \ldots \cdot d_N)^K$. Find the expected value of $A$.

It can be proved that the expected value of $A$ can be expressed as a fraction $P/Q$, where $P$ and $Q$ are coprime positive integers and $Q$ is coprime to $998,244,353$. You should compute the value of $P \cdot Q^{-1}$ modulo $998,244,353$, where $Q^{-1}$ denotes the multiplicative inverse of $Q$ modulo $998,244,353$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

### Output
For each test case, print a single line containing one integer ― $P \cdot Q^{-1} \pmod{998244353}$.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 2,000,000$
- $1 \le K \le 10^9$
- the sum of $N$ over all test cases does not exceed $2,000,000$

### Subtasks
**Subtask #1 (20 points):**
- $T = 10$
- $2 \le N \le 7$

**Subtask #2 (30 points):** the sum of $N$ over all test cases does not exceed $100,000$

**Subtask #3 (50 points):** $K = 1$

---

## Examples

**Example 1**

**Input**

```text
2
3 1
4 2
```

**Output**

```text
2
748683279
```

**Explanation**

**Example case 1:** There are $3$ labelled trees with size $3$: the paths $[1-2-3]$, $[1-3-2]$ and $[3-1-2]$.

The expected value is $\left((1 \cdot 2 \cdot 1)^1 + (1 \cdot 1 \cdot 2)^1 + (2 \cdot 1 \cdot 1)^1\right) / 3 = 2$, so $P = 2$, $Q = 1$, $Q^{-1} = 1$ and the answer is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
748683279
```


