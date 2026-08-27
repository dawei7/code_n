# Guided Example: Multiply Two Polynomials

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"poly1": [3, 2, 5], "poly2": [1, 4]}`
- **Required output:** `[3, 14, 13, 20]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `poly1` and `poly2`, where the element at index `i` in each array represents the coefficient of $x^i$ in a polynomial.

The objective is to compute `[3, 14, 13, 20]` from `{"poly1": [3, 2, 5], "poly2": [1, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Polynomial multiplication is coefficient convolution

Let:

`A(x)=sum_i a_i x^i`

and:

`B(x)=sum_j b_j x^j`.

Multiplying one term `a_i x^i` by `b_j x^j` contributes:

`a_i b_j x^(i+j)`.

Therefore the output coefficient at degree `d` is:

`result[d] = sum_(i+j=d) a_i b_j`.

This is the linear convolution of the two coefficient arrays. A nested loop computes it in `O(ab)` for input lengths `a` and `b`, which can be too slow at `50,000` each.

The Fast Fourier Transform converts convolution into pointwise multiplication.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"poly1": [3, 2, 5], "poly2": [1, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose a padding size that prevents circular overlap

The true product has length:

`m = len(poly1)+len(poly2)-1`.

The source chooses `n` as the smallest power of two with `n>=m`. Power-of-two length supports the radix-two FFT.

Both coefficient arrays are padded with zeros to length `n`. A length-`n` discrete Fourier transform naturally corresponds to circular convolution modulo `x^n-1`. Because the true linear convolution has no nonzero coefficient at degree `n` or above, padding to `n>=m` prevents any coefficient from wrapping around.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The true product has length:

`m = len(poly1)+len(poly2)-1`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Transform both arrays separately

The source converts each integer coefficient to a complex number and creates `fa` and `fb`. It then calls forward FFT on each array.

This exact detail differs from the manifest summary. The summary claims both real arrays are packed into one complex FFT and later separated. The protected source does not use that optimization; it performs two independent forward transforms. The mathematical result and `O(n log n)` complexity remain valid, but the implementation has one extra transform relative to the advertised packing trick.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 14, 13, 20]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"poly1": [3, 2, 5], "poly2": [1, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 14, 13, 20]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quadratic convolution:** Simple and exact but :** - **Quadratic convolution:** Simple and exact but infeasible for two arrays near length `50,000`.
- **Number-theoretic transform:** Uses modular arithmetic for exact convolution. Multiple moduli plus CRT may be needed because signed coefficients and output magnitudes exceed one convenient modulus.
- **Complex packing trick:** Two real arrays can be encoded in real and imaginary parts of one transform, matching the manifest summary. The protected code instead runs two forward FFTs.
- **Naive evaluation/interpolation:** Usually slower and more complex than FFT for dense coefficient arrays.
- **One constant polynomial:** The FFT still works, though direct scalar multiplication would be simpler and linear.
- **Negative coefficients:** Spectral multiplication and rounding preserve signs.
- **Zero coefficients:** They participate normally and can lead to internal or trailing zero outputs.
- **Non-power-of-two target length:** Padding advances to the next power of two; output is truncated back to exact `m`.
- **Empty arrays:** The source defensively returns empty, although constraints guarantee non-empty inputs.
- **Floating error:** Rounding assumes absolute error below one half. Exact-transform methods avoid this assumption.
- **Imaginary residue after inverse:** It is numerical noise and is discarded; mathematically coefficients are real.
- **Trailing zero result:** It is retained because output length is prescribed.
- **Sign convention:** Positive-forward/negative-inverse is valid because the two are paired consistently.
- **Manifest mismatch:** Complexity is unchanged, but no single packed FFT appears in the protected solution.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L log L)$. Let `L` be the chosen power-of-two FFT length. Since `m<=L<2m`, `L=Theta(m)`.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
