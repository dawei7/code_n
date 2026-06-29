# Matrix XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATXOR |
| Difficulty Rating | 1864 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [MATXOR](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/MATXOR) |

---

## Problem Statement

Chef has a *tasty ingredient* ― an integer $K$. He defines a *tasty matrix* $A$ with $N$ rows (numbered $1$ through $N$) and $M$ columns (numbered $1$ through $M$) as $A_{i, j} = K + i + j$ for each valid $i,j$.

Currently, Chef is busy in the kitchen making this tasty matrix. Help him find the bitwise XOR of all elements of this matrix.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $N$, $M$ and $K$.

### Output
For each test case, print a single line containing one integer ― the bitwise XOR of all elements of the tasty matrix with the given dimensions made with the given special ingredient.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N, M \leq 2 \cdot 10^6$
- $1 \leq K \leq 10^9$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^6$
- the sum of $M$ over all test cases does not exceed $2 \cdot 10^6$

---

## Examples

**Example 1**

**Input**

```text
2
2 2 5
2 3 7
```

**Output**

```text
14
5
```

**Explanation**

**Example case 1:** The matrix is
$$A = \begin{pmatrix}
5 + 1 + 1 & 5 + 1 + 2\\
5 + 2 + 1 & 5 + 2 + 2\end{pmatrix}
= \begin{pmatrix}
7 & 8 \\
8 & 9
\end{pmatrix} \,.$$

The XOR of all its elements is $7 \oplus 8 \oplus 8 \oplus 9 = 14$.

**Example case 2:** The matrix is
$$A = \begin{pmatrix}
7 + 1 + 1 & 7 + 1 + 2 & 7 + 1 + 3\\
7 + 2 + 1 & 7 + 2 + 2 & 7 + 2 + 3
\end{pmatrix}
= \begin{pmatrix}
9 & 10 & 11\\
10 & 11 & 12
\end{pmatrix} \,.$$

The XOR of all its elements is $9 \oplus 10 \oplus 11 \oplus 10 \oplus 11 \oplus 12 = 5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2 5
```

**Output for this case**

```text
14
```



#### Test case 2

**Input for this case**

```text
2 3 7
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MATXOR)

[Contest: Division 1](https://www.codechef.com/COOK127A/problems/MATXOR)

[Contest: Division 2](https://www.codechef.com/COOK127B/problems/MATXOR)

[Contest: Division 3](https://www.codechef.com/COOK127C/problems/MATXOR)

**Author:**  [Prashant Shishodia](https://www.codechef.com/users/pshishod2645)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Simple

# PREREQUISITES:

XOR-properties, Difference Array

# PROBLEM

You are given a matrix A of dimensions  N \times M which is defined as A_{i, j} = K + i + j. Your task is to find the bitwise xor of all elements of the matrix of given dimensions.

# QUICK EXPLANATION

Each unique number in the matrix will contribute either itself or a 0 to the resultant XOR. Find the number of appearances (say Y) for each unique number populating the matrix. If Y for the unique number X present in the matrix is even, it will contribute (X?X) XOR’d with itself Y/2 times, resulting in a 0. Whereas if Y is odd,  the number itself will be contributed because (X?X) will be XOR’d with itself (Y-1)/2 times, which in turn will be XOR’d with the remaining X, thus contributing 0?X.

# EXPLANATION

We have a matrix A of dimensions N \times M where each element of the matrix is defined as   A_{i, j} = K + i + j. We need to find the bitwise XOR of all elements of the matrix.

Let’s forget K for a moment.

The first observation that we can make is that the number of distinct values present in the matrix will lie in a range [2, N+M] such that every number of this range is present in the matrix.

Proof

Suppose we have an integer S that is the sum of two integers i and j, where i and j lie in a given range. Then, we can always obtain integers S-1 and S+1 incrementing and decrementing either i or j respectively.

Since i and j in context of the given question (row and column indices respectively), lie in a the continuous range of 1 to N, hence for every i\gt 1, i\lt n, j\gt 1 and j\lt m, (i-1, i+1, j-1, j+1) will also lie in the given range, implying that S+1 and S-1 are obtainable. If we are unable to increment i and j, then the sum corresponding to these row and column designations would be the maximum possible for the given range of i and j thus making S+1 unobtainable. Whereas if we are unable to decrement i and j, we would obtain minimum possible S and would not be able to obtain S-1.

This means the S values populating the matrix will lie between 1+1 (corresponding to i=1, j=1 which can’t be decremented further) and N+M (corresponding to i=N, j=M which can’t be incremented further).

Now we are left with finding the number of cells in the matrix such that i+j=X, for all X in the range [2, N+M].

For every row i, our j will vary from 1 to M. The minimum and maximum value present in row i will be i+1 and i+M respectively. Also all the values of range [i+1, i+M] will be present in row i as proved above.

As each row represents a contiguous range [i+1, i+M], we would use the difference array (representing the values in the matrix 2 to M+N) to increment the count of all numbers in a range. We would traverse each row and increment the numbers in the range it represents by 1.

On dissolving the difference array we obtain the number of times (say C) each of the numbers from 2 to N+M are present in the matrix. Now a number from the matrix will contribute to the resultant XOR only if it is present odd number of times i.e. only numbers with odd corresponding C values will contribute to the final XOR. Since if we xor a number with itself even number of times, then the resultant is 0. As

X \oplus X = 0

Now for each element X of the range [2, N+M], if it is present an odd number of times, then we include (X+K) in the resultant XOR. Finally, we output the resultant XOR.

# TIME COMPLEXITY:

O(N+M) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    int t; cin>>t;
    while(t--){
        int n, m, k; cin>>n>>m>>k;

        int ans = 0;
        for(int x = 2; x <= n + m; ++x){
            // i + j = x, 1 <= i <= n, 1 <= x - i <= m
            //  max(1, x - m) <= i <= min(n, x - 1)
            int l = max(1, x - m), r = min(n, x - 1);
            if(r >= l && (r - l + 1) % 2 == 1)ans ^= (k + x);
        }
        cout<<ans<<"\n";
    }
    return 0;
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
typedef long double f80;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
//#define double long double
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const int infi=0x3f3f3f3f;
const ll infl=0x3f3f3f3f3f3f3f3fLL;
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

int sum_n=0,sum_m=0;
void solve() {
	int n=readIntSp(1,1000000),m=readIntSp(1,1000000),k=readIntLn(1,1000'000'000);
	sum_n+=n;
	sum_m+=m;
	assert(sum_n<=1000000&&sum_m<=1000000);
	int ans=0;
	fr(i,2,n+m)
		if(min({i-1,n,m,n+m-i+1})&1)
			ans^=(k+i);
	cout<<ans<<endl;
}
signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
	int t=readIntLn(1,100000);
//	int t;
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
  int n,m,k;
  cin>>n>>m>>k;

  int diff_arr[n+m+5]={};

  for(int i=1;i<=n;i++)
  {
    int l=i+1;
    int r=i+m;

    diff_arr[l]++;
    diff_arr[r+1]--;
  }

  int ans=0;

  for(int i=2;i<=n+m;i++)
  {
    diff_arr[i]+=diff_arr[i-1];

    if(diff_arr[i]%2)
    {
      ans^=(k+i);
    }
  }

  cout<<ans<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
  {
    solve();
  }

return 0;
}

``

</details>
