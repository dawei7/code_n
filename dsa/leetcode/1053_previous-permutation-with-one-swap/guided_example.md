# Guided Example: Previous Permutation With One Swap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [3, 2, 1]}`
- **Required output:** `[3, 1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of positive integers `arr` (not necessarily distinct), return *the **lexicographically** largest permutation that is smaller than* `arr`, that can be **made with exactly one swap**. If it cannot be done, then return the same array.

The objective is to compute `[3, 1, 2]` from `{"arr": [3, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Understand what "largest but smaller" demands

Lexicographic comparison examines arrays from left to right. At the first index where two arrays differ, the array with the smaller value at that index is lexicographically smaller; later positions cannot reverse that decision.

We need an array smaller than `arr`, so the first position changed by the swap must receive a smaller value. Among all arrays satisfying that requirement, we want the largest one. This creates three priorities in order:

1. Preserve the original prefix for as long as possible.
2. At the first changed position, place the largest available value that is still smaller than the original value.
3. If duplicate copies of that chosen value exist, swap with the copy that leaves the suffix as large as possible.

The code realizes these priorities using two right-to-left scans and one swap.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [3, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Locate the rightmost position that can be decreased

The outer loop is:



The loop begins at the final index and moves left. It looks for the first adjacent descent `arr[i - 1] > arr[i]`.

At such a descent, the value at `i - 1` can certainly be decreased: `arr[i]` is to its right and is strictly smaller, so those two positions could be swapped to make the array lexicographically smaller.

Because the scan starts at the right, `i - 1` is the rightmost index that can serve as the first changed position. Choosing it preserves more of the original prefix than choosing any earlier index. Since lexicographic order prioritizes that unchanged prefix before all later values, no solution whose first change occurs earlier can be larger.

The absence of a descent to the right also tells us something important about the suffix. Once the loop finds the rightmost descent, every adjacent pair inside `arr[i:]` is non-decreasing. If a later pair descended, the loop would have found it first. Thus:



This ordered suffix lets the second right-to-left scan identify the best swap partner without sorting.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a swap cannot first decrease a later index

Suppose one tries to preserve the prefix through an index later than `i - 1`. The suffix beginning at `i` is already non-decreasing. At any suffix position `p`, every value to its right is at least `arr[p]`. Swapping `arr[p]` with a later value therefore cannot put a strictly smaller number at `p`.

So no one-swap permutation can have its first decrease strictly to the right of the found pivot. The pivot at `i - 1` is not merely a convenient choice; it is the latest possible first difference.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [3, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate all swaps:** Trying every pair, keeping only smaller results, and selecting the largest takes `O(N^3)` time if every candidate array is copied and compared naively. It ignores the strong lexicographic structure used by the two scans.
- **Sort candidate permutations:** Materializing all one-swap results also requires quadratic candidate count and substantial memory. The pivot argument identifies the winner directly in linear time.
- **Choose the first smaller suffix value:** Scanning the suffix from left to right and accepting the first smaller value can place a value much smaller than necessary at the pivot. The result is valid but not lexicographically largest.
- **Choose the rightmost duplicate blindly:** When the best candidate value appears more than once, using its rightmost occurrence puts the displaced pivot later. Choosing the leftmost duplicate makes the suffix larger.
- **Strictly increasing input:** A strictly increasing array has no descent and is already its multiset's smallest permutation. The function returns it unchanged.
- **All values equal:** Every possible swap leaves the array identical. There is no smaller permutation, so returning the same array is correct.
- **Single element:** There is no pair of positions to swap. The outer range is empty and the original one-element list is returned.
- **Strictly decreasing input:** The rightmost adjacent pair is immediately a descent. Swapping the final two values makes the smallest possible change near the end and gives the largest smaller permutation.
- **Duplicates around the pivot:** The strict candidate test rejects values equal to the pivot, while the neighboring-value guard walks across duplicates of the selected smaller value to their leftmost occurrence.
- **Exactly one swap wording:** When a smaller permutation exists, the code performs exactly one swap. When none exists, the contract explicitly permits returning the unchanged array.
- **Input mutation:** The solution changes `arr` in place. This matches the returned-array contract, but callers retaining the old order must pass a copy.
- **Positive-value constraint:** The reasoning depends only on comparisons, so it would also work for zero or negative integers. Positivity does not require special handling.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the length of `arr`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
