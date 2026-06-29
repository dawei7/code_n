# Programming Languages

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PROGLANG |
| Difficulty Rating | 1001 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [PROGLANG](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/PROGLANG) |

---

## Problem Statement

Chef is a software developer, so he has to switch between different languages sometimes. Each programming language has some features, which are represented by integers here.

Currently, Chef has to use a language with two given features $A$ and $B$. He has two options --- switching to a language with two features $A_1$ and $B_1$, or to a language with two features $A_2$ and $B_2$. All four features of these two languages are pairwise distinct.

Tell Chef whether he can use the first language, the second language or neither of these languages (if no single language has all the required features).

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains six space-separated integers $A, B, A_1, B_1, A_2, B_2$.

---

## Output Format

For each test case, print a single line containing the integer $1$ if Chef should switch to the first language, or $2$ if Chef should switch to the second language, or $0$ if Chef cannot switch to either language.

---

## Constraints

- $1 \leq T \leq 288$
- $1 \leq A, B, A_1, B_1, A_2, B_2 \leq 4$
- $A, B$ are distinct
- $A_1, B_1, A_2, B_2$ are pairwise distinct

---

## Examples

**Example 1**

**Input**

```text
3
1 2 2 1 3 4
3 4 2 1 4 3
1 2 1 3 2 4
```

**Output**

```text
1
2
0
```

**Explanation**

**Example case 1:** The first language has the required features --- features $1$ and $2$.

**Example case 2:** The second language has the required features --- features $3$ and $4$.

**Example case 3:** Neither language has both features $1$ and $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 2 1 3 4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 4 2 1 4 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
1 2 1 3 2 4
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PROGLANG)

[Contest: Division 1](https://www.codechef.com/LTIME99A/problems/PROGLANG)

[Contest: Division 2](https://www.codechef.com/LTIME99B/problems/PROGLANG)

[Contest: Division 3](https://www.codechef.com/LTIME99C/problems/PROGLANG)

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

Chef is a software developer, so he has to switch between different languages sometimes. Each programming language has some features, which are represented by integers here.

Currently, Chef has to use a language with two given features A and B. He has two options — switching to a language with two features A_1 and B_1, or to a language with two features A_2 and B_2. All four features of these two languages are pairwise distinct.

Tell Chef whether he can use the first language, the second language or neither of these languages (if no single language has all the required features).

#
[](#explanation-5)EXPLANATION:

Check if unordered pair (A,B) = any of unordered pairs (A_1,B_1) or (A_2,B_2) and answer accordingly

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
    ll a,b,a1,b1,a2,b2;
    cin>>a>>b>>a1>>b1>>a2>>b2;
    if(a > b) swap(a,b);
    if(a1 > b1) swap(a1,b1);
    if(a2 > b2) swap(a2,b2);

    if(a == a1 && b == b1)
    {
        cout<<1<<endl;
    }
    else if(a == a2 && b == b2)
    {
        cout<<2<<endl;
    }
    else
    {
        cout<<0<<endl;
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
