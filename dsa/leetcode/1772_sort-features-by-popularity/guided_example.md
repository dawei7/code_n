# Guided Example: Sort Features by Popularity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"features": ["a", "aa", "b", "c"], "responses": ["a", "a aa", "a a a a a", "b a"]}`
- **Required output:** `["a", "aa", "b", "c"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string array `features` where $\text{features}[i]$ is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array `responses`, where each $\text{responses}[i]$ is a string containing space-separated words.

The objective is to compute `["a", "aa", "b", "c"]` from `{"features": ["a", "aa", "b", "c"], "responses": ["a", "a aa", "a a a a a", "b a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Popularity counts responses, not word repetitions

A feature's popularity is the number of separate response strings containing it. If one user repeats a feature word several times in one response, that response still contributes only one.

The exact solution processes each response independently. It splits the response into words, converts those words to a set, and increments a global `Counter` once for every distinct word in that response.

The set is the key detail that aligns counting with the definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"features": ["a", "aa", "b", "c"], "responses": ["a", "a aa", "a a a a a", "b a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Tokenize one response

`s.split()` separates a response at whitespace. The input guarantees clean single spaces with no leading or trailing space, but calling `split` without an explicit separator is robust to general whitespace as well.

For `"i like cooler cooler"`, splitting produces two occurrences of `"cooler"`. Wrapping the list in `set(...)` collapses those duplicates. The following loop sees `"cooler"` only once and adds one to its counter.

The set also contains non-feature survey words such as `"i"` and `"like"`. The exact source counts them too, but they never appear in the later `features` sort, so they do not affect the result. Filtering to known features could reduce memory without changing output.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Accumulate across responses

`cnt` begins as an empty `Counter`. For every distinct word `w` in one response, `cnt[w] += 1` records that one more response contains it.

The per-response set is recreated for each survey string. A feature appearing in two different responses is therefore incremented twice, as required. Deduplication does not leak across users.

After all responses, `cnt[w]` is exactly the number of response sets containing word `w`. A feature never mentioned has the Counter default value zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["a", "aa", "b", "c"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"features": ["a", "aa", "b", "c"], "responses": ["a", "a aa", "a a a a a", "b a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["a", "aa", "b", "c"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Filter response words to features:** Build a feature set and increment only recognized words, reducing Counter entries for irrelevant survey language.
- **Explicit pair sort:** Sort tuples `(-count, original index, feature)`. It makes tie behavior visible but stores an index map or decorated list.
- **Count raw split words:** It is incorrect because repeated words in one response would inflate popularity.
- **Substring search:** It would wrongly count feature `"lock"` inside response word `"locker"`.
- **Feature never mentioned:** Counter returns zero, and stable sorting preserves its order among other zero-popularity features.
- **All features tied:** The returned order is identical to `features`.
- **One response repeats a feature:** Its set contributes exactly one.
- **Feature appears in every response:** Its count is the number of responses and it sorts ahead of lower counts.
- **Non-feature words:** They may occupy Counter entries but never become output elements.
- **No duplicate features:** The constraint makes original-index tie ordering unambiguous.
- **Stable sort:** Correct tie handling relies on Python's documented stability.
- **Negative key:** It reverses only popularity direction without reversing tied elements.
- **Spaces:** `split()` handles the guaranteed formatting and would also tolerate extra whitespace.
- **Input preservation:** `sorted` returns a new list rather than rearranging `features` in place.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W+F\log F)$. Let $W$ be the total number of response-word occurrences after splitting, $U$ the number of distinct words across responses, and $F$ the number of features. Tokenization, per-response set creation, and counter updates take expected $O(W)$ time using hashing.
- **Auxiliary Space Complexity:** $O(F)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
