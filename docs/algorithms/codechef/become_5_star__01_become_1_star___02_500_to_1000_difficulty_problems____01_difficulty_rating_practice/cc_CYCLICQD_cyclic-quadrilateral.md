# Cyclic Quadrilateral

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CYCLICQD |
| Difficulty Rating | 735 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CYCLICQD](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CYCLICQD) |

---

## Problem Statement

You are given the sizes of angles of a simple quadrilateral (in degrees) $A$, $B$, $C$ and $D$, in some order along its perimeter. Determine whether the quadrilateral is cyclic.

Note: A quadrilateral is cyclic if and only if the sum of opposite angles is $180^{\circ}$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $A$, $B$, $C$ and $D$.

### Output
Print a single line containing the string `"YES"` if the given quadrilateral is cyclic or `"NO"` if it is not (without quotes).

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq A, B, C, D \leq 357$
- $A + B + C + D = 360$

---

## Examples

**Example 1**

**Input**

```text
3
10 20 30 300
10 20 170 160
179 1 179 1
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Example case 1:** The sum of two opposite angles $A + C = 10^{\circ} + 30^{\circ} \neq 180^{\circ}$.

**Example case 2:** The sum of two opposite angles $A + C = 10^{\circ} + 170^{\circ} = 180^{\circ}$ and $B + D = 20^{\circ} + 160^{\circ} = 180^{\circ}$.

**Example case 3:** The sum of two opposite angles $B + D = 1^{\circ} + 1^{\circ} \neq 180^{\circ}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 20 30 300
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
10 20 170 160
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
179 1 179 1
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice ](https://www.codechef.com/problems/CYCLICQD)

[Contest: Division 3 ](https://www.codechef.com/START5C/problems/CYCLICQD)

[Contest: Division 2 ](https://www.codechef.com/START5B/problems/CYCLICQD)

[Contest: Division 1 ](https://www.codechef.com/START5A/problems/CYCLICQD)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

NONE

# PROBLEM:

Given angles of a quadrilateral in order A, B, C, D, find if the quadrilateral is cyclic.

# EXPLANATION:

For a quadrilateral to be cyclic, the sum of opposite angles should be 180. So just check if A + C = 180 and B+D=180.

Checking only A+C suffice because if A+C=180 then B+D=180 as A+B+C+D = 360.

Or we can also check if A+C = B+D because in this case we have A+B+C+D = A+C+B+D = A+C+A+C=2*(A+C) = 360 so A+C = 360/2 = 180.

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 1e4;
const string newln = "\n", space = " ";
int main()
{
    int t, a, b, c, d; cin >> t;
    while(t--){
        cin >> a >> b >> c >> d;
        assert(a + b + c + d == 360);
        string ans = (a + c == 180 ? "YeS" : "No");
        cout << ans << endl;
    }
}
``

Tester's Solution
``#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <random>

#ifdef HOME
	#include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
	long long x = 0;
	int cnt = 0;
	int fi = -1;
	bool is_neg = false;
	while (true) {
		char g = getchar();
		if (g == '-') {
			assert(fi == -1);
			is_neg = true;
			continue;
		}
		if ('0' <= g && g <= '9') {
			x *= 10;
			x += g - '0';
			if (cnt == 0) {
				fi = g - '0';
			}
			cnt++;
			assert(fi != 0 || cnt == 1);
			assert(fi != 0 || is_neg == false);

			assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
		}
		else if (g == endd) {
			assert(cnt > 0);
			if (is_neg) {
				x = -x;
			}
			assert(l <= x && x <= r);
			return x;
		}
		else {
			//assert(false);
		}
	}
}

string readString(int l, int r, char endd) {
	string ret = "";
	int cnt = 0;
	while (true) {
		char g = getchar();
		assert(g != -1);
		if (g == endd) {
			break;
		}
		cnt++;
		ret += g;
	}
	assert(l <= cnt && cnt <= r);
	return ret;
}
long long readIntSp(long long l, long long r) {
	return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
	return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
	return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
	return readString(l, r, ' ');
}

int main(int argc, char** argv)
{
#ifdef HOME
	if(IsDebuggerPresent())
	{
		freopen("../in.txt", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T = readIntLn(1, 10'000);
	forn(tc, T)
	{
		int A = readIntSp(1, 357);
		int B = readIntSp(1, 357);
		int C = readIntSp(1, 357);
		int D = readIntLn(1, 357);
		assert(A + B + C + D == 360);
		if (A + C == B + D)
			printf("YES\n");
		else
			printf("NO\n");
	}
	//assert(getchar() != -1);
	return 0;
}

``

Editorialist's Solution
``/*
 * @author: vichitr
 * @date: 26th June 2021
 */

#include <bits/stdc++.h>
using namespace std;

void solve() {
	int a, b, c, d;
	cin >> a >> b >> c >> d;
	if (a + c == 180)
		cout << "YES\n";
	else
		cout << "NO\n";

}

int main() {

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int t = 1;
	cin >> t;
	while (t--)
		solve();
	return 0;
}
``

# VIDEO EDITORIAL:

If you have other approaches or solutions, let’s discuss in comments.

</details>
