# Eat Twice

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EATTWICE |
| Difficulty Rating | 1370 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EATTWICE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EATTWICE) |

---

## Problem Statement

Hasan has recently heard about Chef's restaurant, which serves the tastiest dishes. The restaurant has published a list of $N$ dishes (numbered $1$ through $N$) that will be served in the next $M$ days. For each valid $i$, the $i$-th dish will be served only on the $D_i$-th day. Hasan has investigated their tastiness and he knows that for each valid $i$, the $i$-th dish has tastiness $V_i$.

Hasan's budget is only large enough to try two dishes. He wants to choose these two dishes in such a way that their total (summed up) tastiness is as large as possible. However, he cannot try 2 dishes on the same day.

Help Hasan and calculate the maximum possible total tastiness of the dishes he should try.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $D_i$ and $V_i$.

### Output
For each test case, print a single line containing one integer — the maximum total tastiness.

### Constraints
- $1 \le T \le 1,000$
- $2 \le N, M \le 10^5$
- $1 \le D_i \le M$ for each valid $i$
- $1 \le V_i \le 10^9$ for each valid $i$
- there are at least two dishes that are served on different days
- the sum of $N$ over all test cases does not exceed $10^6$
- the sum of $M$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
2
3 6
5 7
1 9
2 5
3 7
5 8
2 5
5 10
```

**Output**

```text
16
15
```

**Explanation**

**Example case 1:** The optimal solution is to try dishes $1$ and $2$.

**Example case 2:** The optimal solution is to try dishes $2$ and $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 6
5 7
1 9
2 5
```

**Output for this case**

```text
16
```



#### Test case 2

**Input for this case**

```text
3 7
5 8
2 5
5 10
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EATTWICE)

[Contest: Division 1](https://www.codechef.com/COOK107A/problems/EATTWICE)

[Contest: Division 2](https://www.codechef.com/COOK107B/problems/EATTWICE)

**Setter:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

# DIFFICULTY:

# PREREQUISITES:

Greedy.

# PROBLEM:

A restaurant makes N dishes in M days with $i$th dish on day d_i and has tastiness v_i. Chef can eat atmost two dishes and not both on the same day. Find the maximum total tastiness of the dishes he can eat.

# EXPLANATION

Let us group dishes based on the day they are made.

On each day,since chef can eat atmost one dish, he will only prefer to eat the dish with highest tastiness. So let us calculate the highest taste of a dish on each day (lets represent it by t_i for i th day).

Now, he will eat on the two days which have highest and second highest value of t_i among all days when a dish is made in the restaurant.

# TIME COMPLEXITY

O(n+m). First part of grouping takes O(n) time. Second part of finding max and second max element in array t among all the m days takes O(m) time.

**Bonus:** We can also reduce time complexity to O(n) which I leave it for the comments.

# SOLUTIONS:

Setter's Solution
``#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <assert.h>
using namespace std;

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
            assert(cnt>0);
            if(is_neg){
                x= -x;
            }
            assert(l<=x && x<=r);
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

int T;
int n,m;
int sm_n=0;
int sm_m=0;

int mx[100100];

int main(){
    //freopen("01.txt","r",stdin);
    //freopen("01o.txt","w",stdout);
    T=readIntLn(1,1000);
    while(T--){
        n=readIntSp(2,100000);
        m=readIntLn(2,100000);
        sm_n += n;
        sm_m += m;
        assert(n<=1000000);
        assert(m<=1000000);
        for(int i=1;i<=m;i++){
            mx[i]=0;
        }
        set<int> g;
        for(int i=1;i<=n;i++){
            int d,v;
            d=readIntSp(1,m);
            g.insert(d);
            v=readIntLn(1,1000000000);
            mx[d]=max(mx[d],v);
        }
        assert(g.size()>1);
        sort(mx+1,mx+1+m);
        cout<<mx[m]+mx[m-1]<<endl;
    }
    assert(getchar()==-1);
}
``

Tester's Solution
``//teja349
#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx
//cout.precision(x)  cout<<fixed<<val;  // prints x digits after decimal in val

using namespace std;
using namespace __gnu_pbds;

#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >
#define flush fflush(stdout)
#define primeDEN 727999983
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

// find_by_order()  // order_of_key
typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

int d[123456],v[123456],maxi[123456];
int main(){
    std::ios::sync_with_stdio(false); cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        int i;
        rep(i,n){
            cin>>d[i]>>v[i];
            maxi[d[i]]=max(maxi[d[i]],v[i]);
        }
        vi vec;
        rep(i,n){
            if(maxi[d[i]]==0)
                continue;
            vec.pb(maxi[d[i]]);
            maxi[d[i]]=0;
        }
        assert(vec.size()>=2);
        sort(all(vec));
        int siz=vec.size();
        cout<<vec[siz-1]+vec[siz-2]<<endl;
    }
    return 0;
}
``

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
