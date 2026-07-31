## General

For each position, count the zero-filled subarrays that end exactly there. If
the current value is nonzero, that count is zero. If it is zero and the current
zero run has length $r$, the valid endings are the last zero alone, the last
two zeros, and so on through the entire run: exactly $r$ choices.

**Accumulate run lengths**

Maintain `run`, the number of consecutive zeros ending at the current
position. Increment it for zero and reset it for any nonzero value, then add it
to the answer. Every qualifying subarray has one unique ending position and is
counted among that position's suffixes, while every counted suffix lies wholly
inside a zero run. The sum is therefore exact.

Equivalently, a complete run of length $r$ contributes
$1+2+\cdots+r=r(r+1)/2$; the incremental method produces this sum without
needing to store or revisit runs.

## Complexity detail

The array is scanned once, giving $O(n)$ time. The current run length and
answer use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sum completed runs:** Detect every maximal zero run and add its triangular
  number; this has the same bounds but needs explicit end-of-array handling.
- **Enumerate every interval:** Testing all possible subarrays is correct but
  requires at least $O(n^2)$ work.
- **No zeros:** Every run length remains zero, so the answer is zero.
- **All zeros:** A length-$n$ array contributes $n(n+1)/2$.
- **Negative nonzeros:** Their sign is irrelevant; every nonzero value resets
  the run.
