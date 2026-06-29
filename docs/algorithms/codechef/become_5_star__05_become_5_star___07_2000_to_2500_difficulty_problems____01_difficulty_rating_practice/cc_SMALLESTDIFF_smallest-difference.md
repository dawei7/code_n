# Smallest Difference

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMALLESTDIFF |
| Difficulty Rating | 2421 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SMALLESTDIFF](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SMALLESTDIFF) |

---

## Problem Statement

Consider a grid $A$ with dimensions $N \times M$, such that all elements of the grid are **distinct**.

A remote controlled car is present at cell $(1,1)$. Chef and Chefina will alternatively move the car with Chef starting first.

- If it is Chef's turn, he will move the car to either right or down by $1$ cell. He moves the car to the cell having **larger** element.
- If it is Chefina's turn, she will move the car to either right or down by $1$ cell. She moves the car to the cell having **smaller** element.

The car stops once it reaches the cell $(N, M)$.

Let us denote the largest element visited by the car by $A_{max}$ and the smallest element as $A_{min}$. Then, the score of the grid is defined as $A_{max} - A_{min}$.

Charlie has an array $B$ containing $N \cdot M$ **distinct** elements. He wants to arrange the elements as a grid of size $N\times M$ such that the score of the grid is **minimised**.

Help Charlie to construct **any such** grid.

Note: **Please use fast I/O for input and pypy for python submissions.**

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — dimensions of the grid $A$.
    - The next line contains $N \cdot M$ distinct elements denoting the array $B$.

---

## Output Format

For each test case, output $N$ lines each containing $M$ spaced integers denoting the grid $A$.

If there are multiple possible answers, print **any** of them.

---

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N, M \leq 1000$
- $1 \leq B_i \leq 10^9$
- All elements of the array $B$ are distinct.
- Sum of $N \cdot M$ over all test cases do not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
2
2 2
5 10 20 40
3 2
2 6 4 1 9 20
```

**Output**

```text
10 5 
20 40 
2 4 
1 6 
20 9
```

**Explanation**

**Test case $1$:** The car starts from $(1, 1)$. Let us consider the moves based on the grid $[[10, 5], [20, 40]]$.
- In Chef's turn, he will move the car to $(2, 1)$ since $A_{(2, 1)} \gt A_{(1, 2)}$.
- In Chefina's turn, she will move the car to $(2, 2)$ as it is the only available choice.

Thus, the car covers the elements $[10, 20, 40]$. The largest element in the path is $40$ while the smallest element is $10$. Thus, the score is $40-10 = 30$. It can be shown that this is the minimum possible score that can be achieved in any configuration of grid.

**Test case $2$:** The car starts from $(1, 1)$. Let us consider the moves based on the grid $[[2, 4], [1, 6], [20, 9]]$.
- In Chef's turn, he will move the car to $(1, 2)$ since $A_{(1, 2)} \gt A_{(2, 1)}$.
- In Chefina's turn, she will move the car to $(2, 2)$ as it is the only available choice.
- In Chef's turn, he will move the car to $(3, 2)$ as it is the only available choice.

Thus, the car covers the elements $[2, 4, 6, 9]$. The largest element in the path is $9$ while the smallest element is $2$. Thus, the score is $9 - 2 = 7$. It can be shown that this is the minimum possible score that can be achieved in any configuration of grid.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SMALLESTDIFF)

[Contest: Division 1](https://www.codechef.com/START71A/problems/SMALLESTDIFF)

[Contest: Division 2](https://www.codechef.com/START71B/problems/SMALLESTDIFF)

[Contest: Division 3](https://www.codechef.com/START71C/problems/SMALLESTDIFF)

[Contest: Division 4](https://www.codechef.com/START71D/problems/SMALLESTDIFF)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2421

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

You are given N, M, and an array B of size N\times M of distinct integers

Consider an N\times M grid A whose values form a permutation of B. The following process is carried out:

- A token is placed at (1, 1) and moved towards (N, M) either right or down each step.

- On odd moves (1-st, 3-rd, etc) the token is moved towards its larger neighbor

- On even moves the token is moved towards its smaller neighbor

- The value of the grid taken equals the difference between the maximum and minimum element on the path.

Construct A such that this value is minimized.

#
[](#explanation-5)EXPLANATION:

First, let’s sort B so that B_1 \lt B_2 \lt \ldots \lt B_{NM}.

Without loss of generality, assume N \leq M.

Note that any path from (1, 1) to (N, M) where we move only right and down will visit exactly N+M-1 cells. Let L = N+M-1 be this length.

Now, ideally we’d like the values on our path to be L consecutive values in B, since this is how we minimize the difference between the largest and smallest of them. However, we also need to account for actually being to place these values to form a valid path, so we can’t just choose any subarray of length L.

The less constraints we have, the better.

So, let’s try to make our path go down first (recall that N \leq M), and then go right after it hits the last row. Once we hit the last row, there’s only one way to go so the maximum/minimum conditions don’t matter anymore and we can freely place anything there, so we only need to worry about the going down part.

Specifically, we need to ensure we choose values such that:

- A_{2, 1} \gt A_{1, 2}

- A_{3, 1} \lt A_{2, 2}

-
A_{4, 1} \gt A_{3, 2}

\vdots

Only by doing so can we ensure we move down for the first N steps.

Notice that the value of A_{1, 1} also doesn’t matter whatsoever.

In particular, we have x = \left\lfloor \frac{N}{2}\right\rfloor constraints of the form A_{i, 1} \gt A_{i-1, 2} and y = \left\lfloor \frac{N-1}{2}\right\rfloor of the form A_{i, 1} \lt A_{i-1, 2}.

Of course, the best way to fulfill these is to pair the largest x elements among our chosen ones with the smallest x *unchosen* elements; and the smallest y chosen elements with the largest y unchosen ones.

In order to fulfill these conditions, we also need to ensure that the smallest x unchosen elements are all smaller than our largest x elements; and the largest y unchosen elements are larger than our smallest y.

In particular, this means that if we pick the subarray [i, i+L-1] then it must satisfy i \gt x and i+L-1+y \leq N\times M.

The minimum difference is thus the minimum value of B_{i+L-1} - B_i across all subarrays that satisfy the above conditions on i, which is easy to find by just iterating across B.

Once you’ve found i, the starting point of the subarray, constructing A is not very hard:

- Place the x largest elements of the chosen subarray at positions A_{2, 1}, A_{4, 1}, A_{6, 1}, \ldots

- Place the elements B_1, B_2, \ldots, B_x at positions A_{1, 2}, A_{3, 2}, \ldots

- Place the y smallest elements of the chosen subarray at A_{3, 1}, A_{5, 1}, \ldots

- Place the elements B_{NM}, B_{NM-1}, \ldots at positions A_{2, 2}, A_{4, 2}, \ldots

- Place all the remaining elements of the subarray at A_{1, 1} and A_{N, 2}, A_{N, 3}, \ldots, A_{N, M} in any order

- Place all the unplaced elements in the grid in some order

After sorting B, the rest of the solution is \mathcal{O}(NM), giving us a solution in \mathcal{O}(NM\log{NM}).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(NM\log{NM}) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``//Utkarsh.25dec
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=1000023;
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
int sumNM=0;
int B[N];
set <int> s;
int n,m;
int A[1005][1005];
ll ans;
void fillGrid()
{
    int blockers=n-1;
    int mini=(blockers+1)/2;
    int maxi=blockers/2;
    int pathLen=n+m-1;
    int optL=0, optR=0;
    for(int i=mini+1;i<=n*m;i++)
    {
        int j=i+pathLen-1;
        int rem=n*m-j;
        if(rem<maxi)
            break;
        if(ans>B[j]-B[i])
        {
            ans=B[j]-B[i];
            optL=i;
            optR=j;
        }
    }
    int curr=optL;
    for(int i=1;i<=n;i++)
    {
        A[i][1]=B[curr++];
        s.erase(A[i][1]);
    }
    for(int j=2;j<=m;j++)
    {
        A[n][j]=B[curr++];
        s.erase(A[n][j]);
    }
    int lar=n*m;
    int sm=1;
    for(int i=1;i<n;i++)
    {
        if(i%2==1)
            A[i][2]=B[sm++];
        else
            A[i][2]=B[lar--];
        s.erase(A[i][2]);
    }
    for(int i=1;i<n;i++)
    {
        for(int j=3;j<=m;j++)
        {
            A[i][j]=(*s.begin());
            s.erase(s.begin());
        }
    }
}
void solve()
{
    s.clear();
    ans=1e18;

    n=readInt(2,1000,' ');
    m=readInt(2,1000,'\n');
    sumNM+=(n*m);
    assert(sumNM<=1000000);
    for(int i=1;i<=n*m;i++)
    {
        if(i==n*m)
            B[i]=readInt(1,1000000000,'\n');
        else
            B[i]=readInt(1,1000000000,' ');
        s.insert(B[i]);
    }
    assert(s.size()==n*m);
    sort(B, B+n*m+1);
    if(n<=m)
    {
        fillGrid();
    }
    else
    {
        swap(n,m);
        fillGrid();
        swap(n,m);
        int C[n+1][m+1];
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                C[i][j]=A[j][i];
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                A[i][j]=C[i][j];
    }
    // cout<<ans<<'\n';
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
            cout<<A[i][j]<<' ';
        cout<<'\n';
    }
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,10000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``// Jai Shree Ram

#include<bits/stdc++.h>
using namespace std;

#define rep(i,a,n)     for(int i=a;i<n;i++)
#define ll             long long
#define int            long long
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define endl           "\n"
#define x              first
#define y              second
#define gcd(a,b)       __gcd(a,b)
#define mem1(a)        memset(a,-1,sizeof(a))
#define mem0(a)        memset(a,0,sizeof(a))
#define sz(a)          (int)a.size()
#define pii            pair<int,int>
#define hell           1000000007
#define elasped_time   1.0 * clock() / CLOCKS_PER_SEC

template<typename T1,typename T2>istream& operator>>(istream& in,pair<T1,T2> &a){in>>a.x>>a.y;return in;}
template<typename T1,typename T2>ostream& operator<<(ostream& out,pair<T1,T2> a){out<<a.x<<" "<<a.y;return out;}
template<typename T,typename T1>T maxs(T &a,T1 b){if(b>a)a=b;return a;}
template<typename T,typename T1>T mins(T &a,T1 b){if(b<a)a=b;return a;}

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
int solve(){
        static int sum = 0;
		int n = readIntSp(2,1e3);
		int m = readIntLn(2,1e3);
		sum += n*m;
		assert(sum <= 1e6);
		vector<int> a = readVectorInt(n*m, 1, 1e9);
		//for(auto &i: a) cin >> i;
		sort(all(a));

		auto solve = [&](int n,int m){
			int rb = (n - 1)/2;
			int lb = (n)/2;
			int ans = LLONG_MAX;
			int l = 0,r = 0;
			for(int i = lb; i < n*m; i++){
				int tl = i;
				int tr = tl + (n + m - 1) - 1;
				if(n*m - tr - 1 < rb) break;
				if(a[tr] - a[tl] < ans){
					ans = a[tr] - a[tl];
					l = tl;
					r = tr;
				}
			}
			vector<int> vis(n*m);
			int temp = l - 1;

			vector<vector<int>> mat(n, vector<int> (m));
			for(int i = 0; i < n; i++){
				vis[l] = 1;
				mat[i][0] = a[l++];
			}
			for(int j = 1; j < m; j++){
				vis[l] = 1;
				mat[n - 1][j] = a[l++];
			}
			for(int i = 0; i + 1 < n; i++){
				if(i & 1){
					mat[i][1] = a[++r];
					vis[r] = 1;
				}else{
					vis[temp] = 1;
					mat[i][1] = a[temp--];
				}
			}
			int tmp = 0;
			for(int i = 0; i + 1 < n; i++){
				for(int j = 2; j < m; j++){
					while(tmp < n*m and vis[tmp]) tmp++;
					vis[tmp] = 1;
					mat[i][j] = a[tmp];
				}
			}
			return mat;

		};
		vector<vector<int>> ans(n, vector<int> (m));
		if(n <= m){
			ans = solve(n,m);
		}else{
			auto res = solve(m,n);
			for(int i = 0; i < n; i++){
				for(int j = 0; j < m; j++){
					ans[i][j] = res[j][i];
				}
			}
		}
		for(auto i: ans){
			for(auto j: i) cout << j << " ";
			cout << endl;
		}

 return 0;
}
signed main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    #ifdef SIEVE
    sieve();
    #endif
    #ifdef NCR
    init();
    #endif
    int t = readIntLn(1,1e4);//cin>>t;
    while(t--){
        solve();
    }
    return 0;
}
``

Editorialist's code (Python)
``import sys
input = sys.stdin.readline
for _ in range(int(input())):
	n, m = map(int, input().split())
	b = sorted(list(map(int, input().split())))
	st, mindif = -1, 10**10
	cells = n+m-1
	swap = False
	if n < m:
		swap = True
		n, m = m, n
	ans = [0]*(n*m)
	for i in range(n*m):
		less = m//2
		more = (m-1)//2
		if i < less: continue
		if i + cells + more > n*m: continue

		if b[i+cells-1] - b[i] < mindif:
			mindif = b[i+cells-1] - b[i]
			st = i
	used = [0]*(n*m)
	lo, hi = 0, n*m-1
	L, R = st, st+cells-1
	for i in range(m//2):
		ans[2*i+1] = b[R]
		ans[2*i+m] = b[lo]
		used[R] = 1
		used[lo] = 1
		lo += 1
		R -= 1
	for i in range((m-1)//2):
		ans[2*i+2] = b[L]
		ans[2*i+1+m] = b[hi]
		used[L] = 1
		used[hi] = 1
		L += 1
		hi -= 1
	onpath = [0] + [m-1 + i*m for i in range(1, n)]
	for i in range(R-L+1):
		ans[onpath[i]] = b[L+i]
		used[L+i] = 1

	ptr = 0
	for i in range(n*m):
		if ans[i] != 0: continue
		while used[ptr] == 1: ptr += 1
		ans[i] = b[ptr]
		ptr += 1
	if swap == False:
		for i in range(n): print(*ans[i*m:i*m+m])
	else:
		for i in range(m): print(*ans[i:n*m+i:m])
``

</details>
