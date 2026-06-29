# Segment Three

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEGTHREE |
| Difficulty Rating | 2089 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SEGTHREE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SEGTHREE) |

---

## Problem Statement

Today is an important day for Chef Hammoda as a lot of customers will be visiting his restaurant.
The restaurant contains $N$ tables, and each customer will sit at one table.

Initially, Chef Hammoda plans for the dish served to the $i$-th table to contain $A_i$ ingredients.
However, he thinks that a group of three dishes is *delicious* if the sum of the number of ingredients of the three dishes is divisible by $3$.

Hammoda wants every consecutive group of $3$ tables to have delicious dishes. To achieve this, he can add as many ingredients as he wants to each dish.
Help him determine the **minimum** number of additional ingredients needed to make every group of three consecutive tables *delicious*.

More formally, solve the following problem:
You are given an array $A = [A_1, A_2, \ldots, A_N]$ of length $N$. You're allowed to increment each element however much you like.
Find the **minimum** number of increments needed so that in the resulting array, the sum of every three consecutive elements is divisible by $3$

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of tables.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — number of ingredients initially present in the $i^{th}$ dish.

---

## Output Format

For each test case, print on a new line a single integer: the minimum number of increments needed to make every length-$3$ subarray of $A$ have a sum that's divisible by $3$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $3 \leq N \leq 10^5$
- $1 \leq a_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 3 
10
2 3 10 25 12 7 10 12 1 46
7
10 12 15 16 17 200 132
```

**Output**

```text
0
3
4
```

**Explanation**

**Test case $1$:** There is only one subarray of length $3$, and its sum already divisible by $3$.

**Test case $2$:** The array after increments can be:
$[2, 3, 10, \underline{26}, 12, 7, \underline{11}, 12, 1, \underline{47}]$
for a total of $3$ increments (the elements underlined were all incremented by $1$ each). Every subarray of length $3$ now has a sum that's divisible by $3$.
It can be proved that it's not possible to achieve this using two or fewer increments.

**Test case $3$:** The array after increments can be:
$[10, 12, \underline{17}, 16, \underline{18}, 200, \underline{133}]$
for a total of $4$ increments.
Here, $15$ was incremented twice to reach $17$, and the other two elements were incremented once each.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
10
2 3 10 25 12 7 10 12 1 46
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
7
10 12 15 16 17 200 132
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SEGTHREE)

[Contest: Division 1](https://www.codechef.com/START99A/problems/SEGTHREE)

[Contest: Division 2](https://www.codechef.com/START99B/problems/SEGTHREE)

[Contest: Division 3](https://www.codechef.com/START99C/problems/SEGTHREE)

[Contest: Division 4](https://www.codechef.com/START99D/problems/SEGTHREE)

***Author:*** [adhoom](https://www.codechef.com/users/adhoom)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2089

# [](#prerequisites-3)PREREQUISITES:

Observation

# [](#problem-4)PROBLEM:

You’re given an array A.

In one step, you can increase one of its elements by 1.

Find the minimum number of moves needed to reach an array for which every subarray of size 3 has a sum divisible by 3.

# [](#explanation-5)EXPLANATION:

First, observe that every element will be increased by either 0, 1, \text{or } 2.

Performing more than two increments on a single element is useless: you could reduce it by 3 and achieve the same result.

Let B be the final array we attain after increments, where each size-3 subarray has its sum divisible by 3.

Notice that, if we fix B_1 and B_2, the rest of the elements of B are also uniquely fixed!

In fact, we can even find them all easily in \mathcal{O}(N) time.

How?

Suppose B_1 and B_2 are fixed. Then,

- (B_1 + B_2 + B_3) must be divisible by 3.

Since B_1 and B_2 are fixed, we already have the sum (B_1 + B_2 + A_3) — and we can only increase A_3.

Since the number of moves required should be minimum, our best bet is to increase A_3 by either 0, 1, \text{ or } 2. Exactly one of these will let us reach a sum that’s divisible by 3.

Notice that this means B_3 is fixed uniquely, to one of \{A_3, A_3+1, A_3+2\}.

- Next, (B_2 + B_3 + B_4) should be divisible by 3.

Once again, B_2 and B_3 are fixed, so B_4 is determined uniquely.

- Continuing on this way from left to right, each B_i is fixed in order, hence fixing the entire array.

Combining this with our first observation (that each A_i will be increased by at most 2) we see that there aren’t too many options to check.

In particular:

- B_1 is one of (A_1, A_1+1, A_1+2)

- B_2 is one of (A_2, A_2+1, A_2+2)

This gives us 3\times 3 = 9 options in total for B_1 and B_2.

For each option, the entire B array can be computed in \mathcal{O}(N) time, as detailed in the spoiler above.

So, simply try all 9 options, compute the B array for them all, and find which of them uses the least number of increments in total.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(9\cdot N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``///       ______        __________                    _____   _____        _____
///      ///  \\\      ||__||   \\\    |||     |||  ||     || |||\\\      ///|||
///     ///    \\\     ||__||    \\\   |||_____|||  ||     || ||| \\\    /// |||
///    ///______\\\    ||__||     \\\  |||_____|||  ||     || |||  \\\  ///  |||
///   ///________\\\   ||__||     ///  |||_____|||  ||     || |||   \\\///   |||
///  ///          \\\  ||__||    ///   |||     |||  ||     || |||            |||
/// ///            \\\ ||__||___///    |||     |||  ||_____|| |||            |||

#include<bits/stdc++.h>
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
using namespace std;
typedef long long ll;
typedef long double ld;
const ll N=1e5+5;
ll a[N];
ll dp[N][4][4];
ll vis[N][4][4];
ll cur=2;
ll n;
ll solve(ll idx,ll prv1,ll prv2)
{
    if(idx==n)return 0;
    ll &ans=dp[idx][prv1][prv2];
    ll &v=vis[idx][prv1][prv2];
    if(v==cur)return ans;
    v=cur;
    ans=4e18;
    for(int i=0;i<3;i++)
    {
        ll x=a[idx];
        ll c=0;
        while(x%3!=i)x++,c++;
        if(prv1==3)ans=min(ans,solve(idx+1,i,prv2)+c);
        else if(prv2==3)ans=min(ans,solve(idx+1,prv1,i)+c);
        else
        {
            if((i+prv1+prv2)%3==0)
            {
                ans=min(ans,solve(idx+1,prv2,i)+c);
            }
        }
    }
    return ans;
}
void test_case()
{
    cin>>n;
    for(int i=0;i<n;i++)cin>>a[i];
    cur++;
    ll ans=4e18;
    ans=min(ans,solve(0,3,3));
    cout<<ans<<endl;
}
int main()
{
//    FIO
//  freopen("input.txt","rt",stdin);
//  freopen("output.txt","wt",stdout);
    ll t;
    t=1;
    cin>>t;
    while(t--)
    {
        test_case();
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
struct dsu{
    vector<ll> parent,height;
    ll n,len;
    dsu(ll n){
        this->n=n;
        parent.resize(n);
        height.resize(n);
        len=n;
        for(ll i=0;i<n;i++){
            parent[i]=i;
            height[i]=1;
        }
    }
    ll find_set(ll x){
        return find_set(x,x);
    }
    ll find_set(ll x,ll orig){
        if(parent[x]==x){
            return x;
        }
        parent[orig]=find_set(parent[x]);
        return parent[orig];
    }
    void union_set(ll u,ll v){
        u=find_set(u),v=find_set(v);
        if(u==v){
            return;
        }
        len--;
        if(height[u]<height[v]){
            swap(u,v);
        }
        parent[v]=u;
        height[u]+=height[v];
    }
    ll getv(ll l){
        l=find_set(l);
        return height[l];
    }
};
void solve(){
    ll n; cin>>n;
    vector<ll> a(n);
    for(auto &i:a){
        cin>>i;
        i%=3;
    }
    ll ans=n;
    for(ll l=0;l<=2;l++){
        for(ll r=0;r<=2;r++){
            ll now=0;
            vector<ll> b={l,r};
            for(ll i=2;i<n;i++){
                b.push_back((6-b[i-1]-b[i-2])%3);
            }
            for(ll i=0;i<n;i++){
                ll cur=a[i];
                while((cur%3)!=b[i]){
                    now++;
                    cur++;
                }
            }
            ans=min(ans,now);
        }
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
    ll test_cases; cin>>test_cases;
    while(test_cases--){
        solve();
    }
    assert(sum_n<=g(1e5));
    assert(getchar()==-1);
    return 0;
}
``

Editorialist's code (Python)
``from itertools import product
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**9
    for x, y in product([0, 1, 2], repeat=2):
        moves = x + y
        p1, p2 = a[0] + x, a[1] + y
        for i in range(2, n):
            cur = p1 + p2 + a[i]
            moves += (-cur)%3
            p1, p2 = p2, (a[i]-cur)%3
        ans = min(ans, moves)
    print(ans)
``

</details>
