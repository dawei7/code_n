## General
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

## Complexity detail
Explain the stated time and auxiliary-space bounds precisely, including the
meaning of any problem-specific variables and why apparently nested work is or
is not repeated.

## Alternatives and edge cases
- **Name a genuine alternative:** compare its complexity, storage, correctness
  risk, or implementation tradeoff with the selected method.
- **Name another alternative when useful:** do not invent one merely to reach a
  fixed number of bullets.
- State each material boundary condition or semantic trap as its own bullet.
- Keep this entire subsection as a scannable list rather than free-text
  paragraphs.
