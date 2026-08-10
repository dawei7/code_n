## General

**There are only two possible target parity patterns**

In a parity-alternating array, every adjacent parity differs. Once the desired parity at index zero is chosen, the parity of every later index is forced. The two possibilities are

$$
\text{even},\text{ odd},\text{ even},\ldots
$$

and

$$
\text{odd},\text{ even},\text{ odd},\ldots.
$$

The source represents these patterns with `k` equal to zero or one. For a value `x` at index `i`, the expression `(x - i) & 1` is constant across a correctly alternating pattern. Subtracting `i` flips the required parity at every step: pattern zero requires `x` and `i` to have the same parity, while pattern one requires opposite parity.

This formulation also works for negative integers in Python. Bitwise `& 1` returns zero for an even integer and one for an odd integer, including negative values.

**Minimum operations for one fixed pattern**

Adding one or subtracting one always flips an integer's parity. Therefore:

- an element that already has its pattern-required parity needs zero operations;
- a mismatching element needs at least one operation; and
- either `x+1` or `x-1` fixes it in exactly one operation.

Consequently, for a fixed pattern, the minimum operation count is simply the number of mismatching indices. The local variable `cnt` counts them.

The global objective is lexicographic: minimize operations first, then minimize range among results using exactly that many operations. Once a pattern's minimum is fixed, every matching element must remain unchanged and every mismatching element must be changed exactly once. Spending an operation on a matching element would make it wrong, and spending additional canceling operations would exceed the minimum count. Thus a mismatching `x` has exactly two relevant final choices, `x-1` and `x+1`.

**Only the extrema need explicit movement choices**

Let `mn` and `mx` be the minimum and maximum of the original array. The helper `f(k)` evaluates the smallest range achievable for pattern `k` without enumerating two choices for every mismatch.

If a mismatching value equals `mn`, moving it to `mn-1` can only push the lower boundary outward. Moving it to `mn+1` is never worse and is the source's choice. Similarly, if a mismatching value equals `mx`, moving it to `mx+1` can only expand the upper boundary, so the source moves it to `mx-1`.

A mismatching value strictly between `mn` and `mx` is treated differently: the source leaves its local proxy `x` unchanged while computing extrema. This does not claim that the final value remains `x`; that would have the wrong parity. It is a compact way to represent the fact that one of `x-1` or `x+1` can be chosen without extending the best boundary determined by the outer values.

For an interior integer,

$$
\texttt{mn}<x<\texttt{mx},
$$

both neighbors lie inside the original closed interval:

$$
\texttt{mn}\le x-1<x+1\le\texttt{mx}.
$$

If the attainable proxy interval has positive width and `x` lies at its lower boundary, choose `x+1`; if it lies at its upper boundary, choose `x-1`; if it lies strictly inside, either safe direction may work. The only exceptional geometry is when all proxy values collapse to one integer. A nontrivial alternating array must contain both parities, so its elements cannot all end at one identical value. The minimum attainable range is then one, which the source enforces with `max(1, b - a)`.

The original extrema also explain why an interior proxy cannot hide a better shrink. A surviving matched minimum is fixed at `mn`; otherwise every occurrence of that minimum can rise by only one, so the lower boundary cannot pass `mn+1`. The analogous upper boundary cannot pass `mx-1`. If an interior proxy becomes an endpoint of the computed interval, it is adjacent to one of those unavoidable inward-shifted boundaries, allowing a parity-correct neighbor choice without producing a range larger than the source reports.

**How the helper computes its pair**

The variables `a` and `b` begin at positive and negative infinity. As the helper scans:

- it increments `cnt` for each parity mismatch;
- it replaces a mismatching global minimum by `x+1`;
- otherwise, it replaces a mismatching global maximum by `x-1`;
- it leaves every matched or interior-proxy value as written; and
- it updates the smallest proxy `a` and largest proxy `b`.

It returns `[cnt, max(1, b - a)]`. The special single-element case is handled before either helper runs, returning `[0,0]`. A one-element array is already parity alternating and genuinely has range zero; the lower bound of one applies only when at least two adjacent values must have different parity.

**Choose between the patterns in the required priority order**

The method computes `f(0)` and `f(1)`, then returns Python's `min` of the two lists. List comparison is lexicographic: it first compares `cnt` and consults the range only when the counts tie. That exactly matches the problem's two-level objective.

For `nums=[0,2,-2]`, one pattern requires changing only the middle value. It may become one or three; choosing one yields `[0,1,-2]` with range three. The competing pattern changes the other positions and cannot beat the first operation count, so the answer is `[1,3]`.

For `nums=[-2,-3,1,4]`, evaluating both patterns reveals that the minimum mismatch count is two. Moving the mismatching original maximum inward rather than outward helps keep the final top boundary small, producing the optimal range six described by the example.

## Complexity detail

Let `N` be the array length. The source computes `min(nums)` and `max(nums)`, each in `O(N)` time, then scans the array once for each of the two patterns. A constant number of linear passes remains `O(N)` total time.

The helper stores only counters, extrema, the pattern bit, and the current value. It does not copy or modify `nums` and does not enumerate possible final arrays. Its auxiliary space is `O(1)`. The two-integer returned list is also constant size. These bounds match the manifest's `O(N)` time and `O(1)` space.

The magnitude of the integers does not affect the number of iterations. Under the usual fixed-width or unit-cost arithmetic model, parity tests and additions are constant time; the stated values and one-step adjustments remain safely within ordinary signed 64-bit range.

## Alternatives and edge cases

- **Enumerate all changed directions:** For a pattern with `m` mismatches, trying `x-1` and `x+1` independently takes `2^m` outcomes. The extrema argument reduces those choices to a linear scan.
- **Dynamic programming over minima and maxima:** A DP could track possible boundaries, but the one-step changes and global original extrema make that state unnecessary. Only outward versus inward movement at the boundaries matters.
- **Greedily minimize each final absolute value:** The objective is the collective range, not the magnitude of individual entries. Moving a negative value toward zero, for example, may be irrelevant or harmful compared with moving it toward the current interval.
- **Evaluate only one starting parity:** The lower-operation pattern depends on the input. Both even-first and odd-first targets must be evaluated, and a tie in operations must be broken by range.
- **Interior values left unchanged in the source:** They are proxies for extrema computation, not literal final assignments. Every mismatching interior value still receives exactly one `+1` or `-1` operation in an actual realizing array.
- **All values equal:** For length greater than one, alternating parity requires changing some positions once. The final range can be one, and `max(1, b-a)` prevents the proxy calculation from incorrectly returning zero.
- **Length one:** It needs no operations and has range zero. The early return is necessary because applying the nontrivial lower bound of one would be wrong.
- **Negative odd numbers:** Python's `& 1` parity check remains correct. Replacing it with language-dependent negative remainder logic should be done carefully in other languages.
- **Duplicate global minima or maxima:** Every mismatching occurrence is moved inward; any matching occurrence remains fixed and continues to anchor that boundary. The per-element scan handles the mixture correctly.
- **Already alternating input:** One of the two patterns has zero mismatches. Because zero operations is globally minimum, the original array cannot be changed merely to improve its range; the source returns that pattern's original range.
- **Exactly optimal operation count:** Additional pairs of operations could preserve parity while changing values farther, but they are forbidden by the secondary objective's domain. Only arrays using exactly the minimum count are considered.
- **Lexicographic list comparison:** Python's `min(f(0), f(1))` is intentional. Comparing only the first entries would lose the required minimum-range tie-break.
