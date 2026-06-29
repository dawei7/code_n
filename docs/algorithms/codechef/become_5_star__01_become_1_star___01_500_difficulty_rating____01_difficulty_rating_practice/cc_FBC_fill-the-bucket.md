# Fill the Bucket

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FBC |
| Difficulty Rating | 419 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FBC](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FBC) |

---

## Problem Statement

Chef has a bucket having a capacity of $K$ liters. It is already filled with $X$ liters of water.

Find the **maximum** amount of extra water in liters that Chef can fill in the bucket without overflowing.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers $K$ and $X$ - as mentioned in the problem.

---

## Output Format

For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \lt K \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
2
5 4
15 6
```

**Output**

```text
1
9
```

**Explanation**

**Test Case $1$:** The capacity of the bucket is $5$ liters but it is already filled with $4$ liters of water. Adding $1$ more liter of water to the bucket fills it to $(4+1) = 5$ liters. If we try to fill more water, it will overflow.

**Test Case $2$:** The capacity of the bucket is $15$ liters but it is already filled with $6$ liters of water. Adding $9$ more liters of water to the bucket fills it to $(6+9) = 15$ liters. If we try to fill more water, it will overflow.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
15 6
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Div-4 Contest](https://www.codechef.com/START29B/problems/FBC)

***Author:*** [ Arpit Kesharwani](https://www.codechef.com/users/anript)

***Tester:*** [ Anshu Garg](https://www.codechef.com/users/anshugarg12)

***Editorialist:*** [Akshat Gupta](https://www.codechef.com/users/akshat468)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Chef has a bucket having a capacity of K liters. It is already filled with X liters of water.

Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.

#
[](#explanation-4)EXPLANATION:

Given a Bucket having K litres of capacity out of which X litres is already filled.

Let Y be the Extra amount which is filled in bucket

so X + Y  is the total amount of water.

Amount of Water \leq Capacity of water

X + Y \leq K

\Rightarrow Y \leq K - X

From the above Equation

Y_{\max} = K - X

Hence the Answer to the Problem is K - X

#
[](#solutions-5)SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int k,x;
	    cin>>k>>x;
	    cout<<k-x <<endl;
	}
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
    int T = readIntLn(1, 100);
    int mn_K = 2000, mx_K = 0;
    for(int i=1;i<=T;++i) {
    	int K = readIntSp(2, 1000);
    	int X = readIntLn(1, K - 1);
    	cout << K - X << "\n";
    	amax(mx_K, K);
    	amin(mn_K, K);
    	cerr << K << " " << X << "\n";
    }
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
