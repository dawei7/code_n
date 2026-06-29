# How many unattempted problems

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRACLIST |
| Difficulty Rating | 264 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PRACLIST](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRACLIST) |

---

## Problem Statement

*CodeChef recently revamped its [practice page](https://www.codechef.com/practice) to make it easier for users to identify the next problems they should solve by introducing some new features:*
- *Recent Contest Problems - contains only problems from the last 2 contests*
- *Separate Un-Attempted,  Attempted, and All tabs*
- *Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience*
- *Popular Topics and Tags*

Our Chef is currently practicing on CodeChef and is a beginner. The count of ‘All Problems’ in the Beginner section is $X$. Our Chef has already ‘Attempted’ $Y$ problems among them. How many problems are yet ‘Un-attempted’?

---

## Input Format

- The first and only line of input contains two space-separated integers $X$ and $Y$ — the count of 'All problems' in the Beginner's section and the count of Chef's 'Attempted' problems, respectively.

---

## Output Format

Output a single integer in a single line — the number of problems that are yet 'Un-attempted'

---

## Constraints

- $1 \leq Y \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
10 4
```

**Output**

```text
6
```

**Example 2**

**Input**

```text
10 10
```

**Output**

```text
0
```

**Example 3**

**Input**

```text
1000 990
```

**Output**

```text
10
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME108A/problems/PRACLIST)

[Contest Division 2](https://www.codechef.com/LTIME108B/problems/PRACLIST)

[Contest Division 3](https://www.codechef.com/LTIME108C/problems/PRACLIST)

[Contest Division 4](https://www.codechef.com/LTIME108D/problems/PRACLIST)

**Setter:** [Hrishikesh](https://www.codechef.com/users/hrishik85)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

264

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Our Chef is currently practicing on CodeChef and is a beginner. The count of ‘All Problems’ in the Beginner section is X. Our Chef has already ‘Attempted’ Y problems among them. How many problems are yet ‘Un-attempted’?

#
[](#explanation-5)EXPLANATION:

Answer is X - Y.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Setter's Solution
``//tt89 ;)
#include <iostream>
using namespace std;

int x,y;

int main() {
    // your code goes here
    cin>>x>>y;
    cout<<x-y<<"\n";
    return 0;
}

``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
ll n;
void solve(int rr){
    cin >> n;
    int ans=0;
    for(int i=1; i<=n ;i++){
        int x;cin >> x;ans+=(x>=1000);
    }
    cout << ans << '\n';
}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    ll x,y;cin >> x >> y;
    cout << x-y << '\n';
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int a, b; cin >> a >> b; cout << a - b;
}
``

</details>
