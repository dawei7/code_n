## General

The desired final order has every `0` before every `1`. A pair of positions is out of order exactly when a `1` appears to the left of a `0`. Such a pair is an inversion.

An adjacent swap of `10` to `01` removes exactly one inversion. Therefore the minimum number of adjacent swaps equals the total number of black-before-white inversions.

The exact source counts these inversions from right to left.

**State maintained during the reverse scan**

`cnt` is the number of `1` characters already seen in the suffix, including the current position after it is incremented. `ans` accumulates how many zeros lie to the right of every encountered one.

At index $i$ containing `1`:

1. Increment `cnt`.
2. The suffix length including $i$ is `n - i`.
3. Of those suffix characters, `cnt` are ones.
4. Therefore `n - i - cnt` are zeros to the right.

The source adds this number to `ans`.

At an index containing `0`, it does nothing immediately. That zero will be counted later once for each one encountered to its left.

**A trace**

For `s = "100"`:

- At index $2$, the character is zero.
- At index $1$, it is also zero.
- At index $0$, `cnt` becomes one. The suffix has length three, so there are $3-1=2$ zeros to its right.

The answer is two, matching the two adjacent swaps needed to move the one past both zeros.

For `"101"`, the rightmost one contributes zero. The leftmost one sees a suffix of length three containing two ones, hence one zero. Total cost is one.

**Why inversion count is a lower bound**

Take any inverted pair consisting of a particular one before a particular zero. In the target arrangement, that zero must end before that one. With only adjacent swaps, their relative order can change only when those two balls cross, which costs one swap.

Each adjacent `10 -> 01` swap changes the relative order of exactly that pair and removes exactly one inversion. No single swap can eliminate two distinct inverted pairs. Hence at least the initial inversion count operations are necessary.

**Why the bound is achievable**

Repeatedly swap any adjacent `10` pair. Every swap reduces the inversion count by one and never creates a new black-before-white inversion elsewhere. When no inversion remains, all zeros precede all ones.

Starting from $I$ inversions, this process terminates after exactly $I$ swaps. The lower bound is achieved, proving the counted value is the minimum.

The algorithm counts without performing the swaps, avoiding repeated string mutation.

## Complexity detail

The reverse loop visits each of the $n$ characters once and does constant work, so time complexity is $O(n)$.

Only `n`, `ans`, `cnt`, and the loop index are stored. Auxiliary space is $O(1)$.

The maximum answer is quadratic in $n$—for all ones followed by all zeros—but Python integers safely hold it.

## Alternatives and edge cases

- **Forward inversion count:** Track ones seen so far and add that count at every zero. It is equivalent to the exact reverse formulation.
- **Track white destinations:** For each zero, add the distance from its current index to its next final white position. This also sums the same inversions.
- **Simulate adjacent swaps:** Correct but may take $O(n^2)$ time and mutable storage when the answer itself is large.
- **Already separated:** A string of zeros followed by ones has no inverted pair and returns zero.
- **All one color:** No opposite-color pair exists, so no swaps are needed.
- **Alternating colors:** Every zero contributes the number of earlier ones; the reverse formula counts the same pairs.
- **Why strict order matters:** A one before another one or a zero before another zero is not an inversion and never needs crossing.
- **Individual ball identities:** Balls of the same color are interchangeable, but counting cross-color pairs remains exact.
- **Large answer:** Use a wide integer type in fixed-width languages because the count can approach $n^2/4$.
- **No matrix or queue:** The final arrangement is implicit; only the minimum operation count is requested.
- **Why suffix zeros equal the formula:** Among the `n-i` positions from $i$ onward, every character is either zero or one. After incrementing `cnt` for the current one, subtracting it from suffix length leaves precisely the zeros.
- **Crossing direction:** To place whites left, each inverted one must move right past each later zero, or equivalently each zero moves left past earlier ones. Both views charge the same crossing once.
- **Stable order within a color:** Adjacent swaps need never exchange two equal-color balls. Their relative identities are irrelevant, and avoiding such swaps preserves the minimum.
- **Worst arrangement:** A prefix of $p$ ones followed by $q$ zeros contains $pq$ inversions. This demonstrates why simulation can be quadratic even though counting is linear.
- **Reverse-loop boundary:** Starting at `n - 1` and ending at zero ensures every later character has already been classified when a one's contribution is calculated.
