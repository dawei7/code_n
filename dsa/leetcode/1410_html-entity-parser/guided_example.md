# Guided Example: HTML Entity Parser

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "&amp; is an HTML entity but &ambassador; is not."}`
- **Required output:** `"& is an HTML entity but &ambassador; is not."`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

**HTML entity parser** is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The objective is to compute `"& is an HTML entity but &ambassador; is not."` from `{"text": "&amp; is an HTML entity but &ambassador; is not."}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parse the original input from left to right

The parser recognizes exactly six encoded strings and replaces each recognized source token with one character. The dictionary `d` is the complete translation table used by the implementation:

| Source token | Appended character |
|---|---|
| `&quot;` | `"` |
| `&apos;` | `'` |
| `&amp;` | `&` |
| `&gt;` | `>` |
| `&lt;` | `<` |
| `&frasl;` | `/` |

The algorithm maintains index `i` as the first unconsumed position in the original `text`. Everything before `i` has already been translated exactly once and represented in `ans`. Everything from `i` onward is still untouched source input.

This one-pass viewpoint is important for nested-looking text. If the source contains `&amp;gt;`, the parser recognizes `&amp;`, appends a literal ampersand, and later copies the remaining characters `gt;`. It returns `&gt;`; it does not recursively parse the ampersand it just produced. Appended output is never fed back into the input scan.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "&amp; is an HTML entity but &ambassador; is not."}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only lengths one through seven are tested

At each position, the inner loop tries:



Python's upper range boundary is excluded, so `l` takes values from 1 through 7. Seven is the length of the longest supported token, `&frasl;`. No valid entity can require a longer slice.

The shorter tokens also fall within that range: `&gt;` and `&lt;` have length four, `&amp;` has length five, `&quot;` and `&apos;` have length six, and `&frasl;` has length seven.

Trying slices that extend beyond the end is safe in Python. `text[i:j]` simply stops at the string boundary rather than raising an error. Those shorter suffixes will not equal a complete dictionary key unless a complete token is actually present.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognizing and consuming an entity

For every candidate ending position `j`, the code asks whether `text[i:j]` is a key in `d`. If it is, the same slice retrieves the replacement:



Appending the dictionary value emits exactly one decoded character. Setting `i = j` consumes the entire source entity, including its leading ampersand and trailing semicolon. The `break` exits the length loop so the entity cannot also be copied character by character.

The code checks lengths from shortest to longest. This is safe for this fixed dictionary because no supported entity token is a complete prefix of another supported token. There is therefore no situation where an early shorter match steals the beginning of a different valid longer match.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"& is an HTML entity but &ambassador; is not."` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "&amp; is an HTML entity but &ambassador; is not."}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"& is an HTML entity but &ambassador; is not."` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check for ampersand first:** Copy ordinary characters immediately and test entities only when `text[i] == '&'`. This reduces constant work while keeping the same $O(n)$ complexity and semantics.
- **Trie of entity tokens:** A trie can consume characters until a token matches or fails. It becomes attractive with a large or extensible entity vocabulary, but six tokens of maximum length seven do not require that machinery.
- **Repeated global replacement:** Calling `replace` once per entity is concise but scans the full string several times and can accidentally introduce ordering questions when one replacement produces text resembling another entity.
- **Regular expression:** A pattern can find supported tokens and use a callback dictionary. It is valid but hides the straightforward consumption invariant behind regex behavior.
- **Recursive decoding:** Parsing newly produced output again is incorrect for this task. `&amp;gt;` should undergo the source scan once rather than automatically becoming `>` through two rounds.
- **Unknown entity-like text:** A string such as `&ambassador;` is not a dictionary key, so every character is preserved.
- **Incomplete entity:** A trailing fragment such as `&quo` never matches a complete key and remains unchanged.
- **Adjacent entities:** After one match sets `i` to its end, the next outer iteration begins exactly at the following entity and decodes it independently.
- **Ordinary ampersand:** A lone `&` fails all token tests and is copied literally.
- **Longest entity:** `&frasl;` is found when `l == 7`; using `range(1, 7)` would miss it because the upper bound is exclusive.
- **Quotes and apostrophes:** The dictionary values use appropriate Python quoting but each represents a single literal output character.
- **All ASCII input:** Characters outside the six supported source sequences pass through unchanged, regardless of whether they have special meaning in broader HTML standards.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of characters in `text`. The outer loop consumes at least one source character per iteration, so it runs at most $n$ times. Each iteration checks at most seven candidate lengths. Every tested slice has length at most seven, and dictionary lookup involves one of these constant-size strings. The work per outer iteration is therefore bounded by a constant, giving $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
