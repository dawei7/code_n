# Sort by swaps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SWPSRT1 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [SWPSRT1](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/SWPSRT1) |

---

## Problem Statement

## Swap Sort

You are given an array $A$ of size $n$ (not exceeding $500$), you are allowed a maximum of $n-1$ swaps where in each swap you can choose **any two** indices $i, j$ such that $0 \leq i, j \leq n-1$ and swap the values of $A_i$ and $A_j$.

Note that you **do not** need to minimise the number of swaps, and you are also **not required** to optimize the time complexity (note that the constraints allow solutions that are $\mathcal{O}(n^2)$ as well), however you **cannot** swap more than $n-1$ times.

There may be many solutions, you can output **any** of them.

### Input

The first line contains a single integer $n$, the number of elements in the array

The second line contains $n$ space separated integers, the elements of the array

### Output

In the first line print the number of swaps you need to perform, let this number be $m$.

In the next $m$ lines, print two space separated integers $i, j$ such that $0 \leq i, j \leq n-1$.

After performing the swaps in the order in which your program gives the output, the array should become sorted in increasing order.
(i.e. $A_i \geq A_{i-1}$ for every $i$ in the range $[1, n-1]$).

### Constraints

$1 \leq n \leq 500$

$-10^9 \leq A_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
3 2 1
```

**Output**

```text
1
0 2
```

**Explanation**

After the first swap, the elements $A_0$ and $A_2$ are swapped, and the array becomes sorted, i.e. $\{1, 2, 3\}$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Sort by swaps Practice Problem in Jump from 2* to 3*](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/SWPSRT1)

### [](#problem-statement-1)Problem Statement:

You are given an array A of size n (not exceeding 500), you are allowed a maximum of n−1 swaps where in each swap you can choose any two indices i, j such that 0≤i, j≤n−1 and swap the values of A_i and A_j.

### [](#approach-2)Approach:

**Enumeration sort** is a simple algorithm that sorts an array by finding the correct position for each element and placing it there. In this problem, we can modify it to count the swaps required and output the swap operations.

#### [](#steps-to-solve-the-problem-3)Steps to Solve the Problem:

-

**Copy and Sort the Array**: Create a copy of the original array and sort it using an in-built function to determine the target state of the array.

-

**Swapping Process**:

- Traverse the original array and for each element, check if it matches the element at the same index in the sorted array.

- If it doesn’t match, find the index `j` in the original array that holds the correct element for the current index `i`.

- Swap the elements at indices `i` and `j`.

- Record the swap operation and increment the swap counter.

-

**Stop After n−1 Swaps**: Ensure the process stops after `n−1` swaps, even if the array isn’t fully sorted, as the constraints limit the maximum number of swaps.

-

**Output**: Print the number of swaps and the pairs of indices swapped.

### [](#complexity-4)Complexity:

- **Time Complexity:** O(n^2), as we may need to iterate through the array up to `n−1` times to find and place elements.

- **Space Complexity:** `O(n)`, due to storing the positions and the list of swaps.

</details>
