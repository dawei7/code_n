# Guided Example: Resulting String After Adjacent Removals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abc"}`
- **Required output:** `"c"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `"c"` from `{"s": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recognizing consecutive letters

Lowercase English letters have consecutive character codes. For ordinary neighbors such as `'a'` and `'b'` or `'m'` and `'n'`, the absolute code difference is one.

The alphabet is circular, so `'a'` and `'z'` are also consecutive. Their code difference is 25. Therefore

`abs(ord(c) - ord(stk[-1])) in (1, 25)`

recognizes every removable pair in either order:

- difference `1` covers ordinary alphabet neighbors;
- difference `25` covers the wraparound pair `a/z`;
- the absolute value makes order irrelevant.

Equal letters have difference zero and are not removed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The stack invariant

After processing the first `t` input characters, `stk` equals the string produced by repeatedly applying the required leftmost-removal rule to exactly that prefix until no removable adjacent pair remains.

This invariant gives both correctness and efficiency.

Initially the processed prefix is empty and the empty stack is its reduced result.

Now assume the invariant holds before reading character `c`. The stack contains no removable adjacent pair; if it did, the prefix would not be fully reduced. Appending `c` cannot change adjacency between any earlier stack characters. The only newly created adjacent pair is `(stk[-1], c)`, provided the stack is nonempty.

- If that pair is not consecutive, no removal is possible anywhere, so appending `c` gives the fully reduced new prefix.
- If it is consecutive, that boundary pair is the only possible removable pair and hence is necessarily the leftmost one. Popping `stk[-1]` while discarding `c` performs exactly that required removal.

After a pop, no second removal is immediately necessary. The character now at the top of the stack has no new character to its right: the incoming `c` was removed together with the old top. The remaining stack is a prefix of the previously reduced stack, so it still contains no removable internal pair.

Thus the invariant holds after every character. At the end, the stack is exactly the mandated final string.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why this respects “leftmost,” not merely some removal order

It is important not to assume that arbitrary removal orders always produce the same result. The proof above ties the stack to the stated leftmost process.

Before a new input character is considered, every removable pair wholly inside the earlier prefix has already been handled. When the new character creates a removable boundary pair, there is no earlier removable pair remaining to its left. The boundary pair is therefore the precise pair the rule would choose next.

The left-to-right stream effectively pauses after each input character until the available prefix is reduced. That is why the stack result matches the specified deterministic sequence of operations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"c"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"c"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly scan and delete from the string:** This directly follows the statement but can require `O(n)` work per deletion due to searching and rebuilding, leading to `O(n^2)` time.
- **Linked list plus a moving pointer:** A linked structure can delete adjacent nodes cheaply, but finding and revisiting the correct leftmost candidate requires more bookkeeping. The stack is the natural representation for a left-to-right cancellation rule.
- **Use modular alphabet indices:** Mapping letters to `0` through `25` and checking whether their circular distance is one is equivalent. The source’s code differences `1` and `25` are simpler for lowercase ASCII-compatible ordering.
- **Ignore the circular pair:** Checking only absolute difference one would fail on `"az"` and `"za"`, both of which must disappear.
- **Empty stack:** The condition begins with `stk and ...`, so the source never reads `stk[-1]` when no survivor exists.
- **One-character input:** The character is pushed and returned because no adjacent pair exists.
- **Two removable characters:** They produce an empty stack and therefore the empty string.
- **Equal adjacent letters:** Their code difference is zero, so they remain; equal letters are not consecutive under the rule.
- **Complete cancellation:** `join` of an empty list is `""`, so no special return branch is needed.
- **No cancellation:** Every character remains in original order because the stack only appends, and the output equals `s`.
- **New adjacency after a removal:** The exposed stack top is compared with the next input character when it arrives, exactly as in the `"adcb"` trace.
- **Order sensitivity:** The invariant proves this stack simulates the required leftmost sequence; it is not relying on an unstated freedom to choose arbitrary removable pairs.
- **Lowercase constraint:** The `ord` difference test depends on the promised lowercase English alphabet. Other alphabets or case combinations would require a different successor relation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `s`. Each character causes constant-time stack work. Across the entire run there are at most `n` pushes and at most `n/2` pops, so the scan takes `O(n)` time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
