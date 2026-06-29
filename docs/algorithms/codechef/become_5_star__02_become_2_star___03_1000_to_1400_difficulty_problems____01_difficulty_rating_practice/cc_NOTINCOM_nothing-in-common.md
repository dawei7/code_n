# Nothing in Common

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOTINCOM |
| Difficulty Rating | 1386 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [NOTINCOM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/NOTINCOM) |

---

## Problem Statement

Alice has quarreled with Berta recently. Now she doesn't want to have anything in common with her!

Recently, they've received two collections of positive integers. The Alice's integers were **A1**, **A2**, ..., **AN**, while Berta's were **B1**, **B2**, ..., **BM**.

Now Alice wants to throw away the minimal amount of number from her collection so that their collections would have no common numbers, i.e. there won't be any number which is present in both collections. Please help Alice to find the minimal amount of numbers she would need to throw away.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two space-separated integer numbers **N** and **M** denoting the amount of numbers in Alice's and Berta's collections respectively.

The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the numbers of Alice.

The third line contains **M** space-separated integers **B1**, **B2**, ..., **BM** denoting the numbers of Berta.

### Output

For each test case, output a single line containing the minimal amount of numbers Alice needs to throw away from her collection so that she wouldn't have any numbers in common with Berta.

### Constraints

- **1** ≤ **Ai**, **Bi**  ≤ **106**

- All numbers are distinct within a single girl's collection.

### Subtasks

- **Subtask #1 (47 points)**: **T** = **25**, **1** ≤ **N, M** ≤ **1000**

- **Subtask #2 (53 points)**: **T** = **5**, **1** ≤ **N, M** ≤ **100000**

---

## Examples

**Example 1**

**Input**

```text
2
3 4
1 2 3
3 4 5 6
3 3
1 2 3
4 5 6
```

**Output**

```text
1
0
```

**Explanation**

**Example case 1.** If Alice throws away the number **3** from her collection, she would obtain **{1, 2}** which is disjoint with **{3, 4, 5, 6}**.

**Example case 2.** Girls don't have any number in common initially. So there is no need to throw away any number.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4
1 2 3
3 4 5 6
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 3
1 2 3
4 5 6
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NOTINCOM)

[Contest](https://www.codechef.com/LTIME44/problems/NOTINCOM)

**Author:** [Sergey Kulik ](https://www.codechef.com/users/errichto)

**Tester:** [Kamil Debowski](https://www.codechef.com/users/pkacprzak)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/errichto)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

Basic programming, sets

### PROBLEM:

The problem can be reformulated as follows: for given two sets of integers A and B, the goal is to find the minimum number of elements from A, such that after removing these elements from A, sets A and B do not have any common elements.

### QUICK EXPLANATION:

Find the intersection of A and B and return its size.

### EXPLANATION:

Since all numbers within A are distinct and also all elements within B are distinct, A and B are sets. What we want to do is to remove the minimum number of elements from A in such a way that A and B do not have any common elements. In other words, it means that we want to make their intersection empty, which means that if C is the intersection of A and B, we have to remove all elements of C, and there is no need to remove any other elements. Thus the problem is reduced to finding the size of the intersection of A and B. Depending on the subtask below methods are possible.

### Subtask 1

In this subtask, we know that each A and B have at most 1000 elements each and there are at most 25 test cases to handle. This allows us to iterate over all elements of A, and for each one perform a full scan over elements of B to check if the element belongs to both sets. For a single test case this method results in O(|A| \cdot |B|) time complexity.

### Subtask 2

In the second subtask, A and B can have up to 10^5 elements, which makes the above approach too slow. However, one can use a hash map to count the number of occurrences of all elements from A and B together. It follows that each element belongs to intersection of A and B if and only if its count is equal to 2. This approach has O(|A| + |B|) time complexity per single test case. It is worth to mention that since all input elements are positive integers not greater than 10^6, one can use a simple array instead of a hash map to compute the counters, which results in a similar time complexity and perhaps even easier implementation.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME44/Setter/NOTINCOM.cpp).

Tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME44/Tester/NOTINCOM.cpp).

</details>
