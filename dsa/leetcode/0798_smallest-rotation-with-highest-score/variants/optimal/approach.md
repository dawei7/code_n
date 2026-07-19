## General
**Track how one element changes score**

After a left rotation by `k`, the element originally at index `i` occupies $(i - k) \bmod n$. When `k` increases by one, that position normally decreases by one. The element stops scoring exactly when its old position equals `nums[i]`, so the transition into rotation `(i - nums[i] + 1) % n` contributes a loss of one.

The same element eventually moves from position `0` to $n - 1$. That wrap happens when entering rotation $(i + 1) \bmod n$ and contributes a gain of one. If the value is zero, the loss and gain occur together and cancel, correctly reflecting that zero always scores.

**Accumulate all rotation events**

First compute the score at rotation `0`. Store every loss and gain in a difference array indexed by the rotation being entered. Scanning rotations `1` through $n - 1$, add the event total for that rotation to the running score. Update the answer only for a strict improvement, which preserves the earliest rotation when several scores tie.

Each element's score can change only at the two recorded boundaries. Therefore, summing all events reproduces its contribution at every rotation; summing across elements reproduces every complete rotation score. Comparing those exact scores and retaining the first maximum returns precisely the required smallest `k`.

## Complexity detail
Computing the initial score, recording two events per element, and scanning the rotations each take $O(n)$ time. The event array uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Bad-interval difference array:** Mark the cyclic range of rotations where each element fails to score, then prefix-sum those ranges; this is another linear formulation of the same boundary events.
- **Construct every rotation:** Materializing or indexing each of the `n` rotations and rescoring all `n` positions takes $O(n^2)$ time.
- **Balanced event structure:** Sorting score-change events can avoid a length-`n` array, but event indices are already bounded integers, so it adds unnecessary logarithmic work.
- **Tied best scores:** Update only when the score is strictly larger so the first, smallest rotation survives.
- **Zero values:** A zero scores at every index; its loss and gain events cancel at the same rotation.
- **Value $n - 1$:** It scores only while occupying the final position.
- **Single element:** Its value must be zero, and rotation `0` is the only candidate.
