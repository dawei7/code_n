# Guided Example: Shortest Palindrome

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aacecaaa"}`
- **Required output:** `"aaacecaaa"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. You can convert `s` to a palindrome by adding characters in front of it.

The objective is to compute `"aaacecaaa"` from `{"s": "aacecaaa"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the construction problem to one palindromic prefix

The original string `s` must remain intact as the suffix of the answer because
characters may be added only in front. Suppose the longest prefix of `s` that
is already a palindrome has length `idx`. Split the string into
`p = s[:idx]` and `t = s[idx:]`. Since `p` is a palindrome, prepending the
reverse of `t` produces

$$
\operatorname{reverse}(t) + p + t.
$$

The left and right copies of `t` mirror each other, and the middle `p` mirrors
itself, so this entire string is a palindrome. In code, that construction is
`s[idx:][::-1] + s`.

Using the longest palindromic prefix is what makes the result shortest. Any
characters of `s` outside the chosen prefix must be mirrored by newly prepended
characters. A shorter palindromic prefix leaves a longer suffix `t` and thus
requires more additions. Conversely, if some construction added fewer than
`len(t)` characters, a longer initial portion of `s` would have to occupy the
self-mirroring center, implying a palindromic prefix longer than the one chosen.

The real task is therefore to find the greatest prefix length that is
palindromic.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aacecaaa"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compare a prefix with its own reverse using two rolling hashes

The exact solution scans `s` once and maintains two polynomial hashes for the
prefix ending at the current character. Each lowercase character is mapped to
an integer from 1 through 26 with `ord(c) - ord('a') + 1`. Mapping `a` to 1
rather than 0 prevents leading `a` characters from disappearing algebraically.

Let the mapped values of a length-$k$ prefix be
$v_0, v_1, \ldots, v_{k-1}$ and let the base be $b=131$. Before applying the
modulus, `prefix` represents

$$
v_0b^{k-1} + v_1b^{k-2} + \cdots + v_{k-2}b + v_{k-1},
$$

while `suffix` represents

$$
v_0 + v_1b + \cdots + v_{k-2}b^{k-2} + v_{k-1}b^{k-1}.
$$

The second expression is the first expression with character order reversed.
If the prefix is a palindrome, its value sequence reads the same in both
directions, so these two polynomial values are equal.

Both hashes are stored modulo `10**9 + 7` to keep numbers bounded. The variable
`mul` holds the next power of 131 needed by the reverse-direction hash. It
starts at 1, which is $131^0$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How each character updates the three values

For each character value `v`, the statement conceptually represented by
`prefix = (prefix * base + v) % mod` shifts every existing coefficient one
power higher and places `v` at power zero. This is the ordinary left-to-right
polynomial hash update.

The update `suffix = (suffix + v * mul) % mod` places the new character at the
highest power used so far. Then `mul = (mul * base) % mod` advances the power
for the next iteration. Thus, after processing index `i`, both hashes describe
exactly `s[:i + 1]`, but in opposite reading directions.

Whenever `prefix == suffix`, the source assigns `idx = i + 1`. The `+1`
converts the zero-based ending index into a prefix length, which is also the
slice boundary required later. Because scanning proceeds from left to right,
every later equality overwrites an earlier one, leaving `idx` at the longest
hash-matching prefix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aaacecaaa"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aacecaaa"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aaacecaaa"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **KMP prefix function:** Build `s + separator + reversed(s)` and use the final prefix-function value as the longest palindromic-prefix length. It is deterministic, runs in $O(n)$ time and $O(n)$ space, and is the technique named by the current manifest even though the exact source instead hashes.
- **Double rolling hash plus verification:** Two independent moduli make collision probability much smaller; directly verifying the final candidate prefix removes the immediate false positive, though finding a fallback after a failed verification needs care to preserve linear time.
- **Manacher's algorithm:** It deterministically finds all palindrome radii in $O(n)$ time and can select the longest one touching index 0. It is more intricate than necessary for this prefix-only goal.
- **Check prefixes from longest to shortest:** Compare each prefix with its reversal and stop at the first palindrome. It is simple but repeated slicing and comparison can take $O(n^2)$ time at the maximum length $5 \cdot 10^4$.
- **Empty string:** The scan has no iterations, `idx == n == 0`, and the method returns `""` without indexing any character.
- **One character:** Its two hashes match immediately, so the method returns the original one-character palindrome.
- **The whole string is a palindrome:** The last iteration sets `idx` to $n$, and no characters are added.
- **Only the first character is palindromic:** Every nonempty string has at least a one-character palindromic prefix. Reversing all characters after index 0 produces the required answer, as in `"abcd"`.
- **Repeated characters:** A string such as `"aaaa"` updates `idx` at every position and is returned unchanged. Repetition is handled by coefficients, not by a special case.
- **Separator choice:** The exact rolling-hash source does not concatenate strings and therefore needs no separator. A KMP alternative must use a delimiter outside the lowercase input alphabet to prevent a match from crossing the boundary incorrectly.
- **Hash collision:** This is a semantic edge case, not merely a performance issue. One modular equality can be a false positive; applications requiring unconditional correctness should prefer deterministic KMP or Manacher rather than relying on the accepted-source probability.
- **Input preservation:** Strings are immutable in Python. The method creates new strings for the suffix and result but never changes `s`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`. The loop performs one constant number of modular
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
