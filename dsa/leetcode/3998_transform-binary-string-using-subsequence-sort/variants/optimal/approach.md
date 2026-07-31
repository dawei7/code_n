## General

Sorting a selected binary subsequence preserves the total number of ones. It can move a zero to the left across an earlier one, but it can never move a one left across an earlier zero. Consequently, every prefix of a reachable target contains no more ones than the corresponding prefix of `s`.

These conditions are also sufficient. Whenever a target zero occurs earlier than its matching source zero, swap it left across a source one by sorting that two-position subsequence `10` into `01`. Repeating such inversion removals produces any target with the same total number of ones and no larger prefix-one count. Thus total equality and the prefix inequalities characterize reachability exactly.

For one pattern, let `needed_ones` be the source's total number of ones minus the pattern's fixed ones. It must lie between zero and the number of question marks. Among all assignments using exactly that many ones, placing them in the rightmost question-mark positions minimizes the number of assigned ones in every prefix. If even this minimum-prefix assignment exceeds a source prefix, every other assignment fails there; if it respects every prefix, it is itself a reachable completion.

Precompute the source's prefix-one counts. For each pattern, count its fixed ones and question marks, determine `needed_ones`, and scan left to right while treating the first `question_count - needed_ones` question marks as zeros and the rest as ones. The pattern is feasible exactly when this scan never exceeds the stored source prefix.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert\texttt{strs}\rvert$. Every pattern also has length $n$. Building the source prefix array takes $O(n)$ time. Each pattern is counted and scanned in $O(n)$ time, for $O(nm)$ total time.

The source prefix array uses $O(n)$ auxiliary space. All per-pattern counters use $O(1)$ space; the required returned boolean array uses $O(m)$ output space and is not included in the auxiliary-space bound.

## Alternatives and edge cases

- **Enumerate wildcard assignments:** Trying all $2^q$ replacements for $q$ question marks is exponential and unnecessary because the rightmost-one assignment dominates every other assignment prefix by prefix.
- **Recount every prefix:** Recomputing both one counts from scratch for every prefix remains correct but takes $O(mn^2)$ time.
- **Wrong total number of ones:** A pattern with too many fixed ones, or too few question marks to supply the missing ones, is immediately impossible.
- **Zero operations:** A completion identical to `s` satisfies both reachability conditions and is accepted.
- **All-zero or all-one source:** Total-count feasibility forces every wildcard consistently; the same prefix test still applies without a special transformation rule.
- **Forced early one:** Equal total counts are not sufficient when a fixed one makes some target prefix exceed the corresponding source prefix.
