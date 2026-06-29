# OR of ANDs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OROFAND |
| Difficulty Rating | 1820 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [OROFAND](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/OROFAND) |

---

## Problem Statement

You are given an array $A$ with $N$ integers. An array's score is defined as the bitwise AND of all its elements. You need to find the bitwise OR of the scores of all possible non-empty subarrays of $A$.

Furthermore, there are $Q$ queries. Each query consists of two integers $X$ and $V$. You need to change the value of the element at index $X$ to $V$. After each query, you again need to find the bitwise OR of the scores of all possible non-empty subarrays.

See the example for more clarification.

###Input:
The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

The first line of each test case contains two space-separated integers $N$ and $Q$ - the size of the array and the number of queries, respectively.

The second line contains $N$ space-separated integers $A_1,\ldots,A_N$.

Each of the next $Q$ lines contains two space-separated integers $X$ and $V$ - the position and the new value of the query, respectively.

###Output:
For each test case print $Q+1$ lines. In the first line print the answer for the original array and in the next $Q$ lines print the answer after every query.

###Constraints
$1 \le T \le 100$

$1 \le N, Q \le 10^5$

$0 \le A_i \le 2^{31}-1$

$1 \le X \le N$

$0 \le V \le 2^{31}-1$

The sum of $N$ over all test cases does not exceed $10^5$

The sum of $Q$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
3 2
1 2 3
1 4
3 0
4 1
1 2 3 4
4 0
```

**Output**

```text
3
7
6
7
3
```

**Explanation**

**Example case 1:** For the original array, all possible subarrays and their scores are as follows.

$AND(1) = 1$, $AND(2) = 2$, $AND(3) = 3$, $AND(1,2) = 0$, $AND(2,3) = 2$, $AND(1,2,3) = 0$.

The bitwise OR of all possible subarray's score is $OR(1,2,3,0,2,0) = 3$.

After the first query new array will be $[4,2,3]$ and the answer will be $7$.

After the second query new array will be $[4,2,0]$ and the answer will be $6$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/OROFAND)

[Contest: Division 1](https://www.codechef.com/COOK128A/problems/OROFAND)

[Contest: Division 2](https://www.codechef.com/COOK128B/problems/OROFAND)

[Contest: Division 3](https://www.codechef.com/COOK128C/problems/OROFAND)

**Author:**  [Harshil Tagadiya](https://www.codechef.com/users/harshil41)

**Tester:**  [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Simple

# PREREQUISITES:

Bitwise Operations, Observation

# PROBLEM:

You are given an array A with N integers. An array’s score is defined as the bitwise AND of all its elements. You need to find the bitwise OR of the scores of all possible non-empty subarrays of A.

You are also asked Q queries. Each query is consists of two integers X and V. You need to change the value of the element at index X to V. After each query, you again need to find the bitwise OR of the scores of all possible non-empty subarray.

# EXPLANATION:

We are given an array A of N integers. The first observation that we can make is that for each query our answer is the Bitwise OR of all its elements. Let’s prove how:

Proof

Suppose we have an array A of N intgers as A_1, A_2,\dots,A_N. There can be two cases possible:

**Case 1:** The i^{th} bit of all the elements is unset i.e. 0.

Consider any non-empty subarray S whose score is X. The score is defined as the bitwise AND of all its elements. Now the i^{th} bit of X will be set only and only if all the elements of this subarray have their i^{th} bit set. As:

0 \And 1 = 0 \\
1 \And 1 = 1

Since no elements had their i^{th} bet set. Hence there exists no subarray whose i^{th} will be set.

Now let’s try to find the Bitwise OR of the scores of all possible non-empty subarrays of A. Suppose the value is Y. Now the i^{th} bit of Y will be set if there exists at least one score whose i^{th} bit is set. As:

0 \hspace{0.1cm}|\hspace{0.1cm} 1 = 1

As we had already proved that there exists no subarray whose i^{th} will be set. Hence the i^{th} bit of our final answer i.e. will be unset.

This means when the i^{th} bit of all the elements of the given array is unset then the i^{th} bit of our answer will be unset.

**Case 2:** There exists at least one element whose i^{th} bit is set i.e. 1.

Now, there exists at least one subarray whose score X has i^{th} bit set i.e. the subarray which consists of single element whose i^{th} is set.

Now let’s try to find the Bitwise OR of the scores of all possible non-empty subarrays of A. Suppose the value is Y. Now the i^{th} bit of Y will be set as there exists at least one score X whose i^{th} bit is set.

This means when the i^{th} bit of at least one of the elements is set then the i^{th} bit of our answer will be set.

Now, we are left with finding the BItwise OR of the array A for each query. Since the value of N and Q are large hence, we won’t be able to find the BItwise OR by traversing the array for each query.

We will again use the property of Bitwise OR, i.e. if there exists at least one element whose i^{th} bit is set, then the i^{th} bit will be set in our answer too. Since the maximum number of bits possible are 31, we will first find the answer in binary form and finally convert that into an integer

To do so, for every bit i we will store the count of elements whose i^{th} bit is set. Now if the count of i^{th} bit is greater than 0 then we will set the i^{th} bit of our answer. Finally, find the answer in integer form and output it.

For each query, we will remove the contribution of the previous element present at index X and add the contribution of V. Finally, we repeat the above procedure to find the answer.

# TIME COMPLEXITY:

O(N*log2(A_i)+Q*log2(A_i)) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, q;
    cin >> n >> q;
    int a[n], bitsCount[32] = {};

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        for (int j = 0; j < 31; j++) {
            if ((a[i] >> j) & 1) {
                bitsCount[j]++;
            }
        }
    }

    int answer = 0;
    for (int j = 0; j < 31; j++)
        answer += (1 << j) * (bitsCount[j] >= 1);
    cout << answer << '\n';

    while (q--) {
        int index, value;
        cin >> index >> value;
        --index;

        // remove old value.
        for (int j = 0; j < 31; j++) {
            if ((a[index] >> j) & 1) {
                bitsCount[j]--;
            }
        }

        a[index] = value;

        // add new value.
        for (int j = 0; j < 31; j++) {
            if ((a[index] >> j) & 1) {
                bitsCount[j]++;
            }
        }

        answer = 0;
        for (int j = 0; j < 31; j++)
            answer += (1 << j) * (bitsCount[j] >= 1);
        cout << answer << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}

``

Tester
``
#include <bits/stdc++.h>

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
    int n, q;
    cin >> n >> q;
    vi a(n + 1);
    int ans = 0;
    vi cnt(31);
    auto del = [&](int val) {
        rep(i, 0, 31) {
            if(val >> i & 1) {
                cnt[i]--;
                if(cnt[i] == 0) ans ^= (1 << i);
            }
        }
    };
    auto add = [&](int val) {
        rep(i, 0, 31) {
            if(val >> i & 1) {
                if(cnt[i] == 0) ans ^= (1 << i);
                cnt[i]++;
            }
        }
    };
    rep(i, 1, n + 1) {
        cin >> a[i];
        add(a[i]);
    }
    cout << ans << '\n';
    while(q--) {
        int x, v;
        cin >> x >> v;
        del(a[x]);
        a[x] = v;
        add(a[x]);
        cout << ans << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

const int mxN=35;
int two[mxN];

void pre()
{
  two[0]=1;

  for(int i=1;i<mxN;i++)
    two[i]=two[i-1]*2;
}

void solve()
{
  int n,q;
  cin>>n>>q;

  int a[n];

  int cnt[mxN]={};

  for(int i=0;i<n;i++)
  {
    cin>>a[i];
    int x=a[i];

    int ind=0;

    while(x)
    {
      if(x%2)
        cnt[ind]++;
      x/=2;
      ind++;
    }
  }

  int ans=0;

  for(int i=0;i<mxN;i++)
  {
    if(cnt[i]!=0)
      ans+=two[i];
  }

  cout<<ans<<"\n";

  while(q--)
  {
    int x,v;
    cin>>x>>v;
    x--;

    int temp=a[x];
    int ind=0;

    while(temp)
    {
      if(temp%2!=0)
        cnt[ind]--;
      temp/=2;
      ind++;
    }

    a[x]=v;
    temp=v;
    ind=0;

    while(temp)
    {
      if(temp%2!=0)
        cnt[ind]++;
      temp/=2;
      ind++;
    }

    ans=0;

    for(int i=0;i<mxN;i++)
    {
      if(cnt[i]!=0)
        ans+=two[i];
    }

    cout<<ans<<"\n";
  }
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  pre();

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
