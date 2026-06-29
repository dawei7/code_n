# Two Piles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPLITMIN |
| Difficulty Rating | 2347 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SPLITMIN](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SPLITMIN) |

---

## Problem Statement

You are given $N$ pairs of integers. The $i$-th pair is $(A_i, B_i)$.
You also have two piles with you, both initially empty.

You will perform the following process:
- For each $i$ from $1$ to $N$, choose **exactly one** of $A_i$ or $B_i$.
- Then, add the chosen integer to one of your two piles.

At the end of the process, both piles **must be non-empty** (i.e, you should have added at least one integer to both).

The *value* of a pile is defined to be its maximum element.
If you make your choices optimally, find the **minimum possible difference** between the *values* of the piles.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the number of pairs.
    - The next $N$ lines describe the pairs. The $i$-th of these lines contains two space-separated integers $A_i$ and $B_i$ — the elements of the $i$-th pair.

---

## Output Format

For each test case, output on a new line the minimum possible difference between the values of the piles.

---

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
1 6
4 9
2
1 9
4 6
4
10 10
23 55
21 80
105 91
```

**Output**

```text
2
3
11
```

**Explanation**

**Test case $1$:** The pairs are $(1, 6)$ and $(4, 9)$.
Choose $6$ from the first pair, and $4$ from the second pair, and place them on different piles.
The maximums are $6$ and $4$, and the difference between them is $|6-4| = 2$.
Achieving a smaller difference is not possible.

**Test case $2$:** The pairs are $(1, 9)$ and $(4, 6)$.
Choose $1$ from the first pair and $4$ from the second pair and place them on different piles, for a difference of $3$.

**Test case $3$:** One optimal solution is:
- From the first pair, place $10$ on pile $1$.
- From the second pair, place $55$ on pile $2$.
- From the third pair, place $80$ on pile $2$.
- From the fourth pair, place $91$ on pile $1$.

The difference between the maximums of the piles is $|80 - 91| = 11$. This is the smallest possible difference.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPLITMIN)

[Contest: Division 1](https://www.codechef.com/START99A/problems/SPLITMIN)

[Contest: Division 2](https://www.codechef.com/START99B/problems/SPLITMIN)

[Contest: Division 3](https://www.codechef.com/START99C/problems/SPLITMIN)

[Contest: Division 4](https://www.codechef.com/START99D/problems/SPLITMIN)

***Author:*** [ziad_el_gafy](https://www.codechef.com/users/ziad_el_gafy)

***Preparer:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2347

# [](#prerequisites-3)PREREQUISITES:

Sorting

# [](#problem-4)PROBLEM:

You’re given N pairs of the form (A_i, B_i).

You also have two empty piles.

From each pair, choose exactly one element and add it to one of the two piles.

Find the minimum possible difference between the maximum elements of the piles. Both piles should be non-empty.

# [](#explanation-5)EXPLANATION:

Let the two piles be P_1 and P_2.

Initially, both are empty.

Let’s fix the maximum element of P_1, say to x; then try to find the optimal maximum element y of P_2.

Without loss of generality, we can assume x \geq y as well; so our task is to find an element that’s as close to x as possible but less than it.

This is easily done with the help of sorting, for example.

However, there are a couple things to be careful about:

- First, if there’s a pair such that A_i \gt x *and* B_i \gt x, then having x as the larger maximum is not possible.

So, we need to ensure that for every pile, at least one element is \leq x.

In particular, we need x \geq \min(A_i, B_i) for all i.

Let M be the maximum among the \min(A_i, B_i) values. Then, x \geq M should hold.

- Second, we need to ensure that x and y don’t belong to the same pair; since if that were the case, we wouldn’t be able to pick both of them and put them in different piles.

With these two points in mind, we end up with a rather simple solution.

Let S be a sorted array of length 2N, containing **all** the elements A_i and B_i.

For example, if the pairs are (1, 2), (2, 3), (1, 4) then S = [1, 1, 2, 2, 3, 4].

Also, for each i, remember which pair S_i comes from.

Further, compute M = \max_{i=1}^N(\min(A_i, B_i)), as we saw above.

Then, for each i from 1 to N:

- Let’s try and treat S_i as x.

For this, S_i \geq M must hold; so if S_{i} \lt M then ignore this index.

- If S_i \geq x does indeed hold, then we need to choose y to be the closest possible element to it.

This, of course, is just S_{i-1}.

However, there is one catch: if S_i and S_{i-1} belong to the same pair, then the optimal value of y is S_{i-2} instead.

- Once y is found, the difference here is (S_i-y).

The final answer is the minimum value of this difference, across all i.

After sorting S, this obviously takes \mathcal{O}(N) time; so the algorithm as a whole takes \mathcal{O}(N\log N) time.

As an aside, notice that we only cared about the two maximums, and not how the other elements were distributed.

However, once x and y are fixed, it’s not hard to see that all the other elements can be distributed properly to achieve this, because of the condition x \geq M.

- Place x in P_1.

- Place y in P_2.

- For every one of the other N-2 pairs, we know one element exists that’s \leq x. Choose one such element and place it in P_1.

This way, the maximum of pile P_1 is x, and the maximum of pile P_2 is y, as we wanted.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Editorialist's code (C++)
``// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include "bits/stdc++.h"
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
    ios::sync_with_stdio(false); cin.tie(0);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<array<int, 2>> a;
        for (int i = 0; i < n; ++i) {
            int x, y; cin >> x >> y;
            a.push_back({x, i});
            a.push_back({y, i});
        }
        sort(begin(a), end(a));

        int ans = INT_MAX, seen = 0;
        vector<int> mark(n);
        for (int i = 0; i < 2*n; ++i) {
            seen += 1 - mark[a[i][1]];
            mark[a[i][1]] = 1;
            if (seen == n) {
                if (a[i][1] == a[i-1][1]) ans = min(ans, a[i][0] - a[i-2][0]);
                else ans = min(ans, a[i][0] - a[i-1][0]);
            }
        }
        cout << ans << '\n';
    }
}
``

Tester's code (C++)
``#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast,unroll-loops")
#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
#define ll long long

/*
------------------------Input Checker----------------------------------
*/

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        if(g=='-'){
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g && g<='9'){
            x*=10;
            x+=g-'0';
            if(cnt==0){
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd){
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
        char g=getchar();
        assert(g!=-1);
        if(g==endd){
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt && cnt<=r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}

/*
------------------------Main code starts here----------------------------------
*/
const ll MOD=1e9+7;
vector<ll> readv(ll n,ll l,ll r){
    vector<ll> a;
    ll x;
    for(ll i=1;i<n;i++){
        x=readIntSp(l,r);
        a.push_back(x);
    }
    x=readIntLn(l,r);
    a.push_back(x);
    return a;
}
const ll MAX=3000300;
ll sum_n=0;
void dbug(vector<ll> a){
    for(auto t:a){
        cout<<t<<" ";
    }
    cout<<endl;
}
ll binpow(ll a,ll b,ll MOD){
    ll ans=1;
    a%=MOD;
    while(b){
        if(b&1)
            ans=(ans*a)%MOD;
        b/=2;
        a=(a*a)%MOD;
    }
    return ans;
}
ll inverse(ll a,ll MOD){
    return binpow(a,MOD-2,MOD);
}
ll gt(ll n,ll freq,ll k){
    ll pw=(binpow(2,k,MOD-1)*freq)%(MOD-1);
    ll now=(binpow(n,pw+1,MOD)-binpow(n,freq,MOD)+MOD)*inverse(n-1,MOD);
    now%=MOD;
    return now;
}
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
typedef tree<ll, null_type, less_equal<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_multiset;
typedef tree<pair<ll,ll>, null_type, less<pair<ll,ll>>, rb_tree_tag, tree_order_statistics_node_update> ordered_pset;
bool check_distinct(vector<ll> a){
    sort(a.begin(),a.end());
    ll n=a.size();
    for(ll i=1;i<n;i++){
        assert(a[i]!=a[i-1]);
    }
    return true;
}
ll g(ll x){
    return x;
}
void solve(){
    ll n=readIntLn(2,g(2e5));
    sum_n+=n;
    vector<pair<ll,ll>> track;
    for(ll i=1;i<=n;i++){
        ll l=readIntSp(1,g(1e9)),r=readIntLn(1,g(1e9));
        track.push_back({l,i});
        track.push_back({r,i});
    }
    sort(track.begin(),track.end());
    multiset<ll> check;
    vector<ll> used(n+5,0);
    set<ll> found;
    ll ans=(ll)(1e18);
    for(auto it:track){
        ll val=it.first,pos=it.second;
        found.insert(pos);
        if(found.size()==n){
            if(used[pos]){
                check.erase(check.find(used[pos]));
            }
            ans=min(ans,val-*(--check.end()));
            if(used[pos]){
                check.insert(used[pos]);
            }
        }
        used[pos]=val;
        check.insert(val);
    }
    cout<<ans<<"\n";
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    ll test_cases=readIntLn(1,g(1e4));
    while(test_cases--){
        solve();
    }
    assert(sum_n<=g(2e5));
    assert(getchar()==-1);
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    pairs = []
    m = 0
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, i))
        pairs.append((b, i))
        m = max(m, min(a, b))
    pairs.sort()
    ans = 10**9
    for i in range(2*n):
        if pairs[i][0] < m: continue
        if pairs[i][1] == pairs[i-1][1]:
            ans = min(ans, pairs[i][0] - pairs[i-2][0])
        else:
            ans = min(ans, pairs[i][0] - pairs[i-1][0])
    print(ans)
``

</details>
