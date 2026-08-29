## General

The task counts index triples, not merely distinct value triples. Two occurrences with the same value are different choices when their indices differ. The exact solution enforces the required order $i<j<k$ directly:

- choose middle index $j$ in the outer loop;
- enumerate every earlier index $i$ through `arr[:j]`;
- use a frequency Counter to count later indices $k$ having the needed third value.

**Maintain counts only to the right of `j`.** Initially `cnt` contains every array occurrence. At the start of the iteration for middle value `b = arr[j]`, the solution performs `cnt[b] -= 1`. Values from earlier outer iterations were already removed, so after this decrement `cnt[x]` equals the number of occurrences of value $x$ at indices strictly greater than $j$.

The Counter may retain zero-count keys, but looking them up still returns zero and does not affect correctness.

**Complete each earlier pair.** For every earlier value `a = arr[i]`, the required third value is forced:

$$
c=\text{target}-a-b.
$$

Every occurrence of $c$ after $j$ gives one valid choice of $k$. Therefore the code adds `cnt[c]`.

There is no need to loop over those later indices individually because their value and count are all that matters once $i$ and $j$ are fixed.

**Why every valid triple is counted once.** Take any valid indices $i<j<k$. When the outer loop reaches its unique middle index $j$, `arr[i]` appears once in the prefix iteration for that exact occurrence, and `cnt[arr[k]]` includes index $k$ because it lies to the right. The target equation makes `arr[k]` the requested $c$, so the triple contributes one.

It cannot be counted under a different middle iteration because its ordered middle index is unique. It cannot be counted twice within the same iteration because index $i$ appears once, and the Counter contributes each right-side occurrence once.

**Why equal values still work.** Suppose `a == b == c`. The prefix loop selects a concrete earlier index $i$, the outer loop fixes a concrete middle index $j$, and `cnt[c]` counts only later occurrences. This automatically produces the binomial number of ordered index triples without special equal-value formulas.

For four equal occurrences, the contributions across middle indices are the number of earlier choices times later choices. Summing gives $\binom{4}{3}=4$.

For `arr = [1,1,2,2,2,2]` and target 5, valid values are $(1,2,2)$. Each of the two 1-indices can be paired with each choice of two ordered 2-indices, yielding $2\binom{4}{2}=12$. The middle-index process produces exactly that total.

**The modulo can be applied incrementally.** Every addition is nonnegative, and modular addition preserves the final remainder. Reducing `ans` at each pair prevents it from growing unnecessarily large.

**State invariant.** Before the prefix loop for index $j$:

- `cnt` contains exactly the multiset of values at indices $j+1$ through $n-1$;
- every previously counted combination has a middle index less than $j$;
- `ans` is the number of valid triples for those processed middle indices, modulo the required number.

Removing current `b` establishes the right-side Counter, and enumerating all earlier occurrences counts precisely the triples whose middle is $j$. The invariant therefore advances to the next iteration.

The exact implementation uses `arr[:j]`, which constructs a new prefix list on every iteration. Iterating indices with `for i in range(j)` would avoid those temporary slices without changing the algorithm.

## Complexity detail

Let $n$ be the array length and $V$ the value-domain size.

- **Time complexity of the exact solution:** $O(n^2)$. There are $\sum_j j=O(n^2)$ earlier-index iterations; creating all `arr[:j]` slices also totals $O(n^2)$ copied elements.
- **Space complexity:** $O(V+n)$ at a moment under implementation-level accounting: the Counter stores value frequencies and the largest temporary slice may contain $O(n)$ elements.

The manifest's $O(n+V^2)$ time and $O(V)$ space describe the editorial's value-frequency case analysis, not this exact index-pair implementation.

## Alternatives and edge cases

- **Frequency-domain case analysis:** Loop over ordered values $a\le b\le c$ and use combinations for all-distinct, two-equal, and three-equal cases. With values 0 through 100, it reaches $O(n+V^2)$.
- **Sorted two pointers:** Sort the array and count multiplicities around matching pairs in $O(n^2)$ time, but sorting changes index order and requires careful combination counts.
- **Triple enumeration:** Directly checking all $i<j<k$ costs $O(n^3)$.
- **Index loops without slicing:** Replace `arr[:j]` with indexed access to preserve $O(n^2)$ time while reducing temporary space.
- **No matching third value:** Counter lookup contributes zero.
- **Third value outside 0 through 100:** Counter also returns zero without a range check.
- **All three values distinct:** Each concrete ordered index triple is counted once.
- **Exactly two values equal:** Concrete-index enumeration handles the multiplicity automatically.
- **All three values equal:** Earlier/middle/later roles produce the correct combination count.
- **Duplicate Counter keys with zero count:** They are harmless.
- **Index order:** Removing through the middle and reading only the prefix is what enforces $i<j<k$.
- **Large answer:** Incremental modulo returns the required residue.
- **Manifest mismatch:** Complexity must reflect the exact nested index enumeration rather than the alternative bounded-value method.
