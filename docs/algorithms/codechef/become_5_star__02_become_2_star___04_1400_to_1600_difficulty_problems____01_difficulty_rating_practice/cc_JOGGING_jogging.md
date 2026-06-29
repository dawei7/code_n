# Jogging

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JOGGING |
| Difficulty Rating | 1484 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [JOGGING](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/JOGGING) |

---

## Problem Statement

Alice jogs everyday to keep herself fit and active. She noticed that she burns $X$ calories when jogging the first kilometer, and for $K > 1$, jogging the $K^{th}$ kilometer burns calories equivalent to the total number of calories burned while jogging the first $K-1$ kilometers.

What is the total number of calories that Alice burns after jogging for $N$ kilometers? The answer can be very large, so report it modulo $10^9 + 7$ ($1000000007$).

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $X$, as described in the problem statement.

---

## Output Format

For each test case, output on a new line the total number of calories that Alice burns after jogging for $N$ kilometers, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^6$
- $1 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
1 2
2 1
12548 1
```

**Output**

```text
2
2
588809226
```

**Explanation**

**Test case $1$:** Alice only jogs one kilometer, which burns $2$ calories since $X = 2$.

**Test case $2$:** Alice jogs two kilometers. The first burns $X = 1$ calorie, and the second also burns $1$ calorie since the total amount burnt before this is $1$ calorie. So, the total is $1 + 1 = 2$ calories burned.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
12548 1
```

**Output for this case**

```text
588809226
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START44A/problems/JOGGING)

[Contest Division 2](https://www.codechef.com/START44B/problems/JOGGING)

[Contest Division 3](https://www.codechef.com/START44C/problems/JOGGING)

[Contest Division 4](https://www.codechef.com/START44D/problems/JOGGING)

**Setter:** [lavish_adm](https://www.codechef.com/users/lavish_adm)

**Testers:** [utkarsh_adm](https://www.codechef.com/users/utkarsh_adm), [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1484

#
[](#prerequisites-3)PREREQUISITES:

Basic modular arithmetic

#
[](#problem-4)PROBLEM:

You have to consider a sequence of numbers where the first element is X. And each element after it, is the sum of all the elements before it. And you need to output the sum of the first N elements of this sequence.

#
[](#explanation-5)EXPLANATION:

Let us look at the first few elements of this sequence:

The first element is X.

The second element is the sum of everything which came before it, which is just X.

The third element is sum of first two, which is X+X = 2X.

The fourth element is sum of first three, which is X+X+2X = 4X.

The fifth element is sum of first four, which is X+X+2X+4X = 8X.

We see a pattern emerging. From the third element onwards, the elements seem to keep doubling. But it’s not obvious why that’s the case.

So now, instead, let’s look directly at the sum of the first i elements:

The sum of the first element is X.

The sum of the first two elements is X+X = 2X.

The sum of the first three elements is X+X + 2X= 4X.

The sum of the first four elements is X+X+2X+4X= 8X.

Here, we again see a very similar pattern, but now, starting from the second sum itself, the sums are double the previous sum.

And this is easy to see why - suppose the sum of the first 5 elements is some Y. Then the 6th element is Y, by definition. So then the sum of the first 6 elements is 2.

So generalizing this, we see that the sums are just X, 2X, 2^2X, 2^3X, 2^4X, 2^5X, \ldots. In particular, the sum of the first N elements is just 2^{N-1}X.

So given X and N, we just have to output (2^{N-1}X) \mod 1000000007. Since there are a lot of testcases, and the powers of 2 are independent of X, we can compute 2^{i} \mod 1000000007 for all values of i from 0 to 10^6, and store them in an array.

And we use the fact that (AB) \mod C = ( (A \mod C) * (B \mod C) ) \mod C to use the precomputed values of the modulos of the powers and get the answer for each testcase in constant time after the precomputation.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N + T).

#
[](#solution-7)SOLUTION:

Tester's Solution
``mod = 10**9 + 7
for _ in range(int(input())):
	n, x = map(int, input().split())
	print((pow(2, n-1, mod)*x)%mod)
``

Editorialist's Solution
``#include <iostream>
using namespace std;

long long int testcases, Pow[1000001], n, x, MOD = 1000000007;

int main() {

	cin>>testcases;

	Pow[0]=1;
	for(int i=1;i<=1000000;i++)
	    Pow[i] = (Pow[i-1] * 2) % MOD;

	while(testcases--)
	{
	    cin>>n>>x;
	    cout<<(x * Pow[n-1]) % MOD << "\n";
	}

	return 0;
}
``

</details>
