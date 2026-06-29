# K Distinct Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISTK |
| Difficulty Rating | 2015 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [DISTK](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/DISTK) |

---

## Problem Statement

An array is said to be **good** if all its elements are distinct, i.e. no two elements of the array are equal to each other.

You are given a positive integer $N$ and an integer $K$ such that $N \leq K \leq \binom{N+1}{2}$.

Construct an array $A$ of length $N$ that satisfies the following conditions
- $A$ has **exactly** $K$ good (contiguous) subarrays, and
- Every element of $A$ is an integer from $1$ to $N$ (both inclusive).

If there are multiple such arrays, you can print **any** of them.

**Note:** It can be shown that for all inputs satisfying the given constraints, there is **always** a valid solution.

---

## Input Format

- The first line contains an integer $T$, the number of testcases. The description of the $T$ testcases follow.
- Each testcase consists of a single line with two space separated integers, $N$ and $K$ respectively.

---

## Output Format

- For each testcase print $N$ space separated integers, the elements of the constructed array.
- If there are multiple outputs, you can print **any** of them.
- Your output will be considered correct only if the following conditions are satisfied,
    - Every element of the array is between $1$ and $N$, and
    - The array has exactly $K$ good subarrays

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $N \leq K \leq \binom{N+1}{2}$
- Sum of $N$ over all testcases is atmost $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5 5
5 15
5 7
```

**Output**

```text
1 1 1 1 1
1 2 3 4 5
1 2 2 1 1
```

**Explanation**

**Test Case 1:** $N = 5, K = 5$. All subarrays of length $1$ are good, therefore every array of size $N$ has at least $N$ good subarrays. If all elements are equal then these will be the only good subarrays so the given array $\{1, 1, 1, 1, 1\}$ is a valid solution. Observe that under the constraints there are $5$ different solutions (one for each value $1$ through $5$) and all of them will be considered correct.

**Test Case 2:** $N = 5, K = 15$. There are only $\binom{N + 1}{2} = 15$ subarrays, including the array itself. Therefore the array itself must be good which leads us to the solution given above. Any permutation of $\{1, 2, 3, 4, 5\}$ is also a valid solution, thus there are $5! = 120$ different solutions to this case and all of them will be considered correct.

**Test Case 3:** $N = 5, K = 7$. The constructed array is $A = \{1, 2, 2, 1, 1\}$. You may verify that the only good subarrays of $A$, in addition to the $5$ subarrays of length $1$, are those shown below (subarrays are highlighted red).
- $\{{\color{red}1}, {\color{red}2}, 2, 1, 1\}$
- $\{1, 2, {\color{red}2}, {\color{red}1}, 1\}$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5
```

**Output for this case**

```text
1 1 1 1 1
```



#### Test case 2

**Input for this case**

```text
5 15
```

**Output for this case**

```text
1 2 3 4 5
```



#### Test case 3

**Input for this case**

```text
5 7
```

**Output for this case**

```text
1 2 2 1 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START25A/problems/DISTK)

[Contest Division 2](https://www.codechef.com/START25B/problems/DISTK)

[Contest Division 3](https://www.codechef.com/START25C/problems/DISTK)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

An array is said to be good if all its elements are distinct, i.e. no two elements of the array are equal to each other.

You are given a positive integer N and an integer K such that N \leq K \leq  {N+1} \choose 2.

Construct an array A of length N that satisfies the following conditions:

-
A has exactly K good (contiguous) subarrays, and

- Every element of A is an integer from 1 to N (both inclusive).

#
[](#explanation-5)EXPLANATION:

Observation

For different types of arrays, check the number of good subarrays present.

-
**Array where all elements are equal:** Here, only the subarrays of length 1 are good. Thus, the total number of good subarrays is N, where N is the length of the array.

-
**Array where all elements are distinct:** If all the elements are distinct, any possible subarray of this array is good. Thus, the total number of good subarrays is {N+1} \choose 2.

- Any other type of array would have M number of good subarrays, where N < M < {N+1} \choose 2.

The number of good subarrays can be changed by introducing/removing duplicates from certain positions.

Note that, not only the number of duplicates, but their position also matters in determining the number of good subarrays.

Solution

All subarrays of length 1 are good. Thus, we need K' = K-N good subarrays of length \geq 2. From now on, we consider subarrays of length \geq 2 only.

An array of length X having distinct elements contributes X \choose 2 to the answer. Since the total number of good subarrays is K', we build an array of length X with **distinct elements** such that X \choose 2 \leq K < {X+1} \choose 2.

We now need K' -  X \choose 2 good subarrays. This number would be less than X.

Why?

We know that K <  {X+1} \choose 2.

? K -  X \choose 2 <  {X+1} \choose 2 - X \choose 2

? K -  X \choose 2 <  X

For the (X+1)^{th} and subsequent elements, we can place the number at position X - ( K' -  X \choose 2 ). This would contribute K' -  X \choose 2 good subarrays, all ending at position X+1. Since all the subsequent elements are duplicates of (X+1)^{th} element, they would not contribute anything.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
#define LL long long
LL seed = chrono::steady_clock::now().time_since_epoch().count();
mt19937_64 rng(seed);
#define rand(l, r) uniform_int_distribution<LL>(l, r)(rng)
clock_t start = clock();

#define getchar getchar_unlocked

namespace IO {
long long readInt(char endd) {
    long long ret = 0;
    char c = getchar();
    while (c != endd) {
        ret = (ret * 10) + c - '0';
        c = getchar();
    }
    return ret;
}
long long readInt(long long L, long long R, char endd) {
    long long ret = readInt(endd);
    assert(ret >= L && ret <= R);
    return ret;
}
long long readIntSp(long long L, long long R) {
    return readInt(L, R, ' ');
}
long long readIntLn(long long L, long long R) {
    return readInt(L, R, '\n');
}
string readString(int l, int r) {
    string ret = "";
    char c = getchar();
    while (c == '0' || c == '?' || c == '1') {
        ret += c;
        c = getchar();
    }
    assert((int)ret.size() >= l && (int)ret.size() <= r);
    return ret;
}
}
using namespace IO;

const int TMAX = 1'00'000;
const int N = (int)1e5;
const LL K = (N * 1LL * (N + 1)) / 2;

LL sum_n = 0;

void solve() {
    int n = readIntSp(1, N);
    sum_n += n;
    LL k = readIntLn(n, (n * 1LL * (n + 1)) / 2);
    k -= n;
    int i = 0, nxt = 1, cur = 0;
    while (k >= cur) {
        cout << cur + 1 << " ";
        ++i;
        k -= cur;
        ++cur;
    }
    while (i < n) {
        cout << cur - k << " ";
        ++i;
    }
    cout << '\n';
}

int main() {
    int T = readIntLn(1, TMAX);
    while (T--) {
        solve();
    }
    assert(sum_n <= 3 * N);
    assert(getchar() == EOF);
    cerr << fixed << setprecision(10);
    cerr << (clock() - start) / ((long double)CLOCKS_PER_SEC) << " secs\n";
    return 0;
}
``

Tester's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--) {
		long long n, k; cin >> n >> k;
	    k -= n;
	    cout << "1 ";
	    int last = 1;
	    for(int i = 1; i < n; i++) {
	        if(!k) cout << last << " ";
	        else if(k >= last) k -= last, last++, cout << last << " ";
	        else cout << last - k << " ", last -= k, k = 0;
	    }
	    cout << "\n";
	}
	return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

void solve()
{
    ll n,k;
    cin>>n>>k;

    ll curr = (n*n+n)/2;
    int pos = n-1;

    while(curr-pos>=k && pos>0){
        curr -= pos;
        pos--;
    }
    int ans[n+1];
    rep_a(i,1,pos+1) ans[i] = i;
    rep_a(i,pos+1, n+1) ans[i] = pos+1;

    ans[curr-k] = pos+1;

    rep_a(i,1,n+1) cout<<ans[i]<<" ";
    cout<<'\n';
}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
       solve();
    }

}
``

</details>
