# Ultimate Fencing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KEEPOUT |
| Difficulty Rating | 2347 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [KEEPOUT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/KEEPOUT) |

---

## Problem Statement

You've recently come into possession of a rather nice piece of land, on which you'd like to build a house.
Unfortunately, one side of this land borders a forest, and you really don't want any dangerous animals showing up at your doorstep. Naturally, you decide to build a fence to keep them out.
Building a fence requires you to place fence posts first.

The border can be thought of as a segment of length $M$ on the $x$-axis, with its endpoints at $x = 0$ and $x = M$. Initially, there are posts only at these two endpoints.

You will place $N$ posts at **distinct** points along this border, one at a time. The $i$-th of them will be placed at point $x = A_i$.
After each post is placed, you'd like to know: what's the longest *empty* segment (i.e, a segment without any posts) along the border?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of fence posts and the length of the border.
    - The second line will contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the positions at which the posts are placed, in order.

---

## Output Format

For each test case, output $N$ space-separated integers on a new line. The $i$-th of them should denote the length of the longest empty segment after the first $i$ posts have been placed.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $N \lt M$
- $2 \leq M \leq 10^9$
- $1 \leq A_i \lt M$
- All the $A_i$ values are **distinct**.
- The sum of $N$ across all tests won't exceed $2\cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2 5
2 4
4 5
4 3 2 1
4 25
10 12 5 19
```

**Output**

```text
3 2
4 3 2 1
15 13 13 7
```

**Explanation**

**Test case $1$:** The posts are placed as follows:
- Initially, the posts are at $[0, 5]$.
- The first post is placed at $x = 2$. The posts are at positions $[0, 2, 5]$.
The largest empty segment is between points $2$ and $5$, with a length of $3$.
- The second post is placed at $x = 4$. The posts are at positions $[0, 2, 4, 5]$.
The largest empty segment is of length $2$, between $2$ and $4$ (and also between $0$ and $2$).

**Test case $2$:** The posts are placed as follows:
- The first one is at $x = 4$, so the posts are at $[0, 4, 5]$. The longest empty segment is between $0$ and $4$, of length $4$.
- The second post is at $x = 3$, so the posts are at $[0, 3, 4, 5]$. The longest empty segment is between $0$ and $3$, of length $3$.
- The third post is at $x = 2$. The longest empty segment is between $0$ and $2$, of length $2$.
- The fourth post is at $x = 1$. The longest empty segment is of length $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5
2 4
```

**Output for this case**

```text
3 2
```



#### Test case 2

**Input for this case**

```text
4 5
4 3 2 1
```

**Output for this case**

```text
4 3 2 1
```



#### Test case 3

**Input for this case**

```text
4 25
10 12 5 19
```

**Output for this case**

```text
15 13 13 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KEEPOUT)

[Contest: Division 1](https://www.codechef.com/SEP23A/problems/KEEPOUT)

[Contest: Division 2](https://www.codechef.com/SEP23B/problems/KEEPOUT)

[Contest: Division 3](https://www.codechef.com/SEP23C/problems/KEEPOUT)

[Contest: Division 4](https://www.codechef.com/SEP23D/problems/KEEPOUT)

***Author & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Binary search

# [](#problem-4)PROBLEM:

There is a line segment of length M.

N operations are performed on it - in the i-th operation, point A_i is marked.

After each operation, find the length of the longest segment without any marked points.

# [](#explanation-5)EXPLANATION:

This problem was intended to be somewhat of an introduction to C++ STL (or whatever your language’s library is) for newer participants; though it is still possible to solve without libraries, if you’d like to do so.

The core idea behind solving the problem is that the empty segments can be directly maintained, because each time we mark a new point, one empty segment breaks into two smaller ones; for a net addition of one segment.

After each such break, notice that the (multi)set of lengths of the empty segments doesn’t change much either - in particular, one length disappears and two lengths appear.

So, solving the problem requires us to be able to support the following quickly:

- Find which empty segment needs to be split into two

- Find out which length disappears, and which ones appear

- Find out the maximum among the remaining lengths

In particular, we need a data structure that supports quick insertion/deletion/getting the maximum, which is what a set does.

This leads to several different ways to implement the problem, some simpler than others.

Below are a couple of them.

Approach 1

The problem can be solved “directly”, by breaking the segments as mentioned earlier.

To do this, let’s maintain a set S of existing posts (initially contains 0 and M), and another set L of the lengths of empty segments (initially contains only M).

Then, for each i from 1 to N:

- First, we need to find which empty segment contains A_i.

To do this, we use binary search.

Let x be the largest element of S that’s \lt A_i, and y be the smallest element of S that’s \gt A_i. Both x and y can be found by binary searching on S (for example, via the `lower_bound` and `upper_bound` functions in C++)

- Now, we know A_i lies in the segment [x, y], and placing a pole there will break it into segments [x, A_i] and [A_i, y].

- So, we can delete the length (y-x) from L, and insert the lengths (A_i - x) and (y - A_i) instead.

- Finally, the maximum element of L is the current answer.

Each of these operations can be done in \mathcal{O}(\log N) using a sorted set (`std::set` in C++, `TreeSet` in Java).

Note that L can contain duplicate elements because lengths may occur more than once; so you should use a datastructure that allows for duplicates such as `std::multiset`.

Approach 2 (slightly longer but simpler and faster)

Another way to implement this is to look at the process in *reverse*.

Instead of adding in posts, let’s start with all of them already there, and remove posts instead.

Notice that going this way, the maximum empty length can only *increase*: in particular, when we remove a pole, the newly created larger segment is the only potential new maximum.

This allows for a simpler implementation, as follows:

- Let S be a set containing all the remaining poles.

Initially, it contains all the A_i, along with 0 and M.

Also keep a variable \text{ans}, denoting the answer. Initialize it to the maximum adjacent difference between elements of S.

- Then, for each i from N to 1, do the following:

- Locate A_i in S using a binary search. Also find the nearest remaining poles to its left and right; say x and y.

When A_i is removed, the new empty segment created has length y-x.

- Set \text{ans} = \max(\text{ans}, y-x), and delete A_i from S.

This way, we easily find all the answers in reverse.

This implementation is much simpler to reason about, and has a lower chance of implementation errors creeping in because you need one less data structure. It also runs a bit faster than the first approach.

The tradeoff is that it’s a bit longer to code than approach 1.

Some languages, such as Python, unfortunately don’t have a builtin data structure that supports the required operations, so you’ll have to code one yourself - for example the [SortedList](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SortedList.py) found here.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++, approach 1)
``// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include "bits/stdc++.h"
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
    ios::sync_with_stdio(false); cin.tie(0);

    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        set<int> posts = {0, m};
        multiset<int> lengths = {m};
        for (int i = 0; i < n; ++i) {
            int x; cin >> x;

            auto it = posts.lower_bound(x);
            int L = *prev(it), R = *it;
            lengths.erase(lengths.find(R-L));
            lengths.insert(x-L);
            lengths.insert(R-x);
            posts.insert(x);
            cout << *lengths.rbegin() << ' ';
        }
        cout << '\n';
    }
}
``

Author's code (C++, approach 2)
``// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include "bits/stdc++.h"
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
    ios::sync_with_stdio(false); cin.tie(0);

    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        vector<int> a(n), ans(n);
        for (int &x : a) cin >> x;
        set<int> s(begin(a), end(a));
        s.insert(0); s.insert(m);
        int mxdif = 0;
        for (auto it = begin(s); it != end(s); ++it) {
            if (next(it) == end(s)) break;
            mxdif = max(mxdif, *next(it) - *it);
        }

        for (int i = n-1; i >= 0; --i) {
            ans[i] = mxdif;
            auto it = s.find(a[i]);
            int L = *prev(it), R = *next(it);
            mxdif = max(mxdif, R-L);
            s.erase(a[i]);
        }
        for (int x : ans) cout << x << ' ';
        cout << '\n';
    }
}
``

</details>
