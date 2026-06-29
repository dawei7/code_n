# Peaceful Party

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAYOR_PARTY |
| Difficulty Rating | 898 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [MAYOR_PARTY](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/MAYOR_PARTY) |

---

## Problem Statement

The mayor of your city has decided to throw a party to gather the favour of his people in different regions of the city.

There are $3$ distinct regions in the city namely $A$, $B$, $C$ comprising of $P_A$, $P_B$ and $P_C$ number of people respectively.

However, the mayor knows that people of the region $B$ are in conflict with people of regions $A$ and $C$. So, there will be a conflict if people from region $B$ are present at the party along with people from region $A$ or $C$.

The mayor wants to invite as many people as possible and also avoid any conflicts. Help him invite **maximum** number of people to the party.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains three integers $P_A$, $P_B$ and $P_C$ - number of people living in regions $A$, $B$ and $C$ respectively.

---

## Output Format

For each test case, output the **maximum** number of people that can be invited to the party.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq P_A, P_B, P_C \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
2 3 4
1 5 2
8 8 8
```

**Output**

```text
6
5
16
```

**Explanation**

**Test case-1:** Mayor can invite all the people from region $A$ and $C$. So the maximum number of people invited is $6$.

**Test case-2:** Mayor can invite all the people from region $B$. So the maximum number of people invited is $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3 4
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
1 5 2
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
8 8 8
```

**Output for this case**

```text
16
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK138A/problems/MAYOR_PARTY)

[Contest Division 2](https://www.codechef.com/COOK138B/problems/MAYOR_PARTY)

[Contest Division 3](https://www.codechef.com/COOK138C/problems/MAYOR_PARTY)

[Contest Division 4](https://www.codechef.com/COOK138D/problems/MAYOR_PARTY)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are 3 distinct regions in the city namely A, B, C consisting of P_A, P_B and P_C number of people respectively.

We know that people of the region B are in conflict with people of regions A and C. So, there will be a conflict if people from region B are present at the party along with people from region A or C.

You want to invite as many people as possible and also avoid any conflicts. Find the maximum number of people you can invite to the party.

#
[](#explanation-5)EXPLANATION:

We are given that the people of region B are in conflict with people of region A and C. This means that if people of region B come to the party, no one else comes.

On the other hand, if the people of region B do not come, people from regions A and C can come together.

The maximum number of people would be the maximum out of these two cases.

Thus, the answer is max(P_B, P_A +P_C).

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
int t;
int n,m;
ll a[300001];
ll s=0;
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    int t;cin >> t;
    while(t--){
    	int x,y,z;
    	cin >> x >> y >> z;
    	cout << max(y,x+z) << '\n';
	}
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int pa, pb, pc;
	    cin>>pa>>pb>>pc;
	    cout<<max(pb, pa+pc)<<endl;
	}
	return 0;
}
``

</details>
