## General

**More than two copies make a split impossible.** Each output array must contain distinct values, so either part can receive at most one occurrence of a given value. Together, the two parts can hold at most two occurrences. If any frequency exceeds `2`, the pigeonhole principle forces a duplicate inside one part.

**The same condition is sufficient.** Give one copy of every twice-occurring value to each part. Suppose there are $d$ such values and $s$ values that occur once. The original length is $2d+s$, which is even, so $s$ is even. Divide the singleton values evenly: each part then contains $d+s/2=n/2$ distinct values. Therefore, no frequency exceeding `2` is the only obstruction.

**Count within the bounded domain.** Since every input value lies from `1` through `100`, use a fixed array indexed by value. Increment its entry while scanning `nums` and return `False` immediately when a count becomes `3`. If the scan finishes, the constructive argument guarantees a valid split.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm reads each element once, taking $O(n)$ time. The count array always has `101` entries because the value domain is fixed independently of $n$, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Hash table:** A frequency map gives the same $O(n)$ time but uses $O(k)$ space for $k$ distinct values instead of exploiting the fixed domain.
- **Sorting:** After $O(n\log n)$ sorting, three equal consecutive values prove impossibility. This changes the input order unless a copy is made and is asymptotically slower.
- **Explicit construction:** Building both output arrays can demonstrate one split, but the frequency condition already decides existence without storing the parts.
- **Two elements:** Any legal two-element input can be split into one element per part, even when the values are equal.
- **All values distinct:** Because $n$ is even, any $n/2$ values can be assigned to each part.
- **Every value appears twice:** Put one occurrence of every value into each part.
- **Exactly three copies:** The third copy makes the answer `False` immediately, regardless of all other values.
- **Equal-size requirement:** Once all duplicate pairs are divided, the number of singleton values is automatically even; no extra balancing condition is needed.
