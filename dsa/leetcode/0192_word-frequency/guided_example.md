# Guided Example: Word Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"stdin": "", "files": {"words.txt": "the day is sunny the the\nthe sunny is is\n"}}`
- **Required output:** `"the 4\nis 3\nsunny 2\nday 1"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a bash script to calculate the frequency of each word in a text file `words.txt`.

The objective is to compute `"the 4\nis 3\nsunny 2\nday 1"` from `{"stdin": "", "files": {"words.txt": "the day is sunny the the\nthe sunny is is\n"}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the shell pipeline as staged data transformations

The script turns a text file into one word per record, sorts equal words
together, counts adjacent equal records, sorts those counts from largest to
smallest, and finally rearranges each line into the requested `word count`
format. Each command has one small responsibility, and the pipe operator sends
one command's standard output into the next command's standard input.

The complete pipeline reads the fixed file `words.txt`; it does not consume
function parameters or caller-provided standard input. Its final command writes
to standard output, matching the Reference contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"stdin": "", "files": {"words.txt": "the day is sunny the the\nthe sunny is is\n"}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize spaces into line boundaries

`cat words.txt` streams the file contents. `tr -s ' ' '\n'` translates every
space into a newline. The `-s` option squeezes repeated translated characters,
so a run of several spaces becomes one newline rather than several empty
records.

Existing newline characters pass through unchanged. Under the Reference's
restricted content—lowercase word characters, spaces, and the physical line
boundaries of the file—every word consequently occupies its own line. This is
the representation the following Unix tools expect.

The initial `cat` is not necessary; `tr -s ' ' '\n' < words.txt` could read the
file directly. It is nevertheless logically correct and makes the left-to-right
pipeline visually explicit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort words so equal values become adjacent

The first `sort` orders the one-word lines lexicographically. Its purpose is not
the final display order. It prepares the stream for `uniq`, which only combines
equal lines that are next to one another.

Without this sort, occurrences of `the` separated by other words would form
different runs and `uniq -c` would report several partial counts. Sorting turns
all occurrences of each word into one contiguous block.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"the 4\nis 3\nsunny 2\nday 1"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"stdin": "", "files": {"words.txt": "the day is sunny the the\nthe sunny is is\n"}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"the 4\nis 3\nsunny 2\nday 1"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Single `awk` counter:** Scan all fields into an associative array, print counts, then sort by the second field; this is the competitive variant and handles general field whitespace better.
- **Direct input redirection:** Replace `cat words.txt | tr ...` with `tr ... < words.txt` to avoid an unnecessary process.
- **`grep -o` tokenization:** Extract lowercase runs explicitly, but behavior and options vary across environments.
- **Repeated spaces:** `tr -s` collapses them into one delimiter.
- **Line breaks:** Existing newlines already separate records and need no translation.
- **Tabs or carriage returns:** Not translated by the exact command; use `awk` or a complete whitespace class if the domain expands.
- **Leading or trailing spaces:** May expose empty-record behavior; filter empty lines for a generalized script.
- **One distinct word:** `uniq -c` emits one record and both sorts remain harmless.
- **Unique-frequency guarantee:** Makes unspecified tie ordering irrelevant.
- **Locale:** Can affect lexical comparison cost/order in the preparatory sort but not grouping equality for identical lowercase words.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u\log u)$. Let $n$ be the number of word occurrences and $c$ the total number of input
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
