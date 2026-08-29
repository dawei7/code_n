## General

Working forward from all ones creates many choices. Working backward is much more constrained: in any forward operation with at least two elements, the newly written sum is strictly larger than every unchanged positive element. Therefore, the largest current target value must be the value written by the most recent operation.

The solution repeatedly reverses that forced last operation, using a max-heap to find the current largest value efficiently.

**Recover the previous value**

Let `mx` be the largest current value, let `s` be the total array sum, and let `t = s - mx` be the sum of all other values. Immediately before the last forward operation, the changed position held some positive value `prev`. The forward operation replaced it with the then-total sum:

$$
mx = prev + t.
$$

One reverse step would give `prev = mx - t`. The other values stay unchanged.

If `t == 0`, the array has one element and its value exceeds one, so it can never have changed from the starting one. If `mx - t < 1`, even one reverse subtraction would produce a nonpositive value. Both cases are impossible, and the method returns false.

**Undo many identical subtractions with a modulus**

When `mx` is much larger than `t`, it may remain the largest after one reverse step. Repeated reverse steps subtract the same unchanged sum `t`:

$$
mx,\ mx-t,\ mx-2t,\ldots
$$

Computing `mx % t` jumps over all those repeated steps at once. The source uses `x = (mx % t) or t`. A nonzero remainder is the last positive value after bulk subtraction. When the remainder is zero, `t` is used instead of zero so the reverse state remains positive. If that state is not actually viable, a later comparison where the maximum is no greater than the rest rejects it. When `t == 1`, choosing one is exactly the reachable end of repeatedly subtracting one.

For example, if `mx = 43` and the other values sum to twenty-one, one reverse step produces twenty-two. Here the modulus is one because two subtractions would pass below positivity, and bulk reversal eventually reconstructs the forced chain.

**Maintain a max-heap with negative values**

Python’s heap is a min-heap, so `pq = [-x for x in target]` stores negated values. The smallest negative value corresponds to the largest original value. `heapify` builds the heap, and `-pq[0]` reads the maximum.

Each iteration pops that maximum, computes the earlier positive value `x`, pushes `-x`, and updates the total with `s = s - mx + x`. Updating the sum algebraically avoids rescanning the heap.

The loop continues while the largest value exceeds one. All values are positive. Therefore, once the maximum is one, every value must be one, exactly the starting array, and the method returns true.

**Why the reverse path decides reachability**

For any reachable non-all-one state, the most recent forward result is necessarily a maximum, and reversing it uses the sum of all unchanged entries. Equal maxima that cannot correspond to a valid last operation are caught by the positivity check. The algorithm performs the only possible reverse reductions, accelerated without changing their positive endpoint.

If it reaches all ones, reversing those recovered steps constructs the target forward. If it encounters an impossible rest or nonpositive predecessor, no alternative last operation could succeed. The returned Boolean is therefore exact.

## Complexity detail

Let $n$ be the array length and $M$ its initial maximum value.

Summing, negating, and heapifying take $O(n)$ time. The modulus reduction shrinks a dominant maximum by a constant-factor effect across successful iterations, leading to $O(\log M)$ heap replacements in the standard analysis. Each pop and push costs $O(\log n)$, so the refined total is

$$
O(n+\log M\log n).
$$

The manifest’s $O(n\log n\log M)$ is a looser upper bound. The heap list stores $n$ integers, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Forward search:** It branches over the replaced index at every step and is infeasible for large targets.
- **Single subtraction per reverse step:** Correct in principle but pseudo-polynomial; an input such as one and one billion would require nearly one billion iterations.
- **Sorted list instead of heap:** Repeatedly finding and replacing the maximum costs more than logarithmic time per step unless a suitable ordered structure is used.
- **Single-element target:** Only `[1]` is reachable. A larger value gives `t == 0` and returns false.
- **All ones:** The maximum is already one, so the loop is skipped and true is returned.
- **Rest sum one:** Repeated subtraction can always reduce the maximum to one; the `or t` expression handles the zero remainder correctly.
- **Maximum not larger than the rest:** The previous value would be nonpositive, so the target is impossible.
- **Positive-value invariant:** Every forward sum and every unchanged entry is positive; a reverse value below one is decisive failure.
- **Input preservation:** The method builds a separate negated heap and does not reorder or modify `target`.
- **Tied maxima:** A valid nonterminal forward state cannot have an unchanged maximum large enough to make the forced predecessor nonpositive; the validation detects such impossible ties.
