# Volume Control

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VOLCONTROL |
| Difficulty Rating | 409 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [VOLCONTROL](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/VOLCONTROL) |

---

## Problem Statement

Chef is watching TV. The current volume of the TV is $X$. Pressing the `volume up` button of the TV remote increases the volume by $1$ while pressing the `volume down` button decreases the volume by $1$. Chef wants to change the volume from $X$ to $Y$. Find the minimum number of button presses required to do so.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $Y$ - the initial volume and final volume of the TV.

---

## Output Format

For each test case, output the minimum number of times Chef has to press a button to change the volume from $X$ to $Y$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2
50 54
12 10
```

**Output**

```text
4
2
```

**Explanation**

**Test Case 1:** Chef can press the `volume up` button $4$ times to increase the volume from $50$ to $54$.

**Test Case 2:** Chef can press the `volume down` button $2$ times to decrease the volume from $12$ to $10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
50 54
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
12 10
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START32A/problems/VOLCONTROL)

[Contest Division 2](https://www.codechef.com/START32B/problems/VOLCONTROL)

[Contest Division 3](https://www.codechef.com/START32C/problems/VOLCONTROL)

[Contest Division 4](https://www.codechef.com/START32D/problems/VOLCONTROL)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Ashley Khoo](https://www.codechef.com/users/errorgorn), [ Nishant Shah](https://www.codechef.com/users/nishant_adm)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is watching TV. The current volume of the TV is X. Pressing the **volume up** button of the TV remote increases the volume by 1 while pressing the **volume down** button decreases the volume by 1. Chef wants to change the volume from X to Y. Find the **minimum** number of button presses required to do so.

#
[](#explanation-5)EXPLANATION:

We are given that current volume of the TV is X. Since Chef wants to change the volume from X to Y, following 3 cases are possible :

-
X \gt Y ; Chef can use volume down button (X-Y) times to change the volume from X to Y

-
X \lt Y; Chef can use volume up button (Y-X) times to change the volume from X to Y

-
X = Y; No button press required

Examples

-

X = 10, Y = 20 ; Since 10 < 20, Chef can use volume up button (20 - 10) = 10 times to change the volume from 10 to 20.

-

X = 8, Y = 5; Since 8 \gt 5, Chef can use volume down button (8 - 5 ) = 3 times to change the volume from 8 to 5.

-

X = 15, Y = 15; No button press required therefore output 0.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Tester-1's Solution
``	// Super Idol???
	//    ?????
	//  ???????
	//    ?????
	//  ??105°C??
	// ????????

	#include <bits/stdc++.h>
	#include <ext/pb_ds/assoc_container.hpp>
	#include <ext/pb_ds/tree_policy.hpp>
	#include <ext/rope>
	using namespace std;
	using namespace __gnu_pbds;
	using namespace __gnu_cxx;

	#define int long long
	#define ll long long
	#define ii pair<ll,ll>
	#define iii pair<ii,ll>
	#define fi first
	#define se second
	#define endl '\n'
	#define debug(x) cout << #x << ": " << x << endl

	#define pub push_back
	#define pob pop_back
	#define puf push_front
	#define pof pop_front
	#define lb lower_bound
	#define ub upper_bound

	#define rep(x,start,end) for(auto x=(start)-((start)>(end));x!=(end)-((start)>(end));((start)<(end)?x++:x--))
	#define all(x) (x).begin(),(x).end()
	#define sz(x) (int)(x).size()

	#define indexed_set tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update>
	//change less to less_equal for non distinct pbds, but erase will bug

	mt19937 rng(chrono::system_clock::now().time_since_epoch().count());

	int a,b;

	signed main(){
		ios::sync_with_stdio(0);
		cin.tie(0);
		cout.tie(0);
		cin.exceptions(ios::badbit | ios::failbit);

		int TC;
		cin>>TC;
		while (TC--){
			cin>>a>>b;
			cout<<abs(a-b)<<endl;
		}
	}
``

Tester-2's Solution
``#include <bits/stdc++.h>
using namespace std;

/*
---------Input Checker(ref : https://pastebin.com/Vk8tczPu )-----------
*/

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true)
    {
        char g = getchar();
        if (g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if (cnt == 0)
            {
                fi = g - '0';
            }
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if (g == endd)
        {
            if (is_neg)
            {
                x = -x;
            }

            if (!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        }
        else
        {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while (true)
    {
        char g = getchar();
        assert(g != -1);
        if (g == endd)
        {
            break;
        }
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r)
{
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r)
{
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r)
{
    return readString(l, r, '\n');
}
string readStringSp(int l, int r)
{
    return readString(l, r, ' ');
}

/*
-------------Main code starts here------------------------
*/

// Note here all the constants from constraints
const int MAX_T = 100;
const int MAX_VAL = 100;

// vars

void solve()
{
    int x, y, z;
    x = readIntSp(1, MAX_VAL);
    y = readIntLn(1, MAX_VAL);

    int answer = abs(x - y);
    cout << answer << '\n';
}

signed main()
{
    int t;
    t = readIntLn(1, MAX_T);

    for (int i = 1; i <= t; i++)
    {
        solve();
    }

    // Make sure there are no extra characters at the end of input
    assert(getchar() == -1);
    cerr << "SUCCESS\n";

    // Some important parameters which can help identify weakness in testdata
    cerr << "Tests : " << t << '\n';
}
``

Editorialist's Solution
``/*prakhar_87*/
#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define inf INT_MAX
#define mod 998244353

void f() {
    int x,y;
    cin>>x>>y;
    cout<<abs(x-y)<<"\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
