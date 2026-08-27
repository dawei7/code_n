# Guided Example: Sort Characters By Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "tree"}`
- **Required output:** `"eetr"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

The objective is to compute `"eetr"` from `{"s": "tree"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count frequencies with `Counter`

`Counter(s)` scans the string and builds a mapping from each character to its number of occurrences. For `s = "tree"`, the mapping contains `t: 1`, `r: 1`, and `e: 2`. Uppercase and lowercase characters are different keys, so `A` and `a` are counted independently without any special logic.

A frequency map is the right summary because the desired order depends only on counts. Once it has been built, the original positions of equal characters no longer matter. The final construction will deliberately gather all copies of a character into one contiguous group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "tree"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a negative sort key produces decreasing order

`cnt.items()` supplies `(character, frequency)` pairs. Python's `sorted` orders keys in increasing order by default. The key function `lambda x: -x[1]` negates each frequency, so a larger original frequency becomes a smaller key:

$$
5 > 2 \quad\Longrightarrow\quad -5 < -2.
$$

Ascending order of the negative values is therefore descending order of the actual frequencies. The code does not need a secondary key. When two characters have equal frequency, either relative order is accepted by the contract.

Python's sort is stable, and `Counter` preserves the first-insertion order of keys in current Python versions, so tied groups commonly follow the order in which their characters first appeared. That behavior is not part of the algorithm's correctness and should not be relied upon by tests: the problem explicitly allows any tie order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt.items()` supplies `(character, frequency)` pairs.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build one contiguous block per character

For every sorted pair `(c, v)`, the expression `c * v` creates a string containing `v` copies of `c`. If the pair is `('e', 2)`, the group is `"ee"`. The generator supplies those groups to `''.join(...)`, which combines them into one output string.

Using `join` is important. Python strings are immutable, so repeatedly doing `answer += group` can repeatedly copy the growing prefix and lead to unnecessary quadratic work. `join` knows all pieces and constructs the final string efficiently.

For `s = "tree"`, the `e` group has frequency two and must come before the one-character `t` and `r` groups. Depending on tie order, the result may be `"eetr"` or `"eert"`; both are valid.

For `s = "cccaaa"`, the two groups both have frequency three. Either `"cccaaa"` or `"aaaccc"` is correct. An interleaving such as `"cacaca"` is not produced, because the reconstruction creates exactly one complete block for each distinct character.

For `s = "Aabb"`, `b` has frequency two, while `A` and `a` each have frequency one. The `bb` group comes first, and the case-distinct singletons may follow in either order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"eetr"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "tree"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"eetr"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Bucket sort by frequency:** Place each distinc:** - **Bucket sort by frequency:** Place each distinct character in a bucket indexed by its count, then scan frequencies from `n` down to `1`. This gives $O(n)$ time even for a growing alphabet, at the cost of an $O(n)$ bucket structure.
- **Heap of distinct characters:** A max-heap can repeatedly extract the largest frequency in $O(k\log k)$ time. It is useful for streaming variants but adds complexity here.
- **Sort all input characters:** A comparator based on frequency can sort all `n` occurrences, but that costs $O(n\log n)$ and must still ensure identical characters remain grouped.
- **Repeated string concatenation:** Logically correct, but immutable-string copying can make construction quadratic. Building pieces and calling `join` avoids that trap.
- **Single character:** The counter has one entry, sorting changes nothing, and the original one-character string is returned.
- **All characters identical:** One group of length `n` is emitted, so the answer equals the input.
- **All frequencies equal:** Any ordering of the character groups is valid; the algorithm's stable tie order is merely one allowed choice.
- **Uppercase versus lowercase:** `A` and `a` are separate counter keys and may have different frequencies.
- **Digits:** Digits are ordinary one-character keys; numeric value plays no role.
- **Empty string outside this contract:** The exact code would return an empty string naturally, although the stated input is nonempty.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $n$ be the length of `s`, and let $k$ be the number of distinct characters.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
