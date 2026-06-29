# Chef and String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECNDSTR |
| Difficulty Rating | 1206 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [RECNDSTR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/RECNDSTR) |

---

## Problem Statement

Chef has a string $S$ consisting of lowercase English characters. Chef defined functions left shift $L(X)$ and right shift $R(X)$ as follows.
- $L(X)$ is defined as shifting all characters of string $X$  one step towards left and moving the first character to the end.
- $R(X)$ is defined as shifting all characters of string $X$ one step towards the right and moving the last character to the beginning.

For example, L("abcd") = "bcda" and R("abcd") = "dabc"

Chef wants to find out whether there exists a string $V$ of the same length as $S$ such that both $L(V) = S$ and $R(V) = S$ holds.

###Input:
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a string $S$.

###Output:
For each test case, If there exists a valid string $V$, print "YES", otherwise print "NO" (without the quotes).

###Constraints
- $1 \le T \le 100$
- $1 \le |S| \le 10^6$
- $S$ contains all lower case English alphabets.
- It's guaranteed that the total length of the strings in one test file doesn't exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
4
a
ab
abcd
aaaaa
```

**Output**

```text
YES
YES
NO
YES
```

**Explanation**

- In the first test case, Chef can choose $V = S$
- In the second test case, Chef can choose $V$ = "ba" which satisfies both conditions.
- There doesn't exist any valid choice for string $V$ in the third test case.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
a
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
ab
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
abcd
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
aaaaa
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RECNDSTR)

[Contest](https://www.codechef.com/RC122020/problems/RECNDSTR)

***Author:***  [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

***Tester:***  [Sachin Yadav](https://www.codechef.com/users/sachin_yadav)

***Editorialist:***  [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

AD-HOC, OBSERVATION

# PROBLEM:

You are given a string S (1 \le |S| \le 10^6) and you have to find out whether there exists a string V of the same length such that both **one left** shift and **one right** shift on the string V produces the same string S.

# QUICK EXPLANATION:

- If there are some valid V existed then one of them should be equal to the resultant string R, produced by applying the **one left** shift over S. Now, if **one left** shift and **one right** shift over R is equal then answer is "YES" otherwise "NO".

# EXPLANATION:

**OBSERVATION:**

- If all character is **equal** in the given string then the answer should be "YES".

- In the case of **two distinct** characters, the given string should have them alternatively and has an even length.

- If there are more than **two distinct** characters in the given string then the answer is "NO".

We can say that the frequency of each character in the string V should be the same as string S because one left shift over V is equal to S and we know that by shift operation the frequency of any character in a string is not changed.

As both **one left** shift and **one right** shift on the string V produces the same string S implies that both **one left** shift and **one right** shift on the string V also be the same. It directly connects the all odd indexed characters and all even indexed characters. It is only possible when:

- if |V| \space \% \space 2 = 0 then all the odd index characters should be equal and all the even index characters should be equal.

- if |V| \space \% \space 2 = 1 then all the characters should be equal.

So, we can get that **one left** or **one right** shift over S is going to be V.

Mathematical Proof

We want a V, such that:

- LeftShift(V) is equal to S

- RightShift(V) is equal to S

1^{st} point is equivalent to saying RightShift(S) is equal to V. So, replacing V in 2^{nd} point, we get: RightShift(RightShift(S)) is equal to S which can further transform into RightShift(S) is equal to LeftShift(S).

# COMPLEXITY:

**TIME:** O(N)

**SPACE:** O(N)

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;

	while(t--)
	{
		int cnt[30] = {0};

		string s;
		cin >> s;

		int n = s.size();

		for(auto i:s)
			cnt[i-'a']++;

		int count = 0;

		for(int i:cnt) if(i) count++;

		bool flag = true;

		for(int i=1;i<s.size();i++)
		{
			if(s[i] == s[i-1])
			{
				flag = false;
				break;
			}
		}

		if(count == 1 || (count == 2 && n%2 == 0 && flag))
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}
``

Tester's Solution
``#include<iostream>
using namespace std;
typedef long long ll;
ll T, N;
string S;
int main()
{
    cin>>T;
    while(T--)
    {
        cin>>S;
        N=S.length();
        cout<<((S.substr(1) + S[0]) == (S[N-1] + S.substr(0,N-1))?"YES\n":"NO\n");
    }
    return 0;
}
``

</details>
