# No sequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOSEQ |
| Difficulty Rating | 2031 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [NOSEQ](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/NOSEQ) |

---

## Problem Statement

Alice gave Bob $3$ integers $N, K,$ and $S$. Help Bob find an $S$-good sequence.

A sequence $B$ of length $N$ is called $S$-good if the following conditions are met:
- $B_i \in \{-1, 0, 1\}$ for each $1 \leq i \leq N$
- $\sum_{i=1}^N B_i\cdot K^{i-1} = S$

If there are multiple $S$-good sequences, print **any** of them.
**If no $S$-good sequence exists, print $-2$.**

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing three space-separated integers — $N, K, $ and $S$.

---

## Output Format

For each test case:
- If no $S$-good sequence exists, print $-2$.
- Otherwise, output $N$ space-separated integers denoting the $S$-good sequence.

If multiple $S$-good sequences exist, you may print any of them.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 100$
- $2 \leq K \leq 100$
- $1 \leq S \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 15
3 6 36
5 5 7
```

**Output**

```text
1 1 1 1
0 0 1
-2
```

**Explanation**

**Test case $1$:** We have $B = [1,1,1,1]$ and $S = 15$
$\sum_{i=1}^N B_i\cdot K^{i-1} = 1\cdot 1 + 2\cdot 1 + 4\cdot 1 + 8\cdot 1 = 15$, hence $B$ is an $S$-good sequence.

**Test case $2$:** We have $B = [0, 0, 1]$ and $S = 36$. $6^2 = 36$ so clearly $B$ is $S$-good.

**Test case $3$:** No $S$-good sequence of length $5$ exists.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 15
```

**Output for this case**

```text
1 1 1 1
```



#### Test case 2

**Input for this case**

```text
3 6 36
```

**Output for this case**

```text
0 0 1
```



#### Test case 3

**Input for this case**

```text
5 5 7
```

**Output for this case**

```text
-2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NOSEQ)

[Contest: Division 1](https://www.codechef.com/START72A/problems/NOSEQ)

[Contest: Division 2](https://www.codechef.com/START72B/problems/NOSEQ)

[Contest: Division 3](https://www.codechef.com/START72C/problems/NOSEQ)

[Contest: Division 4](https://www.codechef.com/START72D/problems/NOSEQ)

***Author:*** [still_me](https://www.codechef.com/users/still_me)

***Testers:*** [the_hyp0cr1t3](https://www.codechef.com/users/the_hyp0cr1t3), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N, K, S, find a sequence B = [B_1, \ldots, B_N] such that:

- B_i \in \{-1, 0, 1\}

- \sum_{i=1}^N B_i\cdot K^{i-1} = S

#
[](#explanation-5)EXPLANATION:

Let’s try to build B from its first position to its last.

Notice that we can rewrite \sum_{i=1}^N B_i\cdot K^{i-1} = S as S = B_1 + \sum_{i=2}^N B_i\cdot K^{i-1} = B_1 + K\cdot x for some integer x.

So, B_1 \equiv S \pmod{K}.

Notice that this (almost) uniquely determines what B_1 should be:

- If S \equiv 0 \pmod{K}, choose B_1 = 0

- If S \equiv 1 \pmod{K}, choose B_1 = 1

- If S \equiv -1 \pmod{K}, choose B_1 = -1

- If none of the above hold, no S-good sequence can exist.

The only edge case here is when K = 2, in which case 1 and -1 are equivalent and you can choose either one.

Now that we know B_1, let’s try to find B_2.

A bit of simple algebra tells us that \displaystyle S = \sum_{i=1}^N B_i\cdot K^{i-1} is equivalent to \displaystyle \frac{S-B_1}{K} = \sum_{i=2}^N B_i\cdot K^{i-2}.

Notice that the last equation is simply asking us to compute a good array for \frac{S-B_1}{K} of length N-1.

So, all we need to do is replace S with \frac{S-B_1}{K} and repeat the above process.

This allows us to compute the values of every B_i.

At the end of the process, if S \neq 0 or we couldn’t compute some B_i, the answer is -2; otherwise print the B array computed.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``//	Code by Sahil Tiwari (still_me)

#include<bits/stdc++.h>
#define still_me main
#define endl "\n"
#define int long long int
#define all(a) (a).begin() , (a).end()
#define print(a) for(auto TEMPORARY: a) cout<<TEMPORARY<<" ";cout<<endl;
#define tt int TESTCASE;cin>>TESTCASE;while(TESTCASE--)
#define arrin(a,n) for(int INPUT=0;INPUT<n;INPUT++)cin>>a[INPUT]

using namespace std;
const int mod = 1e18;
const int inf = 1e18;

long long power(long long a , long long b , long long mod){
    if(b==0)
        return 1;
    long long res = power(a , b/2 , mod);
    res = res*res % mod;
    if(b%2)
        res = res*a % mod;
    return res;
}
int t = 0;

void solve() {
    t++;
    int n , k , s;
    cin>>n>>k>>s;
    vector<int> b(n);
    int i = 0;
    bool flag = 1;
    while(i < min(n , 61ll)) {
        if(s % k == 0) {
            s /= k;
        }
        else if((s-1) % k == 0) {
            s = (s-1ll) / k;
            b[i] = 1;
        }
        else if((s+1) % k == 0) {
            s = (s+1ll) / k;
            b[i] = -1;
        }
        else {
            flag = 0;
            // assert(false);
            // cerr<<t<<endl;
            break;
        }
        i++;
    }
    // cout<<s<<endl;
    if(!flag || s != 0) {
        cout<<"-2"<<endl;
    }
    else {
        print(b);
    }
}

signed still_me()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    // freopen("3.in" , "r" , stdin);
    // freopen("3.out" , "w" , stdout);
    tt{
        solve();
    }
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k, s = map(int, input().split())
    ans = []
    for i in range(n):
        if s%k == 0:
            ans.append(0)
            s //= k
        elif s%k == 1:
            ans.append(1)
            s = (s-1)//k
        elif s%k == k-1:
            ans.append(-1)
            s = (s+1)//k
    if s > 0: print(-2)
    else: print(*ans)
``

</details>
