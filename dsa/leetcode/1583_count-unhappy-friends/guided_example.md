# Guided Example: Count Unhappy Friends

## 1. Instance & Teaching Goal

We are given an even number $N$ of friends labeled $0$ through $N-1$. Each friend $x$ maintains a strictly ordered preference list $\text{preferences}[x]$ ranking all other $N-1$ friends from most preferred to least preferred. The array $\text{pairs}$ partitions the friends into $N/2$ disjoint two-person pairings.

A friend $x$ paired with $y$ is defined as **unhappy** if there exists some other friend $u$ (paired with $v$) such that:
1. $x$ prefers $u$ over their assigned partner $y$.
2. $u$ prefers $x$ over their assigned partner $v$.

We must count the total number of unhappy friends.

We select the representative instance:
$$N = 4, \quad \text{preferences} = [[1,2,3], [3,2,0], [3,1,0], [1,2,0]], \quad \text{pairs} = [[0,1], [2,3]]$$

The number of unhappy friends is:
$$2$$
(Friends $1$ and $3$ form a blocking pair; both prefer each other over their assigned partners $0$ and $2$).

Our teaching goal is to walk through rank-matrix inversion and blocking pair detection from stable matching theory. We demonstrate how to invert preference lists into an $\mathcal{O}(1)$ lookup table of ordinal ranks, and how to verify mutual preference violations for each candidate in linear time.

## 2. Conceptual Foundation & Invariants

Let $\text{rank}[x][w]$ denote the position of friend $w$ in $x$'s preference list:
$$\text{rank}[x][w] = j \iff \text{preferences}[x][j] = w$$
A smaller rank value indicates a higher preference ($0$ being the top choice).

Let $\text{partner}[x]$ be the friend paired with $x$ in $\text{pairs}$.
Friend $x$ paired with $y = \text{partner}[x]$ is unhappy if and only if there exists some candidate $u$ satisfying:
$$\text{rank}[x][u] < \text{rank}[x][y] \quad \land \quad \text{rank}[u][x] < \text{rank}[u][\text{partner}[u]]$$

```
+-------------------------------------------------------------------------+
|                  STABLE MATCHING BLOCKING PAIR DETECTOR                 |
|                                                                         |
| Assigned Pairs: (0, 1) and (2, 3)                                       |
|                                                                         |
| Preference Lists:                                                       |
|   0: [1, 2, 3]  (partner 1 is rank 0 ==> 0 has no better options)       |
|   1: [3, 2, 0]  (partner 0 is rank 2 ==> 1 prefers 3 and 2 over 0)     |
|   2: [3, 1, 0]  (partner 3 is rank 0 ==> 2 has no better options)       |
|   3: [1, 2, 0]  (partner 2 is rank 1 ==> 3 prefers 1 over 2)           |
|                                                                         |
| Test 1: Friend 1 (partner 0)                                            |
|   Better than 0: friend 3 (rank 0). Partner of 3 is 2.                  |
|   Does 3 prefer 1 over 2?                                               |
|     rank_3(1) = 0,  rank_3(2) = 1 ==> 0 < 1 (YES!)                      |
|   ==> Friend 1 is UNHAPPY (mutually prefers 3).                         |
|                                                                         |
| Test 3: Friend 3 (partner 2)                                            |
|   Better than 2: friend 1 (rank 0). Partner of 1 is 0.                  |
|   Does 1 prefer 3 over 0?                                               |
|     rank_1(3) = 0,  rank_1(0) = 2 ==> 0 < 2 (YES!)                      |
|   ==> Friend 3 is UNHAPPY (mutually prefers 1).                         |
|                                                                         |
| Total Unhappy Friends = 2 (friends 1 and 3)                             |
+-------------------------------------------------------------------------+
```

### State Parameter Reference

| Parameter | Type | Domain | Significance in Stability Verification |
|---|---|---|---|
| $N$ | Integer | Even, $[2, 500]$ | Total count of individuals in the matching market |
| $\text{partner}[x]$ | Integer Array | $[0, N-1]$ | Symmetrical matching partner assigned to friend $x$ |
| $\text{rank}[x][w]$ | 2D Integer Array | $[0, N-2]$ | 0-based preference rank that $x$ assigns to friend $w$ |
| $u$ | Integer | $[0, N-1]$ | Candidate alternative friend whom $x$ prefers over $\text{partner}[x]$ |
| $v$ | Integer | $[0, N-1]$ | Current partner of candidate friend $u$ ($\text{partner}[u]$) |
| $\text{ans}$ | Integer | $[0, N]$ | Count of individuals proved to be unhappy |

> [!IMPORTANT]
> **Blocking Pair Symmetry Invariant**:
> If pair $(x, u)$ forms a mutual blocking condition where $x$ prefers $u$ over $y$ and $u$ prefers $x$ over $v$, then BOTH friend $x$ and friend $u$ are individually unhappy. However, each friend is counted at most once in the output accumulator $\text{ans}$.

```mermaid
flowchart TD
    accTitle: Unhappy Friends Verification Pipeline
    accDescr: Pipeline constructing rank lookup matrix, iterating through friends, and scanning higher-preference candidates for mutual preference violations.
    Start([Input: preferences, pairs]) --> BuildPartner["Map partner[x] = y and partner[y] = x for all pairs"]
    BuildPartner --> InvertRanks["Precompute rank[x][w] table in O(1) lookups"]
    InvertRanks --> InitAns["Set ans = 0"]
    InitAns --> LoopFriends[Iterate friend x from 0 to N - 1]
    LoopFriends --> GetPartner["y = partner[x], y_rank = rank[x][y]"]
    GetPartner --> CandidateLoop[Iterate candidates u with rank[x][u] < y_rank]
    CandidateLoop --> CheckMutual{"rank[u][x] < rank[u][partner[u]]?"}
    CheckMutual -- Yes --> Unhappy["ans += 1; break candidate loop (x is unhappy)"]
    CheckMutual -- No --> NextCand[Test next candidate u]
    NextCand --> MoreCands{More candidates u?}
    MoreCands -- Yes --> CandidateLoop
    MoreCands -- No --> NextFriend[Advance to next friend x]
    Unhappy --> NextFriend
    NextFriend --> MoreFriends{x < N - 1?}
    MoreFriends -- Yes --> LoopFriends
    MoreFriends -- No --> Done([Return ans: Total Unhappy Count])
```

## 3. Step-by-Step Worked Execution

We trace the algorithm on $N = 4$:
- Preference lists:
  - Friend 0: $[1, 2, 3]$
  - Friend 1: $[3, 2, 0]$
  - Friend 2: $[3, 1, 0]$
  - Friend 3: $[1, 2, 0]$
- Assigned pairings: $(0, 1)$ and $(2, 3)$.

### Phase 1: Partner Mapping and Rank Table Construction
1. **Partner Map**:
   - $\text{partner}[0] = 1, \quad \text{partner}[1] = 0$
   - $\text{partner}[2] = 3, \quad \text{partner}[3] = 2$
2. **Rank Matrix $\text{rank}[x][w]$**:
   - For Friend 0: $\text{rank}[0][1] = 0, \text{rank}[0][2] = 1, \text{rank}[0][3] = 2$.
   - For Friend 1: $\text{rank}[1][3] = 0, \text{rank}[1][2] = 1, \text{rank}[1][0] = 2$.
   - For Friend 2: $\text{rank}[2][3] = 0, \text{rank}[2][1] = 1, \text{rank}[2][0] = 2$.
   - For Friend 3: $\text{rank}[3][1] = 0, \text{rank}[3][2] = 1, \text{rank}[3][0] = 2$.

### Phase 2: Friend-by-Friend Unhappiness Audit

#### Audit Friend $x = 0$
- Assigned partner: $y = 1$.
- Rank of partner: $\text{rank}[0][1] = 0$ (top choice!).
- Candidates $u$ preferred over $y$: None (rank $< 0$ is empty).
- Status: **Happy**.

#### Audit Friend $x = 1$
- Assigned partner: $y = 0$.
- Rank of partner: $\text{rank}[1][0] = 2$ (lowest choice).
- Candidates preferred over $0$: Friends with rank $< 2$:
  - Friend $3$ ($\text{rank} = 0$)
  - Friend $2$ ($\text{rank} = 1$)
- **Test Candidate $u = 3$**:
  - $3$'s partner is $v = 2$.
  - Rank of $x = 1$ in $3$'s list: $\text{rank}[3][1] = 0$.
  - Rank of partner $v = 2$ in $3$'s list: $\text{rank}[3][2] = 1$.
  - Comparison: $\text{rank}[3][1] < \text{rank}[3][2] \iff 0 < 1$. Holds!
  - Mutual preference satisfied: Friend $1$ prefers $3$ over $0$, and friend $3$ prefers $1$ over $2$.
- Status: **Friend 1 is UNHAPPY**. $\text{ans} = 0 + 1 = 1$. Break candidate search.

#### Audit Friend $x = 2$
- Assigned partner: $y = 3$.
- Rank of partner: $\text{rank}[2][3] = 0$ (top choice!).
- Candidates $u$ preferred over $y$: None.
- Status: **Happy**.

#### Audit Friend $x = 3$
- Assigned partner: $y = 2$.
- Rank of partner: $\text{rank}[3][2] = 1$.
- Candidates preferred over $2$: Friends with rank $< 1$:
  - Friend $1$ ($\text{rank} = 0$).
- **Test Candidate $u = 1$**:
  - $1$'s partner is $v = 0$.
  - Rank of $x = 3$ in $1$'s list: $\text{rank}[1][3] = 0$.
  - Rank of partner $v = 0$ in $1$'s list: $\text{rank}[1][0] = 2$.
  - Comparison: $\text{rank}[1][3] < \text{rank}[1][0] \iff 0 < 2$. Holds!
  - Mutual preference satisfied: Friend $3$ prefers $1$ over $2$, and friend $1$ prefers $3$ over $0$.
- Status: **Friend 3 is UNHAPPY**. $\text{ans} = 1 + 1 = 2$. Break candidate search.

### Termination
All $4$ friends evaluated. Total unhappy friends: $2$.

## 4. Complete Execution Trace

The table below catalogs every friend, their assigned partner, candidate preferences, and the outcome of the mutual preference test.

| Friend $x$ | Partner $y$ | Partner Rank $\text{rank}[x][y]$ | Higher-Ranked Candidates $u$ | Candidate Partner $v$ | $u$'s Rank for $x$ | $u$'s Rank for $v$ | Mutual Check ($\text{rank}_u(x) < \text{rank}_u(v)$) | Unhappy? | Cumulative Count $\text{ans}$ |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | None | - | - | - | - | No | 0 |
| 1 | 0 | 2 | 3, 2 | 3's partner: 2 | $\text{rank}_3(1) = 0$ | $\text{rank}_3(2) = 1$ | $0 < 1$ (**True**) | **YES** | **1** |
| 2 | 3 | 0 | None | - | - | - | - | No | 1 |
| 3 | 2 | 1 | 1 | 1's partner: 0 | $\text{rank}_1(3) = 0$ | $\text{rank}_1(0) = 2$ | $0 < 2$ (**True**) | **YES** | **2** |

### Blocking Pair Summary

$$\text{Blocking Pair} = \{1, 3\}$$
- Friend 1 was assigned 0, but prefers 3 (rank 0 vs. rank 2).
- Friend 3 was assigned 2, but prefers 1 (rank 0 vs. rank 1).
- Both 1 and 3 are unhappy with their assignments.

## 5. Algorithmic Correctness

### Soundness

A friend $x$ is flagged as unhappy if and only if there exists some friend $u$ such that:
1. $u$ precedes $y$ in $x$'s preference list, which is checked by iterating strictly through indices $i \in [0, \text{rank}[x][y] - 1]$.
2. $x$ precedes $v = \text{partner}[u]$ in $u$'s preference list, which is verified by $\text{rank}[u][x] < \text{rank}[u][v]$.
Because both conditions are evaluated via exact rank comparisons against precomputed inverted indices, every detected unhappy friend strictly satisfies the problem definition.

### Completeness

For any unhappy friend $x$, the definition states that at least one such friend $u$ exists.
Because the algorithm examines every single friend $u$ that $x$ prefers over $y$, the candidate $u$ creating the unhappiness condition is guaranteed to be tested.
Upon finding the first valid $u$, $x$ is marked unhappy and counted once. No unhappy friend can be missed.

## 6. Traps This Instance Exposes

1. **Double Counting Mutual Pairs**:
   When $1$ and $3$ form a mutual blocking pair, an algorithm must increment the count for $1$ and increment the count for $3$, but must never increment by $2$ during a single friend's audit. Auditing each friend independently and breaking upon the first violation ensures each unhappy individual is counted exactly once.

2. **Linear Search in Preference Lists ($\mathcal{O}(N)$ Rank Lookup)**:
   Calling `.index()` or searching the preference list repeatedly to find ranks takes $\mathcal{O}(N)$ per check, resulting in $\mathcal{O}(N^3)$ overall time. Precomputing an inverted 2D lookup table $\text{rank}[x][w]$ resolves every preference comparison in $\mathcal{O}(1)$ time.

3. **Asymmetric Preference Fallacy**:
   Friend $x$ preferring $u$ over $y$ is not enough; friend $u$ must ALSO prefer $x$ over $v$. If $u$ is already satisfied with $v$, $u$ will not participate in a blocking pair, so $x$ cannot be declared unhappy through $u$.

4. **Testing Self or Partner as Candidate**:
   The candidate loop should only check friends with higher preference than $y$. Friends ranked worse than $y$, the partner $y$ itself, and $x$ itself are naturally excluded by iterating up to $\text{rank}[x][y] - 1$.

## 7. Complexity Derivation

### Time Complexity

Let $N$ be the number of friends ($N \le 500$).
- **Partner Mapping**: Populating $\text{partner}$ from $N / 2$ pairs takes $\mathcal{O}(N)$ time.
- **Rank Table Precomputation**: Inverting $N$ preference lists of length $N - 1$ takes $N \times (N - 1)$ assignments: $\mathcal{O}(N^2)$ time.
- **Unhappiness Verification**:
  - For each of the $N$ friends, $x$ evaluates at most $N - 1$ candidates $u$.
  - For each candidate $u$, checking $\text{rank}[u][x] < \text{rank}[u][v]$ takes $\mathcal{O}(1)$ table lookups.
  - Verification across all friends takes at most $\mathcal{O}(N^2)$ operations.

Total time complexity is strictly:
$$\mathcal{O}(N^2)$$
For $N = 500$, $N^2 = 250\,000$ operations, executing in under 10 milliseconds.

### Auxiliary Space Complexity

- **Rank Matrix**: A 2D integer array of size $N \times N$ requires $N^2$ integer entries: $\mathcal{O}(N^2)$ space.
- **Partner Array**: An array of size $N$ requires $\mathcal{O}(N)$ space.

Total auxiliary space complexity is:
$$\mathcal{O}(N^2)$$
For $N = 500$, this uses approximately 1 MB of memory.
