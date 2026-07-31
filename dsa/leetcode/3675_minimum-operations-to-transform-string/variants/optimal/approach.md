## General

Multiple occurrences of one letter are indistinguishable because an operation always advances all of them together. When an advanced group reaches another occupied letter, the two groups merge and can move together thereafter.

Ignore `a` and let the alphabetically smallest remaining letter have zero-based rank $p$, where `a` has rank $0$. Advancing this group once per letter from rank $p$ through `z` and then to `a` takes $26-p$ operations. During that forward sweep it reaches and absorbs every occupied letter with a larger rank, so the entire non-`a` portion arrives at `a` within those operations. Existing `a` characters never need to move.

This count is also unavoidable. The group beginning at rank $p$ cannot move backward, disappear, or reach `a` without traversing each of the $26-p$ successor steps. Merging can let other groups share those steps but cannot shorten this group's route. Hence $26-p$ is the exact minimum. If no non-`a` character exists, the answer is zero.

Scan `s` once to find the minimum positive letter rank, then return its circular distance to zero.

## Complexity detail

The scan examines $n$ characters and stores only one rank, so it takes $O(n)$ time and $O(1)$ auxiliary space. Any correct algorithm must inspect the complete string in the worst case because an unexamined position could contain the smallest non-`a` letter and change the answer.

The benchmark defines its size as the string length $n$ and distributes all non-`a` letters throughout the input. The accepted scan visits the string once. A calibrated correct alternative redundantly rescans the entire string once for every character, producing quadratic growth without changing any result.

## Alternatives and edge cases

- **Simulate each replacement:** At most 25 useful steps are needed, but rebuilding or scanning the string after every step performs unnecessary work.
- **Repeated minimum searches:** Recomputing the same smallest rank for every position is correct but grows quadratically.
- **All `a` characters:** No operation is needed, and there is no positive rank from which to measure a distance.
- **Only `z` characters:** One operation wraps every occurrence directly to `a`.
- **Presence of `b`:** Any `b` forces the maximum answer 25 because it has the longest forward route to `a`.
- **Duplicate letters:** Multiplicity does not increase the operation count because all equal occurrences advance simultaneously.
- **Existing `a` characters:** They may remain untouched while every other group advances and eventually merges into them.
