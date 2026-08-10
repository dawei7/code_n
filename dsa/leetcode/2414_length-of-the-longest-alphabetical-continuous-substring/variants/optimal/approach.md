## General

**A valid substring is an exact successor run**

Within an alphabetical continuous substring, every next character must be exactly one alphabet position after the previous:

```text
a -> b -> c -> ...
```

It is not enough for characters merely to increase. `'a'` followed by `'c'` skips a letter and breaks continuity. `'z'` followed by `'a'` is also invalid because the alphabet does not wrap.

The algorithm tracks the length `cnt` of the current exact-successor suffix and `ans` as the longest such run seen.

**Compare numeric character codes**

`map(ord, s)` lazily converts letters to code points. For consecutive values `x` and `y`, the condition:

```python
y - x == 1
```

is true precisely when the second lowercase English letter is the immediate alphabet successor of the first.

ASCII/Unicode lowercase code points are consecutive, so no lookup table is needed.

**Initialize the first character**

The input is nonempty. Any one-character substring appears in the alphabet string and is continuous, so both `ans` and `cnt` begin at one.

`pairwise(...)` then yields every adjacent code-point pair. If the successor condition holds, the current run extends and `cnt` increments. The code updates `ans` with the larger run length.

If the condition fails, `cnt` resets to one because the current character begins a new valid one-character run.

**Why `ans` need not update on reset**

A reset produces run length one. `ans` was initialized to one and never decreases, so resetting cannot create a new larger maximum. Updating only inside the extension branch is sufficient.

**Trace `"abacaba"`**

`a -> b` differs by one, so the run grows to length two. `b -> a` breaks and resets. `a -> c` skips `b` and also breaks. Later adjacent pairs produce runs of at most two.

The maximum remains two, corresponding to substring `"ab"`.

For `"abcde"`, every adjacent difference is one. `cnt` grows from one through five, and `ans` ends at five.

**Why counting the longest suffix solves all substrings**

After processing position `i`, `cnt` equals the longest alphabetical continuous substring ending exactly at `i`. If the previous pair is consecutive, every valid suffix ending at `i-1` can be extended, and the maximal one grows by one. If not, no multi-character valid substring can cross that boundary, so only the singleton remains.

Every substring has a unique ending position. Taking the maximum of these exact ending lengths therefore finds the longest anywhere in `s`.

**Formal invariant**

Before each pair update, `cnt` is the length of the maximal valid suffix ending at the pair's first character, and `ans` is the greatest run length over all processed endings.

When `y=x+1`, appending `y` preserves continuity and yields the only possible longer suffix. When not, every suffix containing both characters fails at their adjacency, so reset is exact. Updating the maximum preserves the second invariant.

Initialization establishes both at index zero, and induction proves the returned result.

**Why substrings, not subsequences**

The scan only extends across adjacent source characters. It cannot skip an interfering letter. This matches the contiguous substring requirement. A subsequence solution that skipped characters would answer a different problem.

**No cyclic alphabet**

Code-point difference from `'z'` to `'a'` is negative 25, not one. The condition rejects `"za"` automatically, as the statement requires.

**Invalid boundaries partition the search space**

Whenever an adjacent pair fails the exact-successor test, no valid substring can include characters on both sides of that boundary. Every candidate crossing it contains the same invalid adjacency. The string is therefore divided into maximal successor runs, and the answer is simply the greatest run length. The online counter computes those lengths without explicitly storing the runs. This boundary view also proves that resetting loses no possible longer candidate: all future valid substrings must begin on or after the character to the right of the failure.

**Difference one is both necessary and sufficient**

If every adjacent code-point difference inside a substring is one, repeated addition shows its letters are `c, c+1, c+2, ...` and hence it appears contiguously in the alphabet string. Conversely, any substring of the alphabet has exactly those adjacent differences. The local comparison therefore captures the full global definition; no separate search inside `"abcdefghijklmnopqrstuvwxyz"` is required.

## Complexity detail

Let $n$ be the string length. The lazy map and `pairwise` iterator process $n-1$ adjacent pairs. Each performs constant-time arithmetic and assignments, giving $O(n)$ time.

Only two counters and iterator state are kept. Auxiliary space is $O(1)$.

No substring objects are created, so memory does not grow with the longest run.

## Alternatives and edge cases

- **Compare characters directly:** Test `ord(y) == ord(x) + 1` without mapping the entire iterator. It has the same complexity.
- **Split at failures:** Record maximal runs and take their lengths. This is equivalent but needs more bookkeeping.
- **Enumerate substrings:** Testing every substring takes quadratic or worse time.
- **One character:** Initialization returns one.
- **Entire string continuous:** The answer is `len(s)`.
- **Repeated character:** Difference zero breaks the run.
- **Skipped alphabet letter:** Difference greater than one breaks the run.
- **Decreasing pair:** Negative difference breaks the run.
- **`"za"`:** There is no wraparound, so it forms only singleton runs.
- **Substring requirement:** Characters cannot be skipped to repair a broken adjacency.
