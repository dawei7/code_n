# Maximum Length Even Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXEVNSUB |
| Difficulty Rating | 1221 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [MXEVNSUB](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MXEVNSUB) |

---

## Problem Statement

You are given an integer $N$. Consider the sequence containing the integers $1, 2, \ldots, N$ in increasing order (each exactly once). Find the maximum length of its contiguous subsequence with an even sum.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

---

## Output Format

For each test case, print a single line containing one integer --- the maximum length of a contiguous subsequence with even sum.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
3
4
5
```

**Output**

```text
3
4
4
```

**Explanation**

**Example case 1:** The optimal choice is to choose the entire sequence, since the sum of all its elements is $1 + 2 + 3 = 6$, which is even.

**Example case 3:** One of the optimal choices is to choose the subsequence $[1, 2, 3, 4]$, which has an even sum.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MXEVNSUB)

[Contest: Division 1](https://www.codechef.com/LTIME99A/problems/MXEVNSUB)

[Contest: Division 2](https://www.codechef.com/LTIME99B/problems/MXEVNSUB)

[Contest: Division 3](https://www.codechef.com/LTIME99C/problems/MXEVNSUB)

***Author:*** [ Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Tester:*** [ Anay Karnik](https://www.codechef.com/users/karnikanay)

***Editorialist:*** [Mohan Abhyas](https://www.codechef.com/users/mohan_abhyas)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an integer N. Consider the sequence containing the integers 1, 2, \ldots, N in increasing order (each exactly once). Find the maximum length of its contiguous subsequence with an even sum.

#
[](#explanation-5)EXPLANATION:

\sum_{k=1}^{k=n} k = n*(n+1)/2

Take whole sequence if above sum is even else leave out 1 to make sum even

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#solutions-7)SOLUTIONS:

[details = “Editorial’s Solution”]

``#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define forn(i,e) for(ll i = 0; i < e; i++)

void solve()
{
	ll n;
    cin>>n;
    ll sum = (n*(n+1))/2;
    if(sum%2)
    {
        cout<<n-1<<endl;
    }
    else
    {
        cout<<n<<endl;
    }
}

int main()
{
	ll t=1;
	cin >> t;
    forn(i,t) {
    	solve();
    }
    return 0;
}
``

</details>
