# Chef and Interesting Subsequences 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFINSQ |
| Difficulty Rating | 1646 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CHEFINSQ](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CHEFINSQ) |

---

## Problem Statement

Chef has a sequence $A_1, A_2, \ldots, A_N$. This sequence has exactly $2^N$ subsequences. Chef considers a subsequence of $A$ *interesting* if its size is exactly $K$ and the sum of all its elements is minimum possible, i.e. there is no subsequence with size $K$ which has a smaller sum.

Help Chef find the number of interesting subsequences of the sequence $A$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the number of interesting subsequences.

### Constraints
- $1 \le T \le 10$
- $1 \le K \le N \le 50$
- $1 \le A_i \le 100$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 20$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
4 2
1 2 3 4
```

**Output**

```text
1
```

**Explanation**

**Example case 1:** There are six subsequences with length $2$: $(1, 2)$, $(1, 3)$, $(1, 4)$, $(2, 3)$, $(2, 4)$ and $(3, 4)$. The minimum sum is $3$ and the only subsequence with this sum is $(1, 2)$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS :

Contest : [Division 1](https://www.codechef.com/SEPT19A/problems/CHEFINSQ)

Contest : [Division 2](https://www.codechef.com/SEPT19B/problems/CHEFINSQ)

Practice

**Setter :** [Aman Gupta](https://www.codechef.com/users/theabd1234)

**Tester :** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist :** [Anand Jaisingh](https://www.codechef.com/users/anand20)

# DIFFICULTY :

Easy

# PREREQUISITES  :

Ad-Hoc logic, Binomial Coefficients.

# PROBLEM :

Given an array A of size N, you need to find the number of sub sequences of this array of length K, such that the sum of these sub sequences is the minimum possible sum of a sub sequence of length K

# QUICK EXPLANATION :

It can be proved that the minimum possible sum of a subsequence of length K from the given array A[] is the sum of the K smallest elements of array A[]. Let the maximum element among the K smallest elements of the array be Z , and let the number of times it occurs among the K smallest elements of the array be Y. Also, let cnt(i) indicate the number of times element i occurs in the given array. Then, we can additionally prove that the answer equals  \binom{cnt(Z)}{Y}

# EXPLANATION :

**Claim :**

The minimum possible sum of a subsequence of length K from the given array A of size N is the sum of the K  smallest elements of the array.

**Proof :**

Let’s call the minimum possible sum of a subsequence of length K as Sum and let initially let Sum be equal to the sum of the K smallest elements of the array. Now, let’s try and pick some  integer Y not included among the K smallest elements. Now, we try and replace some element X included among the K smallest elements.

In such a situation, Sum transforms to Sum+Y-X. But, since we know that Y \ge X , then Y-X \ge 0 . Hence, it’s never optimal to pick any element outside of the K smallest elements of the array, since in such a case, Sum can only possibly increase.

**Claim** :

Let the maximum element among the K smallest elements of the array be Z , and let the number of times it occurs among the K smallest elements of the array be Y. Also, let cnt(i) indicate the number of times element i occurs in the given array. Then the answer is \binom{cnt(Z)}{Y}

**Proof :**

First, let’s imagine we remove all elements  \ge Z  from the array. Then, the number of elements we will be left with will be M < K . It’s easy to see since we remove at least all elements with position  \ge K  (After sorting )

Now, we need to make M equal to K. In order to do that we need to keep on adding Z to the array. We obviously cannot add any element  > Z . But since Z occurs a total of cnt(i) times in the given array and  K-M=Y, so we can still make a subsequence with the same possible sum in \binom{cnt(Z)}{Y} different ways.

Now, the factorial way of computing binomial coefficients may be too much here, i.e. \binom{N}{R}=\frac{N!}{R! \cdot (N-R)!} N! can be too large to fit into any primitive data types. But remember, after division, \binom{N}{R} is good enough to fit into a long long integer. So instead, we can use the recurrence :

 C(i,j)=C(i-1,j-1)+C(i-1,j)

This is the way of computing Pascal’s Triangle, and you can read further about it [here](https://en.wikipedia.org/wiki/Pascal%27s_triangle).

That’ it, Thank you !

Your Comments are Welcome !

# COMPLEXITY ANALYSIS :

**Time Complexity :**  O( (MaxN)^2+ T \cdot N \lg N ) , where  MaxN \approx 50

**Space Complexity:** O((MaxN)^2)

# SOLUTION LINKS :

Setter
``#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
	long long x = 0;
	int cnt = 0;
	int fi = -1;
	bool is_neg = false;
	while (true) {
		char g = getchar();
		if (g == '-') {
			assert(fi == -1);
			is_neg = true;
			continue;
		}
		if ('0' <= g && g <= '9') {
			x *= 10;
			x += g - '0';
			if (cnt == 0) {
				fi = g - '0';
			}
			cnt++;
			assert(fi != 0 || cnt == 1);
			assert(fi != 0 || is_neg == false);

			assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
		}
		else if (g == endd) {
			assert(cnt > 0);
			if (is_neg) {
				x = -x;
			}
			assert(l <= x && x <= r);
			return x;
		}
		else {
			assert(false);
		}
	}
}

string readString(int l, int r, char endd) {
	string ret = "";
	int cnt = 0;
	while (true) {
		char g = getchar();
		assert(g != -1);
		if (g == endd) {
			break;
		}
		cnt++;
		ret += g;
	}
	assert(l <= cnt && cnt <= r);
	return ret;
}
long long readIntSp(long long l, long long r) {
	return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
	return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
	return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
	return readString(l, r, ' ');
}

int main(int argc, char** argv)
{
#ifdef HOME
	if (IsDebuggerPresent())
	{
		freopen("../in.txt", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T, K, N;

	vector< vector<int64_t> > binom(60, vector<int64_t>(64));
	binom[0][0] = 1;
	for (int i = 1; i < 60; ++i)
	{
		binom[i][0] = 1;
		for (int j = 1; j < 60; ++j)
		{
			binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
		}
	}
	T = readIntLn(1, 10);
	for (int tc = 0; tc < T; ++tc)
	{
		N = readIntSp(1, 50);
		K = readIntLn(1, N);
		vector<int> A(N);
		for (int i = 0; i < N; ++i)
		{
			if(i + 1 < N)
				A[i] = readIntSp(1, 100);
			else
				A[i] = readIntLn(1, 100);
		}
		//assert(getchar() == -1);
		sort(A.begin(), A.end());

		int Z = A[K - 1];
		int cnt = 0, lcnt = 0;
		for (int i = 0; i < N; ++i)
		{
			if (i < K && A[i] == Z)
				++lcnt;
			if (A[i] == Z)
				++cnt;
		}
		printf("%lld\n", binom[cnt][lcnt]);
	}
	assert(getchar() == -1);
	return 0;
}
``

Tester
``#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

int main(int argc, char** argv)
{
#ifdef HOME
	if (IsDebuggerPresent())
	{
		freopen("../in.txt", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T, K, N;

	vector< vector<int64_t> > binom(60, vector<int64_t>(64));
	binom[0][0] = 1;
	for (int i = 1; i < 60; ++i)
	{
		binom[i][0] = 1;
		for (int j = 1; j < 60; ++j)
		{
			binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
		}
	}

	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc)
	{
		scanf("%d %d", &N, &K);
		vector<int> A(N);
		for(int i = 0; i < N; ++i)
			scanf("%d", &A[i]);
		sort(A.begin(), A.end());

		int Z = A[K - 1];
		int cnt = 0, lcnt = 0;
		for (int i = 0; i < N; ++i)
		{
			if (i < K && A[i] == Z)
				++lcnt;
			if (A[i] == Z)
				++cnt;
		}
		printf("%lld\n", binom[cnt][lcnt]);
	}
	return 0;
}
``

Editorialist
``//#pragma GCC optimize("Ofast,no-stack-protector")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")
//#pragma GCC target("avx,tune=native")
// Anand Jaisingh

#include<bits/stdc++.h>

using namespace std;

typedef complex<double> base;
typedef long double ld;
typedef long long ll;

#define pb push_back
#define pii pair<int,int>
#define pll pair< ll , ll >
#define vi vector<int>
#define vvi vector< vi >
const int maxn=(int)(2e5+5);
const ll mod=(ll)(1e9+7);
int a[maxn];
ll dp[55][55];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);

    int t;cin>>t;

    dp[0][0]=1;

    for(int i=1;i<51;i++)
    {
        dp[i][0]=1;

        for(int j=1;j<51;j++)
        {
            dp[i][j]=dp[i-1][j]+dp[i-1][j-1];
        }
    }

    while(t>0)
    {
        int n,k;

        cin>>n>>k;map<int,int> m1;

        for(int i=0;i<n;i++)
        {
            cin>>a[i];

            m1[a[i]]++;
        }

        sort(a,a+n);

        int ptr=k-1,val=0;

        while(ptr>=0 && a[ptr]==a[k-1])
        {
            ptr--;val++;
        }

        ll res=dp[m1[a[k-1]]][val];

        cout<<res<<endl;

        t--;
    }

    return 0;
}
``

</details>
