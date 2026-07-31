## General

**One total removes repeated suffix work**

Compute the sum $T$ of the complete array. While scanning possible split
indices from left to right, maintain the prefix sum $L$ through the current
index. The corresponding right sum is then `T - L`, so the split is valid
exactly when `L >= T - L`.

Stop before the final element. Including it in the left side would leave an
empty right side, which is not a legal split.

**Why every valid split is counted once**

Before testing index $i$, adding `nums[i]` makes $L$ equal to the sum of
indices $0$ through $i$. Since $T$ contains every element, subtracting $L$
leaves exactly the sum from $i+1$ through $n-1$. The comparison therefore
matches the definition at that index. The loop visits every legal split index
$0$ through $n-2$ once, incrementing only when its exact sums satisfy the
inequality, so the final counter is the requested number.

Negative values need no special case: both running sums and the comparison are
ordinary signed integer operations. Equality qualifies because the condition
is greater than or equal to, not strictly greater than.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Computing the total and scanning the
$n-1$ split positions each take $O(n)$ time. Only the total, prefix sum, and
counter are stored, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recompute both sides per split:** Summing the left and right portions from scratch is correct but takes $O(n^2)$ time.
- **Prefix-sum array:** It answers each split in constant time after preprocessing but uses $O(n)$ space when one running prefix is sufficient.
- **Two elements:** There is exactly one legal split position.
- **Equality:** Count a split whose left and right sums are equal.
- **Negative totals:** The same signed comparison applies; do not assume prefix sums increase.
- **All zeroes:** Every legal split has equal sums and qualifies.
- **Last index:** Never test it because the right part would be empty.
- **Large magnitudes:** The total may exceed a 32-bit signed integer in some languages, so use a sufficiently wide accumulator.
