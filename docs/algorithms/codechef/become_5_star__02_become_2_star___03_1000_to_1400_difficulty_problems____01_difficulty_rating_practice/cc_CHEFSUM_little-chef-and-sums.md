# Little Chef and Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSUM |
| Difficulty Rating | 1252 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHEFSUM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHEFSUM) |

---

## Problem Statement

Our little chef is fond of doing additions/sums in his free time. Today, he has an array **A** consisting of **N** positive integers and he will compute prefix and suffix sums over this array.

He first defines two functions **prefixSum(i)** and **suffixSum(i)** for the array as follows. The function **prefixSum(i)** denotes the sum of first **i** numbers of the array. Similarly, he defines **suffixSum(i)** as the sum of last **N - i + 1** numbers of the array.

Little Chef is interested in finding the minimum index **i** for which the value **prefixSum(i) + suffixSum(i)** is the minimum. In other words, first you should minimize the value of **prefixSum(i) + suffixSum(i)**, and then find the least index **i** for which this value is attained.

Since, he is very busy preparing the dishes for the guests, can you help him solve this problem?

### Input

The first line of the input contains an integer **T** denoting the number of test cases.

The first line of each test case contains a single integer **N** denoting the number of integers in the array **A**.

The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the array **A**.

### Output

For each test case, output a single line containing the answer.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N, A[i]** ≤ **105**

### Subtasks

- **Subtask #1 : (20 points) ** **1 ≤ N ≤ 100**

- **Subtask #2 : (80 points) ** Original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2 3
4
2 1 3 1
```

**Output**

```text
1
2
```

**Explanation**

**Example case 1.** Let's calculate prefixSum(i) + suffixSum(i) for all indexes **i** in the sample case.
`
prefixSum(1) + suffixSum(1) = 1 + 6 = 7
prefixSum(2) + suffixSum(2) = 3 + 5 = 8
prefixSum(3) + suffixSum(3) = 6 + 3 = 9
`

The minimum value of the function is 7, which is attained at index 1, so the answer would be 1.

**Example case 2.** Let's calculate prefixSum(i) + suffixSum(i) for all indexes **i** in the sample case.
`
prefixSum(1) + suffixSum(1) = 2 + 7 = 9
prefixSum(2) + suffixSum(2) = 3 + 5 = 8
prefixSum(3) + suffixSum(3) = 6 + 4 = 10
prefixSum(4) + suffixSum(4) = 7 + 1 = 8
`

The minimum value of the function is 8, which is achieved for indices 2 and 4. The minimum of these two indices 2, 4 is index 2. Hence, the answer will be 2.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
2 1 3 1
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFSUM)

[Contest](http://www.codechef.com/SEPT17/problems/CHEFSUM)

**Author:** [Prateek Gupta](http://www.codechef.com/users/prateekg603)

**Tester:** [Jingbo Shang](http://www.codechef.com/users/jingbo_adm)

**Editorialist:** [Hanlin Ren](http://www.codechef.com/users/r_64)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

You are given an array A of length N. Let PrefixSum(i) denote the sum of first i elements, and SuffixSum(i) denote the sum of last N-i+1 elements. Find an index i that PrefixSum(i)+SuffixSum(i) is the minimum. If there are many such indices, find the smallest one.

### QUICK EXPLANATION:

There are many solutions to this problem:

- We can calculate PrefixSum and SuffixSum in O(N) time, and just do what the problem asks; 64-bit integer types are needed;

- We can find the minimum element in the array, m, and output the smallest index i that A_i=m.

### EXPLANATION:

## subtask 1

We enumerate i. For a specific i, we compute the sum of first i elements(A[1\sim i]) and the sum of last N-i+1 elements(A[i\sim N]), then add the two sums together. We maintain the smallest answer ans and corresponding index. We enumerate i from 1 to N, so we only update the answer if PrefixSum(i)+SuffixSum(i) is strictly smaller than ans.

In this subtask, N\le 100 and A[i]\le 10^5, so PrefixSum(i)+SuffixSum(i)\le 10^7+10^5. When initializing ans, we need a number that’s big enough.

``ans = 20000000 //2*10^7
for i = 1 to N
	tmp = PrefixSum(i) + SuffixSum(i)
	if tmp < ans then
		ans = tmp
		ans_i = i
print ans_i
``

The overall complexity is O(N^2).

## subtask 2

We can compute PrefixSum and SuffixSum in O(N) time:

\begin{aligned}
PrefixSum(i)=&\begin{cases}0&i < 1\\PrefixSum(i-1)+A[i]&1\le i\le N\end{cases},\\
SuffixSum(i)=&\begin{cases}0&i > N\\SuffixSum(i+1)+A[i]&1\le i\le N\end{cases}.
\end{aligned}

Pseudocode:

``PrefixSum[0] = 0
for i = 1 to N
	PrefixSum[i] = PrefixSum[i - 1] + A[i]
SuffixSum[N + 1] = 0
for i = N downto 1
	SuffixSum[i] = SuffixSum[i + 1] + A[i]
``

Note that PrefixSum(i)+SuffixSum(i) can be very large: if N=10^5 and all A[i]'s are 10^5, then this sum can be as large as 10^{10}+10^5, so we should initialize ans to be a number big enough(e.g. 10^{11}). Also, 32-bit integers aren’t big enough to store such kind of numbers; we need 64-bit integers.

## A simpler solution

What is PrefixSum(i)+SuffixSum(i)? this sums up all elements in 1\sim i, and all elements in i\sim N. Thus, let Sum=A[1]+A[2]+\dots+A[N] be the sum of all numbers, then PrefixSum(i)+SuffixSum(i)=Sum+A[i], since only element i is counted twice, and all other elements are counted exactly once.

So, to find the index i that minimizes PrefixSum(i)+SuffixSum(i), we only need to find i that minimizes A[i]. Let m be the minimum element among A, we just find the smallest index i that A[i]=m.

Pseudocode:

``m = 100000
for i = 1 to N
	m = min(m, A[i])
for i = 1 to N
	if A[i] == m then
		print i and break
``

This approach is also O(N) and is easier to implement. Also, it doesn’t involve 64-bit integers.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/SEPT17/Setter/CHEFSUM.cpp)(This is not author’s, but Praveen’s).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/SEPT17/Tester/CHEFSUM.cpp).

Editorialist’s solution can be found [here](http://www.codechef.com/download/Solutions/SEPT17/Editorialist/CHEFSUM.py)

</details>
