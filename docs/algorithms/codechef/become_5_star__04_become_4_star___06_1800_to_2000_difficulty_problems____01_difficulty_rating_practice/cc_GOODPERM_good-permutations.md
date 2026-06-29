# Good Permutations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GOODPERM |
| Difficulty Rating | 1823 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [GOODPERM](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/GOODPERM) |

---

## Problem Statement

You have a sequence $a$ with length $N$ created by removing some elements (possibly zero) from a permutation of numbers $(1, 2, \dots, N)$. When an element is removed, the length of the sequence doesn't change, but there is an empty spot left where the removed element was. You also have an integer $K$.

Let's call a permutation $p_1, p_2, \dots, p_N$ *good* if:
- it is possible replace empty spots in $a$ by numbers in such a way that we obtain the permutation $p$
- the number of positions $i$ ($1 \lt i \le N$) such that $p_i \gt p_{i-1}$ is equal to $K$

Your task is to find the number of good permutations.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $a_1, a_2, \dots, a_N$. Each element of this sequence is either $0$ (indicating an empty spot previously occupied by a removed element) or an integer between $1$ and $N$ inclusive.

### Output
For each test case, print a single line containing one integer — the number of good permutations.

### Constraints
- $1 \le T \le 300$
- $0 \le K \lt N \le 8$
- each integer between $1$ and $N$ inclusive appears in $a$ at most once

---

## Examples

**Example 1**

**Input**

```text
1
3 1
2 0 0
```

**Output**

```text
2
```

**Explanation**

**Example case 1:** The two possible good permutations are $(2,3,1)$ and $(2,1,3)$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/COOK95A/problems/GOODPERM)

[Div2](https://www.codechef.com/COOK95B/problems/GOODPERM)

[Practice](https://www.codechef.com/problems/GOODPERM)

**Setter-** [Igor Barenblat](https://www.codechef.com/users/barenuz)

**Tester-** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

Simple

### PRE-REQUISITES:

[STL](https://www.geeksforgeeks.org/stdnext_permutation-prev_permutation-c/), [Generate all Permutations of an Array](https://www.geeksforgeeks.org/heaps-algorithm-for-generating-permutations/)

### PROBLEM:

Given a partially filled permutation p, we have to find number of possible good permutations from it. A permutation is good if-

- It has all numbers from [1,n]

- Number of positions such that p_i>p_{i-1} is exactly equal to K

### QUICK EXPLANATION:

**Key to Success-** Anyone with good knowledge of STL and implementation skills can do this question very, very easily!

We generate all permutations of [1,n] and check if-

- it satisfies the condition of number of p_i>p_{i-1} equal to K.

- it can be achieved from sequence A

We can easily use C++ STL’s next_permutation() to generate the permutations easily.

### EXPLANATION:

This editorial will have a single section. There is little concept to be discussed, hence we will discuss the cleanest way of implementing it quickly. We will refer to **Setter’s** solution for it

**Setter’s Solution-**

**"I took the input Mr. Editorialist. WTF THIS QUESTION SO `DIPHICULT` I CANT SOLVE WTFWTF?!"**

Hold your breath young man/woman/boy/girl/whatever. We shall deal with the question one step at a time, i.e. [@step_by_step](/u/step_by_step) .

The first thing will be, to make a new array for permutations. **Remember, that repetitions are not allowed in permutations, and all numbers in range [1,n] must occur exactly once!!**

Since we plan to use next_permutation() function from STL, lets generate the lexicographically smallest permutation first. In other words, initialize new permutation array p[] as- p[]=\{1,2,3,...,n\}. Code for it-

``for (int i=1;i<=n;i++){
        p[i]=i;
    }
``

Our next_permutation() will generate ALL permutations for us. We only have to check 2 things-

- If that permutation is achievable from a

- It satisfies the condition of number of p_i>p_{i-1} equal to K.

When will a permutation be achievable from a? Recall that, we can **only** fill in 0's, and not shuffle permutation a. Hence, we can say that a permutation is valid IF AND ONLY IF-

-
A_i==0 and P_i doesnt occur elsewhere in A_i.

-
A_i \neq 0 and P_i==A_i.

In other words, if A_i is 0 and the element P_i can be inserted in A, or if A_i \neq 0, then P_i must be equal to A_i, because shuffling/moving-elements is not allowed.

A sample code for that is-

```for (int i=1;i<=n;i++){
            if (a[i]>0 && a[i]!=p[i]){
                //Invalid Permutation
            }
        }`
``

Note that we didnt check for "A_i==0 and P_i doesnt occur elsewhere in A_i." It is redundant. Why? (Q1)

Now what is left is, simply, to check the count of P_i>P_{i-1} being equal to K. Simple looping for that is needed. A sample code-

`for (int i=2;i<=n;i++){ if (p[i]>p[i-1]){ cnt++; } }`

A full overview of working loop is given in tab below-

Click to view
``do{
        int cnt=0;
        for (int i=1;i<=n;i++){
            if (a[i]&&a[i]!=p[i]){
                cnt-=100;
            }
        }
        for (int i=2;i<=n;i++){
            if (p[i]>p[i-1]){
                cnt++;
            }
        }
        ans+=(cnt==k);
    }
    while (next_permutation(p+1,p+n+1));
``

Thats it! We’re done with this question now as well

### SOLUTION:

The setter and tester’s code are pasted in tabs below because [@admin](/u/admin) can take some time in linking the solutions. Please refer to them

[Setter](http://www.codechef.com/download/Solutions/COOK95/setter/GOODPERM.cpp)

Click to view
``#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define files(name) name!=""?freopen(name".in","r",stdin),freopen(name".out","w",stdout):0
#define all(a) a.begin(),a.end()
#define len(a) (int)(a.size())
#define elif else if
#define mp make_pair
#define pb push_back
#define fir first
#define sec second

using namespace std;
#define int long long

typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long double ld;
typedef long long ll;

const int arr=2e5+10;
const int ar=2e3+10;
const ld pi=acos(-1);
const ld eps=1e-10;
const ll md=1e9+7;

///---program start---///

int a[arr];
int p[arr];

void solve()
{
    int n,k;
    cin>>n>>k;
    for (int i=1;i<=n;i++){
        cin>>a[i];
    }
    for (int i=1;i<=n;i++){
        p[i]=i;
    }

    int ans=0;
    do{
        int cnt=0;
        for (int i=1;i<=n;i++){
            if (a[i]&&a[i]!=p[i]){
                cnt-=100;
            }
        }
        for (int i=2;i<=n;i++){
            if (p[i]>p[i-1]){
                cnt++;
            }
        }
        ans+=(cnt==k);
    }
    while (next_permutation(p+1,p+n+1));

    cout<<ans<<"\n";
}

main()
{
    #ifdef I_love_Maria_Ivanova
        files("barik");
        freopen("debug.txt","w",stderr);
    #endif

    int test;
    cin>>test;
    while (test--){
        solve();
    }
}
``

[Tester](http://www.codechef.com/download/Solutions/COOK95/tester/GOODPERM.cpp)

Click to view

**Its VERY scary for newbies. Dont open it!!**

Click to view

**You wont agree huh? A glimpse is given in next tab. Heed my warning!**

Click to view

**The only persistence I like is in persistent segment trees. Open next tab at your own risk!!**

Click to view
``for (int i = 2; i <= n; ++i) {
		memset(ndp, 0, sizeof(ndp));
		for (int mask = 0; mask < 1 << 8; ++mask) {
			for (int last = 0; last < 8; ++last) {
				for (int cnt = 0; cnt < 8; ++cnt) {
					if (dp[mask][last][cnt] > 0) {
						if (p[i] == 0) {
``

Click to view

**Want the full solution still? Fineeee**

Click to view
``#include <bits/stdc++.h>

using namespace std;

const int MaxN = (int)4e5 + 10;
const int MOD = (int)1e9 + 7;
const int INF = 1e9;

int p[10];
int dp[1 << 8][8][8];
int ndp[1 << 8][8][8];

void solve() {
	int n, k;
	scanf("%d%d", &n, &k);
	set < int > s;
	for (int i = 1; i <= n; ++i) {
		scanf("%d", &p[i]);
		if (p[i] > 0) {
			assert (!s.count(p[i]));
			s.insert(p[i]);
		}
	}
	memset(dp, 0, sizeof(dp));
	if (p[1] == 0) {
		for (int i = 1; i <= n; ++i) {
			dp[1 << (i - 1)][i - 1][0] = 1;
		}
	} else {
		dp[1 << (p[1] - 1)][p[1] - 1][0] = 1;
	}
	for (int i = 2; i <= n; ++i) {
		memset(ndp, 0, sizeof(ndp));
		for (int mask = 0; mask < 1 << 8; ++mask) {
			for (int last = 0; last < 8; ++last) {
				for (int cnt = 0; cnt < 8; ++cnt) {
					if (dp[mask][last][cnt] > 0) {
						if (p[i] == 0) {
							for (int nlast = 0; nlast < 8; ++nlast) {
								if (~mask & (1 << nlast)) {
									ndp[mask | (1 << nlast)][nlast][cnt + (nlast > last)] += dp[mask][last][cnt];
								}
							}
						} else {
							if (~mask & (1 << (p[i] - 1))) {
								ndp[mask | (1 << (p[i] - 1))][p[i] - 1][cnt + (p[i] - 1 > last)] += dp[mask][last][cnt];
							}
						}
					}
				}
			}
		}
		memcpy(dp, ndp, sizeof(ndp));
	}
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		ans += dp[(1 << n) - 1][i][k];
	}
	printf("%d\n", ans);
}

int main() {
//	freopen("input.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	while (t --> 0) {
		solve();
	}
	return 0;
}
``

Editorialist Solution will be put on demand

Time Complexity=O(N!*N) (Setter)

Time Complexity=O(???) (Tester)

### CHEF VIJJU’S CORNER

**1. Note that we didnt check for "A_i==0 and P_i doesnt occur elsewhere in A_i." It is redundant. Why?**

Click to view

**Simply because, if the element corresponding to that A_i is at some other position, and all elements occur only once, then a mismatch at the position where A_i\neq 0 is confirmed.**

**2. Tester’s Solution-** He solved it using dp+bitmask, which should deserve a mention here :).

Click to view

**Permutation: solution with bitmasks. Make a dp table as-**

dp[i][mask][last][cnt]

**How many permutations with filled first i positions. Subset of elements on those positions = mask.**

q[i] = last

**and there was cnt p[i] > p[i-1]**

**Transitions processing in O(N) if p[i+1] = 0 and in O(1) if p[i+1] != 0**

**3. Refer to Tester’s code and his notes. Derive the time complexity of his solution in worst case.**

Click to view

O({2}^{N}*{N}^{3}*K)

**4. Test Case Bank-**

Click to view

**Official Input-** [https://pastebin.com/SvrCRxSh](https://pastebin.com/SvrCRxSh)

**Official Output-** [https://pastebin.com/QEXfi5J8](https://pastebin.com/QEXfi5J8)

**5. Related Problems-**

-
[B. Petr and Permutations](http://codeforces.com/problemset/problem/986/B)- Not very related, but very, veryyyy fun xD

- [B. Open Communication](http://codeforces.com/problemset/problem/993/B)

</details>
