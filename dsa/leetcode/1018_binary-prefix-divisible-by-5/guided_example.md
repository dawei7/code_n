# Guided Example: Binary Prefix Divisible By 5

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 1]}`
- **Required output:** `[true, false, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary array `nums` (**0-indexed**).

The objective is to compute `[true, false, false]` from `{"nums": [0, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: How one more binary digit changes a prefix

Let the numeric value of the prefix ending just before the current bit be `P`. Appending a binary bit `v` shifts every existing digit one place to the left and places `v` in the units position. Numerically, the new prefix is

$$
P_{\text{new}} = 2P + v.
$$

For example, binary `101` has value five. Appending zero gives `1010`, whose value is ten, and appending one would give `1011`, whose value is eleven. This recurrence makes a left-to-right traversal natural: the next prefix depends only on the preceding prefix and the next bit.

A tempting implementation would store the complete value and repeatedly compute `P = 2 * P + v`. The array may contain `10^5` bits, however, so the full prefix can have tens of thousands of decimal digits. Fixed-width languages would overflow quickly, and even Python's arbitrary-precision integers would spend increasing time and memory manipulating enormous numbers.

The task never asks for the prefix values themselves. It asks only whether each value is divisible by five. Divisibility depends solely on the remainder modulo five, so all information beyond that remainder can be discarded.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why keeping only the remainder loses nothing

Suppose `P = 5q + r`, where `r` is the remainder and therefore lies between zero and four. After appending `v`,

$$
2P + v = 2(5q + r) + v = 10q + 2r + v.
$$

The term `10q` is divisible by five. It contributes nothing to the new remainder. Consequently,

$$
(2P + v) \bmod 5 = (2r + v) \bmod 5.
$$

This identity is the entire reason the algorithm can remain constant-sized. Whether the discarded quotient `q` is small or unimaginably large makes no difference to the next remainder.

The variable `x` stores this remainder. It begins at zero, which is the value of the empty prefix modulo five. For each input bit `v`, the statement `x = (x << 1 | v) % 5` computes the next remainder.

The expression `x << 1` shifts `x` left by one bit and is numerically equal to `2 * x`. Because a left shift makes the low bit zero and `v` is guaranteed to be either zero or one, bitwise OR with `v` puts that bit into the newly opened low position. Therefore, `x << 1 | v` equals `2 * x + v` for every valid input. The parentheses ensure the complete append operation is reduced modulo five afterward.

After the update, `ans.append(x == 0)` adds a Boolean for the prefix that now includes `v`. A number is divisible by five exactly when its remainder modulo five is zero. The comparison produces Python `true` or `false` directly, so no later conversion is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A step-by-step trace

Take `nums = [0, 1, 1]`. Initially `x = 0` and `ans` is empty.

The first bit is zero. Shifting zero and appending zero still gives zero, and zero modulo five is zero. The code appends `true`. This correctly recognizes that the one-bit prefix `0` represents the number zero, which is divisible by five.

The second bit is one. The update computes `2 * 0 + 1 = 1`, whose remainder is one. The code appends `false`. Notice that the written prefix `01` is allowed in the input even though standard integer representations do not use a leading zero; its numeric value is still one.

The third bit is one. The update computes `2 * 1 + 1 = 3`, whose remainder is three. The code appends another `false`. The final result is `[true, false, false]`.

For a trace that demonstrates remainder reuse, consider prefix value `13`, whose remainder modulo five is three. Appending bit one creates `27`. The algorithm does not need thirteen: it computes `2 * 3 + 1 = 7` and reduces that to remainder two, exactly matching `27 \bmod 5`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, false, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, false, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build every full prefix integer:** This follows the same recurrence but omits the per-step modulo. It is mathematically simple, yet it overflows fixed-width types and makes Python arithmetic progressively more expensive. Retaining only the remainder is both safer and more efficient.
- **Convert each prefix slice independently:** Joining `nums[0..i]` into text and parsing it repeats almost all earlier work for every index, leading to quadratic total input processing and many temporary objects.
- **Use decimal divisibility rules:** Rules based on the final decimal digit do not apply directly to a binary digit stream. The modular recurrence works in any base and uses the actual base-two construction.
- **Store a table of five transitions:** A small table could map each pair of current remainder and next bit to the next remainder. That is equivalent to the formula and can remove arithmetic, but it is less transparent and does not improve the asymptotic bounds.
- **Use addition instead of bitwise OR:** `(x * 2 + v) % 5` or `((x << 1) + v) % 5` is equally correct. OR works only because valid `v` is zero or one and the shifted value's low bit is zero.
- **Leading zeroes:** Prefixes may begin with one or many zeroes. They do not require special handling because appending zero to remainder zero keeps it zero, and numeric value is independent of written leading zeroes.
- **The value zero:** Zero is divisible by five. Therefore, any all-zero prefix correctly produces `true`.
- **A one-element array:** The loop appends exactly one answer. Input `[0]` returns `[true]`, while `[1]` returns `[false]`.
- **Long input:** Even at the maximum length of `10^5`, `x` never exceeds four after an iteration. The method's numeric state is completely independent of the potentially enormous full prefix.
- **Why equality with zero is enough:** There is no need to test `x % 5` again when appending. The assignment has already reduced `x` into the canonical remainder range.
- **Order of operations:** The modulo must apply after appending the new bit. Reducing the old `x` is already implicit in the invariant, but testing before the update would report divisibility for the previous prefix rather than the current one.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = len(nums)`. The `for` loop processes each of the `N` bits exactly once. Every iteration performs one shift, one bitwise OR, one remainder operation on a value smaller than ten, one comparison, and one append. All are constant-time operations here because `x` is always below five. Total time is therefore `O(N)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
