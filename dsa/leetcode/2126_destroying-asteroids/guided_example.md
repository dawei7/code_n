# Guided Example: Destroying Asteroids

We trace the step-by-step execution of the optimal greedy sorting approach on a representative problem instance:

- **Initial Planet Mass (`mass`):** $10$
- **Asteroid Masses (`asteroids`):** `[3, 9, 19, 5, 21]`
- **Expected Output:** `true`

This instance demonstrates why confronting asteroids in monotonically increasing order of mass represents an optimal greedy choice, proving how each smaller victory accumulates mass to overcome larger subsequent obstacles.

---

## 1. Problem Overview & Representative Instance

We control a planet with initial mass $M_0$. A field of asteroids with masses $A = [a_1, a_2, \dots, a_n]$ surrounds the planet. We may engage asteroids in any chosen permutation.
When the planet collides with an asteroid of mass $a$:
- If current planet mass $M \ge a$, the asteroid is destroyed, and its mass is permanently absorbed: $M \leftarrow M + a$.
- If current planet mass $M < a$, the planet is destroyed and the mission fails.

We must determine whether an ordering exists such that all asteroids can be successfully absorbed.

Consider our instance with initial mass $M_0 = 10$ and asteroids `[3, 9, 19, 5, 21]`:
- Engaging asteroid $19$ or $21$ immediately would cause catastrophic failure ($10 < 19$).
- Engaging smaller asteroids first ($3$, $5$, $9$) boosts the planet's mass to $27$, easily overpowering $19$ and subsequently $21$.

---

## 2. Mathematical & Algorithmic Principles

### Monotonic Feasibility Dominance
Suppose at some stage the planet has mass $M$ and a remaining multiset of asteroids $S$.
Let $x = \min(S)$ be the minimal mass among all remaining asteroids:
1. **Impossibility Condition:** If $M < x$, then because $x \le y$ for all $y \in S$, we have $M < y$ for every remaining asteroid. The planet cannot destroy any asteroid in $S$. Therefore, no valid continuation exists regardless of permutation.
2. **Monotonic Gain:** If $M \ge x$, absorbing $x$ increases the planet's mass to $M' = M + x > M$. Since mass accumulation is monotonic and non-decreasing, taking $x$ early never restricts future choices; it strictly expands the set of destroyable asteroids.

### Greedy Sorting Strategy
Because the optimal choice at every stage is always to engage the smallest available asteroid, sorting the entire array `asteroids` in non-decreasing order:

$$a_{(1)} \le a_{(2)} \le \dots \le a_{(n)}$$

guarantees that if any valid permutation exists, the sorted order will succeed.
We verify:

$$M_0 + \sum_{j=1}^{i-1} a_{(j)} \ge a_{(i)} \quad \forall i \in \{1, \dots, n\}$$

| Step Parameter | Meaning | Update Relation |
|---|---|---|
| Asteroid $a_{(i)}$ | $i$-th smallest asteroid | Tested against current mass |
| Collision Condition | Required threshold | $M_{i-1} \ge a_{(i)}$ |
| Post-Collision Mass | Mass absorbed | $M_i = M_{i-1} + a_{(i)}$ |
| Termination Condition | Early abort trigger | $M_{i-1} < a_{(i)} \implies \text{return false}$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Initial state: `mass = 10`.
Input asteroids: `[3, 9, 19, 5, 21]`.
Sorting in ascending order yields: `[3, 5, 9, 19, 21]`.

### Collision 1: Asteroid $a_{(1)} = 3$
- Current planet mass: $10$.
- Comparison: $10 \ge 3$ (Successful collision).
- Absorbed mass: $10 + 3 = 13$.

### Collision 2: Asteroid $a_{(2)} = 5$
- Current planet mass: $13$.
- Comparison: $13 \ge 5$ (Successful collision).
- Absorbed mass: $13 + 5 = 18$.

### Collision 3: Asteroid $a_{(3)} = 9$
- Current planet mass: $18$.
- Comparison: $18 \ge 9$ (Successful collision).
- Absorbed mass: $18 + 9 = 27$.

### Collision 4: Asteroid $a_{(4)} = 19$
- Current planet mass: $27$.
- Comparison: $27 \ge 19$ (Successful collision).
- Absorbed mass: $27 + 19 = 46$.

### Collision 5: Asteroid $a_{(5)} = 21$
- Current planet mass: $46$.
- Comparison: $46 \ge 21$ (Successful collision).
- Absorbed mass: $46 + 21 = 67$.

All $5$ asteroids have been destroyed. The final output is `true`.

---

## 4. Comprehensive State Trace

The detailed execution trace across the sorted sequence is tabulated below:

| Sequence Index $i$ | Asteroid Mass $a_{(i)}$ | Planet Mass Before Impact | Threshold Check ($M \ge a_{(i)}$) | Collision Outcome | Planet Mass After Impact |
|---|---|---|---|---|---|
| $1$ | $3$ | $10$ | $10 \ge 3$ (True) | Destroyed & Absorbed | $13$ |
| $2$ | $5$ | $13$ | $13 \ge 5$ (True) | Destroyed & Absorbed | $18$ |
| $3$ | $9$ | $18$ | $18 \ge 9$ (True) | Destroyed & Absorbed | $27$ |
| $4$ | $19$ | $27$ | $27 \ge 19$ (True) | Destroyed & Absorbed | $46$ |
| $5$ | $21$ | $46$ | $46 \ge 21$ (True) | Destroyed & Absorbed | $67$ |

Final verification: All collisions succeed, returning `true`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Every collision is verified against the strict inequality $M \ge a$. When this condition holds, the planet absorbs $a$ and gains mass, accurately reflecting the physical rules defined by the problem.

**Completeness.** By exchange argument, suppose there exists an optimal permutation $\pi$ that destroys all asteroids. If $\pi$ does not match sorted order, there must exist two adjacent asteroids $\pi_k > \pi_{k+1}$. Because the planet was able to destroy $\pi_k$, its mass prior to step $k$ was at least $\pi_k$. Since $\pi_k > \pi_{k+1}$, its mass was strictly greater than $\pi_{k+1}$. Swapping $\pi_k$ and $\pi_{k+1}$ allows the planet to destroy $\pi_{k+1}$ first, gaining its mass and making the subsequent collision with $\pi_k$ even safer. Repeatedly applying adjacent inversions sorts the permutation without ever violating feasibility. Thus, if any valid permutation exists, the sorted order is guaranteed to be valid.

---

## 6. Edge Cases & Anti-Patterns

- **Immediate Failure on Smallest Element:** If `mass` is strictly less than the smallest asteroid in the array ($M < \min(A)$), the algorithm halts on the very first comparison, returning `false` in $\mathcal{O}(1)$ checks after sorting.
- **Equal Mass Collisions:** If $M = a$, the rule $M \ge a$ permits destruction, correctly allowing equal-mass absorption.
- **Large Cumulative Mass:** With $10^5$ asteroids of mass up to $10^5$, total mass can reach $10^{10}$, requiring standard 64-bit integers in typed languages to prevent arithmetic overflow.
- **Anti-Pattern — Dynamic Max/Min Heap:** Maintaining a priority queue of available asteroids dynamically takes $\mathcal{O}(n \log n)$ time with high constant overhead. Static sorting accomplishes the exact same greedy order in a single contiguous memory pass.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \log n)$, where $n$ is the number of asteroids. Sorting the array takes $\mathcal{O}(n \log n)$ comparisons. The subsequent greedy simulation traverses the sorted array in a single linear pass taking $\mathcal{O}(n)$ time.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$ or $\mathcal{O}(n)$ depending on the in-place sorting implementation (e.g. Heapsort uses $\mathcal{O}(1)$ auxiliary space, Timsort uses $\mathcal{O}(n)$).
