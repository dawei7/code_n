# Sort by Adjacent Swaps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADJSRT |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [ADJSRT](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/ADJSRT) |

---

## Problem Statement

## Sort by Adjacent Swaps

You are given an array $A$ (of size $n$) and you can only perform the adjacent swaps on the array, i.e. you can choose
an index $i$ ($0 \leq i \leq n-2$) and swap the values present in $A_i$ and $A_{i+1}$.

Sort the array using **minimum** number of adjacent swap operations.

Note that there may be multiple possible outputs, you can print **any** of them.

### Input

The first line contains a single integer $n$, the number of elements in the array

The second line contains $n$ space separated integers, the elements of the array

### Output

In the first line print the number of swaps that your solution performs on the array, let this number be $m$

In the next line print $m$ space separated integers, each between $0$ and $n-2$ (inclusive), the $i^{th}$ integer denotes that
$A_i$ and $A_{i+1}$ are swapped.

Note that $m$ must be equal to the minimum number of adjacent swap operations required to sort the array.

### Constraints

$1 \leq n \leq 10^5$

$-10^9 \leq A_i \leq 10^9$

It is guaranteed that for the given array, the minimum number of swaps required is no more than $10^5$

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
3
0 1 0
```

**Explanation**

The first operation swaps the first two elements of the array ($A_0$ and $A_1$), so the array becomes $\{2, 3, 1\}$

The second operation swaps the second and third elements of the array, so the array becomes $\{2, 1, 3\}$

The third operation swaps the first two elements of the array, so the array becomes $\{1, 2, 3\}$

You can verify that it cannot be done in less than $3$ operations.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Sort by Adjacent Swaps Practice Problem in Jump from 2* to 3*](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/ADJSRT)

### [](#problem-statement-1)Problem Statement:

You are given an array A (of size `n`) and you can only perform the adjacent swaps on the array, i.e. you can choose an index i (0≤i≤n−2) and swap the values present in A_i and A_i+1.

Sort the array using minimum number of adjacent swap operations.

### [](#approach-2)Approach:

The problem can be solved using a modified version of **bubble sort**:

- **Basic Bubble Sort Concept**:

- Traverse the array from the beginning to the end.

- If the current element is greater than the next element, swap them.

- Repeat this process until the array is sorted.

- **Tracking Swaps**:

- Maintain a counter for the number of swaps performed.

- Store the indices of each swap in a vector or array for output.

- **Stopping Condition**:

- If a full pass through the array results in no swaps, the array is already sorted.

**Implementation Steps**:

- Initialize an array or list to keep track of the indices where swaps are made.

- Initialize a counter for the number of swaps.

- Perform the bubble sort:

- Traverse the array from the beginning to the end.

- Compare each element with the next one.

- If the current element is greater than the next, swap them and record the index.

- Increment the swap counter each time a swap is made.

- Repeat the above process until no swaps are needed (indicating that the array is sorted).

- Output the total number of swaps and the recorded indices.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(n^2)` in the worst case, where `n` is the size of the array. This occurs when the array is sorted in reverse order.

- **Space Complexity:** `O(m)`, where `m` is the number of swaps, to store the indices.

</details>
