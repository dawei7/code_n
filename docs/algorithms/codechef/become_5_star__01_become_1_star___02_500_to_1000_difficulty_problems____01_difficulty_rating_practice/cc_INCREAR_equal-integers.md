# Equal Integers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INCREAR |
| Difficulty Rating | 852 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [INCREAR](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/INCREAR) |

---

## Problem Statement

Chef has two integers $X$ and $Y$. Chef wants to perform some operations to make $X$ and $Y$ equal. In one operation, Chef can either:
- set $X := X + 1$
- or set $Y := Y + 2$

Find the minimum number of operations required to make $X$ and $Y$ equal.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers $X$ and $Y$.

---

## Output Format

For each test case, print the minimum number of operations required to make $X$ and $Y$ equal.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
5
3 4
5 5
7 3
5 2
7 12
```

**Output**

```text
1
0
2
3
5
```

**Explanation**

Let $(x, y)$ denote the values of $X$ and $Y$ respectively.

**Test case $1$:** Only one operation is required: $(3, 4) \xrightarrow{X := X + 1}{} (4, 4)$

**Test case $2$:** No operations are required since $X$ and $Y$ are already equal.

**Test case $3$:** Two operations are required: $(7, 3) \xrightarrow{Y := Y + 2}{} (7, 5) \xrightarrow{Y := Y + 2}{} (7, 7)$

**Test case $4$:** Three operations are required. One such sequence of operations is: $(5, 2) \xrightarrow{Y := Y + 2}{} (5, 4) \xrightarrow{X := X + 1}{} (6, 4) \xrightarrow{Y := Y + 2}{} (6, 6)$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5 5
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
7 3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
5 2
```

**Output for this case**

```text
3
```



#### Test case 5

**Input for this case**

```text
7 12
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START41A/problems/INCREAR)

[Contest Division 2](https://www.codechef.com/START41B/problems/INCREAR)

[Contest Division 3](https://www.codechef.com/START41C/problems/INCREAR)

[Contest Division 4](https://www.codechef.com/START41D/problems/INCREAR)

Setter: [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Lavish Gupta ](https://www.codechef.com/users/lavish_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

852

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has two integers X and Y. Chef wants to perform some operations to make X and Y equal. In one operation, Chef can either:

- set X := X + 1

- or set Y := Y + 2

Find the minimum number of operations required to make X and Y equal.

#
[](#explanation-5)EXPLANATION:

There are two cases:

**Case 1** X\leq Y: Since, Y cannot be decreased by any method, therefore X has to be increased by at least Y-X. Thus, this is the minimum number of operations and all operations are of type 1.

**Case 2**  X>Y: Y has to be made at least X. Therefore the minimum number of operations is ceil(\frac{(Y-X)}{2}). If X and Y don’t have the same parity then Y would be increased to X+1 by doing these operations and thus we need to do one more operation which is increasing X by 1.

\therefore answer = ((X\leq Y)?Y-X:\frac{(X-Y+1)}{2}+1- (X%2==Y%2))

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int x, y; cin >> x >> y;
		if (y >= x) {
			cout << (y - x) << '\n';
		} else {
			if (y % 2 == x % 2) {
				cout << (x - y) / 2 << '\n';
			} else {
				cout << 2 + (x - y) / 2 << '\n';
			}
		}
	}
	return 0;
}
``

Editorialist's solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
ll INF = 1e18;
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int x, y;
    cin >> x >> y;
    cout << ((x <= y) ? y - x : 1 - (x % 2 == y % 2) + (x - y + 1) / 2) << '\n';
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int test = 1;
    cin >> test;
    while (test--)
        sol();
}

``

</details>
