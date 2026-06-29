# First and Last

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIRSTANDLAST |
| Difficulty Rating | 932 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [FIRSTANDLAST](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FIRSTANDLAST) |

---

## Problem Statement

You are given an array $A = [A_1, A_2, \ldots, A_N]$ of length $N$.

You can right rotate it any number of times (possibly, zero). What is the maximum value of $A_1 + A_N$ you can get?

**Note:** Right rotating the array $[A_1, A_2, \ldots, A_N]$ once gives the array $[A_N, A_1, A_2, \ldots, A_{N-1}]$. For example, right rotating $[1, 2, 3]$ once gives $[3, 1, 2]$, and right rotating it again gives $[2, 3, 1]$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
5 8
3
5 10 15
4
4 4 4 4
```

**Output**

```text
13
25
8
```

**Explanation**

**Test case $1$:** Whether you right rotate the array or not, you will always end up with $A_1+A_N = 13$.

**Test case $2$:** It is optimal to right rotate the array once after which the array becomes $[15,5,10]$ with $A_1 + A_N = 25$.

**Test case $3$:** No matter how much you right rotate the array, you will always obtain $A_1 + A_N = 8$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
5 8
```

**Output for this case**

```text
13
```



#### Test case 2

**Input for this case**

```text
3
5 10 15
```

**Output for this case**

```text
25
```



#### Test case 3

**Input for this case**

```text
4
4 4 4 4
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK142A/problems/FIRSTANDLAST)

[Contest Division 2](https://www.codechef.com/COOK142B/problems/FIRSTANDLAST)

[Contest Division 3](https://www.codechef.com/COOK142C/problems/FIRSTANDLAST)

[Contest Division 4](https://www.codechef.com/COOK142D/problems/FIRSTANDLAST)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

932

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array A=[A_1,A_2,…,A_N] of length N.

You can right rotate it any number of times (possibly, zero). What is the maximum value of A_1+A_N you can get?

Note: Right rotating the array [A_1,A_2,…,A_N] once gives the array [A_N,A_1,A_2,…,A_{N?1}]. For example, right rotating [1,2,3] once gives [3,1,2], and right rotating it again gives [2,3,1].

#
[](#explanation-5)EXPLANATION:

Note that any two consecutive elements in the “circular” array A can be right rotated such that one becomes A_1 and the other becomes A_N (circular here means A_N is adjacent to A_1 as well). Therefore, the solution is to simply find the max sum of two consecutive elements on the circular array A.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
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
    int n=readInt(2,100000,'\n');
    sumN+=n;
    assert(sumN<=100000);
    int A[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        if(i==n)
            A[i]=readInt(1,1000000000,'\n');
        else
            A[i]=readInt(1,1000000000,' ');
    }
    ll ans=0;
    for(int i=1;i<n;i++)
        ans=max(ans,(ll)A[i]+A[i+1]);
    ans=max(ans,(ll)A[1]+A[n]);
    cout<<ans<<'\n';
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
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
const int N=2e6+1;
ll a[N];
int main(){
	ios::sync_with_stdio(false);
	int t;cin >> t;
	while(t--){
		int n;cin >> n;
		ll ans=0;
		for(int i=1; i<=n ;i++){
			cin >> a[i];
			if(i>=2) ans=max(ans,a[i]+a[i-1]);
		}
		ans=max(ans,a[1]+a[n]);
		cout << ans << '\n';
	}
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(ans, a[i] + a[(i + 1) % n]);
        }
        cout << ans << '\n';
    }
}
``

</details>
