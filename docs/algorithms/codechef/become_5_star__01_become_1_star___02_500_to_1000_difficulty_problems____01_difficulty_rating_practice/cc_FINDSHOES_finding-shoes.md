# Finding Shoes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FINDSHOES |
| Difficulty Rating | 646 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FINDSHOES](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FINDSHOES) |

---

## Problem Statement

Chef has $N$ friends. Chef promised that he would gift a pair of shoes (consisting of one left shoe and one right shoe) to each of his $N$ friends. Chef was about to go to the marketplace to buy shoes, but he suddenly remembers that he already had $M$ left shoes.

What is the minimum number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his $N$ friends?

For example, if $N = 2$, $M = 4$, then Chef already has $4$ left shoes, so he must buy $2$ extra right shoes to form $2$ pairs of shoes.

Therefore Chef must buy at least $2$ extra shoes to **ensure** that he is able to get $N = 2$ pairs of shoes.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $M$ - the number of Chef's friends and the number of left shoes Chef has.

---

## Output Format

For each test case, output the minimum number of extra shoes that Chef will have to buy to ensure that he is able to get $N$ pairs of shoes.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $0 \leq M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
2 4
6 0
4 3
```

**Output**

```text
2
12
5
```

**Explanation**

**Test Case 1:** Discussed in the problem statement

**Test Case 2:** Chef initially has no left shoes. He must buy $6$ more left shoes and $6$ more right shoes to form $6$ pairs of shoes.

**Test Case 3:** Chef initially has $3$ left shoes. He must buy $1$ more left shoe and $4$ more right shoes to form $4$ pairs of shoes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6 0
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
4 3
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

[Contest Division 1](https://www.codechef.com/START32A/problems/FINDSHOES)

[Contest Division 2](https://www.codechef.com/START32B/problems/FINDSHOES)

[Contest Division 3](https://www.codechef.com/START32C/problems/FINDSHOES)

[Contest Division 4](https://www.codechef.com/START32D/problems/FINDSHOES)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Ashley Khoo](https://www.codechef.com/users/errorgorn), [ Nishant Shah](https://www.codechef.com/users/nishant_adm)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has N friends. Chef promised that he would gift a pair of shoes (consisting of one left shoe and one right shoe) to each of his N friends. Chef was about to go to the marketplace to buy shoes, but he suddenly remembers that he already had M left shoes.

What is the **minimum** number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his N friends?

#
[](#explanation-5)EXPLANATION:

Given that Chef needs to buy N pair of shoes i.e. N left shoes and N right shoes.

**For left shoes**

Since Chef already has M left shoes, following 2 cases are possible

-

M \geq N; In this case, Chef doesn’t need to buy any left shoe as he already has the required quantity.

-

M \lt N; In this case, Chef will need to buy N-M more left shoes to gift a total of N left shoes.

**For right shoes**

Chef will need to buy all the required N right shoes since there are no right shoes already present with him.

Therefore, minimum number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his N friends is given by following equation

**Minimum** number of shoes Chef needs to buy are  = N + max(0, N-M)

Examples

N = 5, M = 4;

Minimum number of shoes Chef needs to buy are  = 5 + max(0, 1) = 6

N = 5, M = 6;

Minimum number of shoes Chef needs to buy are  = 5 + max(0, -1) = 5

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Tester-1's Solution
``// Super Idol???
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
		cout<<a+max(0LL,a-b)<<endl;
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
int opt_a = 0;
int opt_b = 0;

void solve()
{
    int n, m;

    n = readIntSp(1, MAX_VAL);
    m = readIntLn(0, MAX_VAL);

    int answer = n + n - min(m, n);

    if (m < n)
        opt_a++;
    else
        opt_b++;

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
    cerr << "Option  A : " << opt_a << '\n';
    cerr << "Option  B : " << opt_b << '\n';
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
    int n, m;
    cin >> n >> m;
    cout << n + max(0ll, n - m) << "\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
