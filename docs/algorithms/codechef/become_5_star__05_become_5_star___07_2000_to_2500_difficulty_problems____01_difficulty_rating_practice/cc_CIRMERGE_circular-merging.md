# Circular Merging

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CIRMERGE |
| Difficulty Rating | 2208 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CIRMERGE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CIRMERGE) |

---

## Problem Statement

$N$ integers $A_1, A_2, \ldots, A_N$ are placed in a circle in such a way that for each valid $i$, $A_i$ and $A_{i+1}$ are adjacent, and $A_1$ and $A_N$ are also adjacent.

We want to repeat the following operation exactly $N-1$ times (until only one number remains):
- Select two adjacent numbers. Let's denote them by $a$ and $b$.
- Score $a+b$ penalty points.
- Erase both $a$ and $b$ from the circle and insert $a+b$ in the space between them.

What is the minimum number of penalty points we can score?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing one integer — the minimum number of penalty points.

### Constraints
- $1 \le T \le 10$
- $2 \le N \le 400$
- $1 \le a_i \le 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (10 points):**
- $2 \le N \le 10$
- $a_i \le 10$ for each valid $i$

**Subtask #2 (10 points):**
- $2 \le N \le 25$
- $a_1, a_2, \ldots, a_N$ are distinct powers of $2$ (including $1$)

**Subtask #3 (10 points):** $2 \le N \le 100$

**Subtask #4 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3
10 10 1
```

**Output**

```text
32
```

**Explanation**

- $[10,10,1] \rightarrow [10, 11]$, penalty:  $11$
- $[10,11] \rightarrow [21]$, penalty:  $21$
- Total penalty: $11+21=32$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS :

Contest : [Division 1](https://www.codechef.com/JULY19A/problems/CIRMERGE)

Contest : [Division 2](https://www.codechef.com/JULY19B/problems/CIRMERGE)

[Practice](https://www.codechef.com/problems/CIRMERGE)

**Setter :** [Erfan Alimohammadi](https://www.codechef.com/users/erfaniaa)

**Tester :** [Alipasha Montaseri](https://www.codechef.com/users/alipasha132) / [Kasra Mazaheri](https://www.codechef.com/users/kmaaszraa)

**Editorialist :** [Anand Jaisingh](https://www.codechef.com/users/anand20)

# DIFFICULTY :

Easy-Medium

# PREREQUISITES  :

Dynamic Programming

# PROBLEM :

Given a circular array A of size N, in a single move, we can merge two adjacent elements a,b into a single element a+b, and we need to add a+b to our score. After N-1 operations, what is the minimum possible score we can achieve ?

# QUICK EXPLANATION :

Assume we perform the given operation over any array A. Then, after performing any sequence of moves after which A has only 2 elements, it can be proved that the original elements of the array get partitioned into 2 sub arrays. ( When we merge 2 elements, we consider they are in the same partition, and each sub array corresponds to an element among the 2 remaining elements in A ).

So, we build a dynamic programming solution, where we cut the given array into 2 sub arrays in every possible way, and then solve individually for those 2 sub arrays ( recursively, considering them to be the originally given arrays), after which we can know the best possible way to divide the original array into 2 parts, that can be merged into a single element using the lowest cost.

# EXPLANATION :

First, let’s try and device a simulation based strategy that works for smaller sized arrays and brute forces each possible way in the most naive manner.

We can do this as follows : For each pair of adjacent elements, we try and merge them and go to the next step with a new array. We keep doing this, until we have only 1 element left.

For example, you could look at some pseudo-code for such a function in the tab below

Pseudo Code
``  int solve(int[] a)
  {
      n=a.length;

      if(size(a)==1)
      {
            return 0;
      }

      ret=Infinity;

      for(int i=0;i<n;i++)
      {
            int[] b=merge(a,i,(i-1+n)%n);

            ret=min(ret,a[i]+a[(i-1+n)%n]+solve(b));
      }

      return ret;
  }
``

However, it turns out that the complexity of such solutions is of the order of O(N!) and is only good enough to solve the 1^{st} sub task.

**Subtask 2:**

Since here all the A[i]'s are distinct powers of 2, we can use a greedy approach to solve this sub task. The approach is : In each move, select from the array 2 adjacent elements with the lowest sum, and merge them. Continue until exactly 1 element remains.

**Full Score**

One thing we can notice is that there may be many many possible ways to reach the same array b from the beginning ( using the brute force used for the 1^{st} subtask ), and we don’t need to calculate the answer for the  same array again and again.

For example , consider the initial array to be : [1,2,3,4,5]. We can get to the array [1,9,5]   by first merging the 2^{nd} and 3^{rd} elements and the the new 2^{nd} and 3^{rd} elements. But, we can get to the same array similarly, by first merging the 3^{rd} and 4^{th} elements and then the 2^{nd} and 3^{rd} elements.

So, if we know the possible states the array can go to, and calculate them only once, we are doing much better. Now, let’s try and see the states a single 3 sized array can go to :

[ \{1 \},\{ 2 \}, \{ 3 \} ]  -> [ \{1,2 \},\{ 3 \}] ->[ \{1,2,3 \}]

[ \{ 1 \},\{ 2 \},\{ 3 \} ]  -> [ 1 \},{2}, \{3 ] ->[ \{1,2,3 \}]

[ \{1 \},\{2 \},\{3 \}]  -> [ \{1 \},\{ 2,3 \}]->[ \{1,2,3 \} ]

For a given array  [a_0,a_1,a_2,....a_{n-1}] , assume we performed a sequence of operations after which only 2 elements are remaining. It can now easily be proved that the original elements of the array get merged and partitioned into 2 sub arrays of the original array. ( Don’t forget sub arrays can also be circular )

We can prove this easily : assume 2 indexes i and j are already on the same side of the partition. For this to happen, all elements between them ( moving from the left / right ) will also have to be on the same side of the partition.

This fact helps us a lot. Now, instead of trying to merge elements from top to bottom and create new arrays, we can instead go from bottom to top, computing the answer for smaller sized sub arrays, that will in the future help us compute answer for larger arrays.

We use 0 based indexing for the input array, and for the DP. Now, let’s store in dp[l][r] the minimum possible answer, if we assume the sub array l..r to be the input array. Then, we can calculate dp[l][r] as follows :

 dp[i][(i+1) \% n] = a[i] + a[(i+1) \% n]

 dp[i][j] = min_{k=l}^{k!=r} dp[i][k]+dp[k+1][r] + sum(l,r)

This uses the fact the the possible ways in which the elements of the sub array [l...r] can be merged into 2 elements always partitions the given sub array into two further sub arrays. Note that using this approach, we expect to have already calculated dp[l][k] and dp[k+1][r] that are smaller sized sub arrays.

The final number we’re looking for is the minimum among  dp[(i+1) \% n][i] , \hspace{0.2cm} i=0,1,2...n-1

And, now let’s try and calculate the complexity of such a solution :

We have N sub arrays of each size from 1 to N. To calculate the answer for a sub array of size Z, it takes O(Z) time. So, it’s :

N \cdot (1+2+3+....+N ) = \frac{N \cdot (N+1)}{2} \cdot N \approx O(N^3) .

This approach is good enough to pass all tests.

Your comments are welcome !

# COMPLEXITY ANALYSIS :

**Time complexity :** O(T \cdot N^3 )

**Space Complexity :** O(N^2)

# SOLUTION LINKS :

Setter
``    #include <bits/stdc++.h>

    using namespace std;

    const long long INF = 1e18;
    const int MAXN = 510;

    int n, t;
    long long dp[MAXN][MAXN], a[MAXN], sum[MAXN][MAXN], ans;

    inline int mod(int x) {
    	if (x < n)
    		return x;
    	if (x >= n)
    		return x - n;
    }

    long long solve(int l, int r) {
    	if (dp[l][r] != -1)
    		return dp[l][r];
    	if (l == r)
    		return dp[l][r] = 0;
    	if (mod(l + 1) == r)
    		return dp[l][r] = a[l] + a[r];
    	long long ret = INF;
    	for (int i = l; i != r; i = mod(i + 1))
    		ret = min(ret, solve(l, i) + solve(mod(i + 1), r) + sum[l][r]);
    	return dp[l][r] = ret;
    }

    int main() {
    	ios::sync_with_stdio(0);
    	cin >> t;
    	while (t--) {
    		cin >> n;
    		memset(dp, -1, sizeof dp);
    		// memset(sum, 0, sizeof sum);
    		for (int i = 0; i < n; i++)
    			cin >> a[i];
    		ans = INF;
    		for (int i = 0; i < n; i++) {
    			sum[i][i] = a[i];
    			for (int j = mod(i + 1); j != i; j = mod(j + 1)) {
    				sum[i][j] = sum[i][mod(j + n - 1)] + a[j];
    			}
    		}
    		for (int i = 0; i < n; i++) {
    			ans = min(ans, solve(i, mod(i + n - 1)));
    		}
    		cout << ans << endl;
    	}
    	return 0;
    }
``

Tester
``#  include<bits/stdc++.h>

using namespace std;

const int N = 500 + 77;
const long long inf = 2e18;
int T;
int n , a[N];
long long ans , dp[N][N] , ps[N];
inline void Test() {
   memset(dp , 63 , sizeof(dp));
   scanf("%d" , & n);
   for(int i = 1;i <= n;++ i)
      scanf("%d" , a + i) , dp[i][i] = 0 , ps[i] = ps[i - 1] + a[i];
   for(int len = 2;len <= n;++ len) {
      for(int le = 1;le <= n;++ le) {
         int ri = le + len - 1;
         if(ri > n)
            ri -= n;
         if(le <= ri) {
            for(int k = le;k < ri;++ k)
               dp[le][ri] = min(dp[le][ri] , dp[le][k] + dp[k + 1][ri] + ps[ri] - ps[le - 1]);
         } else {
            for(int k = le;k < n;++ k)
               dp[le][ri] = min(dp[le][ri] , dp[le][k] + dp[k + 1][ri] + ps[n] - ps[le - 1] + ps[ri]);
            dp[le][ri] = min(dp[le][ri] , dp[le][n] + dp[1][ri] + ps[n] - ps[le - 1] + ps[ri]);
            for(int k = 1;k < ri;++ k)
               dp[le][ri] = min(dp[le][ri] , dp[le][k] + dp[k + 1][ri] + ps[n] - ps[le - 1] + ps[ri]);
         }
      }
   }
   ans = dp[1][n];
   for(int f = 2;f <= n;++ f)
      ans = min(ans , dp[f][f - 1]);
   printf("%lld\n" , ans);
}
int main() {
   scanf("%d" , & T);
   while(T --)
      Test();
   return 0;
}
``

Editorialist
``   //#pragma GCC optimize("Ofast,no-stack-protector")
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

    const int maxn=(int)(505);
    const ll mod=(ll)(1e9+7);
    ll a[maxn],pre[maxn];
    ll dp[maxn][maxn];
    int n;

    ll getSum(int l,int r)
    {
        if(l<=r)
        {
            return pre[r]-(l==0?0:pre[l-1]);
        }

        return pre[n-1]-pre[l-1]+pre[r];
    }

    int main()
    {
        ios_base::sync_with_stdio(0);cin.tie(0);

        int t;cin>>t;

        while(t>0)
        {
            cin>>n;

            for(int i=0;i<n;i++)
            {
                cin>>a[i];
            }

            pre[0]=a[0];

            for(int i=1;i<n;i++)
            {
                pre[i]=pre[i-1]+a[i];
            }

            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    dp[i][j]=LONG_LONG_MAX;
                }
            }

            for(int i=0;i<n;i++)
            {
                dp[i][i]=0;
            }

            for(int size=2;size<=n;size++)
            {
                for(int i=0;i<n;i++)
                {
                   int l=i,r=(i+size-1)%n;

                   for(int j=l;j!=r;j=(j+1)%n)
                   {
                       dp[l][r]=min(dp[l][r],dp[l][j]+dp[(j+1)%n][r]+getSum(l,r));
                   }
                }
            }

            ll res=LONG_LONG_MAX;

            for(int i=0;i<n;i++)
            {
                int l=i,r=(i-1+n)%n;

                res=min(res,dp[l][r]);

             //   cout<<l<<" "<<r<<" "<<dp[l][r]<<endl;
            }

            cout<<res<<endl;

            t--;
        }

        return 0;
    }
``

</details>
