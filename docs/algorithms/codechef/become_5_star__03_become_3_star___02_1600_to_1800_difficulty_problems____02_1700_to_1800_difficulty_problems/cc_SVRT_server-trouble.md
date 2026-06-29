# Server Trouble

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SVRT |
| Difficulty Rating | 1791 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SVRT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SVRT) |

---

## Problem Statement

You are the Chief Engineer of a fast growing start-up. You wish to place $K$ servers in some distinct locations from among $N$ locations. The locations, numbered $1, 2, \ldots, N$ are arranged in a circular manner. The distance between every adjacent location is 1 unit. $1$ and $N$ are adjacent.

You want to place the servers such that the maximum shortest distance between any two adjacent servers is as less as possible. Find this minimum possible distance that can be achieved, and also the minimum number of pairs of adjacent servers separated by this distance.

### Input:

- The first line contains a single integer, $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space-separated integers $N$ and $K$, denoting the number of locations, and the number of servers, respectively.

### Output:

For test case, output two space-separated integers $D$ and $X$, denoting the minimum possible maximum shortest distance that can be achieved between any two adjacent servers, and the minimum number of pairs of servers separated by this distance, respectively, in a separate line.

### Constraints
- $1 \le T \le 10^5$
- $3 \le K \le N \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
6 3
10 6
10 4
```

**Output**

```text
2 3
2 4
3 2
```

**Explanation**

- **Sample Test $1$:** Let the locations be numbered from $1$ to $6$. We can place the servers at locations $1$, $3$ and $5$. Thus, the distances between locations $1$ and $3$, $3$ and $5$, and $5$ and $1$ are all $=2$, which is the lowest possible maximum distance that can be achieved here. There are $3$ pairs of locations separated by this distance.

- **Sample Test $2$:** Let the locations be numbered from $1$ to $10$. We can place the servers at locations $1,2,4,6,8$ and $10$. Thus, the minimum possible maximum distance between any two adjacent servers is $2$. There shall be at least $4$ pairs of servers separated by this distance. Here, they are $(2,4)$, $(4,6)$, $(6,8)$ and $(8,10)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 3
```

**Output for this case**

```text
2 3
```



#### Test case 2

**Input for this case**

```text
10 6
```

**Output for this case**

```text
2 4
```



#### Test case 3

**Input for this case**

```text
10 4
```

**Output for this case**

```text
3 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SVRT)

[Contest: Division 1](https://www.codechef.com/START2A/problems/SVRT)

[Contest: Division 2](https://www.codechef.com/START2B/problems/SVRT)

[Contest: Division 3](https://www.codechef.com/START2C/problems/SVRT)

**Author:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Easy

# PREREQUISITES:

Observation, Maths

# PROBLEM:

You wish to place K servers across N locations. The locations are arranged in a circular manner. You want to place the servers such that the maximum clockwise distance between any two adjacent servers is as less as possible. Find this minimum possible distance that can be achieved, and also the minimum number of pairs of servers separated by this distance.

# EXPLANATION:

Let’s visualize this problem as we have a circle of length N and we made K cuts on this circle. Then we divide the circle from where the cuts had been made. Hence we will get K pieces of the circle. We need to minimize the maximum length possible of any piece.

The optimal way to divide the circle into K pieces is to divide it into the pieces of length N/K. But after dividing it into K pieces there might be some residual that is still left. Hence we will have two cases:

**CASE 1** : When (N mod K=0)

- In this case when N is completely divisible by K, then there will be no residual left after dividing the circle into K pieces of length N/K. In this case the maximum length that is possible is N/K and the number of pieces of this length are K.

**CASE 2**: When (N mod K \neq 0)

-

In this case, when N is not completely divisible by K then after dividing the circle into K pieces of length N/K, there will be a residual left of length (N mod K).

-

Since K is always greater than (N mod K). Hence from the residual, we will give unit length to (N mod K) pieces such that the length of  (N mod K) pieces will increase by a unit length.

-

Hence, In this case the maximum length that is possible is (N/K+1) and the number of pieces of this length are (N mod K).

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS

Setter
``//created by Whiplash99
import java.io.*;
import java.util.*;
class A
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int i,N;

        int T=Integer.parseInt(br.readLine().trim());
        StringBuilder sb=new StringBuilder();

        while (T-->0)
        {
            String[] s=br.readLine().trim().split(" ");
            N=Integer.parseInt(s[0]);
            int K=Integer.parseInt(s[1]);

            int D=(N+K-1)/K;
            int X=(N%K==0)?K:(N-K*(N/K));

            sb.append(D).append(" ").append(X).append("\n");
        }
        System.out.println(sb);
    }
}
``

Tester
``#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
#ifndef rd
#define trace(...)
#define endl '\n'
#endif
#define pb push_back
#define fi first
#define se second
#define int long long
typedef long long ll;
typedef double f80;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll,ll> pll;
#define double long double
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const int infi=0x3f3f3f3f;
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int mod=998244353;
//const int mod=1000000007;
typedef vector<int> vi;
typedef vector<ll> vl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> oset;
auto clk=clock();
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim) {
	uniform_int_distribution<int> uid(0,lim-1);
	return uid(rang);
}
int powm(int a, int b) {
	int res=1;
	while(b>0) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
}

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

void solve() {
	int n=readIntSp(3,1000'000'000),k=readIntLn(3,n);
	int lol=(n-1)/k+1;
	cout<<lol<<" "<<(n-1)%k+1<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(1);
	int t=readIntLn(1,100000);
//	cin>>t;
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int n,k;
  cin>>n>>k;

  int d=n/k;
  int x=k;

  if(n%k!=0)
  {
    d++;
    x=n%k;
  }

  cout<<d<<" "<<x<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
