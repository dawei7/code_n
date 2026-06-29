# Practice makes us perfect

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRACTICEPERF |
| Difficulty Rating | 467 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PRACTICEPERF](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRACTICEPERF) |

---

## Problem Statement

Most programmers will tell you that one of the ways to improve your performance in competitive programming is to [practice a lot of problems](https://www.codechef.com/practice).

Our Chef took the above advice very seriously and decided to set a target for himself.
- Chef decides to solve **at least** $10$ problems every week for $4$ weeks.

Given the number of problems he actually solved in each week over $4$ weeks as $P_1, P_2, P_3,$ and $P_4$, output the number of weeks in which Chef met his target.

---

## Input Format

There is a single line of input, with $4$ integers $P_1, P_2, P_3,$ and $P_4$. These are the number of problems solved by Chef in each of the $4$ weeks.

---

## Output Format

Output a single integer in a single line - the number of weeks in which Chef solved **at least** $10$ problems.

---

## Constraints

- $1 \leq P_1, P_2, P_3, P_4 \leq 100$

---

## Examples

**Example 1**

**Input**

```text
12 15 8 10
```

**Output**

```text
3
```

**Explanation**

Chef solved at least $10$ problems in the first, second and fourth weeks. He failed to solve at least $10$ problems in the third week. Hence, the number of weeks in which Chef met his target is $3$.

**Example 2**

**Input**

```text
2 3 1 10
```

**Output**

```text
1
```

**Explanation**

Chef solved at least $10$ problems in the fourth week. He failed to solve at least $10$ problems in all the other three weeks. Hence, the number of weeks in which Chef met his target is $1$.

**Example 3**

**Input**

```text
12 100 99 11
```

**Output**

```text
4
```

**Explanation**

Chef solved at least $10$ problems in all the four weeks. Hence, the number of weeks in which Chef met his target is $4$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MAY222A/problems/PRACTICEPERF)

[Contest Division 2](https://www.codechef.com/MAY222B/problems/PRACTICEPERF)

[Contest Division 3](https://www.codechef.com/MAY222C/problems/PRACTICEPERF)

[Contest Division 4](https://www.codechef.com/MAY222D/problems/PRACTICEPERF)

Setter: [Arjun](https://www.codechef.com/users/admin%202)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

467

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Most programmers will tell you that one of the ways to improve your performance in competitive programming is to [practice a lot of problems](https://www.codechef.com/practice).

Our Chef took the above advice very seriously and decided to set a target for himself.

- Chef decides to solve **at least** 10 problems every week for 4 weeks.

Given the number of problems he actually solved in each week over 4 weeks as P_1, P_2, P_3, and P_4, output the number of weeks in which Chef met his target.

#
[](#explanation-5)EXPLANATION:

Chef meets his target in a particular week if the number of problems solved by him in that particular week \geq 10. Initialize answer as 0. Iterate over weeks from i =1\: to\: 4 and add 1 to the answer if P_i\geq 10. Output the final value of answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``#include <iostream>
using namespace std;

int main() {

	int ans1 = 0;
	int a;
	for(int i=1;i<=4;i++)
	{
	    cin>>a;
	    if(a>=10)
	        ans1++;
	}

	cout<<ans1<<"\n";

	return 0;
}

``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int a, b, c, d, ans = 0;
    cin >> a >> b >> c >> d;
    ans += (a >= 10);
    ans += (b >= 10);
    ans += (c >= 10);
    ans += (d >= 10);
    cout << ans;
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int test = 1;
    // cin>>test;
    while (test--)
        sol();
}

``

</details>
