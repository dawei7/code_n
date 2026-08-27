# Guided Example: Count Substrings with Only One Distinct Letter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaaba"}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the number of substrings that have only **one distinct** letter*.

The objective is to compute `8` from `{"s": "aaaba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Counting one equal-character run

Inside a run, every position contains the same letter, so every nonempty contiguous interval is valid. There are $L$ substrings of length one, $L-1$ substrings of length two, and so on, down to one substring of length $L$. Their total is

$$
L+(L-1)+\cdots+1=\frac{L(L+1)}{2}.
$$

Another beginner-friendly way to see the same formula is to count by starting position. From the run’s first position, a valid substring may end at any of $L$ positions. From the second position, it has $L-1$ choices. This continues until the last position has one choice. Both views count every interval once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaaba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the two pointers discover maximal runs

The code begins with `i = 0`. This variable is the first index of the next run that has not yet been counted. While `i < n`, it sets `j = i` and advances `j` while two conditions hold: `j` is still inside the string, and `s[j] == s[i]`. Because `s[i]` is the run’s character, the inner loop moves across exactly the consecutive copies of that character.

When the inner loop stops, `j` is the exclusive end of the run. Either `j == n`, meaning the run reaches the end of the string, or `s[j]` differs from `s[i]`, meaning a new run begins at `j`. The run occupies the half-open interval from `i` through `j` and has length `j - i`. Here “through `j`” means up to but not including `j`; the half-open form avoids adding or subtracting one when measuring the length.

The solution adds

`(1 + j - i) * (j - i) // 2`

to `ans`. If $L=j-i$, this is exactly $(L+1)L/2$. The division is performed after multiplication. One of two consecutive integers $L$ and $L+1$ is always even, so the product is divisible by two and integer division loses nothing.

Finally, `i = j` moves the outer pointer directly to the first character of the next run. No character from the completed run is reconsidered by a later outer iteration.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code begins with `i = 0`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following the example from start to finish

For `s = "aaaba"`, the first run starts at zero. The inner pointer advances to three, so $L=3$ and the solution adds $3 \cdot 4 / 2=6$. Those six occurrences are three length-one substrings, two length-two substrings, and one length-three substring.

The next run is the single `"b"` at index three. Its length is one, so it contributes one. The last `"a"` is another separate length-one run and contributes one. It must not be combined with the earlier `"a"` characters because the `"b"` between them prevents a contiguous substring from using both regions. The final answer is $6+1+1=8$.

For a string of ten identical letters, there is one run of length ten, so the answer is $10 \cdot 11 / 2=55$. The algorithm obtains that result without constructing any of the 55 substrings.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaaba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Ending-at-this-index dynamic programming:** Tr:** - **Ending-at-this-index dynamic programming:** Track the number of valid substrings ending at the current character. Increase that number when the character matches its predecessor; otherwise reset it to one. Adding these values also gives $O(n)$ time and $O(1)$ space.
- **Enumerate all substrings:** Generating intervals and checking their distinct letters is unnecessarily expensive, taking at least quadratic time and potentially cubic work with repeated scans.
- **Single-character string:** One maximal run of length one contributes $1 \cdot 2 / 2=1$, so the only substring is counted.
- **All characters equal:** The inner loop reaches `n` once, and the formula counts all $n(n+1)/2$ nonempty substrings.
- **Every adjacent character differs:** Every run has length one. Each contributes one, so the answer is exactly $n$.
- **Same letter in separated runs:** Runs such as the two `"a"` regions in `"aba"` must remain separate. Contiguity prevents combining them across the different middle character.
- **Exclusive run endpoint:** When the inner loop ends, `j` is not part of the completed run. The correct length is `j - i`, and setting `i = j` starts precisely at the unprocessed character.
- **Occurrence counting rather than distinct text:** Two equal substrings at different index intervals both count. The run formula naturally counts intervals, not unique string values.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. Although the solution contains a loop inside another loop, it is not quadratic. Within a run, `j` advances across each character once. After the run is counted, `i` jumps to that same exclusive endpoint. Across the entire execution, the inner-loop pointer performs $n$ successful character visits in total, plus a constant amount of boundary work per run.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
