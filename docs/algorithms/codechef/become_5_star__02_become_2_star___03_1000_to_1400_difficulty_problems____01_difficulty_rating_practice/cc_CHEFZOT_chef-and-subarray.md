# Chef and Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFZOT |
| Difficulty Rating | 1191 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CHEFZOT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFZOT) |

---

## Problem Statement

Chef loves research! Now he is looking for subarray of maximal length with non-zero product.

Chef has an array **A** with **N** elements: **A1**, **A2**, ..., **AN**.

Subarray **Aij** of array **A** is elements from index **i** to index **j**: **Ai**, **Ai+1**, ..., **Aj**.

Product of subarray **Aij** is product of all its elements (from **ith** to **jth**).

### Input

- First line contains sinlge integer **N** denoting the number of elements.

- Second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the elements of array.

### Output

- In a single line print single integer - the maximal length of subarray with non-zero product.

### Constraints

- **1** ≤ **N** ≤ **100000**

- **0** ≤ **Ai** ≤ **10000**

---

## Examples

**Example 1**

**Input**

```text
6
1 0 2 3 0 4
```

**Output**

```text
2
```

**Explanation**

For the first sample subarray is: {2, 3}.

**Example 2**

**Input**

```text
1
0
```

**Output**

```text
0
```

**Explanation**

For the second sample there are no subbarays with non-zero product.

**Example 3**

**Input**

```text
3
1 0 1
```

**Output**

```text
1
```

**Explanation**

For the third sample subbarays is {1}, (the first element, or the third one).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFZOT)

[Contest](http://www.codechef.com/JUNE14/problems/CHEFZOT)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

processing of arrays

### PROBLEM:

Given an array A. Find maximum length of sub-array with product of its elements being non zero.

### EXPLANATION

-

Product of a sub-array will be zero if and only if it contains at least one zero element.

So we have to find out maximum size of the sub-array not containing zero.

-

So we can start processing the array from left to right and keep track of last position where we had found the zero element, at each step

we will compute the maximum size of the sub-array ending at the current position and not having any zeros in it (For i th  element, the size of the sub-array will

be i - lastZeroIndex where lastZeroIndex is the index of the last zero found).

-

Finally we will take the maximum of all those values for each index i from 1 to N.

Please see the simple **pseudo code.**

``lastZeroIndex = 0, ans = 0
for i = 1 to N:
	if a[i] == 0:
		lastZeroIndex = i
	cur = i - lastZeroIndex
	ans = max(ans, cur)
``

**Complexity**:

O(N), You just need a single pass of the array a.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Tester’s solution](http://www.codechef.com/download/Solutions/2014/June/Tester/CHEFZOT.cpp)

</details>
