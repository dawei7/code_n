# Guided Example: Remove Letter To Equalize Frequency

## 1. The instance and what "exactly one" forbids

Take `word = "abcc"`, for which the required answer is `true`. The lesson then
turns to `word = "aazz"`, whose answer is `false`, because the two instances
differ only in ways that the phrase *exactly one letter* makes decisive.

The task is not "can the frequencies be made equal". It is "can they be made
equal by deleting exactly one character, neither more nor fewer". That
qualification is the whole difficulty of the problem, and every failure in this
lesson is a violation of it rather than a failure of the counting itself.

## 2. Positions collapse to letter types

The statement asks about an index, but the effect of a deletion depends only on
which **letter** is deleted, not on which of its occurrences was chosen. If a
letter $c$ occurs $m$ times, deleting any one of those $m$ positions lowers the
frequency of $c$ by one and leaves every other letter's frequency untouched.

So the search space shrinks from $n$ candidate positions to at most
$\sigma \le 26$ candidate letter types, where $\sigma$ is the number of distinct
letters in `word`. This is not an approximation: two positions holding the same
letter produce literally the same frequency table, so testing the type once
covers every position of that type.

## 3. The frequency table and the zero-count rule

Let $\mathrm{cnt}[c]$ be the number of occurrences of letter $c$ in the original
word. Deleting one occurrence of $c$ produces the vector
$\mathrm{cnt}'$ with

$$
\mathrm{cnt}'[c] = \mathrm{cnt}[c] - 1,
\qquad
\mathrm{cnt}'[d] = \mathrm{cnt}[d] \ \text{ for } d \ne c .
$$

The resulting word is valid exactly when all letters that are **still present**
have the same frequency. A letter with $\mathrm{cnt}'[d] = 0$ is absent from the
resulting word and imposes no requirement at all. That gives the test:

$$
\lvert\{\, \mathrm{cnt}'[d] : d \text{ is a letter and } \mathrm{cnt}'[d] > 0 \,\}\rvert = 1 .
$$

The set on the left collects distinct positive frequencies; it has size one
precisely when every surviving letter shares a single common frequency. The
resulting word is never empty, because the input has at least two characters and
only one is removed, so the set on the left is never itself empty.

Zero must be excluded, not rounded away. Deleting the only occurrence of a letter
is a legal move, and afterwards that letter simply does not participate.

| Letter | $\mathrm{cnt}[c]$ in `"abcc"` | Present after deleting one `c` | Compared? |
|---|---|---|---|
| `a` | 1 | yes, frequency 1 | yes |
| `b` | 1 | yes, frequency 1 | yes |
| `c` | 2 | yes, frequency 1 | yes |

## 4. Worked trace of `"abcc"`

The word has three distinct letters, so exactly three trials run. The table
records the state of the frequency table inside each trial, before the table is
restored.

| Trial | Letter deleted | Frequencies during trial | Positive frequencies | Distinct positive values | Verdict |
|---|---|---|---|---|---|
| 1 | `a` | `a = 0`, `b = 1`, `c = 2` | `1, 2` | 2 | fail, restore |
| 2 | `b` | `a = 1`, `b = 0`, `c = 2` | `1, 2` | 2 | fail, restore |
| 3 | `c` | `a = 1`, `b = 1`, `c = 1` | `1, 1, 1` | 1 | success, answer `true` |

Trials 1 and 2 are the instructive failures. Deleting an `a` makes `a` vanish, so
the trial compares only `b = 1` and `c = 2`; those differ, and the deletion is
rejected. It is *not* rejected because `a` reached zero. If zeros were compared,
trial 1 would show `0, 1, 2` and trial 3 would still show `1, 1, 1` — the final
answer would happen to survive here, but the rule would be wrong, as the next
section shows.

Trial 3 succeeds because the original word had exactly one over-represented
letter: `c` appeared twice while `a` and `b` appeared once. Reducing the lone
excess by one equalises everything.

## 5. Failure instances and the trap they expose

`word = "aazz"` looks like an easy success: the two frequencies are already equal
at $2$ and $2$. But the operation is mandatory, so "leave it alone" is one of the
forbidden moves.

| Trial | Letter deleted | Frequencies during trial | Positive frequencies | Distinct positive values | Verdict |
|---|---|---|---|---|---|
| 1 | `a` | `a = 1`, `z = 2` | `1, 2` | 2 | fail |
| 2 | `z` | `a = 2`, `z = 1` | `2, 1` | 2 | fail |

Every legal move destroys the balance that was already present, so the answer is
`false`. The same mechanism rejects `"aabbcc"` (each trial turns `2, 2, 2` into
`1, 2, 2`) and `"aaabbb"` (each trial turns `3, 3` into `2, 3`). Once every
frequency is equal and more than one letter is present, no single deletion can
preserve equality.

Contrast with instances where deletion of a whole letter type is the answer:

| Instance | Original frequencies | Trial that succeeds | Frequencies after deletion | Answer |
|---|---|---|---|---|
| `"abbcc"` | `a = 1`, `b = 2`, `c = 2` | delete the only `a` | `b = 2`, `c = 2` | `true` |
| `"aaa"` | `a = 3` | delete one `a` | `a = 2` | `true` |
| `"ab"` | `a = 1`, `b = 1` | delete either letter | one letter with frequency 1 | `true` |
| `"aaabbbbcc"` | `a = 3`, `b = 4`, `c = 2` | none | — | `false` |

Two facts fall out of this table. First, the common frequency does not have to be
1: `"aaa"` succeeds with the surviving frequency 2. Second, a letter reaching
frequency zero is a feature, not an error, which is why the positive-only filter
matters — without it, `"abbcc"` would be misjudged, because the vanished `a`
would contribute a spurious `0` next to `b = 2` and `c = 2`.

## 6. Why the reasoning is correct

**Invariant of the trial loop.** At the start of every trial the frequency table is
identical to the table built from the original word. This holds initially by
construction, and it is restored after each failed trial. Consequently every
trial measures the effect of *exactly one* deletion rather than the accumulated
effect of all deletions attempted so far.

**Soundness.** If trial $c$ finds a single distinct positive frequency, then the
word obtained by removing one occurrence of $c$ has all present letters equally
frequent. That word differs from the input at exactly one position, so it is a
legitimate witness for the required single deletion, and reporting `true` is
correct.

**Completeness.** Suppose some index $p$ is a valid deletion, and let $c$ be the
letter at that position. Because $c$ occurs in the word, $c$ is one of the keys
of the original frequency table and is therefore tried. Deleting any other
occurrence of $c$ yields the same resulting frequency vector, so trial $c$ must
observe the same single distinct positive frequency and report success. No valid
deletion can be missed, because positions are grouped by an equivalence that
preserves the only quantity the test inspects.

**Exhaustiveness of the failure.** If no trial succeeds, then for every letter
type the deletion leaves at least two different positive frequencies. Since every
position of the word belongs to exactly one letter type, no position can be a
valid deletion, and reporting `false` is correct. This is where the mandatory
"exactly one" condition is enforced: the algorithm never tests the zero-deletion
state, so an already-equal input with more than one letter is correctly rejected.

## 7. Boundary conditions this instance family exposes

| Situation | Instance | Answer | Why |
|---|---|---|---|
| Minimum length | `"ab"` | `true` | Removing one character always leaves a single letter type with frequency 1. |
| One distinct letter | `"aaa"` | `true` | Deleting one occurrence leaves one letter type, whose frequency is trivially uniform. |
| All letters distinct | `"abcd"` | `true` | Each trial leaves the other letters at frequency 1. |
| Already equal, two types | `"aazz"` | `false` | Equality exists before the move, but the move is compulsory and breaks it. |
| Already equal, three types | `"aabbcc"` | `false` | Same mechanism with more letters; each trial produces `1, 2, 2`. |
| Deleted letter disappears | `"abbcc"` | `true` | The vanished letter is ignored because only positive frequencies are compared. |
| Two different frequency classes | `"aaabbbbcc"` | `false` | Frequencies `3, 4, 2`; one decrement can repair at most one class. |
| Perfectly balanced larger counts | `"aaabbb"` | `false` | Both trials produce `2` next to `3`. |
| Maximum length | any 100-character word | depends | Only $\sigma \le 26$ trials are ever needed, so length affects only the counting pass. |

## 8. Alternative methods and their trade-offs

| Method | Time | Auxiliary space | Why it is not used here |
|---|---|---|---|
| Delete each of the $n$ positions and recount | $O(n^2)$ | $O(n)$ | Simulates the statement literally but rebuilds a whole string and a whole table per position, repeating work that is identical within a letter type. |
| Sort the surviving frequencies per trial | $O(\sigma^2 \log \sigma)$ | $O(\sigma)$ | A sorted list decides equality, but distinguishing *distinct positive values* is exactly what a set does in one pass. |
| Characterise from the frequency-of-frequencies | $O(n)$ | $O(\sigma)$ | Cases such as "one letter has frequency 1 and the rest are equal" or "one unique maximum is exactly one above the rest" can be enumerated directly; it is faster in prose but easy to mis-handle the zero-count and mandatory-deletion cases. |
| Enumerate letter types and test a set of positive frequencies | $O(n + \sigma^2)$ | $O(\sigma)$ | Chosen. The grouping argument removes the redundant work, and a single set membership test expresses the condition without special cases. |

## 9. Cost of the method: complexity derivation

Let $n = \lvert\texttt{word}\rvert$ and let $\sigma$ be the number of distinct
letters in it, so $\sigma \le 26$.

*Time.* Building the frequency table reads every character once, which costs
$O(n)$ under the standard assumption that a letter maps to a table slot in
constant time. Then $\sigma$ trials run; each trial changes one entry, scans the
$\sigma$ stored entries to collect the positive ones, and is undone. Each trial is
$O(\sigma)$, so the trials cost $O(\sigma^2)$. The total is

$$
T(n) = O(n) + O(\sigma^2).
$$

Because the alphabet is fixed at 26 lowercase English letters, $\sigma^2 \le 676$
is a constant, and the bound collapses to $T(n) = O(n)$. The quadratic term in
$\sigma$ is honest but irrelevant at this input size; it would matter only if the
alphabet were allowed to grow with $n$.

*Auxiliary space.* The only structure proportional to anything is the frequency
table, which holds at most 26 entries regardless of how long the word is. The
per-trial set of positive frequencies holds at most $\sigma$ values and is
discarded at the end of each trial. Auxiliary memory is therefore

$$
S(n) = O(\sigma) = O(1).
$$

The input string is never copied or mutated: only counts change, and they change
back.
