# Guided Example: Longest Balanced Substring After One Swap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "100001"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary string `s` consisting only of characters `'0'` and `'1'`.

The objective is to compute `4` from `{"s": "100001"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prefix balance turns substring counts into subtraction

Let $P_i$ be the balance of prefix `s[0..i]`:

$$
P_i
=
\#1\text{s in }s[0..i]
-
\#0\text{s in }s[0..i].
$$

Define the empty prefix before index 0 to have balance $P_{-1}=0$. For a substring from $j+1$ through $i$, its balance is

$$
P_i-P_j.
$$

If $P_i=P_j$, the substring has equally many zeros and ones. Its length is $i-j$.

The dictionary `pos` maps each prefix balance to all indices where that balance has occurred. It begins with `{0: [-1]}` so a balanced substring starting at index 0 is handled by the same formula as every other substring.

At index `i`, the source updates `pre` to $P_i$, appends `i` to `pos[pre]`, and uses the earliest occurrence `pos[pre][0]`. Among all earlier positions with the same balance, the earliest produces the longest zero-balance substring ending at `i`:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "100001"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What one swap can change inside a chosen substring

Swapping two positions both inside the substring does not change its counts. Swapping two positions both outside also does not change them. A useful swap exchanges one character inside with one character outside.

If a substring has two more ones than zeros, exchanging an inside `'1'` with an outside `'0'` changes its balance by

$$
-1-1=-2.
$$

The removed inside one decreases the one count, and the inserted zero increases the zero count. A balance of $+2$ becomes zero.

Symmetrically, a substring with two extra zeros has balance $-2$. Swapping an inside zero for an outside one changes the balance by $+2$ and makes it balanced.

No other nonzero balance can be repaired by one swap. A cross-boundary swap changes the encoded substring sum only by $-2$, $0$, or $+2$. Therefore every answer window must have original balance

$$
0,\quad +2,\quad\text{or}\quad -2.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Swapping two positions both inside the substring does not ch... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Finding a window with two extra ones

For a window $j+1..i$ to have balance $+2$, its earlier prefix must satisfy

$$
P_j=P_i-2.
$$

That is why the source looks for `pre - 2` in `pos`.

Let $j$ be the earliest occurrence of that prefix balance and let the window length be

$$
\ell=i-j.
$$

If the window has $o$ ones and $z$ zeros, then

$$
o+z=\ell
\quad\text{and}\quad
o-z=2.
$$

Solving gives

$$
z=\frac{\ell-2}{2}.
$$

The source has already counted all zeros in the entire string as `cnt0`. An outside zero exists exactly when

$$
\frac{\ell-2}{2}<\texttt{cnt0}.
$$

This appears as



When the condition holds, the earliest prefix gives a repairable window of length `i - p[0]`.

The needed inside one is guaranteed: a balance-$+2$ window has two more ones than zeros, so it cannot contain no ones.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "100001"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all swaps:** Trying $O(N^2)$ swaps a:** - **Enumerate all swaps:** Trying $O(N^2)$ swaps and then searching each resulting string is far too slow; the balance-change observation represents all useful swaps implicitly.
- **Longest zero-sum substring only:** Equal-prefix logic without the $\pm2$ cases misses windows that become balanced through one cross-boundary swap.
- **Store only two prefix positions:** The source stores every occurrence, but its feasibility logic reads only the earliest and second-earliest positions for each balance.
- **No swap needed:** A balance-zero window is accepted directly; “at most one” does not require changing the string.
- **All characters identical:** There is no opposite character anywhere to exchange, so no nonempty balanced substring can be formed and the result is zero.
- **Outside character may be on either side:** The total-count test covers characters before and after the candidate; their location outside the substring does not matter because any two indices may be swapped.
- **Inside majority character always exists:** A $+2$ window necessarily contains a one, and a $-2$ window necessarily contains a zero, so only the outside opposite needs an explicit test.
- **Endpoint sentinel:** Prefix index $-1$ allows candidates beginning at string index 0 to have length `i - (-1) = i + 1`.
- **Second-occurrence fallback:** Equal prefix balances enclose a nonempty balanced block, guaranteeing that shortening past it releases both a zero and a one outside without changing the $\pm2$ imbalance.
- **Odd-length substring:** It cannot contain equal counts, and it also cannot have balance $\pm2$ because balance parity matches length parity; such a window is never selected.
- **Swapping equal characters:** It changes nothing and is already covered by the no-swap balance-zero case.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{s}\rvert$. The initial `s.count("0")` scans the string once, costing $O(N)$ time. The main loop also scans all $N$ characters once.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
