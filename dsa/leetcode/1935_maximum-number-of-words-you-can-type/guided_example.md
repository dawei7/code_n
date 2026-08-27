# Guided Example: Maximum Number of Words You Can Type

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "hello world", "brokenLetters": "ad"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

The objective is to compute `1` from `{"text": "hello world", "brokenLetters": "ad"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce each word to a membership test

A word can be fully typed exactly when none of its characters belongs to `brokenLetters`. The solution first converts the broken-letter string to a set:

`s = set(brokenLetters)`.

Set membership is expected $O(1)$, so each keyboard check becomes the direct question `c not in s`. The contract says broken letters are distinct, but using a set would also harmlessly remove duplicates.

Next, `text.split()` produces the words in order. The input guarantees single spaces with no leading or trailing space, so this yields exactly the intended words and no empty strings. The no-argument form of `split` would also tolerate runs of whitespace, though that extra behavior is not needed here.

For a word `w`, the expression

`all(c not in s for c in w)`

is true only when every character passes the working-key test. Python's `all` short-circuits: as soon as one broken character is found, the remaining characters of that word need not be inspected because the word is already impossible to type.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "hello world", "brokenLetters": "ad"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert Boolean results into the answer

The outer generator produces one Boolean per word. In Python, `true` has integer value one and `false` has integer value zero when summed. Therefore

`sum(all(...) for w in text.split())`

counts exactly the words for which every character is typeable.

For `text = "hello world"` and `brokenLetters = "ad"`, the set is `{"a", "d"}`. Every letter of `"hello"` is outside it, so `all` returns true and contributes one. The scan of `"world"` eventually reaches `d`, returns false, and contributes zero. The result is one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer generator produces one Boolean per word.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why checking every character is necessary

A word must be typed in full. Finding one working character says nothing about its other letters, so `any` would express the wrong rule. Conversely, one broken occurrence is enough to reject the whole word, even when every other occurrence is typeable.

Repeated letters need no special counting. If a repeated character is broken, the first occurrence makes `all` false. If it works, all occurrences pass the same constant-time membership check.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "hello world", "brokenLetters": "ad"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Streaming character scan:** Track whether the :** - **Streaming character scan:** Track whether the current word has encountered a broken key, count it at each space, and handle the final word afterward. This gives $O(N+B)$ time and $O(B)$ space without materializing word substrings.
- **Set intersection per word:** `set(w).isdisjoint(s)` is expressive but allocates another set for every word. The exact `all` approach can short-circuit and avoids those sets.
- **Search the broken string directly:** Testing `c not in brokenLetters` avoids building a set but costs $O(B)$ per tested character; with $B\le26$ it is still asymptotically linear but has a less robust bound.
- **No broken letters:** The set is empty, every membership test succeeds, and all words are counted.
- **Every word contains a broken letter:** Every inner `all` is false and the result is zero.
- **A broken letter repeated in one word:** The first encountered occurrence rejects the word; later occurrences need not be scanned.
- **Single word:** `split` returns a one-element list, and the method returns either zero or one.
- **Single-character word:** It is typeable exactly when that character is absent from the broken set.
- **Shared broken character across words:** Each affected word is rejected independently, as required.
- **Spaces are not keys being tested:** Splitting removes separators before character checks, so a space can never make a word fail.
- **Input formatting guarantee:** Single separators and no outer spaces ensure no empty words. The chosen `split()` would also ignore extra whitespace if it appeared.
- **Exact-space caveat:** Although the fixed broken-letter set is constant-sized, the word list and substring objects created by `split` make this source $O(N)$ in peak auxiliary space.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+B)$. Let $N$ be the length of `text` and $B$ the length of `brokenLetters`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
