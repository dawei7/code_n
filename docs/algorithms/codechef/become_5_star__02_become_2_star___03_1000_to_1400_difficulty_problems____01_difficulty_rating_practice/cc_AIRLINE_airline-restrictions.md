# Airline Restrictions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AIRLINE |
| Difficulty Rating | 1042 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [AIRLINE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/AIRLINE) |

---

## Problem Statement

Chef has $3$ bags that she wants to take on a flight. They weigh $A$, $B$, and $C$ kgs respectively. She wants to check-in exactly two of these bags and carry the remaining one bag with her.

The airline restrictions says that the total sum of the weights of the bags that are checked-in cannot exceed $D$ kgs and the weight of the bag which is carried cannot exceed $E$ kgs. Find if Chef can take all the three bags on the flight.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each testcase contains a single line of input, five space separated integers $A, B, C, D, E$.

---

## Output Format

For each testcase, output in a single line answer `"YES"` if Chef can take all the three bags with her or `"NO"` if she cannot.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 36000$
- $1 \leq A, B, C \leq 10$
- $15 \leq D \leq 20$
- $5 \leq E \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1 15 5
8 7 6 15 5
8 5 7 15 6
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** Chef can check-in the first and second bag (since $1 + 1 = 2 \le 15$) and carry the third bag with her (since $1 \le 5$).

**Test case $2$:** None of the three bags can be carried in hand without violating the airport restrictions.

**Test case $3$:** Chef can check-in the first and the third bag (since $8 + 7 \le 15$) and carry the second bag with her (since $5 \le 6$).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 15 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
8 7 6 15 5
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
8 5 7 15 6
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

[Practice ](https://www.codechef.com/problems/AIRLINE)

[Contest: Division 1 ](https://www.codechef.com/SEPT21A/problems/AIRLINE)

[Contest: Division 2 ](https://www.codechef.com/SEPT21B/problems/AIRLINE)

[Contest: Division 3 ](https://www.codechef.com/SEPT21C/problems/AIRLINE)

**Author:** [Daanish Mahajan ](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has 3 bags that she wants to take on a flight. They weigh A, B, and C kgs respectively. She wants to check in exactly two of these bags and carry the remaining one bag with her.

The airline restrictions say that the total sum of the weights of the bags that are checked-in cannot exceed D kgs and the weight of the bag which is carried cannot exceed E kgs. Find if Chef can take all the three bags on the flight.

#
[](#explanation-5)EXPLANATION:

Just do as the problem say and check all the possible combinations. If any of the combinations satisfy the airline rules, we can simply print YES otherwise NO.

The possible combinations that can be are as follows:

- Bag A and Bag B are checked in while Bag C is carried.

- Bag B and Bag C are checked in while Bag A is carried.

- Bag A and Bag C are checked in while Bag B is carried.

If any of the combinations satisfy the airline rules then Chef can take all the three bags and hence print YES else NO.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case.

#
[](#solutions-7)SOLUTIONS:

Author
``#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define rb pop_back
#define ti tuple<int, int, int>
#define pii pair<int, int>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define mp make_pair
#define mt make_tuple

using namespace std;

const int maxt = 36000;
const string newln = "\n", space = " ";

int main()
{
    int t, a, b, c, d, e; cin >> t;
    while(t--){
        cin >> a >> b >> c >> d >> e;
        string ans = "No";
        if((a + b <= d && c <= e) || (a + c <= d && b <= e) || (b + c <= d && a <= e)){
            ans = "YeS";
        }
        cout << ans << endl;
    }
}
``

Tester
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

template<class T> bool umin(T& a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T& a, T b) { return a < b ? (a = b, true) : false; }

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
			assert(false);
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
	if (IsDebuggerPresent())
	{
		freopen("../in.txt", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T = readIntLn(1, 36'000);
	int sumN = 0;
	forn(tc, T)
	{
		int A = readIntSp(1, 10);
		int B = readIntSp(1, 10);
		int C = readIntSp(1, 10);
		int D = readIntSp(15, 20);
		int E = readIntLn(5, 10);
		if ((A + B <= D && C <= E) ||
			(A + C <= D && B <= E) ||
			(B + C <= D && A <= E))
			printf("YES\n");
		else
			printf("NO\n");
	}
	assert(getchar() == -1);
	return 0;
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
	int a,b,c,d,e;
	cin>>a>>b>>c>>d>>e;

	if(((a+b)<=d && c<=e) || ((a+c)<=d && b<=e) || ((c+b)<=d && a<=e))
		cout<<"YES"<<endl;
	else
		cout<<"NO"<<endl;
}

int32_t main()
{
	// freopen("input.txt","r",stdin);
	// freopen("output.txt","w",stdout);

	int t;
	cin>>t;

	while(t--)
		solve();

return 0;
}
``

</details>
