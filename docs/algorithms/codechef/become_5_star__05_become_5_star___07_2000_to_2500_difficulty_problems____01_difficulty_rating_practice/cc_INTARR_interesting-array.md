# Interesting Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INTARR |
| Difficulty Rating | 2145 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [INTARR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/INTARR) |

---

## Problem Statement

An array is called *interesting* if no subarray of length **greater than** $2$ is non-increasing or non-decreasing.

Chef has an array $A$ of length $N$. He wants to make the array **interesting** by rearranging the elements in any order.

If there exist multiple such arrays, output any one.
If no such array exists, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ denoting the length of array $A$.
    - The next line contains $N$ space separated integers, $A_1, A_2, \ldots, A_N$

---

## Output Format

For each test case, output on a single line, any possible **interesting** array.
If no such array is possible, output $-1$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
2 2 2
4
2 6 5 2
5
5 5 2 4 2
```

**Output**

```text
-1
6 2 5 2
5 2 4 2 5
```

**Explanation**

**Test case $1$:** There is no way of arranging the elements such that no subarray of length greater than $2$ is non-increasing or non-decreasing.

**Test case $2$:** A possible rearrangement of the elements is $[6, 2, 5, 2]$. Note that the subarrays of length greater than $2$ are $\{[6, 2, 5], [2, 5, 2], [6, 2, 5, 2]\}$. None of these subarrays are non-increasing or non-decreasing.

**Test case $3$:** A possible rearrangement of the elements is $[5, 2, 4, 2, 5]$. Note that the subarrays of length greater than $2$ are $\{[5, 2, 4], [2, 4, 2], [4, 2, 5], [5, 2, 4, 2], [2, 4, 2, 5], [5, 2, 4, 2, 5]\}$. None of these subarrays are non-increasing or non-decreasing.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 2 2
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
4
2 6 5 2
```

**Output for this case**

```text
6 2 5 2
```



#### Test case 3

**Input for this case**

```text
5
5 5 2 4 2
```

**Output for this case**

```text
5 2 4 2 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/INTARR)

[Contest: Division 1](https://www.codechef.com/START68A/problems/INTARR)

[Contest: Division 2](https://www.codechef.com/START68B/problems/INTARR)

[Contest: Division 3](https://www.codechef.com/START68C/problems/INTARR)

[Contest: Division 4](https://www.codechef.com/START68D/problems/INTARR)

***Author:*** [inov_360](https://www.codechef.com/users/inov_360)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2145

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

Given an array A, rearrange it so that every sorted subarray has length \leq 2.

#
[](#explanation-5)EXPLANATION:

If N \leq 2, any rearrangement works so let’s assume N \geq 3.

Notice that if A_i = A_{i+1} for some i, then at least one of the subarrays [A_{i-1}, A_i, A_{i+1}] and [A_{i}, A_{i+1}, A_{i+2}] will exist, and be sorted.

So, if we are to rearrange it, the final array cannot have adjacent equal elements.

Let’s use this information to analyze what a valid final array can look like.

Suppose we fix the element A_1. Then, A_2 \neq A_1; let’s assume A_2 \gt A_1 for now. Note that:

-
[A_1, A_2, A_3] shouldn’t be sorted, so A_3 \lt A_2 must hold.

-
[A_2, A_3, A_4] shouldn’t be sorted, so A_4 \gt A_3 must hold.

-
[A_3, A_4, A_5] shouldn’t be sorted, so A_5 \lt A_4 must hold.

\vdots

Notice that this essentially makes A have a ‘zig-zag’ pattern, i.e,

A_1 \lt A_2 \gt A_3 \lt A_4 \gt A_5 \lt \ldots

If A_2 \lt A_1 we get a similar zig-zag pattern, but with the peaks and valleys flipped; either way it’s a zig-zag.

Now, let’s try to put A into the pattern A_1 \lt A_2 \gt A_3 \lt A_4 \gt A_5 \lt \ldots

Our aim when doing this is to ensure that we never place equal elements next to each other. So, ideally, A_i and A_{i+1} are ‘far apart’ for every i.

The optimal way to do this is as follows:

- Let S denote the sorted array of A, so S_1 \leq S_2 \leq \ldots \leq S_N

- Set A_1 = S_1, A_3 = S_2, \ldots

- More generally, set A_{2k-1} = S_k

- The above process used elements S_1, S_2, \ldots, S_M, where M = \left\lceil \frac{N}{2} \right\rceil

- To fill the even positions, we do something similar. Set A_2 = S_{M+1}, A_4 = S_{M+2}, \ldots

- That is, set S_{2k} = S_{M+k}

Note that this process makes A_i and A_{i+1} be about N/2 positions apart (in sorted order) for every i, which is the best we can hope far.

This gives us a candidate zig-zag array A. Now check if it is valid (by looking at all size-3 subarrays), and if it is, print it.

If it isn’t valid, use a similar process to create a zig-zag array based on the pattern A_1 \gt A_2 \lt A_3 \gt A_4 \lt A_5 \gt \ldots

Notice that one easy way to do this is to simply repeat the above process on the reverse of S.

Once again, check if the obtained array is valid and print it if it is.

If both checks above fail, the answer is -1: every zig-zag rearrangement will include some pair of adjacent equal elements.

Proof

This is surprisingly a bit non-trivial to prove, and needs some case analysis.

Let’s construct the array A_1 \lt A_2 \gt A_3 \lt \ldots using the process as described above.

Suppose there are adjacent equal elements. Let i be the smallest index such that A_i = A_{i+1}.

The order in which we placed elements specifically tells us the following:

-
i = 2k for some k \geq 1

- A_{2} = A_{4} = \ldots = A_{2k} = A_{2k+1} = A_{2k+3} = \ldots

Let this element be x. The above tells us that x appears at least \left\lceil \frac{N}{2} \right\rceil times in A.

If it appears \gt \left\lceil \frac{N}{2} \right\rceil times, the pigeonhole principle tells us that there will always be some adjacent equal elements, so the answer will always be -1.

Now, suppose x appears exactly \left\lceil \frac{N}{2} \right\rceil times. There are now two cases to consider, based on the parity of N.

- When N is odd, the only possible situation when a valid zig-zag array exists is when x is either the smallest or the largest element of A: these two cases correspond to the two constructions we had above.

- When N is even, a valid zig-zag array always exists because we can place elements in the form `x _ x _ x _ ... x _ _ x _ x ... _ x`, and choosing the spot where we flip from `x _` to `_ x` can be done based on how many elements are \lt x.

- Once again, depending on whether x is the smallest element or not, you can see this corresponds to one of the constructions above.

This completes the proof.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ll long long
#define db double
#define el "\n"
#define ld long double
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)
#define all(ds) ds.begin(), ds.end()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef vector< long long > vi;
typedef pair<long long, long long> ii;
typedef priority_queue <ll> pq;
#define o_set tree<ll, null_type,less<ll>, rb_tree_tag,tree_order_statistics_node_update>

const ll mod = 1000000007;
const ll INF = (ll)1e18;
const ll MAXN = 1000006;

ll po(ll x, ll n){
    ll ans=1;
    while(n>0){ if(n&1) ans=(ans*x)%mod; x=(x*x)%mod; n/=2;}
    return ans;
}

bool fun(vector<ll> &a){
    int n = a.size();
    int c[n];

    int j = (n+1)/2;

    c[0] = a[0];
    int k = 1;
    for(int i = 1; i<(n+1)/2; i++){
        c[k++] = a[j++];
        c[k++] = a[i];
    }
    if(k<n) c[k] = a[j];
    int ok = 1;

    for(int i=1; i+1<n; i++){
        ok &= ( !(c[i-1] <= c[i] && c[i] <= c[i+1])
                        && !(c[i-1] >= c[i] && c[i] >= c[i+1]));
    }

    if(ok){
        rep(i,n) cout<<c[i]<<" ";
        cout<<el;
        return true;
    }

    j = n/2;
    k = 0;
    for(int i = 0; j < n; i++){
    	c[k++] = a[j++];
    	if(i<n/2) c[k++] = a[i];
    }

    ok = 1;
    for(int i=1; i+1<n; i++){
        ok &= ( !(c[i-1] <= c[i] && c[i] <= c[i+1])
                        && !(c[i-1] >= c[i] && c[i] >= c[i+1]));
    }

     if(ok){
        rep(i,n) cout<<c[i]<<" ";
        cout<<el;
        return true;
    }
    return ok;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    int T=1;
    cin >> T;
    while(T--){
        int n;
        cin>>n;

        vector<ll> a(n);
        rep(i,n) cin>>a[i];

        sort(all(a));

        bool z = fun(a);
        if(!z){

                cout<<-1<<el;
        }

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}
``

Editorialist's code (Python)
``def check(ar):
	n = len(ar)
	for i in range(n-2):
		if ar[i] >= ar[i+1] >= ar[i+2]: return 0
		if ar[i] <= ar[i+1] <= ar[i+2]: return 0
	return 1
for _ in range(int(input())):
	n = int(input())
	a = sorted(list(map(int, input().split())))
	b, c = [0]*n, [0]*n
	b[0::2], b[1::2] = a[:(n+1)//2], a[(n+1)//2:]
	c[0::2], c[1::2] = a[n//2:], a[:n//2]
	if check(b): print(*b)
	elif check(c): print(*c)
	else: print(-1)
``

</details>
