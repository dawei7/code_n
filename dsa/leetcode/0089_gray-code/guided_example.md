# Guided Example: Gray Code

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2}`
- **Required output:** `[0, 1, 3, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An **n-bit gray code sequence** is a sequence of $2^n$ integers where:

The objective is to compute `[0, 1, 3, 2]` from `{"n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why shifting and XOR produce a Gray value

Write the bits of $i$ from most significant to least significant as $b_{n-1},b_{n-2},\ldots,b_0$. Shifting right by one puts a `0` above the most significant bit and moves each original bit one position to the right. XOR therefore makes the Gray bit in position $k$ equal to the difference between two neighboring binary bits:

$$
g_{n-1}=b_{n-1},\qquad g_k=b_{k+1}\oplus b_k\quad(0\le k<n-1).
$$

That relationship is the heart of the method. Gray code records whether adjacent binary positions agree, rather than copying the binary digits directly. The one-line list comprehension is compact because the bit operation already performs all $n$ of those neighboring comparisons at once.

For $n=3$, the ordinary indices and transformed values are:

| $i$ | binary $i$ | `i >> 1` | XOR result $G(i)$ |
|---:|:---:|:---:|:---:|
| 0 | `000` | `000` | `000` |
| 1 | `001` | `000` | `001` |
| 2 | `010` | `001` | `011` |
| 3 | `011` | `001` | `010` |
| 4 | `100` | `010` | `110` |
| 5 | `101` | `010` | `111` |
| 6 | `110` | `011` | `101` |
| 7 | `111` | `011` | `100` |

Reading the final column as integers gives `[0, 1, 3, 2, 6, 7, 5, 4]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why consecutive outputs differ in exactly one bit

When binary $i$ is incremented to $i+1$, some suffix changes. Suppose $i$ ends in $t$ consecutive `1` bits. The increment turns those $t$ bits into `0` and changes the `0` immediately before them into `1`. Every more significant bit stays fixed. Thus `i ^ (i + 1)` is a run of exactly $t+1$ low `1` bits.

Let

$$
X=i\oplus(i+1).
$$

Using associativity and commutativity of XOR,

$$
G(i)\oplus G(i+1)=X\oplus(X\mathbin{\texttt{>>}}1).
$$

Because $X$ is a low run of `1` bits, shifting it right removes only its highest `1`; every lower `1` occurs in both operands and cancels under XOR. The result therefore has exactly one set bit. XOR identifies precisely the positions at which two values differ, so having one set bit proves that $G(i)$ and $G(i+1)$ differ in exactly one bit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why all generated values are distinct

Generating $2^n$ entries would not be sufficient if two indices could map to the same Gray value. The transformation is reversible. Starting with the most significant binary bit, which equals the most significant Gray bit, each following binary bit can be recovered from the preceding recovered binary bit and the current Gray bit. In symbols, $b_{n-1}=g_{n-1}$ and $b_k=b_{k+1}\oplus g_k$. Therefore one Gray bit pattern corresponds to exactly one binary index. Different indices cannot collide.

There are $2^n$ indices in the loop, all outputs are distinct, and every output uses at most $n$ bits because both operands do. Consequently the result contains every integer in $[0,2^n-1]$ exactly once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 3, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 3, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Reflected iterative construction:** Begin with `[0]`. For each new bit, traverse the existing sequence backward and append each value with that bit set. This is also $O(2^n)$ time and $O(1)$ auxiliary space excluding the output. It is often easier to discover from examples, while the selected formula is shorter and computes each position independently.
- **Recursive reflection:** First construct the $(n-1)$-bit sequence, then append its reverse with bit $n-1$ set. It expresses the mathematical reflection directly but uses $O(n)$ call-stack space in addition to the output.
- **Backtracking over the hypercube:** Treat each $n$-bit number as a vertex and connect values that differ in one bit, then search for a Hamiltonian cycle beginning at zero. This models the contract naturally but introduces a visited set and potentially enormous search. A deterministic Gray construction makes that search unnecessary.
- **Bit-operation precedence:** Write `i ^ (i >> 1)` with parentheses. The selected source does so, avoiding any need for a reader to remember Python's precedence rules.
- **Minimum input:** For $n=1$, the indices are `0` and `1`, and the result is `[0, 1]`. The only adjacent pair and the wraparound pair both differ in the single available bit.
- **Hypothetical zero-bit input:** The stated constraints begin at $n=1$, but the formula would still return `[0]` for $n=0$. Whether a one-element cyclic sequence is considered to differ from itself in one bit is irrelevant because that input is outside the contract.
- **Multiple valid answers:** The problem accepts any valid sequence. The formula deterministically returns the reflected binary Gray ordering; it does not need to reproduce an example's exact list if another valid ordering is shown.
- **Binary width and leading zeros:** Integers do not store leading zeros, but comparisons are understood in exactly $n$ bit positions. For example, with $n=3$, integer `1` represents `001`. Omitting stored leading zeros does not change which positions differ.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=2^n$ be the required number of output values.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
