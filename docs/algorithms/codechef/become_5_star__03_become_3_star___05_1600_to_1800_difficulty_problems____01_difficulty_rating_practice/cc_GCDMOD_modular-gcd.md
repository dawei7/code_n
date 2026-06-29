# Modular GCD

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCDMOD |
| Difficulty Rating | 1741 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [GCDMOD](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/GCDMOD) |

---

## Problem Statement

At ShareChat, there are are plenty of interesting problems to solve. Here is one of them.

Given integers $A$, $B$ and $N$, you should calculate the GCD of $A^N + B^N$ and $|A - B|$. (Assume that $GCD(0, a) = a$ for any positive integer $a$). Since this number could be very large, compute it modulo $1000000007$ ($10^9 + 7$).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $A$, $B$ and $N$.

### Output
For each test case, print a single line containing one integer — the required GCD modulo $10^9 + 7$.

### Constraints
- $1 \le T \le 10$
- $1 \le A, B, N \le 10^{12}$
- $B \le A$

### Subtasks
**Subtask #1 (10 points):** $1 \le A, B, N \le 10$

**Subtask #2 (40 points):** $1 \le A, B, N \le 10^9$

**Subtask #3 (50 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
10 1 1
9 1 5
```

**Output**

```text
1
2
```

**Explanation**

**Example case 1:** $GCD(10^1 + 1^1, 10 - 1) = GCD(11, 9) = 1$

**Example case 2:** $GCD(9^5 + 1^5, 9 - 1) = GCD(59050, 8) = 2$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
9 1 5
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/AUG18B/problems/GCDMOD)

[Contest](https://www.codechef.com/AUG18B/problems/GCDMOD)

**Author:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

**Tester:** [Mark Mikhno](https://www.codechef.com/users/famafka)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

EASY-MEDIUM

# Prerequisites

GCD, Modular Exponentiation, Overflow-handling

# Problem

Find the GCD of A^N + B^N and (A - B) modulo 1000000007.

# Explanation

The only property required to solve the complete problem is GCD(U, V) = GCD(U \% V, V). If you are unfamiliar with this, you can see the proof [here](http://joequery.me/notes/proof-a-bqr-gcd/).

Now the problem remains finding the value of (A^N + B^N) % (A - B). This is can be easily done using modular exponentiation in O(\log{N}) complexity. You can read about on [wikipedia](https://en.wikipedia.org/wiki/Modular_exponentiation) and implementation at [Geeks for Geeks](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/).

With the above 2 things, you are almost close to the full solution. The only thing left now is to handle overflows in languages like C++ and Java. First, understand why we might get overflow and then how we handle it.

Note that we are computing A^N % (A - B). Since, (A - B) can be of the order {10}^{12}, the intermediate multiplications during exponentiation can be of the order of {10}^{12} * {10}^{12} = {10}^{24} which is too large to fit in **long long** data type. Due, to overflows, you will get the wrong answer. To deal with overflows, below are 3 different methods:

- Using “int_128” inbuilt datatype in C++. For details, you can refer to [mgch solution].

This approach has a complexity of O(1).

- Using an idea similar to modular exponentiation. Instead of carrying out multiplication operations, we use addition operations. Below is a pseudo-code for it:

``
	# Returns (a * b) % m
	def mul_mod(a, b, m):
		x = 0, y = a
		while b > 0:
			if b & 1:
				# No overflows in additons.
				x = (x + y) % m
			y = (y + y) % m
			b >>= 1
		return x

``

This approach has a complexity of O(\log{B}).

- Using idea similar to karatsuba trick. This is specific only to this question as constraints are upto {10}^{12} and not {10}^{18}. We can split a as a_1 * {10}^{6} + a_2 and b as b_1 * {10}^{6} + b_2. Note that all a_1, b_1, a_2, b_2 are now less than or equal to {10}^{6}. Now we multiply both of them and there will be no overflow now in intermediate multiplications as the maxmium value can be {10}^{12} * max(a_1, b_1) = {10}^{18}. The setter code using this approach.

The time complexity of this approach is O(1).

The final corner case to solve the problem is the case when A = B. This is because calculating A^N + B^N % (A - B), would lead to runtime error while calculating modulo 0. For this case, we use the fact that GCD(U, 0) = U. Thus the answer is simply A^N + B^N.

The last part is just printing the answer modulo 1000000007.

The overall time complexity is O(\log{N} + \log{max(A, B)}). The first is for calculating the modular exponentiation and the second part is for calculating GCD. The space complexity is O(1).

Once, you are clear with the above idea, you can see the author implementation below for help.

Note that since the number of test cases was small, another approach which iterates over divisors of (A - B) to find the answer will also pass within the time limit if proper care is taken of overflows and the case A = B.

Feel free to share your approach as well, if it was somewhat different.

# Time Complexity

O(\log{N} + \log{max(A, B)})

# Space Complexity

O(1)

# SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/AUG18/setter/GCDMOD.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/AUG18/tester/GCDMOD.cpp).

mgch’s solution can be found [here](http://www.codechef.com/download/Solutions/AUG18/editorialist/GCDMOD.cpp).

</details>
