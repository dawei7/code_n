# Counting Pretty Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NUM239 |
| Difficulty Rating | 873 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [NUM239](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/NUM239) |

---

## Problem Statement

Vasya likes the number $239$. Therefore, he considers a number *pretty* if its last digit is $2$, $3$ or $9$.

Vasya wants to watch the numbers between $L$ and $R$ (both inclusive), so he asked you to determine how many pretty numbers are in this range. Can you help him?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.

### Output
For each test case, print a single line containing one integer — the number of pretty numbers between $L$ and $R$.

### Constraints
- $1 \le T \le 100$
- $1 \le L \le R \le 10^5$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
1 10
11 33
```

**Output**

```text
3
8
```

**Explanation**

**Example case 1:** The pretty numbers between $1$ and $10$ are $2$, $3$ and $9$.

**Example case 2:** The pretty numbers between $11$ and $33$ are $12$, $13$, $19$, $22$, $23$, $29$, $32$ and $33$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
11 33
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/NUM239)

[Contest](https://www.codechef.com/LTIME61A/problems/NUM239)

**Author:** [Ivan Safonov](https://www.codechef.com/users/isaf27)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

CAKEWALK

# Prerequisites

Prefix sums

# Problem

You are given to integers L and R. Find the number of integers which have the last digit as 2, 3 or 9 and lie in the range [L, R].

# Explanation

As the constrainsts are small on L and R, we can pre-calculate all good numbers. Then each test case just asks to find out how many good numbers lie within the given range. This can be easily answered using prefix-sums. If you don’t know about prefix-sums, you can read it [here](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/). Basically the idea is the following:

\sum_{i=l}^{i=r} A_i = \sum_{i=1}^{i=r} A_i - \sum_{i=1}^{i=l-1} A_i

\sum_{i=l}^{i=r} A_i = \text{(Prefix-sum at i=r)} - \text{(Prefix-sum at i=l-1)}

Below is a pseudo-code for it:

``
	def init():
		for i in [1, 1000000]:
			last_digit = i % 10
			if last_digit == 2 or last_digit == 3 or last_digit == 9:
				good[i] = 1
			else:
				good[i] = 0

		# Build prefix sum
		for i in [1, 1000000]:
			good[i] += good[i-1]

	def solve(l, r):
		ans = good[r] - good[l-1]
		return ans

``

The time complexity of the above approach will be O(N + T), where N = 100000 is for pre-computation and T is for answering every test case in O(1) using prefix-sums. The space complexity of the above approach will be O(N) for storing the prefix array of good elements.

### Bonus Problem

Solve the problem without any pre-computation and in O(1) memory.

Idea:

Click to view

Note that every consecutive number from “x…0” to “x…9” has 3 good numbers.

Feel free to share your approach, if it was somewhat different.

# Time Complexity

O(N + T)

# Space Complexity

O(N)

# Solution Links

[Setter’s solution](http://www.codechef.com/download/Solutions/LTIME61/setter/NUM239.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME61/tester/NUM239.cpp)

[Editorialist solution](http://www.codechef.com/download/Solutions/LTIME61/editorialist/NUM239.cpp)

</details>
