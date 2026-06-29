# Plusle and Minun on Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PMA |
| Difficulty Rating | 1412 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [PMA](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/PMA) |

---

## Problem Statement

Chef has an array $A$ of length $N$. He defines the *alternating sum* of the array as:
- $S = |A_1| - |A_2| + |A_3| - |A_4| + \ldots (-1)^{N-1}\cdot |A_N|$

Chef is allowed to perform the following operation on the array **at most once**:
- Choose two indices $i$ and $j$ $(1 \leq i <  j \leq N)$ and swap the elements $A_i$ and $A_j$.

Find the **maximum** *alternating sum* Chef can achieve by performing the operation **at most once**.

**Note:** $|X|$ denotes the absolute value of $X$. For example, $|-4| = 4$ and $|7| = 7$.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- First line of each test case contains a single integer $N$ - size of the array $A$.
- Second line of each test case contains $N$ space separated integers - denoting the elements of array $A$.

---

## Output Format

For each testcase, output in a single line, the **maximum** *alternating sum* Chef can obtain by performing the operation **at most once**.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2
10 -10
7
-3 -2 -1 0 1 2 3
```

**Output**

```text
0
6
```

**Explanation**

**Test Case $1$:** One optimal way is to perform no operations. Thus the alternating sum is $|10| - |-10| = 10 - 10 = 0$.

**Test Case $2$:** One optimal way is to choose $i = 2$ and $j = 5$. After swapping, the array is $[-3, 1, -1, 0, -2, 2, 3]$. The alternating sum in this case is $|-3| - |1| + |-1| - |0| + |-2| - |2| + |3| = 6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
10 -10
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
7
-3 -2 -1 0 1 2 3
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PMA)

[Div-4 Contest](https://www.codechef.com/START29D/problems/PMA)

[Div-3 Contest](https://www.codechef.com/START29C/problems/PMA)

[Div-2 Contest](https://www.codechef.com/START29B/problems/PMA)

[Div-1 Contest](https://www.codechef.com/START29A/problems/PMA)

***Author:*** [Agamya Yadav](https://www.codechef.com/users/ultimate_zero)

***Tester:*** [Anshu Garg](https://www.codechef.com/users/anshugarg12)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A of size N.

Operation: You can select two indexes i and j (  i \lt j ) and swap A_i and A_j.

Alternating \space Sum =  S = |A_1| - |A_2| + |A_3| - |A_4| + \ldots (-1)^{N-1}\cdot |A_N|

With **atmost one** operation find the maximum Alternating \space Sum.

#
[](#explanation-5)EXPLANATION:

Since,

 S = |A_1| - |A_2| + |A_3| - |A_4| + \ldots (-1)^{N-1}\cdot |A_N|

It can be observed that using an operation is useful if and only if i and j are of different parity.

Let,

S_1 = \sum_{i \space is \space odd}A_i

S_2 = \sum_{i \space is \space even}A_i

Then,

S = S_1 - S_2

Let’s suppose we swap A_i and A_j, where i is odd and j is even and new alternating sum will become S'. Then,

S' = (S_1 - |A_i| + |A_j|) - (S_2 + |A_i| - |A_j|) = S  + 2 \cdot (|A_j| - |A_i|)

So, to maximize S', we need to maximize |A_j| and minimize |A_i|.

Let,

|A_i|_{min} be minimum value of |A_i| where i is odd.

|A_j|_{max} be maximum value of |A_j| where j is even.

then **maximum** Alternating \space Sum = \max(S, S + 2 \cdot (|A_j|_{max} - |A_i|_{min}))

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solutions-7)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
#define ll long long int
using namespace std;

void solve(){
    int n;
    cin>>n;
    vector<ll> a(n);
    ll sum = 0;
    ll mini = INT_MAX, maxi = INT_MIN;

    for(int i = 0; i < n; i++){
    	cin>>a[i];
    	if(i % 2 == 0){
    	    sum = sum + abs(a[i]);
    	    mini = min(mini, abs(a[i]));
    	}
    	else {
    	    sum = sum - abs(a[i]);
    	    maxi = max(maxi, abs(a[i]));
    	}
    }

cout<<max(sum, sum + 2LL* (maxi - mini))<<"\n";

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin>>t;
    while(t--)solve();
    return 0;
}
``
````

Tester's Solution
``#include<bits/stdc++.h>
using namespace std ;

#define ll              long long
#define pb              push_back
#define all(v)          v.begin(),v.end()
#define sz(a)           (ll)a.size()
#define F               first
#define S               second
#define INF             2000000000000000000
#define popcount(x)     __builtin_popcountll(x)
#define pll             pair<ll,ll>
#define pii             pair<int,int>
#define ld              long double

template<typename T, typename U> static inline void amin(T &x, U y){ if(y < x) x = y; }
template<typename T, typename U> static inline void amax(T &x, U y){ if(x < y) x = y; }

#ifdef LOCAL
#define debug(...) debug_out(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) 2401
#endif

long long readInt(long long l,long long r,char end){
    long long x = 0;
    int cnt = 0;
    int first =-1;
    bool is_neg = false;
    while(true) {
        char g = getchar();
        if(g == '-') {
            assert(first == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9') {
            x *= 10;
            x += g - '0';
            if(cnt == 0) {
                first = g - '0';
            }
            ++cnt;
            assert(first != 0 || cnt == 1);
            assert(first != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && first > 1)));
        }
        else if(g == end) {
            if(is_neg) {
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
string readString(int l,int r,char end){
    string ret = "";
    int cnt = 0;
    while(true) {
        char g = getchar();
        assert(g != -1);
        if(g == end) {
            break;
        }
        ++cnt;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
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

int _runtimeTerror_()
{
    int T = readIntLn(1, 1e5);
    int mx_N = 0, mn_N = 1e6, sum_N = 0;
    for(int i=1;i<=T;++i) {
    	vector<vector<int>> g(2);
    	int N = readIntLn(2, 1e5);
    	amax(mx_N, N);
    	amin(mn_N, N);
    	sum_N += N;
    	ll ans = 0;
    	for(int i=1;i<=N;++i) {
    		int x;
    		if(i != N) {
    			x = readIntSp(-1e9, 1e9);
    		}
    		else {
    			x = readIntLn(-1e9, 1e9);
    		}
    		g[i & 1].push_back(abs(x));
    		if(i & 1) {
    			ans += abs(x);
    		}
    		else {
    			ans -= abs(x);
    		}
    	}

    	sort(all(g[0])), sort(all(g[1]));
    	ans = max(ans, ans + 2 * g[0].back() - 2 * g[1][0]);
    	cout << ans << "\n";
    }
    cerr << T << " " << mn_N << " " << mx_N << " " << sum_N << "\n";
    assert(sum_N <= 2e5);
    assert(getchar() == -1);
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    #ifdef runSieve
        sieve();
    #endif
    #ifdef NCR
        initncr();
    #endif
    int TESTS = 1;
    //cin >> TESTS;
    while(TESTS--) {
        _runtimeTerror_();
    }
    return 0;
}
``
````

</details>
