# Max Mex

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEX |
| Difficulty Rating | 1478 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [MEX](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/MEX) |

---

## Problem Statement

You are given a multi-set **S** of **N** integers, and an integer **K**. You want to find the maximum value of Minimum Excluded Value ([**MEX**](https://en.wikipedia.org/wiki/Mex_(mathematics))) of the multi-set given that you are allowed to add at most any **K** integers to the multi-set. Find the maximum value of MEX that you can obtain.

MEX (Minimum Excluded Value) is defined as the smallest non-negative integer (0, 1, 2, ...) that does not appear in a given multiset or array. Few examples of MEX of a multi-set are as follows. MEX of the multi-set {0} is 1, {1} is 0, {0, 1, 3} is 2, {0, 1, 2, 3, 5, 6} is 4.

### Input

The first line of the input contains an integer **T** denoting the number of testcases.

The first line of each test case contains two space seperated integers **N** and **K** denoting the size of the multi-set and the maximum number of extra integers that you can add in the multi-set respectively.

The second line contains **N** space separated integers denoting the multi-set **S**: **S1**, **S2** ,.... **SN**.

### Output

For each testcase, output the answer in a single line.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N** ≤ **105**

- **0** ≤ **K** ≤ **105**

- **0** ≤ **Si** ≤ **2 * 105**

### Subtasks

- **Subtask #1** (15 points): **K**=0.

- **Subtask #2** (85 points): Original Constraints.

---

## Examples

**Example 1**

**Input**

```text
4
3 0
1 0 2
3 1
1 0 2
4 3
2 5 4 9
2 0
3 4
```

**Output**

```text
3
4
6
0
```

**Explanation**

**Example case 1.** As **K** = 0, so we can't add any element to the multi-set. Elements of the set are {1, 0, 2}. The MEX value of this set is 3.

**Example case 2.** As **K** = 1, you are allowed to add at most 1 element to the multi-set. The multi-set are {1, 0, 2}. You can add element 3 to the multi-set, and it becomes {1, 0, 2, 3}. The MEX value of this multi-set is 4. There is no other way to have higher value of MEX of the set by adding at most one element to the multi-set.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 0
1 0 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 1
1 0 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4 3
2 5 4 9
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
2 0
3 4
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK

[Practice](https://www.codechef.com/problems/MEX)

[Contest](https://www.codechef.com/OCT17/problems/MEX)

**Author:** [Hruday Pabbisetty](https://www.codechef.com/users/hruday968)

**Tester:** [Alexey Zayakin](https://www.codechef.com/users/alex_2008)

**Editorialist:** [Jakub Safin](https://www.codechef.com/users/xellos0)

### DIFFICULTY

SIMPLE

### PREREQUISITIES

sorting, greedy algorithms

### PROBLEM

You are given a multiset of non-negative integers of size N; maximise its [minimum excluded](https://en.wikipedia.org/wiki/Mex_(mathematics)) non-negative integer by adding at most K integers to it.

### QUICK EXPLANATION

Sort S_1,\dots,S_N, remove duplicate elements. Greedily add numbers between elements S_i, the answer is the smallest number you can’t add; it’s possible to add all numbers between two consecutive elements at once.

### EXPLANATION

If we want the mex to be \ge k, we need to have all integers 0 through k-1 in the multiset.

The most straightforward algorithm would be to go through non-negative integers in increasing order. We can ignore integers that are already in the multiset. Whenever encountering an integer x that’s not in the multiset, we need to add it - if we didn’t do it, the mex would be at most x. The first such integer which we can’t add to our multiset (because we already added K of them) is the maximum possible mex.

If we simply mark the numbers from the initial multiset in an array of size \mathrm{max}S, we can determine if a number is in the initial multiset in O(1) and the time complexity of this greedy algorithm is O(\mathrm{max}S+K+N), since we only need to process at most K+N integers before stopping; the memory complexity is O(\mathrm{max}S).

The constraints are low enough that this is enough to solve the problem, but we can do better.

## A faster solution

Let’s make this algorithm independent on \mathrm{max}S.

We can sort the array S_{1..N} in non-decreasing order and discard duplicate elements, since the mex doesn’t depend on how many times each number occurs in the multiset, only which numbers; as we go through all non-negative integers, we can remember the index of the last element S_i we encountered (or i=0 if we haven’t encountered any yet). If i < N, then we know that the next number we could encounter that’s in the multiset is S_{i+1}; when that happens, we can just increment i by 1.

With this approach, we only need O(1) time with O(N) memory to check if a number is in the initial multiset and sorting takes O(N\log{N}), so the whole algorithm takes O(N\log{N}+K) time and O(N) memory.

## An even faster solution

Let’s make it independent on K, too.

Look at what we’re doing so far after sorting S and removing duplicates: add all numbers from 0 up to S_1-1 if we can, skip S_1, add all numbers from S_1+1 up to S_2-1 if we can, skip S_2, etc. Instead of adding numbers in a range [x,y] one by one, why not just subtract y-x+1 from K, since it has the same effect?

So, we can simply go through the numbers S_{1..N} and for each S_i, subtract S_i-1-S_{i-1} from K (we can consider S_0=-1 so that we’re subtracting S_1 for i=1). As soon as we can’t do this, because K < S_i-1-S_{i-1}, the only numbers we can add are S_{i-1}+1 through S_{i-1}+K and the answer will be S_{i-1}+K+1.

Naturally, if this didn’t happen for any i, then we should be adding numbers starting from S_N+1; the first number we couldn’t add is S_N+1+K, so that will be the answer.

This solution takes just O(N\log{N}) time and O(N) memory. There’s an additional \log factor, but we can solve the problem even for very large values of K and S_{1..N}.

### AUTHOR’S AND TESTER’S SOLUTIONS

[Setter’s solution](http://www.codechef.com/download/Solutions/OCT17/Setter/MEX.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/OCT17/Tester/MEX.cpp)

[Editorialist’s solution](https://ideone.com/1EaCz2)

</details>
