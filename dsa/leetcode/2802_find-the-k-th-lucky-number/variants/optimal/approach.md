## General

**View the sequence as levels of a binary tree**

There are $2^m$ lucky numbers with exactly $m$ digits. All shorter lucky numbers are numerically smaller, and within a fixed length the numerical order is the same as lexicographic order because `4` precedes `7`.

This is the same breadth-first ordering as the nonempty binary strings when `0` is renamed `4` and `1` is renamed `7`. Binary strings normally lose leading zeroes when written as integers, so use `k + 1` to supply a permanent leading `1`. After removing that leading bit, the remaining bits identify the $k$-th node in the level-order sequence.

For example, `k = 4` gives `k + 1 = 5`, whose binary representation is `101`. Remove the first `1` to obtain `01`, then map `0` to `4` and `1` to `7`, producing `47`.

For every length $m$, the indices of $m$-digit lucky numbers are $2^m - 1$ through $2^{m+1} - 2$. Adding one makes their binary representations run from a leading `1` followed by $m$ zeroes through a leading `1` followed by $m$ ones. Removing the common leading bit therefore yields every $m$-bit pattern in order. The digit mapping preserves that order and is bijective, so the constructed string is exactly the lucky number at position `k`.

## Complexity detail

Let $m = \lfloor \log_2(k + 1) \rfloor$, the output length. Converting `k + 1` to binary and mapping its suffix each take $O(m) = O(\log k)$ time. The returned string and its construction require $O(m) = O(\log k)$ space.

Writing the answer itself requires $\Omega(m)$ time, so the accepted $O(m)$ construction is asymptotically optimal. The package uses an asymptotic-optimality certificate instead of attempting to distinguish logarithmic runtimes over the small legal output range.

## Alternatives and edge cases

- **Breadth-first generation with a queue:** Appending `4` and `7` produces the sequence correctly, but reaching position `k` takes $O(k)$ time and queue space.
- **Subtract complete length blocks:** Determine $m$ by repeatedly subtracting $2^m$, then convert the zero-based offset within that level; this is correct but more elaborate than the `k + 1` identity.
- **Recursive construction:** Following left and right child choices from the implicit binary tree works, but recursion adds unnecessary call overhead.
- `k = 1` gives binary `10`; dropping the leading bit and mapping `0` returns `"4"`.
- At $k = 2^{m+1} - 2$, the suffix is all ones and the answer is $m$ copies of `7`.
- At the following index $k = 2^{m+1} - 1$, the output length increases and the answer becomes $m+1$ copies of `4`.
- Return a string even though every lucky number is a valid decimal integer.
