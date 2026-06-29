# K-Subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHESUB |
| Difficulty Rating | 2306 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHESUB](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHESUB) |

---

## Problem Statement

You are given two integers $N$ and $K$, and an array $A$ of $N$ integers. You have to choose $K$ disjoint non-empty subarrays such that the score is maximized.

The score is calculated as follows:
$$
\mathrm{Score}= \sum_{i=1}^{K} \mathrm{Sum}[i] \cdot i,
$$

where $\mathrm{Sum}[i]$ denotes sum of elements of $i$-th subarray. By the $i$-th subarray, we mean the $i$-th one in the order from left to right.

Find the maximum score that can be achieved.

**Note:** The subarrays are not required to cover the whole array. It is allowed for some elements of $A$ to belong to none of the subarrays.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\dots,A_N$.

### Output
For each test case, print a single line containing one integer ― the maximum score.

### Constraints
- $1 \le T \le 1000$
- $1 \le N \le 10^5$
- $1 \le K \le \min(100,N)$
- $-10^6 \le A_i \le 10^6$
- The sum of $N$ over all test cases does not exceed $10^5$

### Subtasks
- **Subtask #1 (15 points)**: $K=1$
- **Subtask #2 (35 points):** $K=2$
- **Subtask #3 (50 points):** Original constraints

---

## Examples

**Example 1**

**Input**

```text
2
5 2
1 2 -1 3 1
5 2
-1 2 11 -23 12
```

**Output**

```text
11
37
```

**Explanation**

- **Test Case 1:** One way to choose $2$ disjoint non-empty subarrays is:

$S_1 = [1,2]$ and $S_2 = [3,1]$

The score is $3\cdot 1 + 4\cdot 2 =11$, which is the maximum possible.

- **Test Case 2:** One way to choose $2$ disjoint non-empty subarrays is:

$S_1 = [2,11]$ and $S_2 = [12]$

The score is $13\cdot 1+12\cdot 2 = 37$, which is the maximum possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
1 2 -1 3 1
```

**Output for this case**

```text
11
```



#### Test case 2

**Input for this case**

```text
5 2
-1 2 11 -23 12
```

**Output for this case**

```text
37
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME96A/problems/CHESUB)

[Contest Division 2](https://www.codechef.com/LTIME96B/problems/CHESUB)

[Contest Division 3](https://www.codechef.com/LTIME96C/problems/CHESUB)

[Practice](https://www.codechef.com/problems/CHESUB)

**Setter & Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

**Tester:** [Riley Borgard](https://www.codechef.com/users/monogon)

# DIFFICULTY

Easy-Medium

# PREREQUISITES

DP

# PROBLEM

You are given two integers N and K, and an array A of N integers. You have to choose K disjoint non-empty subarrays such that the score is maximized.

The score is calculated as follows:

\mathrm{Score}= \sum_{i=1}^{K} \mathrm{Sum}[i] \cdot i,

where \mathrm{Sum}[i] denotes sum of elements of i-th subarray. By the i-th subarray, we mean the i-th one in the order from left to right.

Find the maximum score that can be achieved.

# EXPLANATION:

Our goal is to maximize the score, let us see how that can be done for the various subtasks.

### Subtask 1:

K=1

Since we only need to choose 1 non-empty subarray in this subtask. And our goal is to maximize the score, then the optimal choice to choose subarray is the one that has maximum sum among all the choices available.

Hence, this subtask of the problem is reduced to finding the maximum subarray sum such that the subarray is non-empty. This can be easily done by Kadane’s Algorithm.

Time Complexity

O(N) per test case

Solution
``#include <bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
	 int n,k;
   cin>>n>>k;

   int arr[n];
   for(int i=0;i<n;i++)
    cin>>arr[i];

  int ans=arr[0];
  int curr=0;

  for(int i=0;i<n;i++)
  {
    curr+=arr[i];
    ans=max(ans,curr);
    if(curr<0)
      curr=0;
  }

  if(k==1)
    cout<<ans<<"\n";
  else
    exit(0);
}

int32_t main(){

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

### Subtask 2:

K=2

We only need to choose 2 non-empty subarrays in this subtask. If there are two subarrays say S_1 and S_2, then we can say that the index of the first element of the subarray S_2 is always greater than the index of the last element of the subarray S_1.

Suppose we are at index i of the array A, then we can easily find the first subarray from the prefix of the array [A_1, A_2,\dots, A_i] and the other subarray from the suffix of the array [A_{i+1}, A_{i+2},\dots, A_N]. Since our goal is to maximize the score, we will always try to maximize the subarray sum of both prefix and suffix.

Hence for every index i of an array, we will find the maximum subarray sum in prefix [A_1, A_2,\dots, A_i] and maximum subarray sum in suffix [A_{i+1}, A_{i+2},\dots, A_N]. To optimally find the maximum subarray sum for every index i in prefix and suffix we can use prefix and suffix array where the i-th element of prefix array stores the maximum subarray sum possible in [A_1, A_2,\dots, A_i] and similarly for suffix array.

To find the maximum subarray sum we can use Kadane’s Algorithm.

Time Complexity

O(N) per test case

Solution
``#include <bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int n,k;
  cin>>n>>k;

  int arr[n];
  for(int i=0;i<n;i++)
    cin>>arr[i];

  int pre[n],suf[n];

  int ans=arr[0];
  int curr=0;

  for(int i=0;i<n;i++)
  {
    curr+=arr[i];
    ans=max(ans,curr);
    pre[i]=ans;
    if(curr<0)
      curr=0;
  }

  ans=arr[n-1];
  curr=0;

  for(int i=n-1;i>=0;i--)
  {
    curr+=arr[i];
    ans=max(ans,curr);
    suf[i]=ans;
    if(curr<0)
      curr=0;
  }

  ans=INT_MIN;

  for(int i=0;i<n-1;i++)
  {
    int temp=pre[i]+suf[i+1]*2;
    ans=max(ans,temp);
  }

  if(k==2)
    cout<<ans<<"\n";
  else
    exit(0);
}

int32_t main(){

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

### Subtask 3:

Original Constraints

Since the value of K is large enough this time to break our greedy solution. Notice that when we are at some index i of an array we had several choices like:

- Should we include this element in the previous subarray?

- Should we never take this element in any of the K subarrays?

- Should we start our new subarray from this element?

All these types of queries in our mind give us big hint towards Dynamic Programming as well as the states of the DP.

**Now, let’s move towards Dynamic Programming.**

Let’s create our DP as (i,j) which is defined as follows:

DP[i][j] is defined as the maximum score that is possible by taking the first i index of the array A and having exactly j subarrays such that the jth subarray ends at index i .

Suppose we are at index i of an array and we had selected j subarrays till now. Now for this index, i we had choices as:

- Take this element in the j-th subarray, then our transition will be as:

DP[i][j]=DP[i-1[[j]+j*A[i]

- Start a new subarray from this index of an array. Then the transition will be as follows:

DP[i][j]=max(DP[i-1][j-1],DP[i-2][j-1],\dots,DP[1][j-1])+j*A[i]

As we can see that the when we want to start a new subarray from index i if an array then there are several choices and we need to find the maximum among all since our goal is to maximize the score.

To find the maximum, we need to (i-1) iterations for every state leading the time complexity to N^2*K which surely results in TLE.

However, we can do better by using the concept of prefix array. We can define prefix array as:

prefix[i][j]=max(DP[i][j],DP[i-1][j],\dots,DP[1][j])

Hence instead of doing (i-1) iterations, we can simply do it in O(1) by using the concept of prefix array leading us to time complexity of O(N*K) which helps to get AC.

All we need to do is now compute the value of the prefix array. It is quite clear that any column of prefix array will always be sorted in non-decreasing order. Suppose we computed the value of DP[i][j], then we can update our prefix array as:

prefix[i][j]=max(prefix[i-1][j],DP[i][j])

# TIME COMPLEXITY:

O(N*K) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;

#define int long long

int inf = 1e18;

int dp[100010][110];
int prefix[100010][110];

void solve()
{
  int n, k;
	cin >> n >> k;
	int a[n], b[k];

	for(int i=0; i<n; i++)
		cin >> a[i];
	for(int j=0; j<k; j++)
		b[j]=j+1;

	for(int i=0; i<n; i++){
		dp[i][0] = 0;
		prefix[i][0] = 0;
		for(int j=1; j<=k; j++){
			dp[i][j] = -inf;
			prefix[i][j] = -inf;
		}
	}

	dp[0][1] = a[0]*b[0];
	prefix[0][1] = dp[0][1];

	for(int i=1; i<n; i++){
		for(int j=1; j<=k; j++){
			dp[i][j] = max(dp[i-1][j], prefix[i-1][j-1]) + a[i]*b[j-1];
			dp[i][j] = max(dp[i][j], -inf);
			prefix[i][j] = max(prefix[i-1][j], dp[i][j]);
		}
	}

	int ans = -inf;
	for(int i=0; i<n; i++){
		ans = max(ans, dp[i][k]);
	}

	cout << ans << "\n";
}

int32_t main(){
  // freopen("sub5.in","r",stdin);
  // freopen("sub5.out","w",stdout);
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

Tester
``#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int n, k;
    cin >> n >> k;
    vector<ll> a(n + 1);
    rep(i, 1, n + 1) {
        cin >> a[i];
        a[i] += a[i - 1];
    }
    vector<ll> dp(k + 1, LLONG_MIN), mx(k + 1, LLONG_MIN);
    dp[0] = 0;
    mx[0] = 0;
    rep(i, 1, n + 1) {
        for(int j = k; j >= 1; j--) {
            if(mx[j - 1] == LLONG_MIN) {
                dp[j] = LLONG_MIN;
                mx[j] = LLONG_MIN;
            }else {
                dp[j] = max(dp[j], mx[j - 1] + a[i] * j);
                mx[j] = max(mx[j], dp[j] - a[i] * (j + 1));
            }
        }
        mx[0] = max(mx[0], dp[0] - a[i]);
    }
    cout << dp[k] << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

</details>
