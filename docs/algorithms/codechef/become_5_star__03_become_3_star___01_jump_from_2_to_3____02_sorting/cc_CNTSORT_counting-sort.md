# Counting Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTSORT |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [CNTSORT](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/CNTSORT) |

---

## Problem Statement

Given an array $A$ of $N$ integers, such that $1 \le A[i] \le 100$,,

sort $A$ in non-decreasing/ascending order, and display the elements of the sorted array.

### Input:

- The first line contains an integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$, the number of elements in $A$.
- The next line contains $N$ space-separated integers, denoting the elements of array $A$.

### Output:
For each test case, display the elements of the sorted array, in a new line, separated by a space.

### Constraints
- $1 \le T \le 3$
- $1 \le N \le 10^6$
- $1 \le A[i] \le 100$

---

## Examples

**Example 1**

**Input**

```text
2
5
7 2 9 10 1
4
3 7 7 3
```

**Output**

```text
1 2 7 9 10
3 3 7 7
```

**Explanation**

The sample outputs are the sorted orders of the input arrays respectively, sorted in non-decreasing/ascending order.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
7 2 9 10 1
```

**Output for this case**

```text
1 2 7 9 10
```



#### Test case 2

**Input for this case**

```text
4
3 7 7 3
```

**Output for this case**

```text
3 3 7 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Counting Sort Practice Problem in Jump from 2* to 3*](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/CNTSORT)

### [](#problem-statement-1)Problem Statement:

Given an array A of N integers, such that 1≤ A[i] ≤100, sort A in non-decreasing/ascending order, and display the elements of the sorted array.

### [](#approach-2)Approach:

In this problem, you are asked to sort arrays using a specific sorting algorithm called **Counting Sort**.

Counting Sort is an integer sorting algorithm that operates by counting the occurrences of each unique value in the input array. Given that the values in the array are limited to the range `1` through `100`, we can directly use an auxiliary array (let’s call it `count`) to count the occurrences of each number in that range.

The steps for Counting Sort are as follows:

- **Count Occurrences**: Create a count array of size `101` (since values range from `1` to `100`). Each index `i` of the count array will store the frequency of the number `i`.

- **Populate the Count Array**: Traverse the input array and increment the respective index in the count array for each element.

- **Reconstruct the Sorted Array**: After populating the count array, iterate through the count array and reconstruct the sorted array by outputting each number according to its frequency.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N+K)`, where `N` is the number of elements in the array and `K` is the range of numbers. Since `K` is constant `(100)`, this simplifies to `O(N)` for each test case.

- **Space Complexity:** `O(K)`, which is `O(100)`, so it’s constant space for our case.

</details>
