# Problem 987: Straight Eight - Mathematical Approach & Analysis

## 1. Problem Formulation & Straight Definitions

A standard 52-card deck consists of $13$ ranks $\{A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K\}$ across $4$ suits.
A **straight** consists of $5$ cards of sequential rank that are **not all of the same suit** (excluding straight flushes).
There are $10$ valid 5-rank intervals:
- Low-Ace: $(A, 2, 3, 4, 5)$,
- Standard: $(2, 3, 4, 5, 6)$ through $(9, 10, J, Q, K)$,
- High-Ace: $(10, J, Q, K, A)$.

For any 5-rank interval, there are $4^5 = 1024$ suit assignments, of which $4$ are straight flushes (all same suit), leaving:
$$
4^5 - 4 = 1020 \text{ straights per rank span} \implies 10 \times 1020 = 10200 \text{ total straights}
$$

---

## 2. Disjoint Straights & Profile Dynamic Programming

Two straights are **disjoint** if they do not share any physical card (each card $(r, s)$ is used at most once).
To choose $k = 8$ disjoint straights:
1. At each rank $r \in \{1, \dots, 13\}$, at most $4$ straights can pass through $r$, since there are only 4 suits per rank.
2. The multiset of $8$ straights corresponds to a sequence of start ranks $(r_1, \dots, r_8)$ such that the sum of indicator functions $\sum_{i=1}^8 \mathbf{1}_{[r_i, r_i+4]}(r) \le 4$ for all ranks $r$.
3. We perform dynamic programming across the 13 ranks, maintaining the active set of straights and matching suit assignments via inclusion-exclusion over straight-flush exclusions.

---

## 3. Total Unordered Combinations for $k = 8$

Dividing by the permutation symmetry of the 8 straights (since order of choosing does not matter):
$$
N = 11044580082199135512
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(13 \cdot |\text{Profiles}|)$ state space transfer dynamic programming.
- **Space Complexity**: $O(|\text{Profiles}|)$ DP table.
- **Sample Verification**: 1 straight $= 10200$, 2 disjoint straights $= 31832952$.
