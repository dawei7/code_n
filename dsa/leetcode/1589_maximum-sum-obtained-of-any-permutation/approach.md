## General

**Rewrite all requests as position frequencies**

The value placed at index `i` contributes to the total once for every request interval that covers `i`. If index `i` is covered `d[i]` times and the chosen permutation places value `v` there, that position contributes `v * d[i]`.

Therefore, the total over all requests can be rewritten as one dot product:

$$
\sum_{i=0}^{N-1}\text{value-at-position-}i\cdot\text{coverage}[i].
$$

The original request boundaries matter only for calculating coverage counts. After those counts are known, maximizing the total is an assignment problem: decide which number should receive which frequency.

**Difference-array range updates**

Incrementing every covered index separately would cost proportional to each request’s length. With up to $10^5$ requests of length up to $N$, that can be quadratic.

The solution uses `d` as a difference array. For inclusive request `[l, r]`, it performs:

- `d[l] += 1` to mark that coverage rises by one starting at `l`;
- if `r + 1 < n`, `d[r + 1] -= 1` to mark that the added coverage stops after `r`.

No subtraction sentinel is written when `r` is the last index because `d` has length exactly $N$. There is no following in-range position whose coverage must be reduced.

After all requests have deposited their boundary changes, the loop

`d[i] += d[i - 1]`

turns differences into prefix totals. At index `i`, the running sum contains one active increment for every request that started at or before `i` and has not ended before it. Thus `d[i]` becomes exactly the number of request intervals containing index `i`.

For requests `[[1,3],[0,1]]` over five positions, the final frequencies are `[1,2,1,1,0]`. Index one appears in both requests, indices zero, two, and three appear once, and index four appears in none.

**Why large values belong at high-frequency positions**

After coverage counts are available, only the multiset of counts matters because `nums` may be permuted arbitrarily. The code sorts `nums` and `d` in ascending order, then pairs equal indices through `zip(nums, d)`.

This places the smallest values at the smallest frequencies and largest values at the largest frequencies. The rearrangement inequality proves that this pairing maximizes the dot product.

A simple exchange argument makes the reason beginner-friendly. Suppose two values satisfy $a\le b$, while two assigned frequencies satisfy $x\le y$. Pairing in the same order produces $ax+by$. Crossing them produces $ay+bx$. Their difference is:

$$
(ax+by)-(ay+bx)=(b-a)(y-x)\ge 0.
$$

Therefore, assigning the larger value to the larger frequency is never worse. If any arrangement contains an inverted pair—a smaller value assigned to a higher frequency than a larger value—swapping them does not decrease the total. Repeating such swaps leads to the sorted-with-sorted pairing used by the solution, so that pairing is optimal.

**Why positions can be forgotten after counting**

The final permutation itself is not requested, only the maximum sum. Sorting the frequency array loses which original index owns each frequency, but that does not lose the maximum value: after computing an optimal pairing, values could be assigned back to any positions carrying the paired frequencies.

Equal frequencies are interchangeable because swapping values between them changes no contribution. Equal values are also interchangeable. The dot product is sufficient to calculate the best total without constructing the actual permuted array.

**Computing and reducing the answer**

The generator `a * b for a, b in zip(nums, d)` produces each paired contribution, and `sum` adds all $N$ products. `zip` has $N$ pairs because both lists have length $N$.

The modulo operation is applied after the complete mathematical sum:

`... % (10**9 + 7)`.

Python integers do not overflow, so delaying the modulus is safe. Applying the modulus to partial sums would yield the same final remainder, but is not necessary in this language.

The source sorts `nums` in place, so it changes the caller-provided order. It also sorts `d`, which is a local array. The problem asks only for the maximum value and does not require `nums` to remain unchanged.

**Why all requests are counted exactly**

For any fixed index, the prefix sum of the difference markers increases once at each covering request’s left boundary and decreases immediately after its right boundary. Hence its frequency equals its exact multiplicity across the request list.

Expanding the request total and regrouping terms by array position shows that the sum of `nums[i]` inside every interval is identical to multiplying the value at each position by that position’s coverage. The rearrangement argument then proves the sorted assignment maximizes this regrouped expression. The returned modular value is therefore the required maximum total.

## Complexity detail

Let $N$ be the length of `nums` and $R$ be the number of requests.

Each request performs at most two constant-time difference updates, costing $O(R)$. Prefix accumulation costs $O(N)$. Sorting `nums` and `d` costs $O(N\log N)$ each, and the final dot product costs $O(N)$. Total time is $O(R+N\log N)$.

The difference array uses $O(N)$ explicit auxiliary space. The source sorts `nums` in place rather than creating a copy. Under conventional algorithmic accounting, the stated auxiliary bound is $O(N)$ due to `d`. Python’s Timsort may additionally allocate temporary storage proportional to the lists being sorted, but this remains $O(N)$ and does not change the overall bound.

The generator used by `sum` is lazy and does not allocate a separate list of all products.

## Alternatives and edge cases

- **Apply every request directly:** Incrementing coverage throughout each interval can take $O(RN)$ time. Difference markers reduce each interval to constant work.
- **Sort requests or sweep endpoints as events:** This can also recover coverage frequencies, but a fixed-index difference array is simpler because the domain is exactly zero through $N-1$.
- **Assign values greedily without sorting frequencies:** Repeatedly selecting the current largest value and largest count can be correct with heaps, but sorting both arrays is simpler and has the same dominant asymptotic cost.
- **Keep original index identities:** One can sort pairs of `(frequency, index)` to construct an actual optimal permutation. The checked-in method needs only the maximum sum, so identities are unnecessary.
- **Index covered by no request:** Its frequency is zero, so pairing it with a small value preserves larger values for positive frequencies. Its product contributes zero.
- **All positions covered equally:** Every permutation has the same total because all frequency multipliers are equal. Sorting still returns that value.
- **Duplicate requests:** Each copy independently increments coverage, which is correct because every request contributes separately to the total.
- **Single-position request:** The start increment and following decrement make only that position’s frequency rise.
- **Request ending at `n - 1`:** The code omits the out-of-range decrement. Prefix coverage correctly remains active through the final position.
- **Zero values in `nums`:** They naturally pair with the smallest frequencies and contribute zero.
- **Duplicate numbers or counts:** Any order within ties is optimal; sorting need not preserve identity.
- **Modulo timing:** Python safely sums the full value before reducing. Fixed-width languages should reduce during accumulation or use a sufficiently wide type.
- **Input mutation:** `nums.sort()` changes the original list. Pass a copy if later code needs the source ordering.
- **Inclusive endpoints:** The decrement occurs at `r + 1`, not `r`, because position `r` is part of the request.
