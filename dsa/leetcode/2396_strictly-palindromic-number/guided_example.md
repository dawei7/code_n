# Guided Example: Strictly Palindromic Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 99991}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An integer `n` is **strictly palindromic** if, for **every** base `b` between `2` and $n - 2$ (**inclusive**), the string representation of the integer `n` in base `b` is **palindromic**.

The objective is to compute `false` from `{"n": 99991}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The answer is false for every allowed input

The exact solution returns `false` without examining `n` further. This is not a shortcut based on examples or probability. Under the constraint `n >= 4`, every possible input has at least one required base in which its representation is not a palindrome.

To disprove “palindromic in every base,” finding one counterexample base is sufficient. There is no need to convert `n` into all bases from two through `n - 2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 99991}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use base `n - 2` for every `n >= 5`

Let:

$$
b=n-2.
$$

When $n\ge5$, $b\ge3$, so digit `2` is valid in base $b$. Rewrite $n$ as:

$$
n=(n-2)+2=1\cdot b+2.
$$

Therefore, the base-$b$ representation of $n$ is the two-digit string `"12"`. Its reverse is `"21"`, which is different. It is not palindromic.

Base $b=n-2$ lies exactly at the upper endpoint of the bases the definition requires. Thus, this one legal base disproves strict palindromicity for every $n\ge5$.

For example, if `n = 9`, use base seven:

$$
9=1\cdot7+2,
$$

so the representation is `12_7`, immediately disproving the property. The example also shows a failure in base three, but finding more than one counterexample is unnecessary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the boundary value `n = 4`

The same selected base is `n - 2 = 2`, but digit two is not a valid base-two digit, so the two-digit `"12"` derivation cannot be used literally.

Convert four to base two:

$$
4=1\cdot2^2+0\cdot2+0,
$$

giving `"100"`. Its reverse is `"001"`, so it is not a palindrome. Base two is the only base in the required interval `[2, n - 2]` for `n = 4`, and it already fails.

This boundary case completes the proof for the full input domain.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 99991}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert in every required base:** It can verify the definition directly but wastes substantial work; the single counterexample theorem already settles all inputs.
- **Test only base two:** It is insufficient as a general proof because some numbers, such as nine, are palindromic in base two.
- **Use base `n - 2` blindly as `"12"`:** The derivation needs `n >= 5` so base is at least three and digit two is valid.
- **Boundary `n = 4`:** Base two representation `100` supplies the required separate counterexample.
- **Universal versus existential logic:** One failing base is enough to return false, while one successful base is not enough to return true.
- **Upper constraint:** The proof does not depend on `10^5` and works for every integer at least four.
- **No true branch:** This is intentional and fully proved, not an omitted implementation.
- **No base-conversion helper:** Runtime conversion would not improve correctness once the invariant is known.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The function executes one constant return statement. Its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
