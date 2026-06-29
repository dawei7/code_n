# Chef and Sub Array 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSUBA |
| Difficulty Rating | 1908 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [CHEFSUBA](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/CHEFSUBA) |

---

## Problem Statement

Chef has a binary array **A** of length **N**. He also has a frame that can focus on at max **K** consecutive elements of the array.

Chef has a lovely dog which likes to do following two things.

- Shifting the array **A** to the right by one element (**N**-th element becomes 1st, 1st becomes 2nd and so on)

- Asking Chef what is the maximal number of elements equal to 1, that can be captured by a frame (frame can capture **not more** than **K** consecutive elements of array).

Help Chef entertain his Dog!

### Input

The first line of each test case contains three integers **N**, **K** and **P** denoting the number of elements in array **A**, size of a frame and the number of Dog's requests.

The second line contains **N** space-separated integers **A**1, **A**2, ..., **AN** denoting the elements of array.

The third line contains string consisting of **P** characters, i-th character stands for dog's i-th question and equals **'!'** if  Dog shifts the array and **'?'** if dog asks what is the maximal number of ones captured by the frame.

### Output

For each Dog's question output a single line containing an integer corresponding to the answer of the question.

### Constraints

- 1 ≤ **N, K, P** ≤ 105

- 0 ≤ **Ai** ≤ 1

### Subtasks

- **Subtask #1  (30 points)** **N, K, P** ≤ 103

- **Subtask #2 (70 points)** Original constraints.

---

## Examples

**Example 1**

**Input**

```text
5 3 4
1 0 0 1 1
?!!?
```

**Output**

```text
2
3
```

**Explanation**

**Example case 1.**

For the first question , Chef can pick last **3** elements (or last two, no matter) for his frame,
and will have **2** elements equal **1**.

After first shift (exclamation mark) array will become: **1 1 0 0 1**.

After second shift (exclamation mark) array will become: **1 1 1 0 0**.

Now for the second question Chef can pick first **3** elements for his frame,
and will have **3** elements equal **1**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/CHEFSUBA)

[Contest](https://www.codechef.com/MAY17/problems/CHEFSUBA)

**Author:** [Dmytro Berezin](https://www.codechef.com/users/berezin)

**Tester:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak) and [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

EASY-MEDIUM

# Prerequisites

Segment trees, Deque, Rotation trick

# Problem

You are given an array A consisting of 0 and 1. You need to perform 2 type of queries of the array.

- Find the maximum number of 1’s in the array covered by frame having size less than or equal to k

- Shift the array to the right by 1 element. (circular rotation)

# Quick Explanation

Remove the rotation part in problem by duplicating the array. Pre-compute the answer for each window of size less than or equal to k. Use segment trees to answer the maximum in a range.

# Explanation

Let us first remove the query regarding rotation from the problem. This is a known trick where we remove the rotation using duplication of the array. To consider this aspect, see this example below :

Let array A be \{1, 0, 0, 1, 1\}. Duplicate this array i.e. \{1, 0, 0, 1, 1, 1, 0, 0, 1, 1\} and call it as B. Now, you can see that we can obtain all the arrays possible after rotation. They are just contiguous sub-arrays of length n in the above array B. For example, after 2 rotations, we can consider the subarray from position 3 to 7 as the required array. (0-based indexing)

Now, for the rotation query, we just need to handle the starting position in the above array B. So, these queries can be handled in O(1)

Once, we have removed the rotations part from the problem, we can pre-compute the number of 1’s in window of size k for all sub-arrays in B. Also, since we want to maximise the number of 1’s in the frame, we can always greedily chose frame of size k only. Doing this in a naive way will take complexity O(n^2), as we will loop over sub-arrays and each sub-array will take O(n) in worst case. We can using sliding window concept here to calculate the number of ones in all frames of size k. The logic behind this is as follows :

First we compute the answer for all positions which are less the k. After that, suppose we want to find the answer for a position starting at, say x and ending at (x+k-1). We see that only one element moves out of the window and only one element enters the windows as we slide it. Thus, these operations can be done in O(n). Below is a pseudo code for it.

``
sum[0] = 0
for i in 1 to k:
	sum[i] = sum[i-1] + b[i]
for i in k+1 to 2*n:
	sum[i] = sum[i-1] + b[i] - b[i-k]

``

For the sample array B given above and choosing k = 3, the sum array will look like \{1, 1, 1, 1, 2, 3, 2, 1, 1, 2\}.

Now, once we have calculated all the above sums, the question just reduces to finding the windows with maximum sum. Now, if the window is of size greater than or equal to the array size, then the answer is always the number of ones in the array else the answer is the maximum sum we can obtain by starting the window from 1 to (n-k+1). These range maximum queries can be easily with segment trees, sparse tables or in this specific cases using deques.

For handling the above minimum queries using segment trees or sparse table, one can refer to this editorial at [ topcoder ](https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/). For understanding a better algorithm, which uses deque and works in O(n), one can refer to this problem from [ Spoj](https://www.spoj.com/problems/ARRAYSUB/).

# Time Complexity

O(n \log{n}), if using segment trees / sparse tables

O(n) if using deques

# Solution Links

[Setter’s solution]

[Tester’s solution]

[Editorialist solution](https://www.codechef.com/viewsolution/13501361)

</details>
