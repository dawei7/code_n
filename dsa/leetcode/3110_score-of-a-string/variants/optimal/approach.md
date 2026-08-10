## General

**The score is a sum over adjacent edges of the string.** For a string of length $n$, the relevant pairs are positions $(0,1),(1,2),\ldots,(n-2,n-1)$. There are exactly $n-1$ pairs. Each pair contributes the absolute difference between the numeric character codes of its two letters.

The exact source expresses the complete computation in one return statement:

`sum(abs(a - b) for a, b in pairwise(map(ord, s)))`.

Reading it from the inside outward reveals a three-stage lazy pipeline.

**Convert characters to numeric codes.** `map(ord, s)` applies Python's `ord` function to each one-character string. For lowercase English letters these Unicode code points equal their familiar ASCII values: `ord("a") = 97` through `ord("z") = 122`.

The problem specifically speaks of ASCII, and the lowercase input guarantee makes Unicode code points identical for the needed characters. No lookup table or manual alphabet index is required.

`map` is lazy. It does not allocate a list of all codes; it produces each integer as the next stage requests it.

**Generate overlapping adjacent pairs.** `pairwise(...)` consumes the code iterator and yields consecutive pairs. If the codes are `[104,101,108,108,111]` for `"hello"`, it produces:

- `(104,101)`;
- `(101,108)`;
- `(108,108)`;
- `(108,111)`.

The overlap is essential: the second code of one pair becomes the first code of the next. `itertools.pairwise` maintains only enough iterator state to do this and does not materialize all pairs.

**Make each difference direction-independent.** For pair `(a,b)`, `a - b` may be positive, negative, or zero. `abs(a - b)` gives the nonnegative distance required by the definition. It does not matter whether the string rises or falls in alphabet order.

**Sum every contribution.** The generator expression supplies one absolute difference at a time to `sum`. `sum` begins from zero and accumulates them. Every required adjacency appears once, so the returned total exactly equals the score.

**A trace for `"hello"`.** Character codes are 104, 101, 108, 108, and 111. The pair contributions are:

$$
\lvert104-101\rvert=3,
\quad
\lvert101-108\rvert=7,
\quad
\lvert108-108\rvert=0,
\quad
\lvert108-111\rvert=3.
$$

Their sum is 13.

For `"zaz"`, the first pair falls by 25 and the second rises by 25. Absolute value makes both contribute 25, yielding 50.

**A direct correctness argument.** Index the output of `map(ord,s)` as $v_0,\ldots,v_{n-1}$. By the contract, the score is:

$$
\sum_{i=0}^{n-2}\lvert v_i-v_{i+1}\rvert.
$$

`pairwise` yields exactly $(v_i,v_{i+1})$ for those indices and no other pairs. The generator maps each to the matching absolute difference, and `sum` adds them. The source is therefore a direct executable form of the mathematical definition.

**Why no special handling is needed for equal characters.** When adjacent codes match, subtraction gives zero and absolute value preserves zero. Repeated letters contribute nothing automatically.

**Why no final pair goes out of bounds.** `pairwise` stops when its input iterator has no next element. It never asks the source code to index `s[i+1]` manually, so the last character participates only as the second member of the final valid pair.

**The result's maximum size.** Adjacent lowercase letters differ by at most 25. With $n-1$ pairs, the score is at most $25(n-1)$. Under $n\le100$, this is only 2475. Python integer size is not a concern.

## Complexity detail

Each of the $n$ characters is converted once, and each of the $n-1$ adjacent pairs is processed once. Every conversion, subtraction, absolute value, and addition is constant time for this character range. Total time is $O(n)$.

`map`, `pairwise`, and the generator expression are all lazy. They retain only constant iterator state and the running sum, so auxiliary space is $O(1)$. The source does not create a code list or a difference list.

The manifest's $O(n)$ time and $O(1)$ space match the exact implementation.

## Alternatives and edge cases

- **Index loop:** Iterate `i` from zero through `len(s)-2` and add `abs(ord(s[i]) - ord(s[i+1]))`. It is equally correct and may be easier for beginners to debug.
- **List of codes:** Precompute `[ord(c) for c in s]`, but that uses $O(n)$ extra space without improving time.
- **Alphabet positions:** Subtracting `ord("a")` from both characters gives the same differences because the common offset cancels.
- **Minimum length two:** The contract guarantees at least one adjacent pair.
- **Equal adjacent letters:** Contribution is zero.
- **Increasing pair:** Absolute value returns the positive upward gap.
- **Decreasing pair:** Absolute value removes the negative sign.
- **Alternating extremes:** A string such as `"azaz"` gives the largest contribution 25 at every boundary.
- **ASCII versus Unicode:** For lowercase English letters, `ord` returns the ASCII values required by the task.
- **No input mutation:** Iterators only read `s`.
- **Lazy map:** Character codes are produced on demand, not stored.
- **Lazy pairwise:** Only two neighboring codes need to be retained.
- **Empty generator concern:** Not relevant because length is at least two; even for a shorter input, `sum` would safely return zero.
- **Numeric result:** The method returns an integer, not the transformed characters or individual differences.
- **Every pair exactly once:** Overlapping adjacency is intentional and does not double-count an index pair.
