# Guided Representative Examples

Guided examples are code-free, package-authored lessons that solve one carefully
chosen instance from beginning to end. Their purpose is conceptual
understanding: a learner should see what information is maintained, why each
transition is valid, which alternatives have been eliminated, and how the final
answer follows.

They are ordinary Markdown documents, not interactive executions, recorded
animations, solution editorials, or serialized UI state.

## Canonical contract

Each participating LeetCode package owns exactly one optional lesson:

```text
dsa/leetcode/<frontend_id:04d>_<slug>/guided_example.md
```

The server returns that file unchanged from
`/api/docs/by-id/{challenge_id}/guided-example`. Challenge summaries advertise
its presence through `has_guided_example`. The web client renders the Markdown
with GitHub-Flavored Markdown tables and KaTeX mathematics. Relative image
references resolve through the package's existing `assets/` directory.

There is no secondary JSON manifest, playback timeline, code anchor, renderer
family, or duplicated source representation. `guided_example.md` is the sole
lesson artifact.

## Required teaching structure

Every guide should contain:

1. A title of the form `# Guided Example: <problem title>`.
2. One representative input and its required outcome.
3. Numbered, problem-specific sections that derive and execute the method step
   by step.
4. A visible state representation wherever it improves understanding: Markdown
   tables, mathematical displays, text diagrams, or package-local images.
5. An explanation of why the transitions and eliminations are valid.
6. A focused discussion of traps exposed by the chosen instance.
7. A final time and auxiliary-space analysis.

The numbered sections are not a fixed universal template. A graph traversal may
show a frontier and visited set; dynamic programming may show state tables and
dependencies; geometry may use diagrams and equations; a greedy argument may
show the exchange that makes an alternative choice unnecessary. Use the native
technical vocabulary of the algorithm and its mathematical model.

## Choosing the representative input

Prefer the smallest input that exposes the method's decisive ideas. A useful
example often includes one or more of the following:

- a tempting but invalid local choice;
- both directions of a monotone search correction;
- duplicates or boundary values that require precise semantics;
- a state transition that proves a large candidate region impossible;
- more than one valid output when completeness matters; or
- an edge condition handled by the main method rather than a special branch.

Do not choose a long input merely to create more steps. Each row, diagram, and
transition must carry explanatory value.

## Visual language

- Use Markdown tables for arrays, pointer positions, state variables,
  comparisons, partitions, recurrences, and before/after relationships.
- Use LaTeX for equations, invariants, ranks, bounds, and proofs.
- Use fenced `text` diagrams only when spatial structure is clearer than a
  table. A diagram is not a substitute for an explanation.
- Put optional images under the package's `assets/` directory and reference
  them relatively. Provide meaningful alt text and ensure that the surrounding
  prose still communicates the essential conclusion.
- Never rely on color alone. Labels and mathematical relations must carry the
  meaning.

## Code-free boundary

Do not show implementation source, pseudocode, language syntax, solution-file
paths, or line-by-line code commentary. Literal inputs and outputs, identifiers
from the problem contract, mathematical notation, and abstract data-structure
state are allowed.

The canonical solution remains in `solutions/` and is revealed through the
separate Reference workflow according to product rules. The guide should make
that eventual implementation understandable without spelling it out.

## PDF bundles

The left challenge pane owns PDF export. Each PDF symbol mirrors the scope of
the adjacent practice-file download control: one problem, one visible hierarchy
level, or all currently shown problems. A bundle preserves the active set's
problem order and emits documents in this sequence for every problem:

1. Reference
2. Guided Example, when authored
3. Primary-language Solution, only when the user selects **With solution**

The PDF symbol opens a menu with **Without solution** and **With solution**.
Without solution is the source-free Reference and Guided Example bundle. With
solution appends the canonical source in the package's declared primary
language: normally Python 3, or a source-native language such as SQL, Bash, or
JavaScript where the problem requires it. The Reference tab's interactive
solution panel itself is never printed.

Every document begins on a new page. PDF output is always light mode. The
opening table of contents preserves nested set/group hierarchy and links each
problem to its Reference section. It also records the PDF generation timestamp
in UTC. A compact link in every subsequent page margin returns to that first
page.

## Writing standard

- Write for students of computer science and mathematics using correct terms
  such as invariant, monotonicity, rank, partition, soundness, completeness,
  state, frontier, and auxiliary space where they genuinely apply.
- Explain causality: state not only what changes, but why that change cannot
  remove a feasible answer.
- Distinguish value identity from index identity and input space from output
  space whenever the problem requires it.
- Keep prose original and independent. Do not reproduce another platform's
  statement, editorial, diagrams, or visual composition.
- Prefer precise, compact exposition over motivational filler or decorative
  UI language.

## Validation

The regression tests verify endpoint behavior, package availability, common
structural requirements, Markdown content type, and the absence of solution
source markers. Run:

```powershell
.\.venv\Scripts\python.exe -m pytest server\tests\test_guided_examples.py -q
npm.cmd run typecheck --prefix web
npm.cmd run build --prefix web
git diff --check
```
