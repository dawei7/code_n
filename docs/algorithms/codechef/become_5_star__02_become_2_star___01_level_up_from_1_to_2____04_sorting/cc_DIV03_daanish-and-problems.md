# Daanish and Problems

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIV03 |
| Difficulty Rating | 1388 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [DIV03](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/DIV03) |

---

## Problem Statement

Daanish as always is busy creating and solving his favourite and interesting graph problems. Chef assigns each problem a difficulty — an integer between $1$ and $10$. For each valid $i$, there are $A_i$ problems with difficulty $i$.

A participant hacked Daanish's account and got access to the problem proposal document. He can delete up to $K$ problems from the document in order to reduce the difficulty of the contest for himself and his friends. Find the smallest possible value of the difficulty of the most difficult problem which remains after removing $K$ problems.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains $10$ space-separated integers $A_1, A_2, \ldots, A_{10}$.
- The second line contains a single integer $K$.

### Output
For each test case, print a single line containing one integer — the minimum difficulty of the most difficult remaining problem.

### Constraints
- $1 \leq T \leq 2 \cdot 10^4$
- $0 \leq A_i \leq 10^8$ for each valid $i$
- $A_1 + A_2 + \ldots + A_{10} \gt 0$
- $0 \leq K \lt A_1 + A_2 + \ldots + A_{10}$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
5
1 10 1 5 3 2 4 9 0 100
100
2 0 1 0 0 0 0 0 0 10
12
2 0 1 0 0 0 0 10 0 0
0
2 0 1 0 0 0 0 0 0 10
10
1 10 1 5 3 2 4 9 0 100
125
```

**Output**

```text
8
1
8
3
2
```

**Explanation**

**Example case 1:** The participant can remove all $100$ problems with difficulty $10$. Then, there are no problems with difficulties $9$ and $10$, so the maximum difficulty among remaining problems is $8$.

**Example case 2:** The participant can remove all problems with difficulties $3$ and $10$ and any one of the problems with difficulty $1$. Then, the only problem left has difficulty $1$.

**Example case 3:** The participant cannot remove any problem. The document does not contain any problems with difficulties $9$ or $10$, so the maximum difficulty of a problem is $8$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10 1 5 3 2 4 9 0 100
100
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
2 0 1 0 0 0 0 0 0 10
12
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2 0 1 0 0 0 0 10 0 0
0
```

**Output for this case**

```text
8
```



#### Test case 4

**Input for this case**

```text
2 0 1 0 0 0 0 0 0 10
10
```

**Output for this case**

```text
3
```



#### Test case 5

**Input for this case**

```text
1 10 1 5 3 2 4 9 0 100
125
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIV03)

[Contest: Division 3](https://www.codechef.com/LTIME93C/problems/DIV03A)

**Author:**  [Smit Mandavia](https://www.codechef.com/users/l_returns)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Greedy

# PROBLEM:

You are given A_i problems with difficulty i, for each valid i. Each problem is assigned a difficulty in the range of 1 to 10. You need to find the minimum difficulty possible of the most difficult problem after removing any of the K problems.

# EXPLANATION:

Our goal is to minimize the difficulty of the most difficult problem by deleting at most K problems. To do so, we would choose a greedy approach and will delete the most difficult problems first. More formally, we will delete the i^{th} difficulty level problems only and only when there are no problems greater than i^{th} difficulty level present.

Finally, after deleting K problems greedily, we will find the most difficult problem present and output its difficulty level.

# TIME COMPLEXITY:

O(N) per testcase, where N=10.

# SOLUTIONS:

Setter
``#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define mod 1000000007

int main(){
    FIO;
    int t,k,i;
    cin >> t;
    while(t--){
        int a[10];
 	int sum=0;
        for(i=0;i<10;i++){
            cin >> a[i];
            sum+=a[i];
        }
        cin >> k;
        // suffix sum of the array
        for(i=8;i>=0;i--)
            a[i]+=a[i+1];

        // now a[i] denotes number of problems with difficulty i or more
        // Hence answer will the index at which a[i]>k

        for(i=9;a[i]<=k;i--);

        cout << i+1 << "\n";
    }
    return 0;
}

``

Tester
``#include <bits/stdc++.h>
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
typedef long double f80;
#define double long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int infi=0x3f3f3f3f;
//const int mod=998244353;
const int mod=1000000007;
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
	while(b) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
}

long long readInt(long long l, long long r, char endd) {
	long long x=0;
	int cnt=0;
	int fi=-1;
	bool is_neg=false;
	while(true) {
		char g=getchar();
		if(g=='-') {
			assert(fi==-1);
			is_neg=true;
			continue;
		}
		if('0'<=g&&g<='9') {
			x*=10;
			x+=g-'0';
			if(cnt==0) {
				fi=g-'0';
			}
			cnt++;
			assert(fi!=0 || cnt==1);
			assert(fi!=0 || is_neg==false);

			assert(!(cnt>19 || ( cnt==19 && fi>1) ));
		} else if(g==endd) {
			if(is_neg) {
				x=-x;
			}
			assert(l<=x&&x<=r);
			return x;
		} else {
			assert(false);
		}
	}
}
string readString(int l, int r, char endd) {
	string ret="";
	int cnt=0;
	while(true) {
		char g=getchar();
		assert(g!=-1);
		if(g==endd) {
			break;
		}
		cnt++;
		ret+=g;
	}
	assert(l<=cnt&&cnt<=r);
	return ret;
}
long long readIntSp(long long l, long long r) {
	return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
	return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
	return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
	return readString(l,r,' ');
}

int a[11];
void solve() {
	fr(i,1,10)
		if(i!=10)
			a[i]=readIntSp(0,100'000'000);
		else
			a[i]=readIntLn(0,100'000'000);
	int k=readIntLn(0,accumulate(a+1,a+11,0LL)-1);
	for(int i=10; i>0; i--) {
		k-=a[i];
		if(k<0) {
			cout<<i<<endl;
			return;
		}
	}
	assert(0);
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
	int t=readIntLn(1,20000);
//	int t;
//	cin>>t;
	fr(i,1,t)
		solve();
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
  {
    int arr[11];

    for(int i=1;i<=10;i++)
    {
      cin>>arr[i];
    }

    int k;
    cin>>k;

    for(int i=10;i>0;i--)
    {
      int temp=min(arr[i],k);
      arr[i]-=temp;
      k-=temp;
    }

    for(int i=10;i>0;i--)
    {
      if(arr[i]!=0)
      {
        cout<<i<<"\n";
        break;
      }
    }
  }

return 0;
}
``

# VIDEO EDITORIAL:

</details>
