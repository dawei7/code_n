# Create Grid With Exactly K Paths II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3990 |
| Difficulty | Hard |
| Topics | Uncategorized |
| Official Link | [LeetCode](https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/) |

## Problem Description
### Goal
Write an original, source-faithful problem narrative with depth and length
proportionate to the public statement. Follow the source problem's logical
order as closely as independent wording permits: introduce the same scenario
or data model, state every operation rule and guarantee that affects
interpretation, preserve distinctions and boundary semantics, and finish with
the exact requested outcome. Use multiple paragraphs when the source has
substantial context. Rephrase all prose rather than copying LeetCode's text;
fidelity means complete semantic coverage, not sentence-level imitation or
generic padding. Preserve source-native technical vocabulary exactly: do not
replace terms such as `ascending`, `non-decreasing`, `strictly increasing`,
`subarray`, `subsequence`, `at most`, or `exactly` with near-synonyms. Rephrase
surrounding sentences, not mathematical relations or named concepts. Do not
rewrite merely to make the prose different: every departure from the source
should improve clarity, sequencing, semantic coverage, or explanation of a
material boundary condition. Keep source wording and structure when they are
already the clearest independently usable formulation. Do not compress a rich
statement into a one-sentence summary.

Write abstract mathematical relations and formulas in LaTeX using `$...$`
inline or `$$...$$` for a display equation. Prefer conventional notation such as
`\lvert x \rvert`, `\lfloor x \rfloor`, `\lceil x \rceil`, `\min`, `\max`,
`\sum`, and `\log`. Put executable calculations in code spans: assignments,
array or map indexing, slices, function calls, pointer updates, and language
operators remain code, as in `nums[a] = target - nums[b]`. Reserve backticks
as well for identifiers discussed as code, strings, serialized inputs and
outputs, SQL, and other literal data. Use ordinary mathematical symbols rather
than code-styled identifiers inside genuine formulas. Define every
problem-specific complexity symbol in the Function Contract or surrounding
non-collapsed explanation before using it in a bound. When the expression is
long or would otherwise be repeated, prefer a displayed definition:

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

Then use `$S$` in the prose and complexity bounds.

### Function Contract
**Inputs**

- TODO

**Return value**

TODO

### Examples
**Example 1**

- Input: `TODO`
- Output: `TODO`

Add one or two more concise examples when they expose a distinct edge case.

### Required Complexity
- **Time:** $O(...)$
- **Space:** $O(...)$

<details>
<summary>Approach</summary>

#### General

Teach the reasoning, not merely the final technique:

Organize this section around the problem's actual ideas. Derive the method from
the decisive constraints and explain correctness, examples, invariants, or
traces where they materially help. The only level-four subsection headings are
`General`, `Complexity detail`, and `Alternatives and edge cases`; all three are
required in that order. The Two Sum document's sequence must not be copied
mechanically.

Organize a substantial `General` explanation with descriptive bold subheadings
such as `**Why the unique pair must be found**`. Choose each signpost for this
problem (for example, name a state definition, greedy choice, or reconstruction
step); do not repeat a mandatory set across the corpus. A short, simple approach
may need none. Do not introduce additional Markdown heading levels inside
Approach.

Correctness reasoning belongs in every explanation, but not in a mandatory
`Correctness` or `Correctness argument` slot. Integrate it with the relevant
state, transition, exchange argument, construction, or trace rather than
adding another subsection heading.

Let the problem determine the length. A direct observation may need only a
short derivation, but a complex algorithm should receive enough space for its
state, transitions, data structures, worked reasoning, and correctness
argument. Never omit useful explanation to make documents the same size.

Do not include solution code or a reference implementation in the problem document.

#### Complexity detail

Explain the stated time and auxiliary-space bounds precisely, including the
meaning of any problem-specific variables and why apparently nested work is or
is not repeated.

#### Alternatives and edge cases

- **Name a genuine alternative:** compare its complexity, storage, correctness
  risk, or implementation tradeoff with the selected method.
- **Name another alternative when useful:** do not invent one merely to reach a
  fixed number of bullets.
- State each material boundary condition or semantic trap as its own bullet.
- Keep this entire subsection as a scannable list rather than free-text
  paragraphs.

</details>
