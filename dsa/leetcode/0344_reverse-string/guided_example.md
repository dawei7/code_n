# Guided Example: Reverse String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": ["h", "e", "l", "l", "o"]}`
- **Required output:** `["o", "l", "l", "e", "h"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function that reverses a string. The input string is given as an array of characters `s`.

The objective is to compute `["o", "l", "l", "e", "h"]` from `{"s": ["h", "e", "l", "l", "o"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reversal pairs each position with one mirrored position.

For an array of length $n$, the character originally at index $p$ belongs at index

$$
n-1-p
$$

in the reversed array. This mapping is symmetric: the character at `n - 1 - p` belongs at `p`. Therefore reversal can be performed by swapping mirrored pairs rather than creating a second array.

The exact source keeps two indices:

- `i = 0`, initially pointing at the first character;
- `j = len(s) - 1`, initially pointing at the last character.

At every iteration, `i` and `j` identify a mirrored pair that has not yet been placed. Swapping `s[i]` and `s[j]` sends both characters directly to their final reversed positions. The pointers then move inward with `i + 1` and `j - 1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": ["h", "e", "l", "l", "o"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the swap is safe in Python.

The assignment

`s[i], s[j] = s[j], s[i]`

evaluates the right-hand values before writing the left-hand positions. Conceptually, it remembers both old characters and then places them in opposite slots. The first write cannot destroy the value needed by the second write.

In a language without tuple assignment, the same operation would use one temporary character:

1. save the left character;
2. copy the right character into the left position;
3. copy the saved character into the right position.

That temporary is constant-sized, so either form remains an in-place, $O(1)$-auxiliary-space algorithm.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The assignment

`s[i], s[j] = s[j], s[i]`

evaluates the rig... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The key loop invariant.

Before each loop-condition check:

- every position strictly before `i` already contains its final reversed character;
- every position strictly after `j` already contains its final reversed character;
- positions from `i` through `j` are the only part still needing work.

Initially, there are no positions before zero and no positions after `n - 1`, so the invariant is true.

During an iteration, index `i` is mirrored with `j`. At the first iteration, these are `0` and `n - 1`. After both pointers have moved the same number of steps inward, they remain mirrored because

$$
j=n-1-i.
$$

The swap puts both boundary characters of the unresolved interval into their final positions. Incrementing `i` and decrementing `j` then moves those positions into the already-correct outer regions, preserving the invariant.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["o", "l", "l", "e", "h"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": ["h", "e", "l", "l", "o"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["o", "l", "l", "e", "h"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Create a reversed copy:** Slicing with `s[::-1:** - **Create a reversed copy:** Slicing with `s[::-1]` or building a new list is concise, but a standalone copy uses $O(n)$ extra memory. Assigning a slice back may also allocate temporary storage and therefore misses the strict $O(1)$ requirement.
- **- **Built-in in-place reverse:** A library method :** - **Built-in in-place reverse:** A library method such as `s.reverse()` typically performs the same mirrored swaps and can satisfy the contract, but the explicit source makes the two-pointer reasoning visible.
- **- **Recursive mirrored swaps:** Swap the ends and :** - **Recursive mirrored swaps:** Swap the ends and recurse inward. It mutates the list in place but consumes $O(n)$ call-stack space, violating the constant-extra-memory requirement.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`. Each iteration finalizes two positions, so the loop performs $\lfloor n/2\rfloor$ swaps. Each swap and pointer update is constant time. Total time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
