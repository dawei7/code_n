# Counting Mobiles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOBCNT |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [MOBCNT](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/MOBCNT) |

---

## Problem Statement

A **mobile** is a rooted tree with weighted leaves that satisfies the following property: each non-leaf vertex $v$ has exactly two children $L(v)$ and $R(v)$, and the total weight of leaves in the subtree of $L(v)$ is equal to the total weight of leaves in the subtree of $R(v)$.

We have $n$ positive integer weights $a_1, \ldots, a_n$. You have to count the number of **suitable** mobiles. A mobile is **suitable** if the multiset of weights in its leaves is equal to the multiset $\{a_1, \ldots, a_n\}$. Two mobiles are considered different if they are not **equal**. Two mobiles $T_1$ and $T_2$ are **equal** in one of two cases:

- $T_1$ and $T_2$ each consist of a single leaf vertex, and the leaves' weights are equal;
- Respective roots $r_1$ and $r_2$ of $T_1$ and $T_2$ are both not leaves, and subtrees of $L(r_1)$ and $L(r_2)$ are equal mobiles, as well as subtrees of $R(r_1)$ and $R(r_2)$.
Since the answer can be large, print it modulo $10^9 + 7$.

---

## Input Format

- The first line contains a single integer $T$, the number of test cases. $T$ test case descriptions follow.
- Each test case description starts with a line containing a single integer $n$, the number of weights. The next line contains $n$ integers $a_1, \ldots, a_n$ .

---

## Output Format

Print answers for each test case in a new line, in the order of appearance in the input. For each test case print a single integer, the number of different suitable mobiles modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq n \leq 10^5$
- $1 \leq a_i \leq 10^9$
- The sum of all $n$ does not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
5
1
7
3
1 1 2
4
3 3 3 3
4
5 5 10 20
3
1 2 3
```

**Output**

```text
1
2
1
4
0
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
7
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
1 1 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
3 3 3 3
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
4
5 5 10 20
```

**Output for this case**

```text
4
```



#### Test case 5

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
0
```


