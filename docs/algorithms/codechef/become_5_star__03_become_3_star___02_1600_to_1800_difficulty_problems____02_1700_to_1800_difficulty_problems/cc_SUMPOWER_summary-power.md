# Summary Power

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMPOWER |
| Difficulty Rating | 1709 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SUMPOWER](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SUMPOWER) |

---

## Problem Statement

You work as an engineer. You were given an empty board with $K$ consecutive cells; at any moment, each cell can display one character.

You want the board to display a string $S$ with length $N > K$. Since the board isn't large enough, you want to display the string in $N-K+1$ steps. In the $i$-th step ($1 \le i \le N-K+1$), you'll make the board display the characters $S_i, S_{i+1}, \dots, S_{i+K-1}$.

The power required to switch the board from step $i$ to step $i+1$ (for $1 \le i \le N-K$) is equal to the number of characters displayed on the board that have to change between these steps. You should find the total power required for the whole process of displaying a string, i.e. the sum of powers required for switching between all consecutive pairs of steps.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains a single string $S$ with length $N$.

### Output
For each test case, print a single line containing one integer — the total power required for text switching.

### Constraints
- $1 \le T \le 1,000$
- $2 \le N \le 10^5$
- $1 \le K \lt N$
- each character of $S$ is a lowercase English letter
- the sum of $N$ for all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (20 points):**
- $1 \le T \le 100$
- $2 \le N \le 50$

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
6 3
aabbcc
5 2
abccc
4 3
aabb
```

**Output**

```text
4
3
1
```

**Explanation**

**Example case 1:**
- In step $1$, the board is displaying "aab".
- In step $2$, the board is displaying "abb".
- In step $3$, the board is displaying "bbc".
- In step $4$, the board is displaying "bcc".

The power required for switching from the $1$-st to the $2$-nd step is $1$, because cell $1$ changes from 'a' to 'a' (requiring power $0$), cell $2$ changes from 'a' to 'b' (requiring power $1$) and cell $3$ changes from 'b' to 'b' (requiring power $0$); $0 + 1 + 0 = 1$.

The power required for switching between the $2$-nd and $3$-rd step is $2$ and the power required for switching between the $3$-rd and $4$-th step is $1$.

Therefore, the answer is $1 + 2 + 1 = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 3
aabbcc
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
5 2
abccc
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 3
aabb
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/SUMPOWER)

[Contest](https://www.codechef.com/LTIME61A/problems/SUMPOWER)

**Author:** [Ivan Safonov](https://www.codechef.com/users/isaf27)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

EASY

# Prerequisites

Prefix sums, Sliding Window

# Problem

You are given a string S of length N and an integer K. Consider all the (N - K + 1) substrings of S of length K. Find the sum of the hamming distance between 2 consecutive substrings, where hamming distance is defined as the number of positions where the characters of two strings differ.

# Explanation

For simplicity, the editorial assumes 0-based indexing of the string.

## Subtask 1: T ? 100, N ? 50

For the first subtask, a naive brute force is enough to solve it. Below is a pseudo-code for it.

``
	def hamming(string a, string b):
		diff = 0
		for i in [0, len(a) - 1]:
			if a[i] != b[i]:
				diff += 1
		return diff

	def solve(string s, int k):
		ans = 0
		for i in [0, k - 1]:
			sub_1 = s.substring(i, i + k - 1)
			sub_2 = s.substring(i + 1, i + k)
			ans += hamming(sub_1, sub_2)
		return ans

``

The complexity of the above approach will be O(N^2) per test case. This is not efficient for the second subtask.

## Subtask 2: T ? 100, N ? 100000

For this consider, let us consider an example string S = "aabbcc" and K = 3, same as in the problem statement. Below table shows the calculation for the above naive approach.

The naive approach tries to find the hamming distance of every row with the previous one and add it up. Let us see what happens when we try to find the differences along the column and them sum them up. The below table shows the calculation.

What advantage do we have while doing the above calculation in column manner? First, we don’t have to deal with full substrings. Instead, we deal with each column independently and all we care about is whether 2 consecutive characters in S are same or different.

The second one is that there is a lot of repetition in the calculation across columns, meaning that same set of different characters are repeated across many columns. For example, in the above case the pair (a, b) corresponding to letters at indices (1, 2) appears in column 1 and column 2.

So, let us store the difference array, diff, where diff[i] will be 1 if S[i] != S[i-1] else 0. using this, we can clearly see that answer for a column is just a sum of range for diff range. Using prefix sums, we can calculate the answer for every column in O(1). Then, we can add the contribution to all possible columns and find the overall answer.

Below is pseudo-code for the above approach:

``
	def solve(string s, int k):
		for i in [1, len(s) - 1]:
			if s[i] != s[i-1]:
				diff[i] = 1
			else:
				diff[i] = 0
		# Build prefix sum
		for i in [1, len(s) - 1]:
			diff[i] += diff[i-1]

		ans = 0
		for i in [0, k - 1]:
			ans += diff[i + (n - k)] - diff[i]
		return ans

``

The time complexity of the above approach will be O(N + K). The pre-computation will consist of 2 parts. First, finding the diff array and then calculating the prefix sum of diff array. Each step takes O(N) complexity. Then, we find the contribution for every column, which is K in total. The space complexity will be O(N) for this approach.

You can improve the space complexity to O(1) as well using sliding-window to approach to calculate the prefix-sums on the fly and hence the answer for every column.

For more details, you can refer to the editorialist’s solution for help.

### Bonus Problem

Construct a test case where the answer will overflow i.e. will not fit inside integer type and we would require the use of “long long” in C++ and “long” in Java.

Feel free to share your approach, if it was somewhat different.

# Time Complexity

O(N + K) per test case.

# Space Complexity

O(N)

# Solution Links

[Setter’s solution](http://www.codechef.com/download/Solutions/LTIME61/setter/SUMPOWER.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME61/tester/SUMPOWER.cpp)

[Editorialist solution](http://www.codechef.com/download/Solutions/LTIME61/editorialist/SUMPOWER.cpp)

</details>
