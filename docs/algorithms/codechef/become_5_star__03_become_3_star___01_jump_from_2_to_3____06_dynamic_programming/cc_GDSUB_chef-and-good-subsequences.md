# Chef and Good Subsequences

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GDSUB |
| Difficulty Rating | 1999 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [GDSUB](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/GDSUB) |

---

## Problem Statement

Chef is given a sequence of prime numbers $A_1, A_2, \ldots, A_N$. This sequence has exactly $2^N$ subsequences. A subsequence of $A$ is *good* if it does not contain any two identical numbers; in particular, the empty sequence is good.

Chef has to find the number of good subsequences which contain at most $K$ numbers. Since he does not know much about subsequences, help him find the answer. This number could be very large, so compute it modulo $1,000,000,007$.

### Input
- The first line of the input contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
Print a single line containing one integer ― the number of good subsequences with size at most $K$, modulo $1,000,000,007$.

### Constraints
- $1 \le K \le N \le 10^5$
- $2 \le A_i \le 8,000$ for each valid $i$

### Subtasks
**Subtask #1 (40 points):** $A_1, A_2, \ldots, A_N$ are pairwise distinct

**Subtask #2 (60 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
5 3
2 2 3 3 5
```

**Output**

```text
18
```

**Explanation**

There is $1$ good subsequence with length $0$, $5$ good subsequences with length $1$, $8$ good subsequences with length $2$ and $4$ good subsequences with length $3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS :

Contest : [Division 1](https://www.codechef.com/SEPT19A/problems/GDSUB)

Contest : [Division 2](https://www.codechef.com/SEPT19B/problems/GDSUB)

Practice

**Setter :** [Naman Bansal](https://www.codechef.com/users/namanbansal013)

**Tester :** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist :** [Anand Jaisingh](https://www.codechef.com/users/anand20)

# DIFFICULTY :

Easy

# PREREQUISITES  :

Basic Dynamic Programming

# PROBLEM :

You are given a sequence of integers of length N, consisting of  \approx 1000  distinct values. Now, you need to find the number of subsequence of length K of this sequence, such that each pair of elements in the selected subsequence is pair-wise distinct.

# QUICK EXPLANATION :

A quick look at the constraints, and we can prove that the given array A[] can consist of at max  1007  distinct values. So, K  shall always be  \le1007 . Then, we can group numbers with equal values together. Then, the task comes down to finding the number of ways to select K numbers, such that we pick at most 1 number from each group. To accomplish this, we can do some dynamic programming, which runs in approx O(X^2) time, where  X \approx 1000

# EXPLANATION :

Let’s begin by having a look at the constraints. It states that each  A_i \le 8000 , and that the numbers A_i  are prime. Now, we know that prime numbers occur less frequently  than their composite counter parts.

In fact, the number of prime numbers  \le 8000  is exactly 1007 . So, we know that the array given in the input shall also consist of at max 1007 distinct values of A_i. We initially needed to find the number of subsequences consisting of at most K distinct values, where K \le 100,000.

But since the maximum number of distinct values in any subsequence of this array is always  \le 1007, so we can take  K=min(K,1007). Now, we need to solve the original problem using these modified constraints.

Another observation we can make is that the ordering of elements in a subsequence is not important. For example, if we pick some valid subsequence  a_{k_1},a_{k_2}...a_{k_z} , \hspace{0.2cm} z  \le K  , a_i \ne a_j  if  k_i \ne k_j , and  k_1 < k_2 ... <  k_ z  , then in what  ever order we arrange the elements  a_{k_i} , it does not make a difference, they do not break the pairwise distinctness property.

So, the original problem now boils down to finding the number of subsets  \{ k_1,k_2...k_z \} \hspace{0.2cm} z \le K , of the set  \{1,2,...N \} , such that  a[k_i] \ne a[k_j]  if  k_i \ne k_j

We can do a dynamic programming for the following. Let the number of distinct values appearing in the array be ctr. Then we can replace every distinct value appearing in the array by an integer in the range [1,ctr] and our answer remains unchanged.

Also, for each distinct value, let’s maintain a variable cnt[i] that states the number of times i appears in the given array a. Then we can do the following dynamic programming, that is in a way extremely similar to how to construct pascal triangle for binomial coefficients but with a small change :

 dp[i][0]=1 \hspace{0.2cm} \forall \hspace{0.2cm} i \ge 0

 dp[i][j] = dp[i-1][j]+ dp[i-1][j-1] \cdot cnt[i]

The number we are looking for is \sum_{i=0}^{K} dp[ctr][i]

Here, dp[i][j]  indicates the number of valid subsets of size j we can pick considering only array values  \le i

For a fixed (i,j) , the term  dp[i-1][j]  considers the valid subsets using array values  < i  and the second one ensures we pick a single instance of i, and add it to valid subsets of size j-1  consisting of array values  < i  .

Since we have cnt[i] instances of element i in the array, so we can pick exactly one among them in cnt[i] ways.

**On a side note :**

Assume we want to solve this problem without the additional constraint of  A_i \le 8000  and A_i being prime. Then,  N  and K can be as large 10^5. The answer is then given by :

 [x^k] \prod_{i=1}^{ctr} (1+ cnt[i] \cdot x)

That is, the answer is given by the coefficient of [x^k] in the polynomial :

 (1+cnt[1] \cdot x) \cdot (1+ cnt[2] \cdot x) \cdot ......\cdot (1+cnt[ctr] \cdot x)

We can multiply all these smaller polynomials in O(N \cdot log^2 N )  time using high precision FFT Modulo 10^9+7

That’s it, Thank you !

Your comments are welcome !

# COMPLEXITY ANALYSIS :

**Time Complexity :**  O( X^2) , where  X \approx 1000

**Space Complexity** :  O( X^2) , where  X \approx 1000

# SOLUTION LINKS :

Setter
``#include<bits/stdc++.h>
using namespace std;

#define modulo 1000000007
long long dp[1008][1008];

int main()  {
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int n, k;
    cin >> n >> k;
    int x;
    map<int, int> m;
    for(int i = 0; i < n; i++)  {
        cin >> x;
        m[x]++;
    }
    vector<long long> v;
    for(auto i = m.begin(); i != m.end(); i++)  {
        v.push_back(i->second);
    }
    for(int i = 0; i < v.size(); i++)   {
        for(int j = 1; j <= v.size(); j++)  {
            dp[i][j] = 0;
        }
    }
    for(int i = 0; i < v.size(); i++)   {
        dp[i][0] = 1;
    }
    dp[0][1] = v[0];
    for(int i = 1; i < v.size(); i++)   {
        for(int j = 1; j <= v.size(); j++)  {
            dp[i][j] += dp[i - 1][j];
            dp[i][j] = dp[i][j] % modulo;
            dp[i][j] += (dp[i - 1][j - 1]) * v[i];
            dp[i][j] = dp[i][j] % modulo;
        }
    }
    long long ans[v.size() + 1];
    ans[0] = 1;
    for(int i = 1; i <= v.size(); i++)   {
        ans[i] = ans[i - 1] + dp[v.size() - 1][i];
        ans[i] = ans[i] % modulo;
    }
    /*for(int i = 0; i < v.size(); i++)   {
        for(int j = 0; j <= v.size(); j++)  {
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }
    for(int i = 0; i <= v.size(); i++)  {
        cout << ans[i] << " ";
    }
    cout << "\n";*/
    if(k <= v.size())   {
        cout << ans[k];
    }
    else    {
        cout << ans[v.size()];
    }
    return 0;
}
``

Tester
``#include <cstdio>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	const int MAXA = 8002;
	const int MOD = 1e9 + 7;
	int N, K, tmp, sum = 0;
	scanf("%d %d", &N, &K);
	vector<int> A(MAXA), dp(MAXA);
	dp[0] = 1;

	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &tmp);
		A[tmp]++;
	}

	for (int i = 1; i < MAXA; ++i)
	{
		for (int j = i; j > 0; --j)
		{
			dp[j] = (dp[j] + static_cast<int64_t>(dp[j - 1]) * A[i]) % MOD;
		}
	}

	for (int i = 0; i <= K && i < MAXA; ++i)
	{
		sum = (sum + dp[i]) % MOD;
	}
	printf("%d\n", sum);
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
bool pr[maxn];
int a[maxn],cnt[maxn];
int dp[1100][1100];

int add(int a,int b)
{
    int ret=a+b;

    if(ret>=mod)
    {
        ret-=mod;
    }

    return ret;
}

int mul(int a,int b)
{
    ll ret=a*1ll*b;

    if(ret>=mod)
    {
        ret%=mod;
    }

    return (int)ret;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);

   int n,k;cin>>n>>k;

   for(int i=0;i<n;i++)
   {
       cin>>a[i];

       cnt[a[i]]++;
   }

   vector< int > v;v.pb(-1);

   for(int i=0;i<8000;i++)
   {
       if(cnt[i]>0)
       {
           v.pb(cnt[i]);
       }
   }

   assert(v.size()<=1010);

   k=min(k,(int)v.size());

   dp[0][0]=1;

   for(int i=1;i<v.size();i++)
   {
       dp[i][0]=1;

       for(int j=1;j<=k;j++)
       {
           dp[i][j]=add(dp[i-1][j],mul(dp[i-1][j-1],v[i]));
       }
   }

   int ret=0;

   for(int i=0;i<=k;i++)
   {
       ret=add(ret,dp[v.size()-1][i]);
   }

   cout<<ret<<endl;

    return 0;
}
``

</details>
