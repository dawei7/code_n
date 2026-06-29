# The Smallest Pair

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMPAIR |
| Difficulty Rating | 1352 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [SMPAIR](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/SMPAIR) |

---

## Problem Statement

You are given a sequence **a1, a2, ..., aN**. Find the smallest possible value of **ai + aj**, where 1 ≤ **i** < **j** ≤ **N**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each description consists of a single integer **N**.

The second line of each description contains **N** space separated integers - **a1, a2, ..., aN** respectively.

### Output

For each test case, output a single line containing a single integer - the smallest possible sum for the corresponding test case.

### Constraints

- **T** = **105**, **N** = **2** : 13 points.

- **T** = **105**, **2** ≤ **N** ≤ **10** : 16 points.

- **T** = **1000**, **2** ≤ **N** ≤ **100** : 31 points.

- **T** = **10**, **2** ≤ **N** ≤ **105** : 40 points.

- **1** ≤ **ai** ≤ **106**

---

## Examples

**Example 1**

**Input**

```text
1
4
5 1 3 4
```

**Output**

```text
4
```

**Explanation**

Here we pick **a2** and **a3**. Their sum equals to 1 + 3 = 4.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Problem link** : [contest](http://www.codechef.com/LTIME13/problems/SMPAIR) [practice](http://www.codechef.com/problems/SMPAIR)

**Difficulty** : CakeWalk

**Pre-requisites** : Sorting

**Problem** : Given a sequence **a1, a2, …, aN**. Find the smallest possible value of **ai + aj**, where 1 ? **i** < **j** ? **N**

#### Explanation

This problem was the easiest one in the set and it was intended to enable everybody to get some points.

### How to get 13 points

Here you have only two integers **a1** and **a2**, so the only possible sum will be **a1+a2**.

### How to get 60 points

The constraints were designed in such a way that you can iterate through all the possible pairs (**i**, **j**), where 1 ? **i** < **j** ? **N** and check for every obtained sum, whether it’s the minimal one.

### How to get 100 points

The answer is basically the sum of the minimal and the second-minimal element in the array. So you can simply iterate through all the numbers, keeping track of the minimal and the second-minimal number. Or if your programming language has built-in sorting, you can act even simpler, because after the sorting of the array in increasing order, the required minimal and the second-minimal will be the first and the second elements of the sorted array.

### Related links

-
[Reference](http://www.cplusplus.com/reference/algorithm/sort/) in the built-in sorting for C++ users

**Solutions** : [setter](http://www.codechef.com/download/Solutions/LTIME13/Setter/SMPAIR.cpp) [tester](http://www.codechef.com/download/Solutions/LTIME13/Tester/SMPAIR.cpp)

</details>
