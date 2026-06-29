# Median of adjacent maximum numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXMEDIAN |
| Difficulty Rating | 1523 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [MXMEDIAN](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/MXMEDIAN) |

---

## Problem Statement

You are given an array **A** of size **2 * N** consisting of positive integers, where **N** is an odd number. You can construct an array B from **A** as follows, B[i] = max(**A**[2 * i - 1], **A**[2 * i]), i.e. B array contains the maximum of adjacent pairs of array **A**. Assume that we use 1-based indexing throughout the problem.

You want to maximize the [median](https://en.wikipedia.org/wiki/Median) of the array B. For achieving that, you are allowed to permute the entries of **A**. Find out the maximum median of corresponding B array that you can get. Also, find out any permutation for which this maximum is achieved.

### Note

Median of an array of size n, where n is odd, is the middle element of the array when it is sorted in non-decreasing order. Note that n being odd, the middle element will be unique, i.e. at index (n+1) / 2.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains an integer **N**.

The second line of each test case contains **2 * N** space separated integers denoting array **A**.

### Output

For each test case, output two lines.

The first of which should contain an integer corresponding to maximum value of the median of array B that you can get.

In the second line, print **2 * N** integers in a single line denoting any permutation of **A** for which the maximum value of median of array B is achieved.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 50000

- 1 ≤ **A**i ≤ 2 * N

### Subtasks

- **Subtask #1** (25 points) : 1 ≤ N ≤ 3

- **Subtask #2** (75 points) : original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1
1 2
3
1 2 3 4 5 6
3
1 3 3 3 2 2
```

**Output**

```text
2
1 2
5
1 3 2 5 4 6
3
1 3 3 3 2 2
```

**Explanation**

**Example case 1.** There are only two possible permutations of **A**, for both of those B will be 2. The median of B is 2.

**Example case 2.** For following permutation of A: 1 3 2 5 4 6, the corresponding B will be: 3 5 6, whose median is 5, which is the maximum that you can achieve.

**Example case 3.** For A: 1 3 3 3 2 2, the corresponding B will be: 3, 3, 2. Its
median is 3, which is maximum that you can achieve.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/MXMEDIAN)

[Contest](https://www.codechef.com/MAY17/problems/MXMEDIAN)

**Author:** [Praveen Dhinwa](https://www.codechef.com/users/admin2)

**Tester:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak) and [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

EASY

# Prerequisites

Greedy, Sorting, Median

# Problem

You are given an array A of size 2 * N consisting of positive integers, where N is an odd number. You can construct an array B from A as follows, B[i] = max(A[2 * i - 1], A[2 * i]). Consider all permutations of A. Print any one of them which maximises the median of B

# Explanation

The larger elements we have in the array B, the larger will be its median. Since, array B has n elements only, we would like to have the largest n elements of A somehow, go into the array B. Let us assume we have a black box which permutes array A in some manner such that the largest n elements go into array B. Now, what will be the median of array B in such a case? It will be simply the middle element once the array B is sorted.

Now, let us describe the black box now. We see that elements of B are from adjacent elements from A. i.e. they are independent of each other in their selection. Thus, we simply put all the highest n elements in either odd or even positions in array A. This will ensure that are always selected into array B. So, the only requirement is to sort the array A to get the highest n elements. The sorting can be done using mergesort, randomised quick-sort or any inbuilt sort function available.

The above is just one of the methods to construct the array and solve the problem. Multiple solutions to the problem might exist. Feel free to discuss them below.

# Time Complexity

O(n \log{n}) per test case

# Solution Links

[Setter’s solution]

[Tester’s solution]

[Editorialist solution](https://www.codechef.com/viewsolution/13477095)

</details>
