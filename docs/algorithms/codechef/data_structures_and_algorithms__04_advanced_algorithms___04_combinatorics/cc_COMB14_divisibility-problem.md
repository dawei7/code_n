# Divisibility Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COMB14 |
| Difficulty Rating | 932 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Combinatronics |
| Official Link | [COMB14](https://www.codechef.com/learn/course/combinatorics/COMBI02/problems/COMB14) |

---

## Problem Statement

Chef has three numbers $A,$ $B$ and $C$. \
He gives you the following task calculate the number of positive integers smaller than or equal to $N,$ which are divisible by at least one of $A,$ $B$ and $C$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a three integers $N$, $A$, $B$, $C$.

---

## Output Format

Output on $T$ new lines (for each test case):
 - Number of positive integers smaller than or equal to $N$, which are divisible by at least of of $A$, $B$ and $C$

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^9$
- $1 \leq A, B, C \leq min(10^3, N)$

---

## Examples

**Example 1**

**Input**

```text
5
10 2 3 2
5 3 2 4
6 3 3 3
24 12 2 12
20 3 20 3
```

**Output**

```text
7
3
2
12
7
```

**Explanation**

For the second test case: $N$ = $5$, $A$ = $3$, $B$ = $2$ and $C$ = $4$. \
Numbers less than or equal to $N$, which are divisible by either $A$, $B$ or $C$ = {$2$, $3$, $4$}

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 2 3 2
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
5 3 2 4
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
6 3 3 3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
24 12 2 12
```

**Output for this case**

```text
12
```



#### Test case 5

**Input for this case**

```text
20 3 20 3
```

**Output for this case**

```text
7
```


