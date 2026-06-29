# Approximately II

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | APPROX2 |
| Difficulty Rating | 1471 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [APPROX2](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/APPROX2) |

---

## Problem Statement

You are given an array of **N** integers **a1, a2, ..., aN** and an integer **K**. Find the number of such unordered pairs {**i**, **j**} that

- **i** ≠ **j**

- **|ai + aj - K|** is minimal possible

Output  the minimal possible value of **|ai + aj - K|** (where **i** ≠ **j**) and the number of such pairs for the given array and the integer **K**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case consists of two space separated integers - **N** and **K** respectively.

The second line contains **N** single space separated integers - **a1, a2, ..., aN** respectively.

### Output

For each test case, output a single line containing two single space separated integers - the minimal possible value of **|ai + aj - K|** and the number of unordered pairs {**i**, **j**} for which this minimal difference is reached.

### Constraints

- **1** ≤ **T** ≤ **50**

- **1** ≤ **ai, K** ≤ **109**

- **N** = **2** - 31 point.

- **2** ≤ **N** ≤ **1000** - 69 points.

---

## Examples

**Example 1**

**Input**

```text
1   
4 9
4 4 2 6
```

**Output**

```text
1 4
```

**Explanation**

The minimal possible absolute difference of **1** can be obtained by taking the pairs of **a1** and **a2**, **a1** and **a4**, **a2** and **a4**, **a3** and **a4**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Problem link** : [contest](http://www.codechef.com/LTIME12/problems/APPROX2) [practice](http://www.codechef.com/problems/APPROX2)

**Difficulty** : CakeWalk

**Pre-requisites** : Basic programming language constructions knowledge

**Problem** : find the number of pairs for which **|ai+aj-K|** is minimal possible (and this minimal possible value), having the array **a[]** and the integer **K** given.

**Explanation** :

There were two subtasks.

In the first one **N** equals to 2. That means that the minimal difference will always be **|a1+a2-K|** because totally there will be only one pair.

In the second one, **N** is still fairly small, so we can check all possible pairs of {**ai**, **aj**} via a brute force. I.e. we can make two nested cycles, the first one for **i** and the second one for **j** and there check that **|ai+aj-K|** has the minimal possible value.

Actually, the problem can be solved for **N** <= 106 within the same time bounds, but it was decided not to add this subtask in order to enable more people to get the full points. See tester’s solution for the details on this solution.

**Solutions** : [Setter](http://www.codechef.com/download/Solutions/LTIME12/Setter/APPROX2.cpp) [Tester](http://www.codechef.com/download/Solutions/LTIME12/Tester/APPROX2.cpp)

</details>
