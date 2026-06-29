# Mountain

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOUNTAIN |
| Difficulty Rating | 2047 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MOUNTAIN](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MOUNTAIN) |

---

## Problem Statement

You're given an $N\times M$ matrix $A$, where $A_{(i,j)}=i$.

A **mountain** in the matrix is defined as a set of cells and is expressed using $K+2$ integers: $P, K, L_1, L_2, \ldots, L_K$.
This translates to: from the $(P+i-1)^{th}$ row, select the first $L_i$ cells $(1 \leq i \leq K)$ in the row. Refer samples for more clarity.

Your task is to answer $Q$ queries. For the $i^{th}$ query:
- You are given an integer $S_i$ and you need to find a **mountain** with sum $S_i$.

---

## Input Format

- The first line contains three space-separated integers $N$, $M$, and $Q$, the dimensions of the matrix and the number of queries.
- The second line contains $Q$ space-separated integers $S_1,S_2,\ldots,S_Q$, denoting each query.

---

## Output Format

- For each query, if no possible mountain with given sum exists, output $-1$.
- Otherwise, output two lines:
   -  The first line contains two space-separated integers $P$,$K$ $(1 \leq P \leq N,P+K-1 \leq N)$;
   -  The second line contains $K$ space-separated integers $L_1,L_2,\ldots,L_K(1 \leq L_i \leq M)$.

If multiple mountains satisfy the condition, you may print any.

---

## Constraints

- $2 \leq N,M \leq 3\cdot 10^4$
- $1 \leq Q \leq 10$
- $1 \leq S_i \leq M\cdot N\cdot \frac{(N+1)}{2}$

---

## Examples

**Example 1**

**Input**

```text
5 4 4
20 36 1 60
```

**Output**

```text
2 3
2 4 1
1 5
3 1 4 1 3
1 1
1
1 5
4 4 4 4 4
```

**Explanation**

**Query $1$:** A possible mountain that satisfies the condition is highlighted below:

Here, $P = 2$ and $K = 3$ and we are selecting $2, 4,$ and $1$ cells from the second, third, and fourth row respectively. The sum of the highlighted cells is $20$.

**Query $2$:** A possible mountain that satisfies the condition is highlighted below:

Here, $P = 1$ and $K = 5$ and we are selecting $3, 1, 4, 1,$ and $3$ cells from the first, second, third, fourth and fifth rows respectively. The sum of the highlighted cells is $36$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MOUNTAIN)

[Contest: Division 1](https://www.codechef.com/START79A/problems/MOUNTAIN)

[Contest: Division 2](https://www.codechef.com/START79B/problems/MOUNTAIN)

[Contest: Division 3](https://www.codechef.com/START79C/problems/MOUNTAIN)

[Contest: Division 4](https://www.codechef.com/START79D/problems/MOUNTAIN)

***Author:*** [wuhudsm](https://www.codechef.com/users/wuhudsm)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Greedy algorithms

#
[](#problem-4)PROBLEM:

There’s an N\times M grid, with A_{i, j} = i.

A mountain is a set of integers P, K, L_1, L_2, \ldots, L_K, saying that you pick the first L_i integers from row (P+i-1).

Answer Q queries of the following form:

- Given S, find a mountain with sum S.

#
[](#explanation-5)EXPLANATION:

This task can be solved greedily.

Suppose we want a sum of S.

Let’s go from the first row to the last, each time taking as many numbers as possible till we first exceed the sum.

As soon as we exceed it, we can throw out (at most) one number to attain the exact sum we want.

That is, initialize a variable \text{sum} = 0 and set P = 1 since we’re starting from the first row.

Then, for each i from 1 to N:

- If \text{sum} + i\cdot M \lt S, take all M elements from this row and continue. In other words, set L_i = M.

- Otherwise, let j be the smallest integer such that \text{sum} + i\cdot j \geq S. Take these j numbers into the sum, i.e, set L_i = j.

- Now, if \text{sum} = S we’re done.

- Otherwise, remove one element from the row (\text{sum} - S), i.e, decrement L_{\text{sum} - S} by one. Since we took elements in order from smallest to largest, it’s guaranteed that the value of \text{sum} - S is no larger than i, so this is always possible.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) or \mathcal{O}(N+M) per query.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
typedef double db;
typedef long long ll;
typedef unsigned long long ull;
const int N=1000010;
const int LOGN=28;
const ll  TMD=0;
const ll  INF=2147483647;
int n,m,q;
int p[N];
pair<ll,ll> qr[N];
vector<int> ans[N];

int main()
{
	scanf("%d%d%d",&n,&m,&q);
	for(int i=1;i<=q;i++)
	{
		ll  t,sum;
		int L=0,R=n+1,M,p;
		scanf("%lld",&t);
		while(L+1!=R)
		{
			M=(L+R)>>1;
			if((ll)m*(ll)M*(M+1)/2<t) L=M;
			else R=M;
		}
		p=R;sum=(ll)m*(ll)L*(L+1)/2;
		for(int j=1;j<=m;j++)
		{
			sum+=p;
			if(sum>=t)
			{
				printf("%d %d\n",1,p);
				for(int k=1;k<p;k++) printf("%d ",k==sum-t?m-1:m);
				printf("%d\n",j);
				break;
			}
		}
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
        // cerr << res << endl;
        return res;
    }

    string readString(int minl, int maxl, const string &pattern = "") {
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
    int n = in.readInt(2, 30000);
    in.readSpace();
    int m = in.readInt(2, 30000);
    in.readSpace();
    int q = in.readInt(1, 10);
    in.readEoln();
    vector<long long> s(q);
    for (int i = 0; i < q; i++) {
        s[i] = in.readLong(1, m * 1LL * n * (n + 1) / 2);
        (i == q - 1 ? in.readEoln() : in.readSpace());
    }
    for (auto t : s) {
        long long now = 0;
        vector<int> l;
        for (int i = 0; i < n; i++) {
            if (now + (i + 1) <= t) {
                now += i + 1;
                l.emplace_back(1);
            } else {
                break;
            }
        }
        for (int i = (int) l.size() - 1; i >= 0; i--) {
            if (now + (i + 1) * 1LL * (m - 1) <= t) {
                l[i] += m - 1;
                now += (i + 1) * 1LL * (m - 1);
            }
            while (now + (i + 1) <= t && l[i] < m) {
                l[i]++;
                now += i + 1;
            }
        }
        cout << 1 << " " << l.size() << '\n';
        for (int i = 0; i < (int) l.size(); i++) {
            cout << l[i] << " \n"[i == (int) l.size() - 1];
        }
    }
    return 0;
}
``

Editorialist's code (Python)
``n, m, q = map(int, input().split())
queries = list(map(int, input().split()))
for s in queries:
    cursum = 0
    row = 1
    while True:
        if cursum + m*row < s:
            cursum += m*row
            row += 1
        else:
            take = (s - cursum + row-1) // row
            cursum += row * take
            print(1, row)
            for i in range(1, row):
                if cursum - i == s: print(m-1, end = ' ')
                else: print(m, end = ' ')
            print(take)
            break
``

</details>
