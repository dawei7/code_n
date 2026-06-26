# Stable Marriage Problem (Gale-Shapley)

| | |
|---|---|
| **ID** | `greedy_13` |
| **Category** | greedy |
| **Complexity (required)** | $O(N^2)$ Time, $O(N^2)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Gale-Shapley algorithm](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm) |

## Problem statement

Given `N` men and `N` women, where each person has ranked all members of the opposite sex in order of preference.
Marry the men and women together such that there are NO two people of opposite sex who would both rather have each other than their current partners.
If there are no such pairs, the marriages are considered **"Stable"**.
Return a list of the `N` stable couples.

**Input:** A 2D array `men_prefs` of size N x N, and a 2D array `women_prefs` of size N x N.
**Output:** An array/dictionary mapping men to women (or vice versa).

## When to use it

- To solve bipartite matching problems where both sets have strict preference rankings.
- *Trivia:* The Gale-Shapley algorithm mathematically guarantees that a stable matching ALWAYS exists for any equal number of men and women, and won the Nobel Prize in Economics in 2012!

## Approach

**1. The Proposer and the Reviewer:**
The algorithm designates one group as "Proposers" (traditionally the men) and the other as "Reviewers" (the women).
- Men will greedily propose to their top choice remaining on their list.
- Women will tentatively accept the best proposal they receive. If a better proposal comes along later, they will ruthlessly dump their current partner and accept the new one!

**2. The Data Structures:**
- `free_men`: A queue of men who are currently unmarried.
- `women_partner`: An array tracking who each woman is currently engaged to (initially all `-1`).
- `man_next_proposal`: An array tracking the *index* of the next woman a man should propose to in his preference list. (So he doesn't propose to the same woman twice).
- **Optimization:** If a woman receives a new proposal from Man B while engaged to Man A, she needs to know who she prefers. Searching her preference list takes $O(N)$ time. We can pre-compute an `inverse_women_prefs` matrix where `matrix[woman][man]` returns his numerical rank (e.g., 1st choice, 5th choice) in $O(1)$ time!

**3. The Algorithm (While there is a Free Man):**
1. Pop a man `m` from the `free_men` queue.
2. Look at his preference list. Find the highest-ranked woman `w` he hasn't proposed to yet.
3. Does `w` have a partner?
   - **NO:** She accepts! They are engaged.
   - **YES:** She compares her current partner `m_old` against the new proposer `m`.
     - If she prefers `m_old`, she rejects `m`. `m` goes back into the `free_men` queue!
     - If she prefers `m`, she accepts `m`! They are engaged. `m_old` gets dumped and goes back into the `free_men` queue!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_13: Stable Marriage (Gale-Shapley).

Each free man proposes to his next-best. The woman accepts
iff she prefers him to her current match.
"""


def solve(n, men_prefs, women_prefs):
    if n == 0:
        return []
    next_w = [0] * n
    woman_engaged_to = [-1] * n
    man_engaged_to = [-1] * n
    woman_rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for rank, m in enumerate(women_prefs[w]):
            woman_rank[w][m] = rank
    free_men = list(range(n))
    while free_men:
        m = free_men.pop(0)
        w = men_prefs[m][next_w[m]]
        next_w[m] += 1
        if woman_engaged_to[w] == -1:
            woman_engaged_to[w] = m
            man_engaged_to[m] = w
        else:
            current = woman_engaged_to[w]
            if woman_rank[w][m] < woman_rank[w][current]:
                woman_engaged_to[w] = m
                man_engaged_to[m] = w
                man_engaged_to[current] = -1
                free_men.append(current)
            else:
                free_men.insert(0, m)
    return man_engaged_to
```

</details>

## Walk-through

`N = 2`.
`men_prefs`:
- `M0`: `[W1, W0]` (Prefers 1 over 0)
- `M1`: `[W1, W0]` (Prefers 1 over 0)

`women_prefs`:
- `W0`: `[M0, M1]` (Prefers 0 over 1)
- `W1`: `[M1, M0]` (Prefers 1 over 0)

`women_partner = [-1, -1]`. `free_men = [0, 1]`.

1. Pop `M0`.
   - Proposes to `W1` (1st choice).
   - `W1` is free! Engaged! `women_partner = [-1, 0]`.
2. Pop `M1`.
   - Proposes to `W1` (1st choice).
   - `W1` is engaged to `M0`.
   - Compare: `W1` prefers `M1` (Rank 0) over `M0` (Rank 1).
   - Dump! Engaged to `M1`. `women_partner = [-1, 1]`.
   - `M0` gets dumped and added back to `free_men`.
3. Pop `M0`.
   - Proposes to `W0` (2nd choice).
   - `W0` is free! Engaged! `women_partner = [0, 1]`.
4. `free_men` is empty. Terminate.

Result: `(M0-W0)`, `(M1-W1)`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N^2)$ |
| **Average** | $O(N^2)$ | $O(N^2)$ |
| **Worst** | $O(N^2)$ | $O(N^2)$ |

In the worst-case scenario, every single man proposes to every single woman exactly once. There are N men and N women, so there are at most N^2 proposals. Because of our `women_ranks` pre-computation matrix, accepting or rejecting a proposal takes strict $O(1)$ time. Thus, the total time complexity is $O(N^2)$.
Space complexity is $O(N^2)$ to store the `women_ranks` matrix (the input lists are also $O(N^2)$ size).

## Variants & optimizations

- **Proposer Bias:** The Gale-Shapley algorithm is notoriously "Proposer-Optimal" and "Reviewer-Pessimal". The group that proposes will ALWAYS get their absolute best possible stable match. The group that reviews will ALWAYS get their absolute worst possible stable match! To favor the women, simply reverse the algorithm so the women propose.

## Real-world applications

- **The National Resident Matching Program (NRMP):** The actual system used in the United States since 1952 to match thousands of graduating medical students to hospital residency programs. Hospitals rank students, students rank hospitals, and Gale-Shapley flawlessly matches them!
- **CDN Server Allocation:** Matching users to physical Content Delivery Network nodes based on latency preferences and server load capacity limits.

## Related algorithms in cOde(n)

- **[graph_12 - Bipartite Check](../graphs/graph_12_bipartite-check.md)** — The foundational algorithm to separate nodes into two disjoint sets (like Men and Women) before matching them.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
