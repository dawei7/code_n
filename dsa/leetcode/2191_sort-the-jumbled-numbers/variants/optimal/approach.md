## General

**Convert a number without changing the returned value**

Extract decimal digits from right to left. If the current original digit is
`d` at place value `place`, add `mapping[d] * place` to the mapped key. The
place values remain unchanged, so mapped leading zeros naturally disappear
from the resulting integer. Handle the original number `0` separately because
its representation contains one zero digit even though a digit-extraction
loop would not execute.

**Use mapped values only as stable sort keys**

Compute the mapped key when the sorter requests it, but keep the original
number as the array element. A stable sort orders keys non-decreasingly while
retaining input order among equal keys. Python's built-in sort is stable, so
equal mapped values need no explicit index tie-breaker.

The conversion visits every original digit and substitutes exactly the digit
specified by `mapping` at the same decimal position, giving the contract's
mapped numeric value. Sorting by those keys establishes the required
non-decreasing order. Stability supplies precisely the mandated ordering for
ties, while the values themselves remain untouched.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each legal number has at most nine decimal
digits, a fixed bound, so all mapped keys take $O(n)$ time to evaluate. Stable
comparison sorting takes $O(n\log n)$ time and $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Stable insertion sort:** Compare mapped keys while inserting each element.
  It is straightforward but takes $O(n^2)$ time on reverse-ordered input.
- **Decorate with original indices:** Sort triples containing the mapped key,
  input index, and original value. This makes stability explicit but uses
  unnecessary index storage when the language's sort is already stable.
- The integer `0` maps to `mapping[0]`, not to an empty digit sequence.
- Mapped leading zeros are discarded numerically; for example, `007` and `07`
  both have mapped value $7$.
- Equal mapped values preserve input order even when the original numbers
  differ.
- Duplicate original numbers remain separate array elements.
- The returned array contains original values, never their mapped keys.
