# Formal Mathematical Specification: Stable Marriage Problem (Gale-Shapley)

## 1. Definitions and Notation

Let $M = \{m_1, m_2, \dots, m_n\}$ be the set of $n$ men and $W = \{w_1, w_2, \dots, w_n\}$ be the set of $n$ women. 

*   **Preference Relations:** For each $m \in M$, there exists a strict total ordering $\succ_m$ over $W$. Similarly, for each $w \in W$, there exists a strict total ordering $\succ_w$ over $M$. We denote $w_i \succ_m w_j$ if man $m$ prefers woman $w_i$ over $w_j$.
*   **Matching:** A matching $\mu$ is a bijection $\mu: M \cup W \to M \cup W$ such that for all $m \in M$, $\mu(m) \in W$, and for all $w \in W$, $\mu(w) \in M$, satisfying $\mu(\mu(x)) = x$.
*   **Stability:** A matching $\mu$ is **stable** if there exists no pair $(m, w)$ such that:
    1. $w \succ_m \mu(m)$ (Man $m$ prefers woman $w$ over his current partner).
    2. $m \succ_w \mu(w)$ (Woman $w$ prefers man $m$ over her current partner).
    Such a pair $(m, w)$ is called a **blocking pair**.
*   **State Space:** The state of the algorithm at iteration $k$ is defined by the tuple $\mathcal{S}_k = (\text{free\_men}_k, \text{engaged}_k, \text{next\_proposal}_k)$, where $\text{engaged}_k \subset M \times W$ represents the set of current tentative engagements.

## 2. Algebraic Characterization

The Gale-Shapley algorithm constructs a matching $\mu$ through a sequence of proposals. Let $P_m \subseteq W$ be the set of women to whom man $m$ has already proposed.

**Invariant:** At any step of the algorithm, if $m$ is not engaged, then for all $w \in P_m$, $w$ is currently engaged to some $m' \in M$ such that $m' \succeq_w m$.

**Transition Function:**
Let $m$ be a free man. Let $w = \text{argmax}_{\succ_m} \{W \setminus P_m\}$. The transition $\mathcal{S}_k \to \mathcal{S}_{k+1}$ is defined as:
1. If $w$ is unmatched: $\mu(m) = w$.
2. If $w$ is matched to $m'$:
   - If $m \succ_w m'$, then $\mu(m) = w$ and $m'$ becomes free.
   - If $m' \succ_w m$, then $m$ remains free and $P_m = P_m \cup \{w\}$.

**Convergence:**
The algorithm terminates when the set of free men is empty. The number of proposals is bounded by $n^2$, as each man proposes to each woman at most once. Since the set of engaged pairs is monotonically improving for the reviewers (women) in terms of their preference rankings, and the proposers (men) move down their preference lists, the process must terminate in a stable matching $\mu^*$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the number of proposals. 
*   **Upper Bound:** Each man $m \in M$ has a preference list of length $n$. In the worst case, every man proposes to every woman exactly once. Thus, the total number of proposals is bounded by $N^2$.
*   **Per-Proposal Cost:** By pre-computing the inverse preference matrix $R_w \in \mathbb{Z}^{n \times n}$ where $R_w[m]$ returns the rank of man $m$ for woman $w$, the comparison $m \succ_w m'$ is reduced to a constant time lookup: $R_w[m] < R_w[m']$.
*   **Total Time:** The algorithm performs $O(N^2)$ proposals, each requiring $O(1)$ time for preference comparison and pointer updates. Thus, the total time complexity is $T(N) = O(N^2)$.

### Space Complexity
*   **Preference Matrices:** Storing `men_prefs` and `women_prefs` requires $O(N^2)$ space.
*   **Inverse Preference Matrix:** The `woman_rank` matrix requires $O(N^2)$ space to allow $O(1)$ lookup.
*   **Auxiliary Structures:** The arrays `next_w`, `woman_engaged_to`, and `man_engaged_to` each require $O(N)$ space.
*   **Total Space:** The dominant term is the storage of the preference and rank matrices, yielding a total space complexity of $S(N) = O(N^2)$.