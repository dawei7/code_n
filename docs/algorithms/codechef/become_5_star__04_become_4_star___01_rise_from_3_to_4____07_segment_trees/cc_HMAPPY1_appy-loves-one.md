# Appy Loves One

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HMAPPY1 |
| Difficulty Rating | 1932 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [HMAPPY1](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/HMAPPY1) |

---

## Problem Statement

Chef has a sequence $A_1, A_2, \ldots, A_N$; each element of this sequence is either $0$ or $1$. Appy gave him a string $S$ with length $Q$ describing a sequence of queries. There are two types of queries:
- '!': right-shift the sequence $A$, i.e. replace $A$ by another sequence $B_1, B_2, \ldots, B_N$ satisfying $B_{i+1} = A_i$ for each valid $i$ and $B_1 = A_N$
- '?': find the length of the longest contiguous subsequence of $A$ with length $\le K$ such that each element of this subsequence is equal to $1$

Answer all queries of the second type.

### Input
- The first line of the input contains three space-separated integers $N$, $Q$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains a string with length $Q$ describing queries. Each character of this string is either '?', denoting a query of the second type, or '!', denoting a query of the first type.

### Output
For each query of the second type, print a single line containing one integer — the length of the longest required subsequence.

### Constraints
- $1 \le K \le N \le 10^5$
- $1 \le Q \le 3 \cdot 10^5$
- $0 \le A_i \le 1$ for each valid $i$
- $S$ contains only characters '?' and '!'

### Subtasks
**Subtask #1 (30 points):**
- $1 \le N \le 10^3$
- $1 \le Q \le 3 \cdot 10^3$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
5 5 3
1 1 0 1 1
?!?!?
```

**Output**

```text
2
3
3
```

**Explanation**

- In the first query, there are two longest contiguous subsequences containing only $1$-s: $A_1, A_2$ and $A_4, A_5$. Each has length $2$.
- After the second query, the sequence $A$ is $[1, 1, 1, 0, 1]$.
- In the third query, the longest contiguous subsequence containing only $1$-s is $A_1, A_2, A_3$.
- After the fourth query, $A = [1, 1, 1, 1, 0]$.
- In the fifth query, the longest contiguous subsequence containing only $1$-s is $A_1, A_2, A_3, A_4$ with length $4$. However, we only want subsequences with lengths $\le K$. One of the longest such subsequences is $A_2, A_3, A_4$, with length $3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/HMAPPY1/)

[Contest: Division 1](https://www.codechef.com/NOV18A/problems/HMAPPY1)

[Contest: Division 2](https://www.codechef.com/NOV18B/problems/HMAPPY1)

**Setter:** [Himanshu Mishra](https://www.codechef.com/users/hmrockstar)

**Tester:** [Zhong Ziqian](https://www.codechef.com/users/fjzzq2002)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Easy

### PREREQUISITES:

Segment Tree, Deque.

### PROBLEM:

Given a cyclic array A of length N, with current position being the first element, Perform following operations.

-
! Shift all elements to the right and make the last element as the first element.

-
? print the maximum number of consecutive 1s in the array. In case the answer is more than K, print K.

### SUPER QUICK EXPLANATION

- The value of K is irrelevant. We just need to calculate the longest contiguous sequence of 1s after any number of shifts.

- If we append an array to itself, the problem reduces to, Given a sequence of length 2*N, we need to answer the maximum length of the contiguous sequence of 1s in the range [pos, pos+n-1].

- We can use Segment Tree to calculate this, storing information for every node in segment tree [l,r] (Max length of consecutive ones in range l to r, Number of 1s at prefix of [l, r], Number of 1s at suffix of [l, r] and whether the segment contains a zero at all.)

- We can maintain a shift pointer which, on every shift query, moves one step to the left, and in case it is already at position 0, it moves to position N-1. This way, answer to every query is same as the answer to query [shuft, shift+N-1] to above segment tree.

### EXPLANATION

First of all, let’s see the brute force solution.

We can actually shift the array in O(N) time and for answering queries, we can iterate over the whole array again in O(N) time, Giving Overall Time complexity O(Q*N) which shall time out.

Now, Let us focus on a faster solution.

There are two (or even more) solutions, out of which, I am going to share a more general one, which has wider applications than the other, the Segment Tree solution.

In Segment Tree, we usually store some information for a node, and we should be able to combine information of two child nodes to get the same information for the parent node.

Segment Tree is simple, so, I’ll be focusing more on finding the answer using segment tree. Segment tree resources are listed at the end.

Let us call maximum length of contiguous 1s in a range [l,r] as range max of [l,r].

Now, For this problem, to answer the query, we need the range max for a segment.

Suppose we have it calculated the range max of two segments [l, mid] and [mid+1,r] and we need to combine this to calculate range max for segment [l,r].

But, the catch here is, that we cannot directly assume that maximum length of contiguous 1s in the range [l,r] is **just** the maximum of range max of both children.

Consider example: The array is 1 1 0 1 1 1 0 0

Assume l = 1, r = 8 and mid = 4. We see, that range max for [l,mid] is 2 and [mid+1,r] is 2, but range max of segment [l,r] is 3. This happened because the left segment’s suffix merged with the right segment’s prefix to form a larger segment. The left child had a suffix length 1, and the right child had prefix length 2, which merged to form a segment of length 3. Hence, we also need to store the length of contiguous 1s at the start of the segment as well as at the end of the segment.

Also, we need another variable telling whether a segment contains at least one 0 or not. The reason is, that if a segment does not contain 0 at all, this means that prefix and suffix are same as the length of a segment. This case needs to be handled specially.

Now, we are ready to merge the information of two children to calculate the same information for the parent node.

We need to consider all four cases, whether the left child contains 0, and whether the right child contains 0 or not. So, Here we go.

- If both left and right child do not contain 0, we see, that the range consists of all 1s, hence, prefix, suffix as well as range max are equal to the length of the segment.

- If only left child contains 0, we can see, that by merging, prefix of left child become prefix of parent, suffix of parent is the length of right child plus suffix of left child, and range max is maximum of range max of both segments, and the segment length formed by merging suffix of left child with whole right segment.

- If only right child contains 0, we can see, that prefix of the parent is formed by merging whole left child with the prefix of right child, and suffix of the parent is just the suffix of right child. The range max is the maximum of range max of both segments, as well as the maximum of segment length formed by merging whole left child with the prefix of the right child.

- Now, Both child contains 0, Then we see, that prefix of left child become prefix of parent, suffix of right child become suffix of parent, and range max of segment is maximum of range max of both segments, and the segment formed by merging suffix of left child and prefix of right child.

Proving the above is not hard, and this gives us a very neat and simple solution to solve the problem.

Let us append the array to itself, so we get a new array B of length 2*N with property that B[i] = B[i+N] \forall i \in [0, N-1]. Now, Consider one by one, the segments [0, N-1], [1, N], [2, N+1] and so on. You can see, that it is basically the different shifts of the array. So, we can change the rotation to shifts in the array B.

We can reformulate the problem as.

Given an array B of length 2*N, we need to find maximum length of contiguous sequence between range [P, P+N-1] for a given P

This can be easily answered using the above segment tree.

But as the problem says, we should report a segment only of length \leq K, we print K if the length of the sequence we find is greater than K.

This completes another Segment Tree problem. But we still need to practice segment trees, so here we go.

An excellent blog on Segment tree [here](https://codeforces.com/blog/entry/15890).

A nice set of problems to practice we may find [here](https://www.codechef.com/certification/prepare#advanced).

**Alternative Implementations**

An alternate solution could be based on observation, that after handling the case in which array consists of 1 only, there will be at least two disjoint segments consisting of 1s only, considering First and Last elements to be neighbors. At any moment, due to shifting, only one of these segments can be split (divided due to the border). We can see, that we can find the maximum length of contiguous sequence containing 1 by considering the position of the shift, and making cases on basis of the position of largest two segments consisting of 1s only, which we can find beforehand.

### Time Complexity

Time complexity is O((N+Q)*logN). O(N*logN) for building Segment Tree while (Q*logN) for processing answer queries.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/NOV18/setter/HMAPPY1.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/NOV18/tester/HMAPPY1.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/NOV18/editorialist/HMAPPY1.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
