# Symmetric Swaps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SYMARRSWAP |
| Difficulty Rating | 2041 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SYMARRSWAP](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SYMARRSWAP) |

---

## Problem Statement

Chef has two arrays $A$ and $B$ of the same size $N$.

In one operation, Chef can:
- Choose an index $i$ $(1 \leq i \leq N)$ and swap the elements $A_i$ and $B_i$.

Chef came up with a task to find the **minimum** possible value of **($A_{max} - A_{min}$)** after performing the swap operation any (possibly zero) number of times.

Since Chef is busy, can you help him solve this task?

Note that $A_{max}$ and $A_{min}$ denote the maximum and minimum elements of the array $A$ respectively.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains one integer $N$ — the number of elements in each array.
    - The second line consists of $N$ space-separated integers $A_1, A_2,\ldots ,A_N$ denoting the elements of the array $A$.
    - The third line consists of $N$ space-separated integers $B_1, B_2, \ldots ,B_N$ denoting the elements of the array $B$.

---

## Output Format

For each test case, output on a new line, the **minimum** possible value of **($A_{max} - A_{min}$)** in the array $A$ after doing swap operation any number of times.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
1 2
2 1
3
1 5 3
2 3 1
4
4 2 5 1
5 3 4 1
```

**Output**

```text
0
1
3
```

**Explanation**

**Test case $1$:** Chef can make the following operations:
- Operation $1$: Choose $i=1$ and swap $A_1$ with $B_1$.

By doing the above operations, array $A$ becomes $[2, 2]$. Here $(A_{max} - A_{min}) = 0$. It can be shown that this is the minimum value possible.

**Test case $2$:** Chef can make the following operations:
- Operation $1$: Choose $i=1$ and swap $A_1$ with $B_1$.
- Operation $2$: Choose $i=2$ and swap $A_2$ with $B_2$.

By doing the above operations, array $A$ becomes $[2, 3, 3]$. Here $(A_{max} - A_{min}) = 1$. It can be shown that this is the minimum value possible.

**Test case $3$:** Chef can make the following operations:
- Operation $1$: Choose $i=2$ and swap $A_2$ with $B_2$.
- Operation $2$: Choose $i=3$ and swap $A_3$ with $B_3$.

By doing the above operations, array $A$ becomes $[4, 3, 4, 1]$. Here $(A_{max} - A_{min}) = 3$. It can be shown that this is the minimum value possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
2 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3
1 5 3
2 3 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
4 2 5 1
5 3 4 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SYMARRSWAP)

[Contest: Division 1](https://www.codechef.com/JAN231A/problems/SYMARRSWAP)

[Contest: Division 2](https://www.codechef.com/JAN231B/problems/SYMARRSWAP)

[Contest: Division 3](https://www.codechef.com/JAN231C/problems/SYMARRSWAP)

[Contest: Division 4](https://www.codechef.com/JAN231D/problems/SYMARRSWAP)

***Author:*** [rkyouwill](https://www.codechef.com/users/rkyouwill)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Sorting, two pointers

#
[](#problem-4)PROBLEM:

You have two arrays A and B. In one move, you can swap A_i and B_i for some 1 \leq i \leq N.

Find the minimum possible value of \max(A) - \min(A) that you can attain.

#
[](#explanation-5)EXPLANATION:

Unlike the [easier version](https://www.codechef.com/problems/ARRSWAP) of this problem, it’s no longer possible to put any N elements we want into A.

Instead, let’s once again consider the *sorted* array C of length 2N consisting of every element from A and B.

Suppose we fix C_L to be the smallest element we choose. We’ll try to find the optimal maximum element for C_L.

Suppose we also fix C_R to be the maximum element (where L \lt R). Can you say anything about the subarray [C_L, C_{L+1}, \ldots, C_R]?

Answer

We want to pick N elements from this subarray to put into A.

Notice that for any N elements we put into A, there must be one element corresponding to each index (since the i-th position can only contain A_i or B_i).

So, suppose we also knew an array \text{ind} of length 2N denoting which index each element of C belongs to, i.e, \text{ind}_i = j means that A_j = C_i or B_j = C_i.

Then, we can choose C_L to be the minimum and C_R to be the maximum if and only if [\text{ind}_L, \text{ind}_{L+1}, \ldots, \text{ind}_R] contains every integer from 1 to N at least once.

Computing the \text{ind} array is not hard: just make C an array of *pairs* of (value, index) and then sort it as usual.

The above discussion should tell you how to find an optimal R in, at the very least, \mathcal{O}(N) time for a fixed L:

Iterate R starting from L, and stop the first time the \text{ind} array contains every integer from 1 to N.

This gives a solution in \mathcal{O}(N^2), which is too slow for our purposes.

To improve it, let’s reuse some computations.

Let f(L) denote the optimal R-value for when L is the left endpoint.

Then, it’s not hard to see that f(L)\leq f(L+1).

Proof

Let R_1 = f(L) and R_2 = f(L+1).

We know [L+1, R_2] is the smallest subarray starting at L+1 containing all N indices.

In particular, this means the subarray [L, R_2] also contains all N indices.

But, [L, R_1] is the smallest subarray starting at L that contains all indices.

So, R_1 \leq R_2 must hold, which proves our claim.

This allows us to apply a 2-pointer approach:

- Iterate L from 1 to 2N. Also keep a variable R, initially equal to 1.

- For a fixed L, increase R till the subarray [L, R] contains all N indices.

- If no such R exists, stop.

- Otherwise, set \text{ans} = \min(\text{ans}, C_R - C_L)

- Then, increase L by 1 and continue. Note that R remains unchanged.

This way, both L and R only increase, each making 2N steps at most.

Note that this requires us to maintain the set of available indices at each step.

This can be done using an array ct of size N, where ct[i] denotes the number of times we have index i.

Also keep a variable denoting the number of non-zero elements of ct.

Then,

- When moving R to R+1, increment ct[\text{ind}_{R+1}] by 1.

- When moving L to L+1, decrement ct[\text{ind}_{L}] by 1.

- At each step, don’t forget to update the number of non-zero elements.

This gives us a solution in \mathcal{O}(N) after sorting.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
#define f first
#define se second
#define endl "\n"
#define pb push_back
#define ll long long int
#define pi pair<int,int>
#define all(st) st.begin(),st.end()
#define rep(i,l,r) for(int i=l;i<r;i++)
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
    	int n;
    	cin>>n;
    	vector<int> a(n),b(n);
    	rep(i,0,n) cin>>a[i];
    	rep(i,0,n) cin>>b[i];
    	vector<pi> c;
    	rep(i,0,n) c.pb({a[i],i}),c.pb({b[i],i});
    	sort(all(c));
    	vector<int> freq(n);
    	int ans=1e9,unique=0,l=0,r=0;
    	while(r<2*n){
    		freq[c[r].se]++;
    		if(freq[c[r].se]==1) unique++;
    		if(unique==n){
    			while(unique==n){
    				ans=min(ans,c[r].f-c[l].f);
    				freq[c[l].se]--;
    				if(freq[c[l].se]==0) unique--;
    				l++;
    			}
    		}
    		r++;
    	}
    	cout<<ans<<endl;
    }
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct input_checker {
    string buffer;
    int pos;

    const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const string number = "0123456789";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lower = "abcdefghijklmnopqrstuvwxyz";

    input_checker() {
        pos = 0;
        while (true) {
            int c = cin.get();
            if (c == -1) {
                break;
            }
            buffer.push_back((char) c);
        }
    }

    int nextDelimiter() {
        int now = pos;
        while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
            now++;
        }
        return now;
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        int nxt = nextDelimiter();
        string res;
        while (pos < nxt) {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int minl, int maxl, const string& pattern = "") {
        assert(minl <= maxl);
        string res = readOne();
        assert(minl <= (int) res.size());
        assert((int) res.size() <= maxl);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int minv, int maxv) {
        assert(minv <= maxv);
        int res = stoi(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    long long readLong(long long minv, long long maxv) {
        assert(minv <= maxv);
        long long res = stoll(readOne());
        assert(minv <= res);
        assert(res <= maxv);
        return res;
    }

    void readSpace() {
        assert((int) buffer.size() > pos);
        assert(buffer[pos] == ' ');
        pos++;
    }

    void readEoln() {
        assert((int) buffer.size() > pos);
        if (buffer[pos] != '\n') {
            cerr << int(buffer[pos]) << endl;
        }
        assert(buffer[pos] == '\n');
        pos++;
    }

    void readEof() {
        assert((int) buffer.size() == pos);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    input_checker in;
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 2e5);
        sn += n;
        in.readEoln();
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            a[i] = in.readInt(1, 1e9);
            (i == n - 1 ? in.readEoln() : in.readSpace());
        }
        vector<int> b(n);
        for (int i = 0; i < n; i++) {
            b[i] = in.readInt(1, 1e9);
            (i == n - 1 ? in.readEoln() : in.readSpace());
        }
        for (int i = 0; i < n; i++) {
            if (a[i] > b[i]) {
                swap(a[i], b[i]);
            }
        }
        multiset<int> st;
        for (int i = 0; i < n; i++) {
            st.emplace(a[i]);
        }
        int ans = *st.rbegin() - *st.begin();
        vector<pair<int, int>> c(n);
        for (int i = 0; i < n; i++) {
            c[i] = make_pair(a[i], b[i]);
        }
        sort(c.begin(), c.end());
        for (int i = 0; i < n; i++) {
            st.erase(st.find(c[i].first));
            st.emplace(c[i].second);
            ans = min(ans, *st.rbegin() - *st.begin());
        }
        cout << ans << '\n';
    }
    assert(sn <= 2e5);
    in.readEof();
    cerr << sn << endl;
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([min(a[i], b[i]), i])
        c.append([max(a[i], b[i]), i])
    c.sort()
    ans, ptr = 10**10, 0
    last = [-1]*n
    have = 0
    for i in range(2*n):
        val, id = c[i]
        if last[id] == -1: have += 1
        last[id] = i
        if have < n: continue
        while True:
            if last[c[ptr][1]] == ptr: break
            ptr += 1
        ans = min(ans, c[i][0] - c[ptr][0])
    print(ans)
``

</details>
