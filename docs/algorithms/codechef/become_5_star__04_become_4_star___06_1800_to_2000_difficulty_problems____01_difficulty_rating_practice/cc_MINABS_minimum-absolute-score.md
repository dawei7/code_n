# Minimum Absolute Score

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINABS |
| Difficulty Rating | 1836 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [MINABS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/MINABS) |

---

## Problem Statement

You are given two strings $A$ and $B$ of length $N$ consisting of lowercase English letters. Your objective is to make both the strings equal.

You can apply one of the following $2$ operations at each index $i$:
- Convert char $A_i$ to $B_i$ by doing right cyclic shift of character $A_i$. This **increases** your score by amount equal to cyclic shifts done.
- Convert char $B_i$ to $A_i$ by doing right cyclic shift of character $B_i$. This **decreases** your score by amount equal to cyclic shifts done.

Your starting score is zero.
If the operations are applied optimally, find the **minimum [absolute](https://en.wikipedia.org/wiki/Absolute_value) score** possible after making both the strings equal.

**Note:** A single right cyclic shift converts one character to the next in alphabetical order, except for $z$ which goes to $a$. That is, the sequence looks like
$$
a \to b \to c \to \ldots \to y \to z \to a \to b \to \ldots
$$
So, for example converting $a$ to $e$ requires $4$ right cyclic shifts, and converting $k$ to $i$ requires $24$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains one integer $N$ — the length of strings $A$ and $B$.
    - The second line contains string $A$.
    - The third line contains string $B$.

---

## Output Format

For each test case, output on a new line the minimum absolute score possible after making both the strings equal.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- Both strings $A$ and $B$ have same length $N$ and contain only lowercase English letters.
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
abb
baz
3
zzc
aaa
4
fxbs
dkrc
5
eaufq
drtkn
```

**Output**

```text
2
0
11
9
```

**Explanation**

**Test case $1$:** The minimum *absolute* score can be obtained as follows:
- Apply operation $1$ at position $1$, converting $a$ to $b$ for a cost of $+1$.
- Apply operation $2$ at position $2$, converting $a$ to $b$ for a cost of $-1$.
- Apply operation $2$ at position $3$, converting $z$ to $b$ for a cost of $-2$.

The score is then $1 -1 -2 = -2$, with absolute value $2$. This is the lowest possible absolute value attainable.

**Test case $2$:** Apply operations as follows:
- Operation $1$ at index $1$, $z\to a$ for a cost of $+1$
- Operation $1$ at index $2$, $z\to a$ for a cost of $+1$
- Operation $2$ at index $3$, $a\to c$ for a cost of $-2$

This gives us a final score of $1 + 1 - 2 = 0$, which has absolute value $0$. It is not possible to do better than this.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
abb
baz
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
zzc
aaa
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4
fxbs
dkrc
```

**Output for this case**

```text
11
```



#### Test case 4

**Input for this case**

```text
5
eaufq
drtkn
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINABS)

[Contest: Division 1](https://www.codechef.com/START63A/problems/MINABS)

[Contest: Division 2](https://www.codechef.com/START63B/problems/MINABS)

[Contest: Division 3](https://www.codechef.com/START63C/problems/MINABS)

[Contest: Division 4](https://www.codechef.com/START63D/problems/MINABS)

***Author:*** [Ram Gopal Pandey](https://www.codechef.com/users/grayhathacker)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1836

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have two strings A and B. You’d like to make them equal.

You can either right-rotate A_i to reach B_i for positive cost, or right-rotate B_i to reach A_i, for negative cost.

Find the minimum **absolute** cost possible.

#
[](#explanation-5)EXPLANATION:

Let’s first convert every A_i to B_i using right rotations. At the i-th index, this has a cost of:

-
B_i - A_i, if A_i \leq B_i

-
B_i - A_i + 26, if A_i \gt B_i.

Let this cost for index i be C_i, and S = \sum_{i=1}^N C_i be our initial cost.

Now, we want to use the B_i \to A_i right rotation at some indices instead to make the absolute value of S as low as possible.

Let’s see how this changes S:

- First, we must subtract C_i from S, since we aren’t using the A_i \to B_i rotation anymore.

- Then, we add the cost of the B_i \to A_i rotation to S. Note that this is exactly -(26 - C_i) (you can derive this from the definition of C_i given above).

So, our change is S \to S - C_i - (26 - C_i) = S - 26.

This means it doesn’t matter which index we choose, the score is only going to decrease by 26.

So, the possible scores we can obtain are \{S, S - 26, S - 2\cdot 26, S - 3\cdot 26, \ldots, S - N\cdot 26\}. The answer is thus the minimum absolute value among all these N+1 values, which can easily be found in \mathcal{O}(N).

Note that there is an even simpler implementation: since we can only subtract 26, the value of S can always be brought into the range [-26, 26].

The answer is thus simply the minimum of (S\bmod 26) and ((-S) \bmod 26).

For example, if S = 100, the answer is the minimum of (100\bmod 26) = 22 and (-100 \bmod 26) = 4, which is 4.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int, char> msi;
typedef pair<int, int> pa;
typedef long long int ll;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		string a, b;
		cin >> a >> b;
		int ans = 0;
		for (int i = 0; i < n; i++)
			ans += b[i] - a[i];
		ans = (ans % 26 + 26) % 26;
		cout << min(ans, abs(26 - ans)) << "\n";
	}

	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, a, b = int(input()), input(), input()
    ans = 0
    for i in range(n):
        ans += ord(a[i]) - ord(b[i]) + 26
    print(min(ans%26, (-ans)%26))
``

</details>
