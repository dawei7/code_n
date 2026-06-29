# Angled Flip

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AFLIP |
| Difficulty Rating | 1835 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [AFLIP](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/AFLIP) |

---

## Problem Statement

You are given two $N \times M$ integer matrices $A$ and $B$. You are allowed to perform the following operation on $A$ as many times as you like (possibly, zero):

- Pick any square submatrix of $A$ and flip it about either its [main diagonal or its antidiagonal](https://en.wikipedia.org/wiki/Main_diagonal).

For example, suppose you choose the submatrix
$
\begin{bmatrix}
1 \;\;\;\; 2 \;\;\;\; 3 \\
4 \;\;\;\; 5 \;\;\;\; 6 \\
7 \;\;\;\; 8 \;\;\;\; 9
\end{bmatrix}
$
.

It can be converted into either
$
\begin{bmatrix}
1 \;\;\;\; 4 \;\;\;\; 7 \\
2 \;\;\;\; 5 \;\;\;\; 8 \\
3 \;\;\;\; 6 \;\;\;\; 9
\end{bmatrix}
$
by flipping about the main diagonal, or
$
\begin{bmatrix}
9 \;\;\;\; 6 \;\;\;\; 3 \\
8 \;\;\;\; 5 \;\;\;\; 2 \\
7 \;\;\;\; 4 \;\;\;\; 1
\end{bmatrix}
$
by flipping about the antidiagonal.

Is it possible to convert $A$ to $B$ by performing this operation several (possibly, zero) times?

**Note:** For the purposes of this problem, a submatrix of a matrix is the intersection of a **contiguous** segment of rows with a **contiguous** segment of columns.

For example, if
$ A =
\begin{bmatrix}
1 \;\;\;\; 2 \;\;\;\; 3 \\
4 \;\;\;\; 5 \;\;\;\; 6 \\
7 \;\;\;\; 8 \;\;\;\; 9
\end{bmatrix}
$
then $\begin{bmatrix} 2 \end{bmatrix}$, $\begin{bmatrix} 5 \;\;\;\; 6 \\ 8 \;\;\;\; 9 \end{bmatrix}$, and $\begin{bmatrix}1 \\ 4\end{bmatrix}$ are submatrices of $A$, while $\begin{bmatrix}1 \;\;\;\; 3 \\ 7 \;\;\;\; 9\end{bmatrix}$ *is not*.

A square submatrix is a submatrix with the same number of rows and columns.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of rows and columns of the matrices, respectively.
    - The next $N$ lines describe the matrix $A$. The $i$-th of these lines contains $M$ space-separated integers ― the values $A_{i, 1}, A_{i, 2}, \ldots, A_{i, M}$.
    - The next $N$ lines describe the matrix $B$. The $i$-th of these lines contains $M$ space-separated integers ― the values $B_{i, 1}, B_{i, 2}, \ldots, B_{i, M}$.

---

## Output Format

For each test case, print `YES` if its possible to convert $A$ to $B$, else print `NO`.

Each character of the output may be printed in either uppercase or lowercase. For example, the strings `YES`, `yes`, `yeS`, `YeS` will all be treated as identical.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N,M \leq 3 \cdot 10^5$
- $1 \leq A_{i, j},B_{i, j} \leq 10^9$
- The sum of $N\cdot M$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2 3
1 2 3
4 5 6
1 4 3
6 5 2
3 3
12 11 8
7 1 1
9 2 4
4 1 8
2 1 11
9 7 12
```

**Output**

```text
YES
YES
```

**Explanation**

**Test case $1$:** $A$ can be converted to $B$ as follows:
$$
\begin{bmatrix} 1 \;\;\;\; 2 \;\;\;\; 3 \\ 4 \;\;\;\; 5 \;\;\;\; 6 \end{bmatrix} \to \begin{bmatrix} 1 \;\;\;\; \textcolor{red}{6} \;\;\;\; \textcolor{red}{3} \\ 4 \;\;\;\; \textcolor{red}{5} \;\;\;\; \textcolor{red}{2} \end{bmatrix} \to \begin{bmatrix} \textcolor{red}{1} \;\;\;\; \textcolor{red}{4} \;\;\;\; 3 \\ \textcolor{red}{6} \;\;\;\; \textcolor{red}{5} \;\;\;\; 2 \end{bmatrix}
$$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
1 2 3
4 5 6
1 4 3
6 5 2
3 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
12 11 8
7 1 1
9 2 4
4 1 8
2 1 11
9 7 12
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AFLIP)

[Contest: Division 1](https://www.codechef.com/AUG221A/problems/AFLIP)

[Contest: Division 2](https://www.codechef.com/AUG221B/problems/AFLIP)

[Contest: Division 3](https://www.codechef.com/AUG221C/problems/AFLIP)

[Contest: Division 4](https://www.codechef.com/AUG221D/problems/AFLIP)

***Author:*** [Ashish Gangwar](https://www.codechef.com/users/kryptonix171)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Nishant Shah](https://www.codechef.com/users/nishant403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1835

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You have two N \times M matrices A and B. In one move, you can choose any square submatrix of A and flip it about one of its two longest diagonals. Can A be made equal to B?

#
[](#explanation-5)EXPLANATION:

Let’s first get one edge case out of the way: when N = 1 or M = 1, it is not possible to make any moves, so the answer is “YES” if A = B and “NO” otherwise.

A common idea when solving such types of problems (you are given a string/array/matrix, perform some operations on one of them, tell whether one structure can be converted to another) is to look for an *invariant*, that is, a property that doesn’t change under the operation.

Playing around with the operation a bit should allow you to see the following invariant:

- Let’s color the grid like a chessboard, with alternating black and white squares.

- Performing any operation only moves elements from white squares to white squares, and black squares to black squares.

This tells us the following:

- Let A_1 be the (multi)set of all elements on white squares of A, and A_2 be the similar multiset for black squares.

- Similarly, define B_1 and B_2 for B.

- Then, if it is at all possible to convert A to B, we must have A_1 = B_1 and A_2 = B_2.

Here’s the nice part: it turns out this condition is not only necessary, but also sufficient!

Proof

The key idea behind this is the fact that it’s always enough to use only 2\times 2 submatrices.

I’ll outline the details of the proof for the white squares below, the exact same reasoning can be applied to the black squares. This proof is easier to visualize than write out, so you are encouraged to try out a few examples on paper.

Let’s look only at the white squares. Suppose we choose a 2\times 2 submatrix and flip it. Note that in this submatrix, there are two white squares and two black squares, each of them forming one diagonal.

What can happen when we flip it?

There are only two cases, depending on which diagonal is flipped:

- The values on white squares remain the same, and the values on black squares are swapped; or

- The values on black squares remain the same, and the values on white squares are swapped

Let’s concentrate only on the second case. This tells us that, given a white square (i, j), we can swap its value with any one of (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1) (if the corresponding square is within the grid, of course) *without changing the values in any other squares*.

When N \gt 1 and M \gt 1, note that this means the set of white squares form a connected graph, whose edges are the swaps described above. Now, we are able to swap any two values on any two white squares by simply following paths along this graph.

Formally, to swap the values on (i_1, j_1) and (i_2, j_2)$:

- Find a path P from (i_1, j_1) to (i_2, j_2). Move the value from (i_1, j_1) to (i_2, j_2) along P

- The value originally on (i_2, j_2) is now on the penultimate node of P, say (i_3, j_3)

- Move this value to (i_1, j_1) by following the reverse of P

- Now note that other than (i_1, j_1) and (i_2, j_2) which have been swapped, the values on all other squares have not been changed.

This tells us that any permutation of values on the white squares is achievable.

Of course, a similar proof holds for the black squares, so the condition A_1 = B_1 and A_2 = B_2 is sufficient.

All that remains is to check the two conditions A_1 = B_1 and A_2 = B_2. This can be done in a variety of ways, for example

- Using maps/dictionaries

- Using sets/multisets

- Simply creating all 4 lists and comparing them after sorting

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(NM \log (N M)) per test case.

#
[](#code-7)CODE:

Setter's Code (C++)
``#include <bits/stdc++.h>
#define int long long int
#define debug cout<<"K"
#define mod 1000000007

using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        vector<vector<int>>a(n,vector <int>(m));
        vector<vector<int>>b(n,vector <int>(m));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            cin>>a[i][j];
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            cin>>b[i][j];
        }
        if(n==1||m==1)
        {
            if(a==b)
            cout<<"YES\n";
            else
            cout<<"NO\n";
            continue;
        }
        multiset<int>black1,black2,white1,white2;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if((i+j)%2==0)
                {
                    black1.insert(a[i][j]);
                    black2.insert(b[i][j]);
                }
                else
                {
                    white1.insert(a[i][j]);
                    white2.insert(b[i][j]);
                }
            }
        }
        if(black1==black2&&white1==white2)
        cout<<"YES\n";
        else
        cout<<"NO\n";

    }
    return 0;
}
``

Tester's Code (C++)
``/*
   - Check file formatting
   - Assert every constraint
   - Analyze testdata
*/

#include <bits/stdc++.h>
using namespace std;

/*
---------Input Checker(ref : https://pastebin.com/Vk8tczPu )-----------
*/

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true)
    {
        char g = getchar();
        if (g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if (cnt == 0)
            {
                fi = g - '0';
            }
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if (g == endd)
        {
            if (is_neg)
            {
                x = -x;
            }

            if (!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        }
        else
        {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while (true)
    {
        char g = getchar();
        assert(g != -1);
        if (g == endd)
        {
            break;
        }
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r)
{
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r)
{
    return readInt(l, r, '\n');
}

/*
-------------Main code starts here------------------------
*/

// Note here all the constants from constraints
const int MAX_T = 1e4;
const int MAX_N = 3e5;
const int SUM_NM = 3e5;
const int MAX_A = 1e9;

// Variables to measure some parameters on test-data
int max_nm = 0;
long long sum_nm = 0;
int yess = 0;
int nos = 0;

void solve()
{
    int n, m;
    n = readIntSp(1, MAX_N);
    m = readIntLn(1, MAX_N);

    max_nm = max(max_nm, n * m);
    sum_nm += n * m;
    assert(sum_nm <= SUM_NM);

    vector<vector<int>> A(n, vector<int>(m)), B(n, vector<int>(m));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (j != m - 1)
            {
                A[i][j] = readIntSp(1, MAX_A);
            }
            else
            {
                A[i][j] = readIntLn(1, MAX_A);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (j != m - 1)
            {
                B[i][j] = readIntSp(1, MAX_A);
            }
            else
            {
                B[i][j] = readIntLn(1, MAX_A);
            }
        }
    }

    multiset<int> sAL, sAR, sBL, sBR;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if ((i + j) % 2 == 0)
                sAL.insert(A[i][j]);
            else
                sAR.insert(A[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if ((i + j) % 2 == 0)
                sBL.insert(B[i][j]);
            else
                sBR.insert(B[i][j]);
        }
    }

    bool already_same = true;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (A[i][j] != B[i][j])
            {
                already_same = false;
            }
        }
    }

    if (already_same || (min(n, m) > 1 && sAL == sBL && sAR == sBR))
    {
        cout << "yEs\n";
        yess++;
    }
    else
    {
        cout << "nO\n";
        nos++;
    }
}

signed main()
{
    int t;
    t = readIntLn(1, MAX_T);

    for (int i = 1; i <= t; i++)
    {
        solve();
    }

    // Make sure there are no extra characters at the end of input
    assert(getchar() == -1);
    cerr << "SUCCESS\n";

    // Some important parameters which can help identify weakness in testdata
    cerr << "Tests : " << t << '\n';
    cerr << "Max N*M : " << max_nm << '\n';
    cerr << "Sum of N*M : " << sum_nm << '\n';
    cerr << "Answered YES : " << yess << '\n';
    cerr << "Answered NO : " << nos << '\n';
}
``

Editorialist's Code (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

/**
 * Disjoint Set
 * Source: Adapted from Aeren and Atcoder Library
 * Description: Data structure to keep a collection of disjoint sets which contain the elements {0, 1, ..., n-1}
 *              Implements both path compression and union by size
 * Methods:
 * (1) int get_root(int u): Find a representative of the set containing u
 * (2) int size(int u): Returns the size of the set containing u
 * (3) bool same_set(int u, int v): Check whether u and v are in the same set
 * (4) bool merge(int u, int v): Merge the sets containing u and v if they are different, returns success of merge
 * (5) vector group_up(): Returns the collection of disjoint sets as a vector of vectors
 *
 * Time: Amortized O(n alpha(n)) for n operations
 * Space: O(n)
 * Tested on Codeforces EDU
 */

struct DSU {
private:
	std::vector<int> parent_or_size;
public:
	DSU(int n = 1): parent_or_size(n, -1) {}
	int get_root(int u) {
		if (parent_or_size[u] < 0) return u;
		return parent_or_size[u] = get_root(parent_or_size[u]);
	}
	int size(int u) { return -parent_or_size[get_root(u)]; }
	bool same_set(int u, int v) {return get_root(u) == get_root(v); }
	bool merge(int u, int v) {
		u = get_root(u), v = get_root(v);
		if (u == v) return false;
		if (parent_or_size[u] > parent_or_size[v]) std::swap(u, v);
		parent_or_size[u] += parent_or_size[v];
		parent_or_size[v] = u;
		return true;
	}
	std::vector<std::vector<int>> group_up() {
		int n = parent_or_size.size();
		std::vector<std::vector<int>> groups(n);
		for (int i = 0; i < n; ++i) {
			groups[get_root(i)].push_back(i);
		}
		groups.erase(std::remove_if(groups.begin(), groups.end(), [&](auto &s) { return s.empty(); }), groups.end());
		return groups;
	}
};

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int t; cin >> t;
	while (t--) {
		int n, m; cin >> n >> m;
		auto get = [&] (int i, int j) {
			return i*m + j;
		};
		DSU D(n*m);
		for (int i = 0; i < n; ++i) for (int j = 0; j+1 < m; ++j) {
			if (i+1 < n) D.merge(get(i, j), get(i+1, j+1));
			if (i-1 >= 0) D.merge(get(i, j), get(i-1, j+1));
		}
		auto grps = D.group_up();
		vector A(n*m, 0), B = A;
		for (auto &x : A) cin >> x;
		for (auto &x : B) cin >> x;
		bool good = true;
		for (auto grp : grps) {
			vector<int> a, b;
			for (int u : grp) {
				a.push_back(A[u]);
				b.push_back(B[u]);
			}
			sort(begin(a), end(a));
			sort(begin(b), end(b));
			good &= a == b;
		}
		if (good) cout << "Yes\n";
		else cout << "No\n";
	}
}
``

</details>
