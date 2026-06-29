# Creating Prefix Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFPRO1 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [PREFPRO1](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/PREFPRO1) |

---

## Problem Statement

A "prefix array" is a data structure commonly used in programming, particularly in algorithms related to strings or arrays. Also known as a "prefix sum array", it stores cumulative sums of elements in an array.

We generally use it to optimize the time complexity of a given algorithm.

Using a prefix array in an array of integers: -

```python
array (a)        -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prefix array (b) -> [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
```

We created a prefix array, which stores a cumulative sum of all the previous indexes of the array. This is our prefix array for **a**.

Similarly, we also have prefix arrays for strings:
```
string s = "codechef";
prefixOfs = [c,co,cod,code,codec,codech,codeche,codechef];
```

We created a prefix array for "codechef". In strings, we use the prefix array in a different manner. We concatenate characters in our prefix array of strings.

**Pseudo Code for prefix sum**
```python
PrefixSum(arr)
Input: Array arr of size N
Output: Prefix sum array prefixSum of size N

Initialize an array prefixSum of size N

prefixSum[0] = arr[0]
for i = 1 to N-1 do
    prefixSum[i] = prefixSum[i-1] + arr[i]
return prefixSum
```

### Task
- In the first line, given an integer N, the length of an array.
- In the second line, given N integers in an array A1, A2,... AN,.
- Print the prefix sum of the array.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq Ai \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
5 3 3 13
```

**Output**

```text
5 8 11 24
```
