# Can You Reach The End

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECHEND |
| Difficulty Rating | 2095 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [RECHEND](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/RECHEND) |

---

## Problem Statement

You are given a positive integer $N$. Consider a square grid of size $N \times N$, with rows numbered  $1$ to $N$ from top to bottom and columns numbered $1$ to $N$ from left to right. Initially you are at $(1,1)$ and you have to reach $(N,N)$. From a cell you can either move one cell to the right or one cell down (if possible). Formally, if you are at $(i,j)$, then you can either move to $(i+1,j)$ if $i \lt N$, or to $(i,j+1)$ if $j \lt N$.

There are exactly $N$ blocks in the grid, such that each row contains exactly one block and each column contains exactly one block. You can't move to a cell which contains a block. It is guaranteed that blocks will not placed in $(1,1)$ and $(N,N)$.

You have to find out whether you can reach $(N,N)$.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains $N$ - the size of the square grid.
- The $i$-th line of the next $N$ lines contains two integers $X_i$ and $Y_i$ indicating that $(X_i, Y_i)$ is the position of a block in the grid.

---

## Output Format

For each test case, if there exists a path from $(1,1)$ to $(N,N)$, output `YES`, otherwise output `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes` and `YES` will all be treated as identical).

---

## Constraints

- $1 \le T \le 1000$
- $2 \le N \le 10^6$
- $1 \le X_i,Y_i \le N$
- $(X_i, Y_i) \ne (1, 1)$ and $(X_i, Y_i) \ne (N, N)$ for all $1 \le i \le N$
- $X_i \ne X_j$ and $Y_i \ne Y_j$ for all $1 \le i \lt j \le N$
- Sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2
2 3
3 1
2
1 2
2 1
```

**Output**

```text
YES
NO
```

**Explanation**

- **Test case $1$:** We can follow the path $(1,1) \to (2,1) \to (2,2) \to (3,2) \to (3,3)$.

- **Test case $2$:** We can't move from the starting point, so it is impossible to reach $(N, N)$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RECHEND)

[Contest: Division 1](https://www.codechef.com/COOK134A/problems/RECHEND)

[Contest: Division 2](https://www.codechef.com/COOK134B/problems/RECHEND)

[Contest: Division 3](https://www.codechef.com/COOK134C/problems/RECHEND)

***Author:*** [Sandeep V](https://www.codechef.com/users/dazlersan1)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There is a square grid of size N\times N, where exactly N cells are blocked. Further, they are distributed such that there is exactly one blocked cell in every row and every column.

Is it possible to move from \left(1, 1\right) to \left(N, N\right) by taking only rightward and downward steps, without passing through any blocked cell?

#
[](#quick-explanation-5)QUICK EXPLANATION:

The answer is `Yes` if and only if no diagonal (with constant i+j) is filled with blocked cells.

#
[](#explanation-6)EXPLANATION:

Drawing out a few examples on paper will likely give you the idea to check whether a diagonal is completely blocked.

This is both a necessary and a sufficient condition for a path to exist.

For convenience, the diagonal consisting of cells \left(i, j\right) such that i + j = c will be called diagonal c.

Proof of necessity

Suppose there is a path from \left(1, 1\right) to \left(N, N\right).

\left(1, 1\right) lies on diagonal 2, and each step we take, whether rightward or downward, moves us from diagonal i to diagonal i+1. As a result, we pass through exactly one square in each diagonal.

The only way such a path can exist is if every diagonal has at least one unblocked cell, making this a necessary condition.

Proof of sufficiency

Suppose that every diagonal has at least one unblocked cell. We will construct a path from \left(1, 1\right) to \left(N, N\right).

There is exactly one blocked cell in the first row - let it be \left(1, x\right) where x > 1. Let k be the smallest integer such that cells \left(1, x\right), \left(2, x-1\right), \dots, \left(k, x+1-k\right) are all blocked but cell \left(k+1, x-k\right) is not blocked.

This diagonal has at least one unblocked cell by assumption, so we know for a fact that k < x, i.e, x - k > 0.

Now do the following:

Move right from \left(1, 1\right) to \left(1, x-k\right). All these cells are not blocked because the only blocked cell in row 1 is in column x.

Then, move down to \left(k+1, x-k\right). Again, all these cells are unblocked because the cells blocked in rows 2, 3, \dots, k occur in columns after x-k, and \left(k+1, x-k\right) is unblocked by assumption.

Next, move right to \left(k+1, x\right). The cells along this path are unblocked because the blocked cells in each of these columns are above the path.

Finally, move down to \left(x, x\right).

We are now at position (x, x). Further, note that cells (x, x), (x+1, x), \dots, (N, x) are all unblocked because (1, x) is blocked.

We can now move from (x, x) to (N, N) via a similar constructive process.

The last row has exactly one blocked cell - let this be (N, y). Clearly, y = x is not possible.

- If y < x, we can simply move down to (N, x) and then right to (N, N), with all intermediate cells being unblocked.

- Suppose y > x. Let r be the smallest integer such that cells \left(N, y\right), \left(N-1, y+1\right), \dots, \left(N-r, y+r\right) are all blocked but cell \left(N-r-1, y+r+1\right) is not blocked.

Since all diagonals of the grid have an unblocked cell, such a r does exist, and will be < N-y.

Now do the following:

Move down to (N-r-1, x).

Next, move right to (N-r-1, y+r+1) - all intermediate cells are unblocked because the blocked cells in these columns are strictly below this path.

Next, move down to (N, y+r+1) - all intermediate cells are unblocked because the blocked cells in these rows are strictly to the left of this path.

Finally, move right to (N, N) and we are done.

All that remains is to check whether some diagonal is indeed blocked. A simple way to do this is to maintain a frequency table of x+y for every cell \left(x, y\right) in the input, and then iterate over every diagonal x+y and check whether freq[x+y] equals the length of that diagonal.

#
[](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(N\log N)  or \mathcal{O}(N) per test.

#
[](#code-8)CODE:

Setter (Python)
``import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    c=dict()
    for i in range(n):
        a,b=map(int,input().split())
        if(a+b in c):
            c[a+b]+=1
        else:
            c[a+b]=1
    fl=1
    for i in range(2,n+1):
        if(i in c):
            if(c[i]==i-1):
                fl=0
                break
    j=n+1
    k=n
    for i in range(n-1):
        if(j in c):
            if(c[j]==k):
                fl=0
                break
        j+=1
        k-=1
        #print(j,k)
    #print(c)
    if(fl==0):
        print("NO")
    else:
        print("YES")
``

Tester (Kotlin)
``import java.io.BufferedInputStream

fun main(omkar: Array<String>) {
    val jin = FastScanner()
    repeat(jin.nextInt(1000)) {
        val n = jin.nextInt(1000000)
        val ys = IntArray(n + 1)
        repeat(n) {
            val x = jin.nextInt(n, false)
            val y = jin.nextInt(n)
            ys[x] = y
        }
        if (ys.toSet().size != n + 1) {
            throw IllegalArgumentException("not all distinct y")
        }
        if ((1..n).any { ys[it] == 0 }) {
            throw IllegalArgumentException("not all distinct x")
        }
        if (ys[1] == 1 || ys[n] == n) {
            throw IllegalArgumentException("start and/or finish blocked")
        }
        println(if ((1..ys[1]).all { it + ys[it] == 1 + ys[1] } || (ys[n]..n).all { it + ys[it] == n + ys[n] }) "nO" else "yEs")
    }
}

class FastScanner {
    private val BS = 1 shl 16
    private val NC = 0.toChar()
    private val buf = ByteArray(BS)
    private var bId = 0
    private var size = 0
    private var c = NC
    private var `in`: BufferedInputStream? = null

    constructor() {
        `in` = BufferedInputStream(System.`in`, BS)
    }

    private val char: Char
        private get() {
            while (bId == size) {
                size = try {
                    `in`!!.read(buf)
                } catch (e: Exception) {
                    return NC
                }
                if (size == -1) return NC
                bId = 0
            }
            return buf[bId++].toChar()
        }

    fun nextInt(): Int {
        var neg = false
        if (c == NC) c = char
        while (c < '0' || c > '9') {
            if (c == '-') neg = true
            c = char
        }
        var res = 0
        while (c >= '0' && c <= '9') {
            res = (res shl 3) + (res shl 1) + (c - '0')
            c = char
        }
        return if (neg) -res else res
    }

    fun nextInt(unused1: Int, unused2: Boolean = true) = nextInt()

    fun nextInt(unused1: Int, unused2: Int, unused3: Boolean = true) = nextInt()
}
``

Editorialist (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,mmx,avx,avx2")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
    ios::sync_with_stdio(0); cin.tie(0);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<array<int, 2>> v(n);
        for (auto &[x, y] : v)
            cin >> x >> y;
        sort(begin(v), end(v));
        int lst = 0;
        for (int i = 1; i < n; ++i) {
            if (v[i][1] == v[i-1][1] - 1) lst = i;
            else break;
        }
        if (v[lst][1] == 1) {
            cout << "No\n";
            continue;
        }

        reverse(begin(v), end(v));
        lst = 0;
        for (int i = 1; i < n; ++i) {
            if (v[i][1] == v[i-1][1] + 1) lst = i;
            else break;
        }
        if (v[lst][1] == n) {
            cout << "No\n";
            continue;
        }
        cout << "Yes\n";
    }
}
``

</details>
