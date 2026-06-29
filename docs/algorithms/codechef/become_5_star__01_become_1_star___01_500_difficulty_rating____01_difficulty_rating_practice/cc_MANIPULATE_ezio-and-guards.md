# Ezio and Guards

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MANIPULATE |
| Difficulty Rating | 427 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MANIPULATE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANIPULATE) |

---

## Problem Statement

Ezio can manipulate **at most** $X$ number of guards with the apple of eden.

Given that there are $Y$ number of guards, predict if he can safely manipulate all of them.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$.

---

## Output Format

For each test case, print $\texttt{YES}$ if it is possible for Ezio to manipulate all the guards. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
5 7
6 6
9 1
```

**Output**

```text
NO
YES
YES
```

**Explanation**

**Test Case $1$:** Ezio can manipulate at most $5$ guards. Since there are $7$ guards, he cannot manipulate all of them.

**Test Case $2$:** Ezio can manipulate at most $6$ guards. Since there are $6$ guards, he can manipulate all of them.

**Test Case $3$:** Ezio can manipulate at most $9$ guards. Since there is only $1$ guard, he can manipulate the guard.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 7
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
6 6
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
9 1
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/APRIL221A)

[Contest Division 2](https://www.codechef.com/APRIL221B)

[Contest Division 3](https://www.codechef.com/APRIL221C)

[Contest Division 4](https://www.codechef.com/APRIL221D)

Setter: [ Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

Tester: [ Istvan Nagy](https://www.codechef.com/users/iscsi), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Vijay](https://www.codechef.com/users/blank_337)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Ezio can manipulate *at most* X number of guards with the apple of eden.

Given that there are Y number of guards, predict if he can safely manipulate all of them.

#
[](#explanation-5)EXPLANATION

We will try to manipulate the maximum number of guards. We are given in the problem that the maximum number of guards Ezio can manipulate is X. Thus if X comes out be less than Y. We will not be able to manipulate all of the guards otherwise we can always manipulate all of them.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <bits/stdc++.h>

using namespace std;

#define nline '\n'
void solve()
{
int x, y;
cin>>x>>y;

if(x>=y)cout<<"YES"<<nline;
else cout<<"NO"<<nline;

}

int main()
{

    int t=1;
    cin >> t;

    while (t--)
    {
        solve();
    }
}

``

</details>
