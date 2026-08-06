## Function Contract

**Inputs**

- `s`: The non-empty string whose contiguous substrings are counted.

Let $n = \lvert s\rvert$. Each candidate substring is identified by an interval with start and end positions inside `s`; the interval qualifies only when its set of characters has size one.

**Return value**

- Return the integer number of qualifying non-empty intervals. Occurrences at different positions count separately even when their substring text is identical.
