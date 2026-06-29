# A temple of Snakes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNTEMPLE |
| Difficulty Rating | 1800 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [SNTEMPLE](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/SNTEMPLE) |

---

## Problem Statement

You want to build a temple for snakes. The temple will be built on a mountain range, which can be thought of as **n** blocks, where height of i-th block is given by **h**i. The temple will be made on a consecutive section of the blocks and its height should start from 1 and increase by exactly 1 each time till some height and then decrease by exactly 1 each time to height 1,
i.e. a consecutive section of 1, 2, 3, .. x-1, x, x-1, x-2, .., 1 can correspond to a temple. Also, heights of all the blocks other than of the temple should have zero height, so that the temple is visible to people who view it from the left side or right side.

You want to construct a temple. For that, you can reduce the heights of some of the blocks. In a single operation, you can reduce the height of a block by 1 unit. Find out minimum number of operations required to build a temple.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains an integer **n**.

The next line contains **n** integers, where the i-th integer denotes **h**i

### Output

For each test case, output a new line with an integer corresponding to the answer of that testcase.

### Constraints

- 1 ≤ **T** ≤ 10

- 2 ≤ **n** ≤ 105

- 1 ≤ **h**i ≤ 109

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 1
4
1 1 2 1
5
1 2 6 2 1
```

**Output**

```text
0
1
3
```

**Explanation**

**Example 1**. The entire mountain range is already a temple. So, there is no need to make any operation.

**Example 2**. If you reduce the height of the first block to 0. You get 0 1 2 1. The blocks 1, 2, 1 form a temple. So, the answer is 1.

**Example 3**. One possible temple can be 1 2 3 2 1. It requires 3 operations to build. This is the minimum amount you have to spend in order to build a temple.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
1 1 2 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5
1 2 6 2 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SNTEMPLE)

[Contest](https://www.codechef.com/SNCKPA17/problems/SNTEMPLE)

**Author:** [admin2](https://www.codechef.com/users/admin2)

**Testers:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

Easy

### PREREQUISITES:

Binary search, precomputation

### PROBLEM:

Let a magic sequence of order m, denoted also by magic(m), be a sequence of a integers starting from 1 and increasing by 1 up to m and then decreasing from m to 1. For example, the magic sequence of order 5 is: 1, 2, 3, 4, 5, 4, 3, 2, 1. Notice that magic(m) has length 2 \cdot m - 1.

Given an array of h of n **positive** integers, denoting consecutive blocks, you want to perform the smallest number operations of reducing the high of a selected block by 1 in such a way that after all operations are performed, there exists exactly one magic sequence in h and all elements of h not included in the magic sequence are 0.

### EXPLANATION:

The problem can be reformulated as follows: find the largest possible integer m, such that there can be formed a magic sequence of order m in h. You might wonder why this problem is equivalent to the one asked in the original statement. Well, let s be the sum of all integers in h. In order to form the resulting sequence magic(m) in h and set all elements in h not included in this sequence to 0, we have to perform s - m \cdot (m+1) - m = s - m^2 operations, because the sum of heights in magic(m) is m^2. Since we want to minimize the number of performed operations, we want to maximize m.

The second crucial observation is that if we can form a sequence magic(m) in h, then for each k < m, we can also for a sequence magic(k) in h. This follows from the fact that in order to transform sequence magic(m) to magic(m-1), the only thing to do is to subtract one from each of its elements and remove the left-most and the right-most elements.

Based on the above two observations, we can use binary search to find the largest m, such that sequence magic(m) can be formed in h. The lower bound for binary search should be set to 1, and the upper bound can be set to for example n, but one can also compute the more exact upper bound, although it doesn’t matter much.

Now, how for a fixed m find out if a sequence magic(m) can be formed in h, and do it in linear time?

One possible solution is to compute two boolean arrays of size n:

L[i] := true if and only if the sequence 1, 2, \ldots, m can be formed in h[i-m+1], h[i-m+2], \ldots, h[i].

R[i] := true if and only if the sequence m, m-1, \ldots, 1 can be formed in h[i], h[i+1], \ldots, h[i+m-1].

Then, sequence magic(m) can be formed in h if and only if there exists i, 1 \leq i \leq n, such that both L[i] and R[i] are true. Thus the problem is reduced to computing arrays L and R.

Let’s take a closer look on how to compute array L. Computing array R is based on the same idea.

First of all, let’s set all entries in L to false. The idea is to iterate over h from left to right (right to left if you want to compute R) while updating variable k denoting the length of the longest sequence 1, 2, 3, \ldots, k ending in the current element, where k is at most m. The below pseudocode illustrates the approach:

``k = 0
for i = 1 to n:
    if h[i] >= k+1:
        k += 1
        if k == m:
            L[i] = true
            k -= 1
    else:
        k = h[i]
``

The above idea is based on the fact that if we have a sequence 1, 2, \ldots, k ending in i-1, then if h[i] is at least k+1 we can extend the sequence by one, and if h[i] is at most k, then the best we can do is to set k to h[i], because a sequence 1, 2, \ldots, k ending at index i-1 can be transformed to a non-longer sequence 1, 2, \ldots, h[i] ending at index i if h[i] \leq k.

Since the computing of arrays L and R takes O(n) time, and the range over we perform binary search has length O(n), the total time complexity is O(n \cdot \log(n)).

As it was pointed out with the comments, the above method can be improved to O(n) solution by avoiding binary search. The idea is to compute arrays L and R at the beginning, without specifying m. We define L[i] (and similarly R[i]) as the maximum length of sequence 1, 2, \ldots ending in i, and compute it as follows:

``k = 0
for i = 1 to n:
    if h[i] >= k+1:
        k += 1
    else:
        k = h[i]
    L[i] = k
``

Then, after computing arrays L and R, we know that the maximum m for which magic sequence of order m exists is \max\limits_{1 \leq i \leq n} \min(L[i], R[i])

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/download/Solutions/SNCKPA17/Setter/SNTEMPLE.cpp).

Tester’s solution can be found [here](https://www.codechef.com/download/Solutions/SNCKPA17/Tester/SNTEMPLE.cpp).

Editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/SNCKPA17/Editorialist/SNTEMPLE.cpp).

</details>
