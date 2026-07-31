## General

Negative positions are fixed barriers, but they do not split the rotation into separate groups. Read every value at least zero from left to right into one sequence. Those are exactly the values allowed to move, and their extraction order is the order that must be rotated.

If this sequence is empty, return the unchanged array. Otherwise reduce `k` modulo the number of movable values. A left rotation by the resulting shift is `values[shift:] + values[:shift]`; this performs all full cycles at once instead of simulating them.

Copy `nums`, then scan its original positions. Whenever the original value is non-negative, write the next rotated value into that position. Skip negative positions, leaving their copied values untouched.

The extracted sequence contains every movable value exactly once in original order. A cyclic left shift therefore gives exactly the required new order. Reinsertion visits precisely the indices that were non-negative in the input, in increasing order, so it places the rotated sequence into the required slots. Every skipped index originally held a negative value and remains unchanged. The result consequently satisfies both the rotation rule and the fixed-position rule.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and let $M$ be the number of non-negative values. Extraction, rotation, and reinsertion take $O(N+M)=O(N)$ time. The extracted and rotated sequences plus the returned copy use $O(N)$ space.

The benchmark defines size as $N$, uses only non-negative values, and sets `k = N - 1`. The direct method reduces `k` once and performs linear slicing and reinsertion. A slower simulation that removes the first movable value and appends it once per requested rotation performs $N-1$ front removals on an $N$-element list, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Direct cyclic index mapping:** Store the movable positions and values, then write `values[(rank + shift) % M]` to the position of each rank; this is also $O(N)$ time and $O(N)$ space.
- **Simulate one rotation at a time:** Repeatedly moving the first extracted value to the end is correct, but front removal can make the method $O(kM)$ and therefore quadratic on legal inputs.
- **Rotate the entire array:** This incorrectly moves negative values and changes their indices.
- **Rotate each positive block separately:** Negative positions are skipped during reinsertion; they do not divide the non-negative values into independent rotations.
- **Zero values:** Zero is non-negative and must be extracted, rotated, and reinserted with positive values.
- **No non-negative values:** There is no sequence to rotate, so return the array unchanged without taking a modulus by zero.
- **One non-negative value:** Every rotation maps the sole movable value back to its original position.
- **`k = 0` or complete cycles:** A zero shift, or a `k` divisible by $M$, preserves the movable order.
- **Oversized `k`:** Reduce it modulo $M$; explicitly simulating all requested rotations is unnecessary.
- **Repeated values:** Equal movable values remain separate occurrences and participate in the same cyclic order.
