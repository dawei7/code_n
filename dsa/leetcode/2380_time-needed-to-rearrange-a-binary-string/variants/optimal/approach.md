## General

Every `'1'` that appears after one or more zeroes must eventually move left across all those zeroes. Two effects determine when that one finishes: the number of zeroes it must cross, and congestion from earlier ones that are also moving.

**Count required crossings.** Scan from left to right and count zeroes seen. A `'1'` encountered when this count is zero is already on the stable side and needs no time.

**Account for the simultaneous pipeline.** For a `'1'` behind zeroes, crossing all preceding zeroes requires at least `zeros` seconds. It also cannot finish earlier than one second after the previous movable `'1'`, because simultaneous replacement prevents two ones from using the same opening in one round. Therefore update:

`seconds = max(zeros, seconds + 1)`.

After processing a prefix, `seconds` is the time at which all its movable ones can be placed before its zeroes. The next one either needs enough time for its own crossings or waits behind that established pipeline. This recurrence captures both lower bounds, and the simultaneous process achieves their maximum, so the final value is the exact completion time.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. The scan examines every character once, giving $O(n)$ time. It stores only the zero count and current completion time, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Literal simulation:** Replacing every `"01"` once per second directly follows the statement but can take $O(n^2)$ time because there may be $O(n)$ rounds.
- **Track moving positions:** A queue of ones or zero openings can model each crossing event, but the two-scalar recurrence is simpler.
- **Already stable:** Strings of the form all ones followed by all zeroes require zero seconds.
- **All equal:** A string containing only one symbol has no `"01"` occurrence.
- **Zero-then-one blocks:** For `a` zeroes followed by `b` ones, the pipeline takes `a + b - 1` seconds when both groups are nonempty.
- **Simultaneity:** A one may move at most one position during a second, even if its replacement creates another `"01"`.
