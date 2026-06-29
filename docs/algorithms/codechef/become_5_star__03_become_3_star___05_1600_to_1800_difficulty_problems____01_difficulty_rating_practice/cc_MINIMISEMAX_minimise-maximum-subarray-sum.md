# Minimise Maximum Subarray Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINIMISEMAX |
| Difficulty Rating | 1649 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [MINIMISEMAX](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/MINIMISEMAX) |

---

## Problem Statement

You are given two positive integers $X$ and $Y$.
Consider an array $A$ consisting of $X$ occurrences of $1$ and $Y$ occurrences of $-2$.

You can rearrange the elements of $A$ in any order.
Rearrange the elements to **minimize** the maximum sum over all subarrays of $A$.
Find the maximum subarray sum of such rearrangement of $A$.

---

## Input Format

- The first line contains a single integer $T$, denoting the number of test cases.
- The only line of each test case contains two space-separated integers $X$ and $Y$, denoting the number of occurrences of $1$ and $-2$ respectively.

---

## Output Format

For each test case, print the maximum sum of subarray if you rearrange $A$ optimally.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X,Y \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
4
1 1
1 3
5 1
2 2
```

**Output**

```text
1
1
3
1
```

**Explanation**

**Test case $1$:** Here either $A = [1,-2]$ or $A = [-2, 1]$. In both cases, maximum subarray sum is $1$.

**Test case $2$:** The array consists of one $1$ and three $-2$. Thus, maximum subarray sum would be $1$.

**Test case $3$:** Consider $A = [1, 1, -2, 1, 1, 1]$. The maximum subarray sum here is $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 3
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 1
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
2 2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINIMISEMAX)

[Contest: Division 1](https://www.codechef.com/START113A/problems/MINIMISEMAX)

[Contest: Division 2](https://www.codechef.com/START113B/problems/MINIMISEMAX)

[Contest: Division 3](https://www.codechef.com/START113C/problems/MINIMISEMAX)

[Contest: Division 4](https://www.codechef.com/START113D/problems/MINIMISEMAX)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You have an array A containing X occurrences of 1 and Y occurrences of -2.

What’s the minimum possible value of the maximum subarray sum of A, if you can freely rearrange its elements?

# [](#explanation-5)EXPLANATION:

Since X\geq 1, it’s always possible to obtain a subarray sum of 1 since A contains a 1.

If we can ensure that no two 1's are adjacent to each other, we can ensure that no subarray has a sum that’s \gt 1.

This is possible if and only if Y \geq X-1, creating the array A = [1, -2, 1, -2, 1, \ldots].

So, if Y\geq X-1, the answer is 1.

What if Y\lt X-1? Well, we certainly can’t prevent some two ones from being adjacent, so the answer is at least 2.

Once again, if we have “enough” -2's, we can ensure that the maximum subarray sum is exactly 2.

For this, we’d need one -2 for two 1's, so that we can create [1, 1, -2, 1, 1, -2, \ldots], that is, we need 2Y\geq X-1 to hold (one -2 after each pair of 1's, except the last pair).

It’s easy to see that with such a construction, the maximum subarray sum is exactly 2.

Next, what if 2Y \lt X-1?

In this case, the answer is just X-2Y, the sum of all the elements.

This is clearly a lower bound on the answer in any case, since it’s always possible to just choose the entire array.

To construct an array that achieves this, simply split all the ones into Y+1 blocks of approximately equal size, and separate the blocks by placing single -2's between them.

“Approximately equal size” means that each block of ones will have size either \left\lfloor \frac{X}{Y+1} \right\rfloor, or \left\lceil \frac{X}{Y+1} \right\rceil.

It’s not hard to see that the maximum subarray sum is to just take the entire array.

Proof

Let [L, R] be one maximum sum subarray.

We’ll prove that L = 1 must hold.

If L \gt 1, there are two choices:

- First, if A_{L-1} = 1, then clearly [L-1, R] is a subarray with larger sum; which can’t happen.

- So, S_{L-1} = -2 should hold.

However, there are at least \left\lfloor \frac{X}{Y+1} \right\rfloor 1's immediately preceding this -2, and since 2Y \lt X-1 we know that \left\lfloor \frac{X}{Y+1} \right\rfloor \geq 3.

So, it’d be optimal to take the -2 along with the block of 1's and attain a larger sum.

So, if L\gt 1, [L, R] can’t be a maximum sum subarray.

Similarly it can be seen that R = N must hold; so choosing the entire array is optimal.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#pragma GCC optimize("O3,unroll-loops")
#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define nline "\n"
#define f first
#define s second
#define pll pair<ll,ll>
#define all(x) x.begin(),x.end()
#define vl vector<ll>
#define vvl vector<vector<ll>>
#define vvvl vector<vector<vector<ll>>>
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
void _print(ll x){cerr<<x;}
void _print(char x){cerr<<x;}
void _print(string x){cerr<<x;}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
template<class T,class V> void _print(pair<T,V> p) {cerr<<"{"; _print(p.first);cerr<<","; _print(p.second);cerr<<"}";}
template<class T>void _print(vector<T> v) {cerr<<" [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T>void _print(set<T> v) {cerr<<" [ "; for (T i:v){_print(i); cerr<<" ";}cerr<<"]";}
template<class T>void _print(multiset<T> v) {cerr<< " [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T,class V>void _print(map<T, V> v) {cerr<<" [ "; for(auto i:v) {_print(i);cerr<<" ";} cerr<<"]";}
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
typedef tree<ll, null_type, less_equal<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_multiset;
typedef tree<pair<ll,ll>, null_type, less<pair<ll,ll>>, rb_tree_tag, tree_order_statistics_node_update> ordered_pset;
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const ll MOD=1e9+7;
const ll MAX=500500;
void solve(){
    ll x,y; cin>>x>>y;
    ll ans=max(x-2*y,1ll+(x>(y+1)));
    cout<<ans<<nline;
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    ll test_cases=1;
    cin>>test_cases;
    while(test_cases--){
        solve();
    }
    cout<<fixed<<setprecision(10);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            if (buffer[pos] == '\r') {
                continue;
            }
            assert(!isspace(buffer[pos]));
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    int tt; cin >> tt;
    while (tt--) {
        int x, y;
        cin >> x >> y;
        if (y >= x - 1) {
            cout << 1 << '\n';
            continue;
        }
        cout << max(2, x - 2 * y) << '\n';
    }
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    if y >= x-1: ans = 1
    elif 2*y >= x-1: ans = 2
    else: ans = x-2*y
    print(ans)
``

</details>
