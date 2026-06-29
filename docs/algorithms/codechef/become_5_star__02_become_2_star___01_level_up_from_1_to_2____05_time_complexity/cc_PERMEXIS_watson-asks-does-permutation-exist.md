# Watson asks Does Permutation Exist

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMEXIS |
| Difficulty Rating | 1207 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [PERMEXIS](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/PERMEXIS) |

---

## Problem Statement

Watson gives an array **A** of **N** integers **A1, A2, ..., AN** to Sherlock. He wants Sherlock to reorganize the array in a way such that no two adjacent numbers differ by more than 1.

Formally, if reorganized array is **B1, B2, ..., BN**, then the condition that **| Bi - Bi + 1 | ≤ 1**, for all **1 ≤ i < N**(where **|x|** denotes the absolute value of **x**) should be met.

Sherlock is not sure that a solution exists, so he asks you.

### Input

First line contains **T**, number of test cases. Each test case consists of **N** in one line followed by **N** integers in next line denoting **A1, A2, ..., AN**.

### Output

For each test case, output in one line **YES** or **NO** denoting if array **A** can be reorganized in required way or not.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **105**

- **1** ≤ **Ai** ≤  **109**

- Sum of **N** over all test cases  ≤ **2*105**

---

## Examples

**Example 1**

**Input**

```text
2
4
3 2 2 3 
2
1 5
```

**Output**

```text
YES
NO
```

**Explanation**

Test case 1:

No need to reorganise.

Test case 2:

No possible way.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
3 2 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2
1 5
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/PERMEXIS)

[Contest](http://www.codechef.com/COOK75/problems/PERMEXIS)

**Author and Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

**Tester:** [Kamil Debowski](http://www.codechef.com/users/errichto)

### DIFFICULTY:

simple

### PREREQUISITES:

logic, basic programming, sorting

### PROBLEM:

You are given a list of integers A_1, A_2, ..., A_N. You have to rearrange them to get B_1, B_2, ..., B_N. Also, the conditions that |B_i - B_{i + 1}| \le 1 should be satisfied \forall i < N.

You have to output if it’s possible to do so.

### QUICK EXPLANATION:

======================

If in sorted array A, any two adjacent elements differ by more than 1, answer is `NO`, otherwise `YES`.

### EXPLANATION:

================

**Claim** : If in sorted array A, any two adjacent elements differ by more than 1, answer is `NO`, otherwise `YES`.

**Proof**: Let’s assume there are two elements l and r in array A, where r - l > 1 and no other element lies between l and r. We have to show that there doesn’t exist a permutation of A where adjacent elements don’t differ by more than 1, no matter what the other elements of array A are.

We assume there exists such a permutation. Then, there are two cases:

-
l occurs before r in this permutation. Since each adjacent element differs by atmost 1, we can observe that we have to go from element l to r and in each step we can either remain at same value or increase by one or decrease by one, with the condition that new value should be present in array A. The only way to reach r is through r-1(since l occurs before r in array), which can’t be achieved since there is no such value in the array A.

-
r occurs before l in this permutation. Since each adjacent element differs by atmost 1, we can observe that we have to go from element r to l and in each step we can either remain at same value or increase by one or decrease by one, with the condition that new value should be present in array A. The only way to reach l is through l + 1(since r occurs before l in array), which can’t be achieved since there is no such value in the array A.

Pseudo code:

``A = []
scan(T)
for test = 0 to T - 1:
	ans = "YES"

	scan(N)
	for i = 0 to N - 1:
		scan(A[i])
	sort(A)
	for i  = 0 to N - 2:
		if A[i + 1] - A[i] > 1:
			ans = "NO"

	print ans
``

### COMPLEXITY:

================

O(N \text{log} N), since we sort array A.

### AUTHOR’S, TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/COOK75/Setter/PERMEXIS.cpp)

[tester](http://www.codechef.com/download/Solutions/COOK75/Tester/PERMEXIS.cpp)

</details>
