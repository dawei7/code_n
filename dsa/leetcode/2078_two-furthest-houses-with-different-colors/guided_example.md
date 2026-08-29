# Guided Example: Two Furthest Houses With Different Colors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"colors": [1, 1, 1, 6, 1, 1, 1]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` houses evenly lined up on the street, and each house is beautifully painted. You are given a **0-indexed** integer array `colors` of length `n`, where $\text{colors}[i]$ represents the color of the $i^{\text{th}}$ house.

The objective is to compute `3` from `{"colors": [1, 1, 1, 6, 1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Start with the largest distance that could possibly exist

For an array of length `n`, no two indices can be farther apart than 0 and `n - 1`. Their distance is $n-1$. The solution therefore compares the colors at the two endpoints first.

If `colors[0] != colors[-1]`, the endpoint pair is valid and already reaches the absolute maximum possible distance. No scan or further proof of a better pair is needed, so the code immediately returns `n - 1`.

This early return handles every input whose outermost houses have different colors, regardless of what appears between them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"colors": [1, 1, 1, 6, 1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When endpoint colors match, find the first disagreement from each side

The more interesting case is

`colors[0] == colors[-1]`.

Call this shared endpoint color $c$. A valid pair cannot use both endpoints because they have the same color. However, the problem guarantees that at least two houses have different colors, so at least one interior house has a color different from $c$.

The first loop starts `i` at 1 and advances while `colors[i] == colors[0]`. When it stops, `i` is the smallest index whose color differs from $c$.

Pairing this house with the right endpoint is valid:

- house `i` has a color different from $c$;
- house `n - 1` has color $c$;
- their distance is `n - 1 - i`, written by the source as `n - i - 1`.

Because `i` is the earliest disagreement, no different-colored house lies farther left. Therefore, among all valid pairs using the right endpoint, this pair has the greatest possible distance.

The second loop starts `j` at `n - 2` and moves left while `colors[j] == colors[0]`. When it stops, `j` is the largest index whose color differs from $c$.

Pairing this house with the left endpoint is valid, and its distance from index 0 is simply `j`. Because `j` is the latest disagreement, it is the farthest valid partner for the left endpoint.

The answer is the larger of these two endpoint-based candidates:

`max(n - i - 1, j)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why an optimal pair always touches an endpoint

The key greedy fact is that some maximum-distance valid pair uses index 0 or index `n - 1`.

Consider any valid pair with indices $a<b$ and different colors. If `colors[a]` differs from the right endpoint's color, then `(a, n-1)` is also valid and its distance is at least $b-a$, because $n-1\ge b$.

Otherwise, `colors[a]` equals the right endpoint's color. Since `colors[a] != colors[b]`, house `b` must differ from the right endpoint.

- If the two endpoint colors differ, pair `(0, n-1)` is already the global maximum, which the early return handles.
- In the remaining case, the endpoints share color $c$. Then `colors[a] = c` and `colors[b] != c`, so pair `(0, b)` is valid and has distance $b$, which is at least $b-a$.

Thus an interior valid pair can always be extended to an endpoint without decreasing its distance. Searching the best valid partner for each endpoint is sufficient.

The exact source makes this even simpler by separating the two endpoint-color cases. When endpoints differ, use both. When they match, every house with a non-$c$ color is a valid partner for either endpoint, so only the leftmost and rightmost such houses matter.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"colors": [1, 1, 1, 6, 1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerating every pair:** Testing all $O(n^2)$ pairs is straightforward and correct, but the endpoint lemma makes almost all of those comparisons unnecessary.
- **One editorial-style pass:** One can scan all indices and update endpoint-based candidate distances whenever a color differs from an endpoint color. That is also $O(n)$; the exact source instead uses an early return plus two boundary searches.
- **Tracking positions for every color:** A map from color to extreme indices can solve the problem, but the answer needs only disagreement with the endpoints, so the extra storage and bookkeeping are unnecessary.
- **Different endpoint colors:** Return `n - 1` immediately. No interior pair can exceed the full-array span.
- **Matching endpoint colors:** Some interior position must differ under the problem guarantee. The two scans locate the extreme such positions safely.
- **Exactly two houses:** Their colors must differ, so the answer is 1 and the early-return branch handles it.
- **Only one exceptional house:** Both scans stop at that same index. The algorithm compares its distance to each endpoint and chooses the farther one.
- **Several non-endpoint colors:** Their identities relative to one another do not matter. Every color different from the common endpoint color is a valid endpoint partner, so only their extreme positions matter.
- **Long equal-color prefix:** The left scan skips it once. The first disagreement is the best partner for the right endpoint because moving farther right can only shorten that distance.
- **Long equal-color suffix:** The right scan skips it once. The final disagreement is the best partner for the left endpoint.
- **Input guarantee is essential:** If every house had the same color, the unguarded scans could leave the array bounds and no valid answer would exist. The stated guarantee rules out that invalid domain.
- **No input mutation:** Because the array is only inspected, callers retain the original color ordering after the result is computed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of houses.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
