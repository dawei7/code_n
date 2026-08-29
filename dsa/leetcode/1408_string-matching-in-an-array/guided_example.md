# Guided Example: String Matching in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["mass", "as", "hero", "superhero"]}`
- **Required output:** `["as", "hero"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of string `words`, return all strings in* *`words`* *that are a substring of another word. You can return the answer in **any order**.

The objective is to compute `["as", "hero"]` from `{"words": ["mass", "as", "hero", "superhero"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the requirement into an existence test

For each candidate word `s`, the question is not how many times it occurs or where it begins. It only asks whether at least one different array element contains `s` as a contiguous substring. That is an existential condition:

$$
\text{keep } s \iff \text{there exists an index } j \ne i \text{ such that } s \text{ is contained in } \texttt{words}[j].
$$

The stored solution expresses that definition almost word for word. The outer loop visits every word together with its index:



Keeping `i` is necessary because the candidate must occur in another word. Every string is trivially a substring of itself, so a search that includes the same array position would incorrectly accept every input.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["mass", "as", "hero", "superhero"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the inner generator checks all possible containers

For the current candidate, this expression examines the array again:



Each generated Boolean combines two requirements:

- `i != j` ensures that `t` comes from a different array position.
- `s in t` uses Python's substring operation, which is true only when all characters of `s` occur contiguously and in order somewhere within `t`.

The word “substring” is stricter than “subsequence.” For example, `"ace"` is a subsequence of `"abcde"` but not a substring because its letters are separated. Python's `in` operation performs the required contiguous search.

The `and` operator short-circuits from left to right. When `i == j`, Python does not even evaluate `s in t`. This avoids counting the candidate's occurrence in itself and skips an unnecessary search.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `any` matches the problem exactly

`any` returns true as soon as the generator produces its first true value. Once one other word contains `s`, no further evidence can change whether `s` belongs in the answer. The early exit saves work when a match occurs near the beginning of the list.

If every different word fails the substring check, the generator is exhausted and `any` returns false. The candidate is then omitted. Thus the condition has exactly the two outcomes required by the contract.

When the condition is true, `ans.append(s)` stores the original string. The algorithm appends at most once for each outer-loop position, even if several different words contain it. The input guarantee that all words are unique further means the returned list cannot contain duplicate string values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["as", "hero"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["mass", "as", "hero", "superhero"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["as", "hero"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit nested loops:** Two ordinary loops plus `break` implement exactly the same method and may be easier for a beginner to debug. The generator with `any` is a concise version of that control flow.
- **Knuth-Morris-Pratt search:** Building an LPS table for each candidate makes each pairwise substring search linear in the text length. It improves the character-comparison bound but adds preprocessing code and state for the short maximum word length of 30.
- **Suffix trie:** Inserting every suffix of every word allows candidates to be queried through trie paths. It avoids checking every pair directly but can use $O(nL^2)$ nodes in the worst case and is substantially more complex.
- **Sort by length:** Processing shorter words first and comparing them only with longer words can skip impossible pairs. The uniqueness guarantee means equal-length distinct words cannot contain one another.
- **Concatenate with separators:** Searching for each word in a combined string is dangerous unless boundaries and the word's own occurrence are handled carefully. A match spanning a separator must never count.
- **Only one input word:** The generator sees only the same index, which fails `i != j`, so `any` is false and the answer is empty.
- **Candidate longer than container:** `s in t` safely returns false; no explicit length guard is required.
- **Candidate equal to another word:** The constraints say all strings are unique. Without that guarantee, equal strings at different indices would correctly count as one being a substring of another position.
- **Several containing words:** `any` stops at the first successful one, and the candidate is appended only once.
- **Substring at an edge:** Matches at position zero or ending at the final character are ordinary valid substring matches and are recognized by `in`.
- **Character order without contiguity:** Merely finding the same letters in order is insufficient. The use of `s in t` enforces adjacency.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2L^2)$. Let $n$ be the number of words and let $L$ be the maximum word length. The outer loop has $n$ iterations. In the worst case, `any` examines all $n$ possible container positions for every candidate, giving $O(n^2)$ pair checks.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
