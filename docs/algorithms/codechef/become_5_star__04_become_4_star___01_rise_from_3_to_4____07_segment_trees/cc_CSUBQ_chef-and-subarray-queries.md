# Chef and Subarray Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CSUBQ |
| Difficulty Rating | 2345 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [CSUBQ](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/CSUBQ) |

---

## Problem Statement

Chef has an array **A** consisting of **N** non-negative integers. Initially, all the elements are zero. Assume 1-based indexing. Chef is given two positive integers **L** and **R**. **(L <= R)** Chef has to execute **Q** number of queries on the array **A**. These queries can be of the following two types:

**1 x y (1 ≤ x ≤ n)** - Replace the value of **xth** array element by **y**.

**2 l r (1 ≤ l ≤ r ≤ n)** - Return the number of subarrays **[a , b]** that lies in subarray **[l , r]** such that the value of the maximum array element in that subarray is atleast **L** and atmost **R**.

         (A subarray **[a , b]** lies in a subarray **[l , r]** if and only if **a >= l** and **b <= r**)

Since, Chef couldn't solve this task, can you please help him solve this task?

### Input

The first line contains four space separated positive integers **N, Q, L** and **R** denoting the total number of elements in an array, total number of queries, value of **L**, and value of **R** respectively.

Each of the next **Q** lines contains one of the two queries described above.

### Output

For each query of type 2, print the required answer in a new line.

### Constraints
**

1 ≤ N, Q ≤ 5 * 10^5
**
**

1 ≤ L ≤ R ≤ 10^9
**
**

1 ≤ l ≤ r ≤ N
**
**

1 ≤ x ≤ N
**
**

1 ≤ y ≤ 10^9
**

### Subtasks

**Subtask #1** (10 points) : 1 ≤ N , Q ≤ 100

**Subtask #2** (15 points) : 1 ≤ N , Q ≤ 5000

**Subtask #3** (27 points) : 1 ≤ Q ≤ 10^4

**Subtask #4** (48 points) : Original Constraints

---

## Examples

**Example 1**

**Input**

```text
5 6 1 10
1 1 2
2 1 5 
1 3 11
1 4 3
2 3 5
2 1 5
```

**Output**

```text
5
2
4
```

**Explanation**

**Query 1.**

 A = {0, 0, 0, 0, 0}

After replacing value of 1st element by 2,

A = {2, 0, 0, 0, 0}

**Query 2.**

A = {2, 0, 0, 0, 0}

All the subarrays that lies in a subarray [1 , 5] whose maximum value is atleast 1 and atmost 10 are -

 [1 , 1], [1 , 2], [1 , 3], [1 , 4] and [1 , 5]. Thus the answer is 5.

**Query 3.**

A = {2, 0, 0, 0, 0}

After replacing value of 3rd element by 11,

A = {2, 0, 11, 0, 0}

**Query 4.**

A = {2, 0, 11, 0, 0}

After replacing value of 4th element by 3,

A = {2, 0, 11, 3, 0}

**Query 5.**

A = {2, 0, 11, 3, 0}

All the subarrays that lies in a subarray [3 , 5] whose maximum value is atleast 1 and atmost 10 are -

 [4 , 4] and [4 , 5]. Thus the answer is 2.

**Query 6.**

A = {2, 0, 11, 3, 0}

All the subarrays that lies in a subarray [1 , 5] whose maximum value is atleast 1 and atmost 10 are -

 [1 , 1], [1 , 2], [4 , 4] and [4 , 5]. Thus the answer is 4.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CSUBQ)

[Contest](http://www.codechef.com/NOV17/problems/CSUBQ)

**Author:** [Deepjal Chhetri](http://www.codechef.com/users/code_hard123)

**Tester:** [Istvan Nagy](http://www.codechef.com/users/iscsi)

**Editorialist:** [Oleksandr Kulkov](https://www.codechef.com/users/melfice)

### DIFFICULTY:

MEDIUM

### PREREQUISITES:

Segment trees

### PROBLEM:

You are to answer the following queries on an array (initially, all elements are zero):

-
**1 x y** - Change x'th element to y

-
**2 l r** - Count the number of subarrays [l_1, r_1] of subarray [l, r] (that is, l\le l_1\le r_1\le r), whose maximum element lies in range [L, R]. **Numbers L and R are the same in all queries.**

### QUICK EXPLANATION:

Write the number of subarrays whose maximum element lies in the range [L, R] as:

|\{\text{subarrays with max}\in[L,R]\}|=|\{\text{subarrays with max} < R+1\}|-|\{\text{subarrays with max} < L\}|

Observe that:

|\{\text{subarrays with max} < X\}|=|\{\text{subarrays with all elements} < X\}|

For X=L and X=R+1, maintain an array whose element at position i is 0 if a[i]\ge X and 1 if a[i] < X. The query 2 now reduces to: “count number of subarrays on segment [l,r] consisting entirely of ones”. This new problem can be solved using segment tree.

### EXPLANATION:

Refer to the “Quick explanation” section for the first part of the solution. The problem is now reduced to answering the following queries for fixed X:

-
**1 x y** - Change x'th element to y (y\in\{0, 1\})

-
**2 l r** - Count the number of subarrays [l_1, r_1] of subarray [l, r] (that is, l\le l_1\le r_1\le r) consisting of 1's. **Number X is the same in all queries.**

Use segment tree to solve this problem. In each node, store the following information:

``struct Node {
    long long num_ones_subarrays;
    int len, len_ones_left, len_ones_right;
};
``

Here,

-
len is the length of the range [l;r] represented by the node (len=r-l+1)

-
num_ones_subarrays is the number of subarrays consisting of ones in the range represented by the node

-
len_ones_left is the length of the largest prefix consisting of ones in the range represented by the node

-
len_ones_right is the length of the largest suffix consisting of ones in the range represented by the node

In order to solve the problem we should show that the stored information is self-sufficient, that is, we can merge two nodes and recalculate all 4 variables. So, suppose that nodes a and b are being merged into node res. Then:

- Length of res range is the sum of lengths of ranges a and b.

- The number of ones subarrays in the res range can be calculated as the sum of number of subarrays lying completely in a range (a.num_ones_subarrays), in b range (b.num_ones_subarrays) and the number of subarrays that cross the boundary between a and b. As the subarrays should be non-empty and should consist of ones, it is a.len_ones_right\times b.len_ones_left.

- The length of the largest prefix of ones in the res range is len_ones_left if there is at least one zero in the range a, that is, if a.len_ones_left \neq a.len. Otherwise, it is a.len_ones_left+b.len_ones_left.

- The length of the largest suffix is computed similarly.

This corresponds to the following `Node` merge code:

``Node merge(Node a, Node b) {
    Node res;

    res.len = a.len + b.len;

    res.num_ones_subarrays =
        a.num_ones_subarrays +
        b.num_ones_subarrays +
        a.len_ones_right * (li)b.len_ones_left;

    res.len_ones_left = a.len_ones_left;
    if (a.len_ones_left == a.len)
        res.len_ones_left += b.len_ones_left;

    res.len_ones_right = b.len_ones_right;
    if (b.len_ones_right == b.len)
        res.len_ones_right += a.len_ones_right;

    return res;
}
``

The time complexity of the solution is O((N+Q)\log N) from the underlying segment tree (it is possible to make it O(N+Q\log N) by building the segment tree in linear time). The memory complexity of the solution is O(N).

The implementation with 2 separate segment trees for different X=L and X=R+1 is enough to get AC, yet it is possible to make it faster via combining the trees into one.

As the input is quite large, care should be taken to avoid unnecessary input lag. For example, using C++ iostreams consider adding:

``ios_base::sync_with_stdio(false);
cin.tie(nullptr);
``

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/NOV17/Setter/CSUBQ.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/NOV17/Tester/CSUBQ.cpp).

Editorialist’s solution can be found [here](http://www.codechef.com/download/Solutions/NOV17/Editorialist/CSUBQ.cpp).

### RELATED PROBLEMS:

</details>
