# Guided Example: Earliest Possible Day of Full Bloom

We trace the step-by-step execution of the optimal greedy sorting by non-increasing growth time approach on a representative problem instance:

- **Planting Times (`plantTime`):** `[1, 4, 3]`
- **Growth Times (`growTime`):** `[2, 3, 1]`
- **Expected Output:** `9`

This instance demonstrates how overlapping parallel growth periods with sequential planting operations dictates the optimal schedule, proving via an exchange argument why prioritizing seeds with longer growth times minimizes the overall completion day.

---

## 1. Problem Overview & Representative Instance

We have $n$ flower seeds. For each seed $i$:
- `plantTime[i]` is the required planting duration (only one seed can be planted on any given day).
- `growTime[i]` is the autonomous growth duration after planting completes. Multiple seeds can grow concurrently in parallel without human intervention.
- A flower blooms on the day immediately following the end of its growth period.

We must determine the earliest possible day on which all flowers are in full bloom.

Consider our instance with $3$ seeds:
- Seed $0$: $p_0 = 1, g_0 = 2$
- Seed $1$: $p_1 = 4, g_1 = 3$
- Seed $2$: $p_2 = 3, g_2 = 1$

Notice that the sum of all planting times is $1 + 4 + 3 = 8$ days. Planting must occur sequentially, but growth occurs in parallel. Planting Seed 1 (which has the largest growth time $g_1 = 3$) first allows its 3-day growth to overlap with the subsequent planting of Seeds 0 and 2.

---

## 2. Mathematical & Algorithmic Principles

### Conservation of Sequential Planting Work
The gardener must spend a total of $T = \sum_{i=0}^{n-1} p_i$ days planting. Because planting cannot be parallelized, this duration $T$ is an unavoidable lower bound on the completion of the planting phase.

### Parallel Growth Overlap and the Exchange Argument
Consider two candidate adjacent seeds $A$ and $B$ scheduled after an elapsed planting time $t$:
- If we plant $A$ then $B$:
  - $A$ finishes planting at $t + p_A$ and blooms at $t + p_A + g_A$.
  - $B$ finishes planting at $t + p_A + p_B$ and blooms at $t + p_A + p_B + g_B$.
  - Combined completion time:

$$T_{AB} = \max(t + p_A + g_A, t + p_A + p_B + g_B)$$

- If we swap their order to plant $B$ then $A$:
  - $B$ finishes planting at $t + p_B$ and blooms at $t + p_B + g_B$.
  - $A$ finishes planting at $t + p_B + p_A$ and blooms at $t + p_B + p_A + g_A$.
  - Combined completion time:

$$T_{BA} = \max(t + p_B + g_B, t + p_B + p_A + g_A)$$

Suppose $g_B > g_A$. Then:
1. $t + p_A + p_B + g_B > t + p_B + g_B$ because $p_A > 0$.
2. $t + p_A + p_B + g_B > t + p_B + p_A + g_A$ because $g_B > g_A$.
Therefore, $T_{AB} > T_{BA}$. Swapping $B$ ahead of $A$ strictly reduces or preserves the makespan of the pair without affecting the start times of subsequent seeds (since $p_A + p_B = p_B + p_A$).

Thus, ordering seeds by **non-increasing growth time** ($g_{(1)} \ge g_{(2)} \ge \dots \ge g_{(n)}$) is mathematically optimal.

| Schedule Metric | Definition | Mathematical Formula |
|---|---|---|
| Cumulative Plant Time ($P$) | End of planting for $k$-th seed | $P_k = \sum_{j=1}^k p_{(j)}$ |
| Individual Bloom Day | Day when $k$-th seed blooms | $B_k = P_k + g_{(k)}$ |
| Global Makespan | Day when all flowers bloom | $\max_{1 \le k \le n} B_k$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Original seed parameters:
- Seed 0: $p = 1, g = 2$
- Seed 1: $p = 4, g = 3$
- Seed 2: $p = 3, g = 1$

### Step 1: Sorting by Descending Growth Time
Sorting pairs $(p, g)$ by $g$ descending:
1. Seed 1: $(p = 4, g = 3)$
2. Seed 0: $(p = 1, g = 2)$
3. Seed 2: $(p = 3, g = 1)$

Initialize cumulative plant days $P = 0$, global bloom day $\mu = 0$.

### Step 2: Processing Seed 1 ($p = 4, g = 3$)
- Planting duration: $4$ days (Days $0 \dots 3$).
- Cumulative planting days: $P \leftarrow 0 + 4 = 4$.
- Bloom day for Seed 1: $P + g = 4 + 3 = 7$.
- Running makespan: $\mu = \max(0, 7) = 7$.

### Step 3: Processing Seed 0 ($p = 1, g = 2$)
- Planting duration: $1$ day (Day $4$).
- Cumulative planting days: $P \leftarrow 4 + 1 = 5$.
- Bloom day for Seed 0: $P + g = 5 + 2 = 7$.
- Running makespan: $\mu = \max(7, 7) = 7$.

### Step 4: Processing Seed 2 ($p = 3, g = 1$)
- Planting duration: $3$ days (Days $5 \dots 7$).
- Cumulative planting days: $P \leftarrow 5 + 3 = 8$.
- Bloom day for Seed 2: $P + g = 8 + 1 = 9$.
- Running makespan: $\mu = \max(7, 9) = 9$.

All seeds planted. Full bloom achieved on day $9$.

---

## 4. Comprehensive State Trace

The chronological progression across the sorted sequence is detailed below:

| Sequence Rank | Original Seed ID | Planting Time $p$ | Growth Time $g$ | Planting Interval | Plant End Day ($P$) | Bloom Day ($P + g$) | Running Makespan ($\mu$) |
|---|---|---|---|---|---|---|---|
| $1$ | Seed 1 | $4$ | $3$ | $[0, 4)$ | $4$ | $4 + 3 = 7$ | $7$ |
| $2$ | Seed 0 | $1$ | $2$ | $[4, 5)$ | $5$ | $5 + 2 = 7$ | $7$ |
| $3$ | Seed 2 | $3$ | $1$ | $[5, 8)$ | $8$ | $8 + 1 = 9$ | $9$ |

Earliest possible day of full bloom: $9$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Every seed $i$ finishes planting at cumulative day $P_i$ and requires an additional $g_i$ days of uninterrupted growth. Thus, flower $i$ cannot bloom before day $P_i + g_i$. All flowers are in full bloom if and only if the current day is at least $\max_i (P_i + g_i)$.

**Completeness.** By the exchange argument, any adjacent inversion where $g_i < g_{i+1}$ can be swapped to non-increasing order without increasing the maximum bloom day. Because adjacent transpositions can sort any permutation and each swap preserves or improves the makespan, the sorted sequence $g_{(1)} \ge g_{(2)} \ge \dots$ achieves the global minimum across all $n!$ possible permutations.

---

## 6. Edge Cases & Anti-Patterns

- **Equal Growth Times:** When two seeds have identical growth times ($g_A = g_B$), their relative order does not affect the pair's maximum completion day ($T_{AB} = T_{BA}$), making any tie-breaking rule valid.
- **Single Seed ($n = 1$):** With only one seed, the bloom day is simply $p_0 + g_0$.
- **Dominant Growth Tail:** A seed with massive growth time (e.g. $p = 1, g = 10^9$) planted first overlaps with all subsequent planting, preventing unnecessary delays.
- **Anti-Pattern — Sorting by Planting Time:** Sorting by shortest planting time first can delay seeds with enormous growth periods, causing late-blooming bottlenecks. Growth time alone dictates priority.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \log n)$, where $n$ is the number of seeds. Pairing and sorting the $n$ seeds by growth time takes $\mathcal{O}(n \log n)$ time. The subsequent linear accumulation pass takes $\mathcal{O}(n)$ time.
- **Auxiliary Space Complexity:** $\mathcal{O}(n)$ to store the zipped index pairs for sorting.
