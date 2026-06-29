# Chef and insomnia

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHINSM |
| Difficulty Rating | 2197 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHINSM](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHINSM) |

---

## Problem Statement

Chef sometimes suffers from insomnia. During sleepless nights, he often plays this game: He creates an array **A** of **N** integers and also decides one integer **K**. After that, he tries to count the number of non-empty contiguous subsequences (subsegments) of **A**, such that there are no bad pairs of integers in this subsegment. A pair **(x, y)** of integers is called bad if **x** is situated to the left of **y** in the array and **x mod y = K**. Finally, before going to sleep, Chef wrote down the answer on a sheet of paper. Sadly, he has forgotten it this morning and want your help regarding that.

### Input

- The first line contains two integers - **N** and **K**.

- Second line contains **N** integers - **A1**, **A2** ... **AN** - separated by spaces, denoting the array **A**.

### Output

A single line containing an integer - the answer to the problem.

### Constraints

- 1 ≤ **N**, **Ai** ≤ 105

- 0 ≤ **K** ≤ 105

### Subtasks

- Subtask 1: **N** ≤ 100 (15 points)

- Subtask 2: **N** ≤ 1000 (15 points)

- Subtask 3: **K** = 0 (10 points)

- Subtask 4: Original constraints (60 points)

---

## Examples

**Example 1**

**Input**

```text
3 2
5 3 1
```

**Output**

```text
4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/AUG15/problems/CHINSM)

[Practice](http://www.codechef.com/problems/CHINSM)

**Author:** [Vlad Mosko](http://www.codechef.com/users/zedthirtyeight)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Medium

### PREREQUISITES:

Divisor lists, intervals, combinatorics, ad hoc

### PROBLEM:

Given an array of integers [A_1, \ldots, A_N] and a number K, find the number of subarrays containing no bad pairs. A pair (i,j) is a **bad pair** if i < j and (A_i \bmod A_j) = K.

### QUICK EXPLANATION:

- For each position j, compute the largest i_j < j such that (i_j,j) is a bad pair. Collect all such bad pairs gotten this way, sorted by j. (There are at most N such pairs, but may be less, because for some j s there could be no such $i_j$s).

- Remove a pair (i_j,j) if j > 1 and i_{j-1} \ge i_j.

- Add the pair (N, N+1) at the end of the list.

- Assume that the list of pairs acquired is [(i_1,j_1), (i_2,j_2), \ldots, (i_m,j_m)]. Then the answer is:

\frac{N(N+1)}{2} - \sum_{n=1}^{m-1} i_n (j_{n+1} - j_n)

To compute all pairs (i_j,j), we need to store, for each value v > K, the maximum i < j such that A_i > K and (A_i \bmod v) = K (there are at most \max A_i such lists). We also store the maximum l < j such that A_l = K. As we increase j, we need update some of these lists: When going to a new value of j we only need to update at most O(\sqrt{\max A_j}) lists.

### EXPLANATION:

Let’s first assume that we have all the bad pairs, and we want to compute the number of subarrays containing no bad pairs. This is just equal to the number of subarrays (which is N(N+1)/2), minus the number of subarrays containing at least one bad pair. We will compute the latter instead, and we’ll call a subarray **bad** if it contains at leaset one bad pair.

First, notice that all {N \choose 2} pairs can be bad pairs (for example, if A_i = 1 for all i and K = 0). Therefore we can’t even compute all the bad pairs, because that is too slow. However, notice that not all bad pairs are important. For example, if the pair p_1 completely contains the pair p_2, then any subarray containing p_1 also contains p_2. Thus, the pair p_1 is redundant, i.e. if we remove the pair p_1 from our list, then the set of bad subarrays stay the same.

Thus we can remove all bad pairs completely containing other bad pairs. Note that after doing so, no two bad pairs share the same left (or right) endpoint any more (otherwise one will contain the other). Since there are at most N endpoints, this reduces the number of bad pairs we have to *at most N-1*, which is more manageable

This also shows that for a given endpoint j, there is only at most one important bad pair (i,j) ending in j, and it’s the one with the maximum i. Therefore, the first step is to compute the maximum i for each j such that (i,j) is bad (ignoring the j s for which there are no such i).

# Bad pairs ending in every position

Assuming A_j > K, (A_i \bmod A_j) = K is equivalent to:

\begin{aligned}
(A_i \bmod A_j) &= K \\\
A_i &\equiv K \pmod{A_j} \\\
A_j &| (A_i - K)
\end{aligned}

This means that A_j is a divisor of (A_i - K).

For every endpoint j, we need to compute the maximum i such that (i,j) is bad. Surely, there are no bad pairs such that A_i < K or A_j \le K, because (A_i \bmod A_j) < K in those cases.

Suppose that, for every value v, K < v \le \max A_i, we store the value i_v, which we define as the maximum i_v < j such that (A_{i_v} \bmod v) = K. Note that i_v is also dependent on j, so as we increase j, we will need to update some of the $i_v$s, but for now, assume we can do those updates. If so, the i we are looking for is simply i_{A_j}

Now for the updates. As we leave a particular value of j and go to the next one (j+1), we need to update some of the $i_v$s, specifically for those v s having (A_j \bmod v) = K. As shown above, this is equivalent to v being a divisor of A_j - K, so we only update for those v s that are divisors of the number A_j - K. This is good, because it has only at most 2\sqrt{A_j - K} such divisors

Unfortunately, the last statement is incorrect for the case A_j = K. If A_j = K, then A_j - K = 0. But every v is a divisor of zero! In this case, updating all the lists may be too slow, so we need to do something else. This is simple; we can simply maintain a separate value l, which is the maximum l < j such that A_l = K. i_v is now modified to exclude those i s such that A_i = K, and for an endpoint j, the i we are looking for is now \max(i_{A_j}, l)  Thus, we maintain the fast running time!

The total running time of this step is O(N \sqrt{\max A_i}).

After getting the bad pairs (i_j,j) for every such j, we can simply remove those pairs for which i_{j-1} \ge i_j, because those pairs are not important. Now we have a list of bad pairs [(i_1,j_1), (i_2,j_2), \ldots, (i_m,j_m)] satisfying the following:

i_1 < i_2 < \cdots < i_m

j_1 < j_2 < \cdots < j_m

# Subarrays containing bad pairs

We now want to compute the number of subarrays containing at least one bad pair.

Each such subarray contains a unique “rightmost” bad pair, so we can compute, for each 1 \le k \le m, the number of subarrays whose rightmost bad pair is (i_k,j_k). Let’s denote this by f(k). Then the number of subarrays containing at least one bad pair is:

\sum_{k=1}^m f(k)

Let’s first compute f(m) (the last one). For a subarray [i\ldots j] to contain (i_m,j_m), it must be true that 1 \le i \le i_m and j_m \le j \le N. There are i_m(N+1-j_m) such choices for such subarrays, therefore f(m) = i_m(N+1-j_m).

Now, let’s compute f(k) for 1 \le k < m. The subarray [i\ldots j] should contain (i_k,j_k), but we need to ensure that this is the rightmost bad pair, i.e. the subarray doesn’t contain (i_{k+1},j_{k+1}). This means that 1 \le i \le i_k and j_k \le j. However, j < j_{k+1} should be true, otherwise it will contain the pair (i_{k+1},j_{k+1}). Therefore, there are i_k (j_{k+1} - j_k) choices for such subarrays, and thus we have f(k) = i_k(j_{k+1} - j_k)

This step runs in O(N) time

Here’s an implementation in C++:

``#include <stdio.h>
#include <algorithm>
using namespace std;
#define ll long long
#define LIM 100111

int I[LIM];

int main() {
    for (int j = 0; j < LIM; j++) I[j] = -1;

    int n, k;
    scanf("%d%d", &n, &k);

    ll total = n*(n+1LL) >> 1;
    int pi = 0, pj = 1;
    #define add_pair(ci,cj) do {\
        total += pi * (pj - (cj));\
        pi = ci;\
        pj = (cj);\
    } while (0)

    int l = 0;
    for (int j = 1; j <= n; j++) {
        int a;
        scanf("%d", &a);
        if (a == k) {
            l = j;
        } else if (a > k) {
            int i = max(I[a], l);
            if (pi < i) {
                add_pair(i, j);
            }

            a -= k;
            for (int v = 1; v * v <= a; v++) {
                if (a % v == 0) I[v] = I[a / v] = j;
            }
        }
    }

    add_pair(n, n+1);

    printf("%lld\n", total);
}
``

Some implementation details:

- We added a sentinel leftmost bad pair (0,1) to make the `add_pair` macro simpler.

- There is also a sentinel rightmost bad pair (N,N+1) so that f(m) (the last pair) is not special

- There is no array A allocated; instead the individual values of A are inputted and processed on the fly.

### Time Complexity:

O(N\sqrt{\max A_i})

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/AUG15/Setter/CHINSM.cpp)

[tester](http://www.codechef.com/download/Solutions/AUG15/Tester/CHINSM.cpp)

</details>
