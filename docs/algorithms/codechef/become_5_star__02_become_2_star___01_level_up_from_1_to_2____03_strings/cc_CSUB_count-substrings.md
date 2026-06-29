# Count Substrings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CSUB |
| Difficulty Rating | 1330 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [CSUB](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/CSUB) |

---

## Problem Statement

Given a string **S** consisting of only **1s** and **0s**, find the number of substrings which start and end both in **1**.

In this problem, a substring is defined as a sequence of continuous characters **Si, Si+1, ..., Sj** where **1 ≤ i ≤ j ≤ N**.

### Input

First line contains **T**, the number of testcases. Each testcase consists of **N**(the length of string) in one line and string in second line.

### Output

For each testcase, print the required answer in one line.

### Constraints

- **1** ≤ **T** ≤ **105**

- **1** ≤ **N** ≤ **105**

- Sum of  **N ** over all testcases ≤ **105**

---

## Examples

**Example 1**

**Input**

```text
2
4
1111
5
10001
```

**Output**

```text
10
3
```

**Explanation**

**Test case $1$:** All substrings of this string start and end with `1`. The substrings are $\{ 1, 1, 1, 1, 11, 11, 11, 111, 111, 1111 \}$. The total count of these substrings is $10$.

**Test case $2$:** Three substrings of this string start and end with `1`. These are $\{1, 1, 10001\}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1111
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
5
10001
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CSUB)

[Contest](http://www.codechef.com/JULY14/problems/CSUB)

**Author:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

**Tester:** [Shang Jingbo](http://www.codechef.com/users/jingbo_adm) and [Gerald Agapov](http://www.codechef.com/users/gerald)

**Editorialist:** [Devendra Agarwal](http://www.codechef.com/users/devuy11)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Adhoc

### PROBLEM:

Given a string S consisting of only 1’s and 0’s, find the number of substrings which start and end both in **1**.

### Quick Explanation

You need to find number of pairs of 1.

### Explanation

Find total number of 1’s in the given string. Let suppose that the total number of 1’s in the string is n , then the answer is (n*(n+1))/2.

**Reason**

Let’s suppose that the n 1’s in the string occur at x1 , x2, … , xn position in the string then all substring starting from xi and ending at xj are taken, so total possible ways in taking it is (n*(n+1))/2

**Pseudo Code**

``solve(string s)
	int n = 0
	for ( i = 0 ; i< s.size() ; i++)
		if s[i] == '1'
			n++
	return (n*(n+1))/2
``

**Complexity**:

O(N), You just need a single pass of the string.

### AUTHOR’S and TESTER’S SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/2014/July/Setter/CSUB.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/2014/July/Tester/CSUB.cpp)

</details>
