## General

**Make the only decision that can fix the current position**

Scan `nums` from left to right. Once the scan reaches index `i`, every earlier
position has already been made `1`. A future operation beginning after `i`
cannot affect `nums[i]`, so the effective value at `i` determines the choice:

- if it is `1`, do not flip at `i`, because that would make the position wrong;
- if it is `0`, a suffix flip beginning at `i` is forced, because no later
  operation can repair this position.

A suffix operation toggles every still-unprocessed bit. Its actual endpoints
do not need to be simulated: only whether the number of previous operations is
even or odd matters. Keep that parity in `flipped`. The current effective bit
is `num ^ flipped`; whenever it is zero, increment the answer and toggle
`flipped`.

**Why the count is minimum**

At each index, the algorithm makes the unique choice compatible with a final
value of `1`. Any successful sequence must flip at exactly the same indices:
skipping a forced flip leaves the current zero permanently unchanged, while an
unforced flip turns the current one into a permanent zero. Inductively, after
each decision the processed prefix is correct, and the algorithm performs no
operation that another valid solution could omit. Its operation count is
therefore minimum.

Every input is solvable because an operation may begin at the final index, so
even the last effective zero can always be flipped by itself.

## Complexity detail

Let $n$ be the length of `nums`. The scan examines each element once, so the
running time is $O(n)$. Only the operation count and one parity bit are stored,
giving $O(1)$ auxiliary space. The input array is not modified.

## Alternatives and edge cases

- **Count run boundaries:** The answer is one when the first bit is zero, plus
  the number of adjacent positions whose values differ. This is the same
  parity argument expressed through constant runs and also takes $O(n)$ time
  and $O(1)$ space.
- **Mutate every chosen suffix:** Explicitly flipping `nums[i:]` follows the
  same forced greedy choices and returns the correct count, but alternating
  inputs make it touch a quadratic number of elements.
- **Dynamic programming:** Storing a best result for every index and parity is
  possible, but each state has only one viable decision, so the table adds
  unnecessary space and bookkeeping.
- A one-element array needs zero operations for `[1]` and one for `[0]`.
- An all-ones array needs no operation, while any nonempty all-zero array needs
  exactly one operation beginning at index `0`.
- Alternating values force a parity change at every boundary; if the first bit
  is zero, an operation is forced at every index.
