# Dynamic Programming - Rod Cutting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP34 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Dynamic Programming |
| Official Link | [PREP34](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_14/problems/PREP34) |

---

## Problem Statement

There is a rod of length $N$ lying on the $X$-axis with its left end at $X = 0$ and right end at $X = N$. You're given $M$ points $A_1, A_2, \dots, A_M$ in the rod such that $0 \lt A_1 \lt A_2 \lt \dots \lt A_M \lt N$. You have to cut the rod at all these points. You can perform these cuts in any order. You can take any segment of the rod that exists, and cut it into two smaller sub-rods. The cost of making a cut is the length of the segment of rod in which you are making the cut.

Your aim is to **minimize** this cost. Find the sequence of these $M$ points in which you will make cuts. If two different sequences of cuts give the same cost, return the **lexicographically smallest** sequence.

Note: Sequence $A$ is lexicographically smaller than sequence $B$ if and only if there exists a position $i$ where $A_i \lt B_i$ and $A_j = B_j$ for all $j \lt i$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains two space-separated integers $N$, $M$ — the length of the rod, the number of points where you've to cut the rod.
- The second line of each test case contains $M$ space-separated integers $A_1,A_2,\ldots,A_M$.

---

## Output Format

For each test case, output on a new line the $M$ space-separated points in which order you will make cuts.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^9$
- $1 \leq M \leq \min(10^2, N - 1)$
- $1 \leq A_i \lt N$
- $0 \lt A_1 \lt A_2 \lt \dots \lt A_M \lt N$
- The sum of $M$ over all test cases won't exceed $1000$.

---

## Examples

**Example 1**

**Input**

```text
3
6 3
1 4 5
6 2
2 4
10 5
1 4 5 6 8
```

**Output**

```text
4 1 5 
2 4 
4 1 6 5 8
```

**Explanation**

**Test case $1$**: There will be $6$ possible orders,
- $[1, 4, 5]$, cost will be $6 + 5 + 2 = 13$.
- $[1, 5, 4]$, cost will be $6 + 5 + 4 = 15$.
- $[4, 1, 5]$, cost will be $6 + 4 + 2 = 12$.
- $[4, 5, 1]$, cost will be $6 + 2 + 4 = 12$.
- $[5, 1, 4]$, cost will be $6 + 5 + 4 = 15$.
- $[5, 4, 1]$, cost will be $6 + 5 + 4 = 15$.

For $[4, 1, 5]$, $[4, 5, 1]$ cost will be $12$ but $[4, 1, 5]$ will be lexicographically smaller.

**Test case $2$**: There will be $2$ possible orders,
- $[2, 4]$, cost will be $6 + 4 = 10$.
- $[4, 2]$, cost will be $6 + 2 = 10$.

For $[2, 4]$, $[4, 2]$ cost will be $10$ but $[2, 4]$ will be lexicographically smaller.

**Test case $3$**: Minimum cost will be $26$. Sequence of cut will be $[4, 1, 6, 5, 8]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 3
1 4 5
```

**Output for this case**

```text
4 1 5
```



#### Test case 2

**Input for this case**

```text
6 2
2 4
```

**Output for this case**

```text
2 4
```



#### Test case 3

**Input for this case**

```text
10 5
1 4 5 6 8
```

**Output for this case**

```text
4 1 6 5 8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we are going to solve a classic rod cutting problem with a twist – not only do we want to minimize the cost of cutting, but when multiple orders yield the same cost, we need to choose the lexicographically smallest sequence of cuts. Recall that the cost of making a cut in a segment is equal to the length of the segment in which the cut is performed. Thus, if you have a rod of length $N$ and a set of cut points $A_1, A_2, \dots, A_M$, you must determine the order of cuts that minimizes the total cost, and if there is a tie, choose the sequence that is lexicographically smallest.

Below, we discuss two approaches that are both efficient and instructive.

---

### **Approach 1: Top-Down Recursion with Memoization**

This method uses recursion to divide the problem into smaller subproblems and caches (memoizes) results to avoid redundant calculations.

#### **Idea:**

1. **Process the Positions:**
   Create an array `pos` that includes the endpoints and the cut points, i.e.
   $$ pos = [0, A_1, A_2, \dots, A_M, N]. $$

2. **Define the Recursive Function:**
   Define a function `dp(i, j)` that returns a pair containing:
   - The minimum cost to cut the segment from `pos[i]` to `pos[j]`.
   - The lexicographically smallest sequence of cuts that produces this minimum cost.

   **Base Case:** If there are no valid cut points between `i` and `j$ (i.e. when $j - i = 1$), there is no cost and an empty sequence.

3. **Recurrence Relation:**
   For every valid cut position `m` between `i` and `j` (i.e. $i < m < j$), calculate:
   $$ \text{candidateCost} = (pos[j]-pos[i]) + dp(i, m).cost + dp(m, j).cost, $$
   and set the candidate sequence as:
   $$ [pos[m]] + \text{dp}(i, m).\text{seq} + \text{dp}(m, j).\text{seq}. $$
   Update the result if this candidate has a lower cost or if the cost is the same but the sequence is lexicographically smaller.

4. **Memoization:**
   Cache the subproblem results using memoization (in C++ a 2D table can be used; in Python, decorators like `@lru_cache` do the job).

This approach has a time complexity of roughly $O(M^3)$ (since there are $O(M^2)$ subproblems and each subproblem iterates over at most $M$ candidates) which is acceptable given the constraints.

---

#### **C++ Code (Top-Down Recursion with Memoization):**

```cpp
#include
using namespace std;

struct Result {
    long long cost;
    vector seq;
};

int N, M;
vector pos;
vector> memo;
vector> computed;

Result solveDP(int i, int j) {
    if(j - i == 1)
        return {0, {}};
    if(computed[i][j])
        return memo[i][j];
    Result best;
    best.cost = LLONG_MAX;
    best.seq = {};
    for (int m = i + 1; m < j; m++) {
        Result left = solveDP(i, m);
        Result right = solveDP(m, j);
        long long candidateCost = pos[j] - pos[i] + left.cost + right.cost;
        vector candidateSeq;
        candidateSeq.push_back(pos[m]);
        candidateSeq.insert(candidateSeq.end(), left.seq.begin(), left.seq.end());
        candidateSeq.insert(candidateSeq.end(), right.seq.begin(), right.seq.end());

        if (candidateCost < best.cost || (candidateCost == best.cost && candidateSeq < best.seq)) {
            best.cost = candidateCost;
            best.seq = candidateSeq;
        }
    }
    memo[i][j] = best;
    computed[i][j] = true;
    return best;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        cin >> N >> M;
        vector cuts(M);
        for(int i = 0; i < M; i++){
            cin >> cuts[i];
        }
        pos.clear();
        pos.push_back(0);
        for(auto c : cuts)
            pos.push_back(c);
        pos.push_back(N);
        int sz = pos.size();
        memo.assign(sz, vector(sz));
        computed.assign(sz, vector(sz, false));

        Result res = solveDP(0, sz-1);
        for (int x : res.seq)
            cout << x << " ";
        cout << "\n";
    }
    return 0;
}
```

#### **Python Code (Top-Down Recursion with Memoization):**

```python
def solve():
    import sys
    sys.setrecursionlimit(10000)
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index]); index += 1
        M = int(input_data[index]); index += 1
        cuts = list(map(int, input_data[index:index+M])); index += M
        pos = [0] + cuts + [N]
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(i, j):
            if j - i == 1:
                return (0, ())
            best_cost = float('inf')
            best_seq = ()
            for m in range(i + 1, j):
                left_cost, left_seq = dp(i, m)
                right_cost, right_seq = dp(m, j)
                candidate_cost = pos[j] - pos[i] + left_cost + right_cost
                candidate_seq = (pos[m],) + left_seq + right_seq
                if candidate_cost < best_cost or (candidate_cost == best_cost and candidate_seq < best_seq):
                    best_cost = candidate_cost
                    best_seq = candidate_seq
            return (best_cost, best_seq)
        cost, seq = dp(0, len(pos) - 1)
        results.append(" ".join(map(str, seq)))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()
```

---

### **Approach 2: Bottom-Up Dynamic Programming (Tabulation)**

This approach builds the solution iteratively using a DP table instead of recursion.

#### **Idea:**

1. **Setting Up the DP Table:**
   Create the positions array as before:
   $$ pos = [0, A_1, A_2, \dots, A_M, N]. $$
   Define a DP table `dp[i][j]` where each entry contains a pair:
   - `dp[i][j].cost`: the minimum cost to cut the segment from `pos[i]` to `pos[j]`.
   - `dp[i][j].seq`: the corresponding lexicographically smallest cut order.

2. **Filling the Table:**
   Process all segments with increasing lengths (from segments that have no internal cut points to segments with one or more cut points). For each segment `[i, j]`, iterate through every possible cut point `m` (with $i < m < j$) and calculate:
   $$ \text{candidateCost} = pos[j] - pos[i] + dp[i][m].cost + dp[m][j].cost, $$
   and candidate sequence:
   $$ [pos[m]] + dp[i][m].seq + dp[m][j].seq. $$
   Choose the candidate with the smallest cost; if there is a tie, choose the one with the lexicographically smallest sequence.

3. **Extracting the Final Answer:**
   The answer will be stored in `dp[0][k-1]`, where $k$ is the number of elements in `pos$.

This approach avoids recursion and is often easier to follow for iterative dynamic programming learners.

---

#### **C++ Code (Bottom-Up DP Tabulation):**

```cpp
#include
#include
#include
#include
using namespace std;

struct State {
    long long cost;
    vector seq;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N, M;
        cin >> N >> M;
        vector cuts(M);
        for(int i = 0; i < M; i++){
            cin >> cuts[i];
        }
        vector pos;
        pos.push_back(0);
        for(auto c : cuts)
            pos.push_back(c);
        pos.push_back(N);
        int kSize = pos.size();

        vector> dp(kSize, vector(kSize, {0, {}}));
        const long long INF = 1e18;

        // Iterate over the length of segments
        for (int len = 2; len < kSize; len++){
            for (int i = 0; i + len < kSize; i++){
                int j = i + len;
                dp[i][j].cost = INF;
                vector bestSeq;
                for (int m = i + 1; m < j; m++){
                    long long candidateCost = (long long)pos[j] - pos[i] + dp[i][m].cost + dp[m][j].cost;
                    vector candidateSeq;
                    candidateSeq.push_back(pos[m]);
                    candidateSeq.insert(candidateSeq.end(), dp[i][m].seq.begin(), dp[i][m].seq.end());
                    candidateSeq.insert(candidateSeq.end(), dp[m][j].seq.begin(), dp[m][j].seq.end());

                    if(candidateCost < dp[i][j].cost){
                        dp[i][j].cost = candidateCost;
                        bestSeq = candidateSeq;
                    }
                    else if(candidateCost == dp[i][j].cost){
                        if(candidateSeq < bestSeq)
                            bestSeq = candidateSeq;
                    }
                }
                if(dp[i][j].cost == INF){
                    dp[i][j].cost = 0;
                    bestSeq.clear();
                }
                dp[i][j].seq = bestSeq;
            }
        }

        for (int i = 0; i < dp[0][kSize - 1].seq.size(); i++){
            cout << dp[0][kSize - 1].seq[i] << (i < dp[0][kSize - 1].seq.size() - 1 ? " " : "\n");
        }
    }
    return 0;
}
```

#### **Python Code (Bottom-Up DP Tabulation):**

```python
def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    out_lines = []
    for _ in range(t):
        N = int(data[index]); index += 1
        M = int(data[index]); index += 1
        cuts = list(map(int, data[index:index+M])); index += M
        pos = [0] + cuts + [N]
        k = len(pos)
        dp = [[(0, []) for _ in range(k)] for __ in range(k)]
        INF = 10**18
        for length in range(2, k):
            for i in range(k - length):
                j = i + length
                best_cost = INF
                best_seq = []
                for m in range(i+1, j):
                    candidate_cost = pos[j] - pos[i] + dp[i][m][0] + dp[m][j][0]
                    candidate_seq = [pos[m]] + dp[i][m][1] + dp[m][j][1]
                    if candidate_cost < best_cost or (candidate_cost == best_cost and candidate_seq < best_seq):
                        best_cost = candidate_cost
                        best_seq = candidate_seq
                dp[i][j] = (best_cost, best_seq)
        out_lines.append(" ".join(map(str, dp[0][k-1][1])))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()
```

---

Both approaches implement the same recurrence relation and ensure that we choose the lexicographically smallest sequence when costs tie. Understanding either method will enhance your grasp of dynamic programming and help you approach similar optimization problems in interviews.

Happy coding and best of luck with your DSA interviews!

</details>
