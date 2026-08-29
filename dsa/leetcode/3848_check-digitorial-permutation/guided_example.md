# Guided Example: Check Digitorial Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 40585}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `true` from `{"n": 40585}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the permutation question into one fixed candidate

A direct reading of the problem may suggest generating every arrangement of the digits of `n` and checking whether each resulting number is a digitorial. That is unnecessary. The important observation is that rearranging digits changes their positions, but it does not change which digits are present or how many times each digit occurs.

For any positive integer `z`, define its digit-factorial sum as

$$
F(z)=\sum_{\text{digit }d\text{ of }z} d!.
$$

Suppose `p` is a permutation of all digits of `n`. Because `p` and `n` have exactly the same digit multiset, they contain the same factorial terms. Their order is irrelevant to addition, so

$$
F(p)=F(n).
$$

Let `S=F(n)`. If some permitted permutation `p` is a digitorial, then the definition of a digitorial requires `p=F(p)`. Combining that equality with the permutation invariance gives

$$
p=F(p)=F(n)=S.
$$

This proves that there cannot be several numerical candidates to search. The only possible successful number is `S` itself. The whole problem therefore becomes: compute `S` once, then ask whether the ordinary decimal representation of `S` uses exactly the same digits as `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 40585}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the source computes the digit-factorial sum

The helper `f(x)` computes `x!` recursively. It returns `1` for both `0` and `1`, which is correct because `0!=1!=1`. For a larger digit it returns `x * f(x - 1)`. The `@cache` decorator remembers results. Although the helper is written for arbitrary nonnegative inputs, this method calls it only with decimal digits, so at most the values `0` through `9` matter.

The method copies `n` into `y` and initializes `x` to zero. Here `x` is the running value of `S`, not a digit. Each loop iteration extracts the last digit with `y % 10`, adds that digit's factorial to `x`, and removes the digit with integer division `y //= 10`. Since the contract makes `n` positive, the loop executes at least once. When it ends, `x` equals `F(n)` exactly.

For example, if `n = 145`, the loop produces

$$
1!+4!+5!=1+24+120=145.
$$

The candidate `S` is therefore `145`, and its digits match the input digits, so the method returns true. For a nontrivial permutation example, imagine that the input digits can be rearranged into some digitorial `p`. The derivation above says that the computed sum must literally be that `p`; the algorithm never needs to guess its order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compare multisets, not numeric order

The final expression compares `sorted(str(x))` with `sorted(str(n))`. Converting each number to a string exposes its canonical decimal digits. Sorting those characters puts equal digit multisets into the same order. Therefore the comparison is true exactly when every digit appears the same number of times on both sides.

This comparison also enforces the requirement that a rearrangement may not start with zero. A positive integer's normal string representation never contains leading zeros. If the candidate `S` has the same complete digit multiset as `n`, then `str(S)` itself supplies a legal ordering whose first character is nonzero. Conversely, an illegal leading-zero arrangement is not needed: any successful number has a canonical representation, and that representation must use all input digits to pass the multiset comparison.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 40585}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate every permutation:** Testing all distinct arrangements is conceptually direct but can require factorially many candidates, and most work is redundant because every arrangement has the same digit-factorial sum. The invariant reduces that entire search to one candidate.
- **Ten-entry digit-frequency arrays:** Count each digit in `n` and in `S` instead of sorting their strings. This preserves the same reasoning while giving genuine `O(D)` time and `O(1)` auxiliary space because the decimal alphabet has size ten; it also matches the complexity advertised by the manifest more closely than the protected source does.
- **Compare only the numeric sum:** Checking whether `S == n` would detect when `n` itself is a digitorial, but it would miss cases in which another ordering of the same digits is the digitorial. The multiset comparison is what permits rearrangement.
- **Zeros in the input:** A zero contributes `0!=1`, not zero. It must also appear equally often in `S`. The string of `S` cannot begin with zero, so a successful equality automatically gives a legal no-leading-zero arrangement.
- **Repeated digits:** Sorting retains multiplicity. For example, one copy of a digit cannot stand in for two copies; both sorted lists must have equal lengths and equal characters at every position.
- **The digits zero and one:** Both contribute one to `S` even though they are different digits. Equal factorial contributions do not make the digits interchangeable, because the final comparison still checks their literal characters.
- **A different number of digits in `S`:** The sorted lists then have different lengths and cannot compare equal. This is correct because a permutation must use every original digit exactly once.
- **Smallest positive input:** For `n=1`, the loop computes `1!=1` and returns true. The special case is already covered by the same invariant and needs no branch.
- **Integer safety and language behavior:** Python integers grow automatically, and the stated limit makes `S` very small in any event. In a fixed-width language, `D\cdot9!` is the relevant upper bound to check before choosing the integer type.
- **Helper availability:** The exact solution requires `functools.cache`. If the execution environment does not pre-import it, the solution needs `from functools import cache`; this is an integration requirement rather than an algorithmic step.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D\log D+E\log E)$. Let `D` be the number of decimal digits in `n`, and let `E` be the number of digits in the computed sum `S`. Extracting the input digits takes `O(D)` time. Factorial evaluation is constant work per decimal digit after the tiny cache is populated; even the first recursive evaluations reach depth at most ten. Constructing the two strings takes `O(D+E)` time.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
