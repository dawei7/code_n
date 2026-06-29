# Bi_lindrome!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QTOO_2523 |
| Difficulty Rating | 1095 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [QTOO_2523](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/QTOO_2523) |

---

## Problem Statement

You are given a string $S$ of length $N$.

Your task is to delete a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of **maximum** length from the string, such that, after concatenating the remaining parts of the string, it becomes a [palindrome](https://en.wikipedia.org/wiki/Palindrome) of length **greater** than $1$.

If this is possible, print the maximum length of the subsequence that can be deleted. Otherwise, print $-1$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $2$ lines of input:
  - The first line consists the a single integer $N$ - the length of string $S$.
  - The second line contains string $S$, consisting of lowercase english alphabets.

---

## Output Format

For each test case, if it is possible to delete a subsequence under the given conditions, print a single integer, denoting the maximum length of the subsequence that can be deleted. Otherwise, print $-1$.

---

## Constraints

- $1 \leq T \leq 2500$
- $3 \leq N \leq 100$
- $S$ consists of lowercase english alphabets.

---

## Examples

**Example 1**

**Input**

```text
3
6
babkhj
3 
abc 
4 
qtoo
```

**Output**

```text
4
-1
2
```

**Explanation**

**Test case $1$:** Possible ways to delete a subsequence are:
- Delete subsequence `khj` to get palindrome `bab`.
- Delete subsequence `akhj` to get palindrome `bb`.

The subsequence having maximum length that can be deleted is `akhj`, having length $4$.

**Test case $2$:** We cannot delete any subsequence under the given conditions.

**Test case $3$:** We can delete the subsequence `qt` to obtain the string `oo`, which is a palindrome. This is the only subsequence that can be deleted and it has length $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
babkhj
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
abc
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
4
qtoo
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/QTOO_2523)

[Contest: Division 1](https://www.codechef.com/COOK144A/problems/QTOO_2523)

[Contest: Division 2](https://www.codechef.com/COOK144B/problems/QTOO_2523)

[Contest: Division 3](https://www.codechef.com/COOK144C/problems/QTOO_2523)

[Contest: Division 4](https://www.codechef.com/COOK144D/problems/QTOO_2523)

***Author:*** [moonlight_cl25](https://www.codechef.com/users/moonlight_cl25)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a string, find the maximum number of characters that can be deleted from it so that the remaining characters form a palindrome of length at least 2.

Print -1 if this is not possible.

#
[](#explanation-5)EXPLANATION:

Any palindrome of length \geq 2 has at least one pair of repeated characters, since the first character equals the last.

This tells us that:

- If S contains at least two occurrences of the same character, the answer is N-2. This is because we can create a palindrome of length 2 by deleting everything else.

- If S doesn’t contain repeated characters, the answer is -1 since creating a palindrome of length \geq 2 is impossible.

So, the only check that needs to be done is whether S contains repeated characters or not.

This can be done in \mathcal{O}(N), or even in \mathcal{O}(N^2) by iterating across all pairs of characters and checking whether they’re equal; since N is small enough.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <iostream>
#include <vector>
using namespace std;

void solve()
{
	vector<int> frq(27);
	int n;
	string s;
	cin >> n >> s;
	for (int i = 0; i < n; i++)
	{
		frq[s[i] - 96]++;
	}

	int answer = -1;
	for (int i = 1; i <= 26; i++)
	{
		if (frq[i] > 1)
		{
			answer = n - 2;
			break;
		}
	}

	cout << answer << endl;
}
int main()
{
	int tc;
	cin >> tc;
	while (tc--)
	{
		solve();
	}
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	s = sorted(input())
	for i in range(n-1):
		if s[i] == s[i+1]:
			print(n-2)
			break
	else:
		print(-1)
``

</details>
