# Count Subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBINC |
| Difficulty Rating | 1478 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [SUBINC](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/SUBINC) |

---

## Problem Statement

Given an array $A_1, A_2, ..., A_N$, count the number of subarrays of array $A$ which are non-decreasing.
A subarray $A[i, j]$, where $1 ≤ i ≤ j ≤ N$ is a sequence of integers ${A_i}$, $A_{i+1}$, ..., ${A_j}$.

A subarray $A[i, j]$ is non-decreasing if $A_i ≤ A_{i+1} ≤ A_{i+2} ≤ ... ≤ A_j$. You have to count the total number of such subarrays.

### Input

- The first line of input contains an integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$ denoting the size of array.

- The second line contains $N$ space-separated integers $A_1$, $A_2$, ..., $A_N$ denoting the elements of the array.

### Output

For each test case, output in a single line the required answer.

### Constraints

-   $1 ≤ T ≤ 5$
-   $1 ≤ N ≤ 10^5$
-   $1 ≤ A_i ≤ 10^9$

### Subtasks

-   **Subtask 1** (20 points) : $1 ≤ N ≤ 100$
-   **Subtask 2** (30 points) : $1 ≤ N ≤ 1000$
-   **Subtask 3** (50 points) : Original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4
1 4 2 3
1
5
```

**Output**

```text
6
1
```

**Explanation**

**Example case 1.**
All valid subarrays are $A[1, 1], A[1, 2], A[2, 2], A[3, 3], A[3, 4], A[4, 4]$.
Note that singleton subarrays are identically non-decreasing.

**Example case 2.**
Only single subarray $A[1, 1]$ is non-decreasing.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 4 2 3
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
1
5
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](http://www.codechef.com/problems/SUBINC)

[Contest](http://www.codechef.com/OCT15/problems/SUBINC/)

# Difficulty

Simple

# Pre-requisites

Simple dynamic programming

# Problem

Count the number of non-decreasing subarrays of the given array **A[]**.

# How to get 20 points

Let’s choose the left bound, say **L**. After the left bound is fixed, let’s choose the right bound, say **R**. And now, let’s check that the subarray **A[L, R]** is non-decreasing.

In other words, let’s iterate through all possible subarrays and then, for each of them, check whether it is a non-descreasing one or not.

Choosing the left bound takes **O(N)** operations, choosing the right bound takes **O(N)** operations too, and checking subarray also takes **O(N)** operations. Since these operations are nested, hence the total complexity will be **O(N3)**.

This solution is good enough to solve the first subtask.

# How to get 50 points

Let’s choose the left bound, say **L**. Let the right bound, say **R**, be equal to **L** initially. Then while the elements are non-decreasing keep increasing the right bound **R**. At some moment, you will certainly stop. The amount of non-decreasing subarrays with the left bound at **L** will be equal to **R-L+1** for every fixed **L**. The sum of all this values is the answer to the problem.

Choosing the left bound takes **O(N)** operations, and finding the right bound takes **O(N)** operations. Since these operations are nested, the complexity of the whole solution will be **O(N2)**.

This solution solves the first and the second subtask, but is still not good enough to get the full points.

# How to get 100 points

Let’s introduce an array **B[]** of **N** elements, where the **i**th element of **B[]** defines the amount of the correct subarrays with the *right* bound equal to **i**.

Now, let’s give the rules for calculating the **i**th element of **B[]**:

- if **A[i-1] ? A[i]**, then **B[i] = B[i-1] + 1** since every non-decreasing subarray that ends at the **(i-1)**th element can be continued with the **i**th element without loss of non-decreasingness and one more non-decreasing subarray that ends at the **i**th element is **A[i, i]**.

- if **A[i-1] > A[i]**, then **B[i] = 1** since any subarray that ends at the **(i-1)**th element will lose its’ non-decreasingness if continued with the **i**th element, so the only suitable subarray will be **A[i, i]**.

So, the answer will be equal to the sum of all elements of **B[]**. The complexity is **O(N)**, because the computation of the array **B** turns out to be a single for-loop with a condition for the computation of **B[i]** inside.

# Setter’s Solution

Can be found [here](http://www.codechef.com/download/Solutions/OCT15/Setter/SUBINC.cpp)

# Tester’s Solution

Can be found [here](http://www.codechef.com/download/Solutions/OCT15/Tester/SUBINC.cpp)

</details>
