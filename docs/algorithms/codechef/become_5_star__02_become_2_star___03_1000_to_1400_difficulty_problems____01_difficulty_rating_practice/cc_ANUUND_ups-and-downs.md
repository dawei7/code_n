# Ups and Downs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANUUND |
| Difficulty Rating | 1198 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ANUUND](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ANUUND) |

---

## Problem Statement

### Problem description

You will be given a zero-indexed array **A**. You need to rearrange its elements in such a way that the following conditions are satisfied:

- **A[i] ≤ A[i+1]** if **i** is even.

- **A[i] ≥ A[i+1]** if **i** is odd.

In other words the following inequality should hold: **A[0] ≤ A[1] ≥ A[2] ≤ A[3] ≥ A[4]**, and so on. Operations **≤** and **≥** should alter.

### Input

The first line contains a single integer **T** denoting the number of test cases. The first line of each test case contains an integer **N**, that is the size of the array **A**. The second line of each test case contains the elements of array **A**

### Output

For each test case, output a single line containing **N** space separated integers, which are the elements of **A** arranged in the required order. If there are more than one valid arrangements, you can output any of them.

### Constraints

- **1** ≤ **N** ≤ **100000**

- **Sum of N in one test file** ≤ **600000**

- **1** ≤ **A[i]** ≤ **10^9**

---

## Examples

**Example 1**

**Input**

```text
2
2
3 2
3
10 5 2
```

**Output**

```text
2 3
2 10 5
```

**Explanation**

**Example case 1.**
**A[0]** ? **A[1]** is satisfied, 2 ? 3.

**Example case 2.**
**A[0]** ? **A[1]** is satisfied, 2 ? 10.
**A[1]** ? **A[2]** is satisfied, 10 ? 5.
**Note:** 5 10 2 is also valid answer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
3 2
```

**Output for this case**

```text
2 3
```



#### Test case 2

**Input for this case**

```text
3
10 5 2
```

**Output for this case**

```text
2 10 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ANUUND)

[Contest](http://www.codechef.com/COOK46/problems/ANUUND)

**Author:** [Anudeep Nekkanti](http://www.codechef.com/users/anudeep2011)

**Tester:** [Gerald Agapov](http://www.codechef.com/users/gerald)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

EASY

### PREREQUISITES:

AD-HOC, sorting

### PROBLEM:

Given an array A. Rearrange the array in such a way that A[1] <= A[2] but A[2] >= A[3] and A[3] <= A[4] upto A[N-1] <>= A[N] (depending on the parity of N) is satisfied.

More Formally,

A[i] <= A[i + 1] if i is odd.

A[i] >= A[i + 1] if i is even.

### QUICK EXPLANATION

- O(N logN) Solution: Sort the array A. Pick A[1], then pick A[N - 1], A[2], A[N - 2] etc upto Nth element.

- O(N) Solution: Go from A[1] to A[N] in left to right order, if at any point of time, condition of given inequalities are not satisfied, then swap the elements in such a way that the condition is satisfied. We will prove in next section why this approach will always work.

### EXPLANATION

#### O(N logN) Solution:

First step is to sort the array A.

Now we have to build an array B such that it contains the elements of A in rearranged way. They B array is our answer to the given problem.

We will first add A[1] in B, then A[N - 1], then A[2], A[N - 2], A[3], A[N - 3] etc.

Note that this approach is always going to produce correct result because at the current step we are always picking the smallest and largest possible numbers which we can still pick, hence the inequality conditions given in the problem are never violated.

**Sample Execution:**

Let A = [4, 3, 5, 1].

Sort the array A.

A now becomes = [1, 3, 4, 5].

Our array B will be [1, 5, 3, 4].

**Complexity**: O(N log N).

All we need to do is to sorting of an array, All other operation costs only O(N) time. Hence time complexity is O(N log N).

#### O(N) Solution

We will go from left to right from A[1] to A[N]. If at any position, our inequality condition is unsatisfied, we will make a swap of i and i + 1 entries.

**Sample Execution:**

Let A = [4, 3, 5, 1, 2].

If we are first element (i = 1): A[1] <= A[2] is not satisfied, so we will swap A[1] and A[2].

So A will now become: [3, 4, 5, 1, 2]

Now we are at second element (i = 2): A[2] >= A[3] is not satisfied, so we will swap A[2] and A[3].

So A will now become: [3, 5, 4, 1, 2]

Now we are at third element (i = 3): A[3] <= A[4] is not satisfied, so we will swap A[3] and A[4].

So A will now become: [3, 5, 1, 4, 2]

Now we are at fourth element (i = 4): A[4] >= A[5] is satisfied, so we dont need to swap.

So A will remain as it is: [3, 5, 1, 4, 2]

**Proof Of Correctness:**

Assume that a, b, c, be the leftmost(Ordered from A[1] to A[N], A[1] is leftmost, A[N] is rightmost) elements of the array A for which condition is not satisfied. Let us assume that a be the elements which just precedes b. (ie order of occurrence of elements is a, b, c)

Let us suppose we want b >= c. (a <= b).

According to our assumption, a <= b is already satisfied, but b >= c is not satisfied (ie b < c)

Now on swapping b and c, our new order of elements will be a, c, b.

Note that now in this order a <= c(because a <= b < c).

and we have c >= b. (because c > b).

We can handle the second case in the exactly similar way too (Case when a >= b is satisfied but b <= c is not satisfied). This case is left for readers to prove.

**Complexity**: O(N):

For each index i from 1 to N, we can make at most 1 swap, Swap operation is constant operation, Hence we will only make total O(N) operations.

### AUTHOR’S, TESTER’S AND EDITORIALIST’s SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/COOK46/Setter/UND.cpp)

[Tester’s solution](http://www.codechef.com/viewplaintext/3925186)

[Editorialists’s solution](http://www.codechef.com/viewplaintext/3923868)

</details>
