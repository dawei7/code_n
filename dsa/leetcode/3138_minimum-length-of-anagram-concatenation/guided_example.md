# Guided Example: Minimum Length of Anagram Concatenation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abba"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.

The objective is to compute `2` from `{"s": "abba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A candidate length must divide the whole string

If `s` is a concatenation of anagrams of some length-$k$ string `t`, then `s` consists of an integer number

$$
q=\frac nk
$$

of blocks, each with length $k$. Therefore, $k$ must divide $n$. The outer loop tests lengths in increasing order and calls `check(i)` only when `n % i == 0`. The first successful length is automatically the minimum requested answer.

Length $n$ always works: there is one block, and `t` may be `s` itself. Thus the function is guaranteed to return even though there is no explicit fallback after the loop.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Anagrams are characterized by letter frequencies

Two strings are anagrams exactly when every letter appears the same number of times in both. Order inside a block does not matter.

The code first builds `cnt = Counter(s)`, the frequency of each character in the complete string. For a candidate block length $k$, there are $q=n/k$ blocks. If every block is an anagram of the same `t`, each block must contain exactly one $q$th share of every global letter count:

$$
q\cdot \operatorname{count}_{block}(c)=\operatorname{count}_{s}(c)
$$

for every character $c$.

Helper `check(k)` slices each aligned block `s[i:i+k]` and builds its counter `cnt1`. It then tests

`cnt1[c] * (n // k) == v`

for every global pair `(c, v)`. If any equality fails, that block cannot have the common frequency vector, so the candidate length is rejected immediately.

There cannot be an extra character in `cnt1` absent from `cnt` because the block is a substring of `s`. Therefore, iterating only over global keys is sufficient.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Two strings are anagrams exactly when every letter appears t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why comparison against global totals works

If all blocks are anagrams, each has the same frequency $a_c$ for letter $c$, and the global count is $q a_c$. Every code equality passes.

Conversely, suppose every block passes. For each global letter $c$, every block's count equals `cnt[c] / q` because the tested product is equal to `cnt[c]`. Thus every block has the same count for every character and all blocks are pairwise anagrams. Any one block can serve as `t`.

This test also rejects impossible divisibility automatically. If a global count $v$ is not divisible by $q$, no integer `cnt1[c]` can satisfy `cnt1[c] * q == v`, so the first inspected block fails.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare each block to the first block:** Build:** - **Compare each block to the first block:** Build the first block's frequency vector and compare all later blocks. This is direct and can avoid global multiplication, with the same per-candidate time.
- **Enumerate divisors first:** Generate divisors in $O(\sqrt n)$ and sort them, avoiding the outer $O(n)$ divisibility scan. The block checks still dominate for many candidates.
- **Prefix frequency arrays:** Precompute 26 prefix counts so each block vector is obtained in $O(26)$ time without slicing. This uses $O(26n)$ space but can reduce repeated character scans.
- **Index-based fixed arrays:** Count each block directly from character indices into a 26-element array. It retains $O(n\tau(n))$ time while avoiding the $O(k)$ slice allocation.
- **Sort each block:** Sorted anagrams compare equal, but sorting every block adds a $\log k$ factor and allocates more data.
- **Length one:** It works only when all characters are identical, because every one-character block must be an anagram of every other.
- **Length n:** It always works because the complete string is one block.
- **Global count not divisible by block count:** The multiplication equality rejects the candidate without requiring an explicit divisibility precheck per character.
- **Repeated arrangements:** Blocks may have completely different orders; only their frequency vectors matter.
- **Early mismatch:** `check` returns immediately on the first differing letter, which improves average time but not the worst-case bound.
- **Fixed alphabet:** The constant-space counter claim for the data structure depends on lowercase English letters. The slice allocation remains input-sized regardless.
- **First passing divisor:** Returning immediately is correct because lengths are visited numerically in ascending order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n sqrt(n))$. Let $\tau(n)$ be the number of positive divisors of $n$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
