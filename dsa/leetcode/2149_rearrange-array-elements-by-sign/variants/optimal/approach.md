## General

**Assign one destination stream to each sign**

Because the output begins positive and signs alternate, every positive value
must occupy an even index and every negative value must occupy an odd index.
The equal sign counts guarantee that these two sets of positions have exactly
the needed capacity.

Allocate the result, keep `positive_index = 0` and `negative_index = 1`, and
scan `nums` from left to right. Write each positive value at the next positive
index and advance that index by two; do the analogous operation for each
negative value. The fixed parity positions establish the required sign
pattern. Since each sign's values are written in encounter order, both
sign-specific relative orders are preserved.

## Complexity detail

Let $n$ be the length of `nums`. The scan and all writes take $O(n)$ time. The
returned arrangement occupies $O(n)$ space; aside from that required output,
the algorithm uses $O(1)$ auxiliary state.

## Alternatives and edge cases

- **Separate sign lists then zip:** Collecting positives and negatives before
  interleaving is also $O(n)$ time, but uses two intermediate lists in addition
  to the result.
- **Repeated stable selection:** Finding the next positive and negative by
  rescanning the input preserves order but costs $O(n^2)$ time.
- **In-place swaps:** Moving values into alternating positions while preserving
  both relative orders requires rotations or shifts and can degrade to
  $O(n^2)$ time; in-place modification is not required.
- The minimum length is two, with one positive and one negative value.
- Zero never appears, so every value belongs unambiguously to one sign stream.
- Duplicate values are distinct occurrences and retain their encounter order.
