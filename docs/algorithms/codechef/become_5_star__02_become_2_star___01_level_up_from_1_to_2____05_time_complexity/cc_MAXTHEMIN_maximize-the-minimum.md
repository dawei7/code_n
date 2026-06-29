# Maximize the Minimum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXTHEMIN |
| Difficulty Rating | 1358 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [MAXTHEMIN](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/MAXTHEMIN) |

---

## Problem Statement

JJ has an array $A$ of size $N$. He can perform the following operations on the array **at most** $K$ times:

- Set $A_i := A_{i + 1}$ where $1 \le i \le N - 1$
- Set $A_i := A_{i - 1}$ where $2 \le i \le N$

He wants to maximize the value of the minimum element of the array $A$. Formally, he wants to maximize the value of $\min\limits_{1 \le i \le N} A_i$.

Can you help him do so?

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $K$ - the size of the array $A$ and the maximum number of operations allowed respectively.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the maximum value of the minimum element of the array $A$ that can be obtained after applying the given operation at most $K$ times.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $0 \le K \le 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
5 4
5 4 3 2 1
6 1
8 2 3 9 6 10
5 2
4 3 4 3 5
5 1000
4 3 4 3 5
```

**Output**

```text
5
3
4
5
```

**Explanation**

**Test Case 1:** We can perform the following operations (in the following order):
- Set $A_2 := A_1$. Array $A$ becomes $[5, 5, 3, 2, 1]$
- Set $A_3 := A_2$. Array $A$ becomes $[5, 5, 5, 2, 1]$
- Set $A_4 := A_3$. Array $A$ becomes $[5, 5, 5, 5, 1]$
- Set $A_5 := A_4$. Array $A$ becomes $[5, 5, 5, 5, 5]$

Therefore the answer is $5$.

**Test Case 2:** We can perform the following operations (in the following order):
- Set $A_2 := A_3$. Array $A$ becomes $[8, 3, 3, 9, 6, 10]$

Therefore the answer is $3$.

**Test Case 3:** We can perform the following operations (in the following order):
- Set $A_2 := A_3$. Array $A$ becomes $[4, 4, 4, 3, 5]$
- Set $A_4 := A_3$. Array $A$ becomes $[4, 4, 4, 4, 5]$

Therefore the answer is $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4
5 4 3 2 1
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
6 1
8 2 3 9 6 10
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
5 2
4 3 4 3 5
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
5 1000
4 3 4 3 5
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

[Contest - Division 4](https://www.codechef.com/START32D/problems/MAXTHEMIN)

[Contest - Division 3](https://www.codechef.com/START32C/problems/MAXTHEMIN)

[Contest - Division 2](https://www.codechef.com/START32B/problems/MAXTHEMIN)

[Contest - Division 1](https://www.codechef.com/START32A/problems/MAXTHEMIN)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#problem-3)PROBLEM:

Given an array A of N integers. You may perform atmost K moves of the following type - change the value of A_i to either of it’s adjacent values.

Determine the maximum possible value of \min (A_1,A_2,\dots,A_N).

#
[](#explanation-4)EXPLANATION:

The solution of the problem boils down to one crucial observation - setting the value of A_i to either of it’s adjacent values is equivalent to erasing element A_i from A.

Then, the problem is reduced to erasing at most K elements from A such that the minimum value is maximised. This can be done by sorting A and erasing the first K smallest elements.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(N\log N)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/61703190).

Author's solution
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const long long INF = 1e18;

const int N = 1e6 + 5;

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(false);
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
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

int sumN = 0;

void solve()
{
    int n = readIntSp(2, 1e5);
    int k = readIntLn(0, 1e5);
    sumN += n;
    vector<int> a = readVectorInt(n, 1, 1e9);
    sort(a.begin(), a.end());
    k = min(k, n - 1);
    cout << a[k] << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 100);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    readEOF();
    assert(sumN <= 2e5);
    return 0;
}
``

Tester's solution
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

int n,k;
int arr[200005];

signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin.exceptions(ios::badbit | ios::failbit);

	int TC;
	cin>>TC;
	while (TC--){
		cin>>n>>k;
		rep(x,0,n) cin>>arr[x];
		sort(arr,arr+n);
		cout<<arr[min(k,n-1)]<<endl;
	}
}
``

</details>
