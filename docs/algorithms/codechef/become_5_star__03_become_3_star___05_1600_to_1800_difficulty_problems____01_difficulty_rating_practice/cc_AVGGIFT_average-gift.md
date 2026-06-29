# Average Gift

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGGIFT |
| Difficulty Rating | 1701 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [AVGGIFT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/AVGGIFT) |

---

## Problem Statement

Chef has a set $S$ containing $N$ **distinct** integers.

Chef wants to gift Chefina an array $A$ of any finite length such that the following conditions hold true:

- $A_i \in S$ $\forall i$. In other words, each element of the array $A$ should belong to the set $S$.
- [Mean](https://en.wikipedia.org/wiki/Mean) value of all the elements in $A$ is **exactly** $X$.

Find whether there exists an array $A$ of finite length satisfying the above conditions.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- First line of each test case contains two integers $N$ and $X$ - denoting the size of set $S$ and the mean value of the required array.
- Second line contains $N$ distinct integers $S_1, S_2, \dots , S_N$ - denoting the set $S$.

---

## Output Format

For each test case, output in a single line, `YES` if there exists an array satisfying the given conditions, `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq S_i \leq 10^9$
- $1 \leq X \leq 10^9$
- $S_i \neq S_j$ for $ i \neq j$
- Sum of $N$ over all test case do not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3 2
1 2 3
1 5
3
2 5
4 6
1 5
5
```

**Output**

```text
YES
NO
YES
YES
```

**Explanation**

**Test Case $1$:** One of the valid arrays is $A = [2,2]$. Here, $2 \in \{1, 2, 3\}$. Also, mean value of the array is $\frac{2+2}{2} = 2$.

**Test Case $2$:** Since all elements of the array can only be equal to $3$, the mean value of $A$ cannot be equal to $5$.

**Test Case $3$:** One of the valid arrays is $A = [4,6]$. Here, $4 \in \{4, 6\}$ and $6 \in \{4, 6\}$. Also, mean value of the array is $\frac{4+6}{2} = 5$.

**Test Case $4$:** One of the valid arrays is $A = [5]$. Here, $5 \in \{5\}$. Also, mean value of the array is $\frac{5}{1} = 5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
1 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 5
3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 5
4 6
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
1 5
5
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

[Contest Division 1](https://www.codechef.com/START38A/problems/AVGGIFT)

[Contest Division 2](https://www.codechef.com/START38B/problems/AVGGIFT)

[Contest Division 3](https://www.codechef.com/START38C/problems/AVGGIFT)

[Contest Division 4](https://www.codechef.com/START38D/problems/AVGGIFT)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1701

#
[](#prerequisites-3)PREREQUISITES:

The average of N values is :  \displaystyle\frac{Sum\:of\:all\:values}{N}

#
[](#problem-4)PROBLEM:

Chef has a set S containing N **distinct** integers.

Chef wants to gift Chefina an array A of any finite length such that the following conditions hold true:

-
A_i \in S \forall i. In other words, each element of the array A should belong to the set S.

-
[Mean](https://en.wikipedia.org/wiki/Mean) value of all the elements in A is **exactly** X.

Find whether there exists an array A of finite length satisfying the above conditions.

#
[](#explanation-5)EXPLANATION:

Let min be the minimum of N given integers and max be the maximum of N given integers, then the average of these N integers always lies in the range [min, max]. Therefore if min>X or max< X the answer is `NO`. Otherwise the answer is always `Yes`.

Proof that the answer is always `yes` for the latter scenario:

**Case 1**: X is present in S, take a single occurrence of X, it has an average of X.

**Case 2**: X is not present in S,

Let a=X-min and b=max-X.

Then \displaystyle\frac{(a\cdot max + b\cdot min)}{(a + b)} = (\displaystyle\frac{(max-X)\cdot min+(X-min)\cdot max)}{(max-X+X-min)}=\displaystyle\frac{X\cdot (max-min)}{(max-min)} = X.

This means we can take a occurrences of the maximum element in S and b occurrences of the minimum element in S to get an average of X.

Thus, if min\leq X\leq max  the answer is always `Yes` else `No`

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
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
int sumN=0;
void solve()
{
    int n=readInt(1,100000,' ');
    int x=readInt(1,1000000000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    set <ll> s;
    int maxi=0,mini=mod;
    for(int i=1;i<=n;i++)
    {
        int c;
        if(i==n)
            c=readInt(1,1000000000,'\n');
        else
            c=readInt(1,1000000000,' ');
        mini=min(mini,c);
        maxi=max(maxi,c);
        s.insert(c);
    }
    assert(s.size()==n);
    if(x>=mini && x<=maxi)
        cout<<"YES\n";
    else
        cout<<"NO\n";
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,1000,'\n');
    //cin>>T;
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n, x, mi = 1e9, mx = 1;
    cin >> n >> x;
    vll v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        mx = max(mx, v[i]);
        mi = min(mi, v[i]);
    }
    cout<<((mx>=x && mi<=x)?"YES\n":"NO\n");
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
