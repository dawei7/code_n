## General

**Count starts that happened, then subtract blooms that ended**

A flower with interval `[start,end]` is blooming at time `p` exactly when

`start <= p <= end`.

The number active at `p` can be computed as:

$$
(\text{flowers with start} \le p)
-
(\text{flowers with end} < p).
$$

Every flower falls into one of these categories after it has started: still active because its end is at least `p`, or already finished because its end is below `p`. Separating start and end times makes both counts available with binary search.

**Sort the two endpoint collections independently**

The exact solution constructs

`start = sorted(a for a, _ in flowers)`

and

`end = sorted(b for _, b in flowers)`.

Pairing a particular start with its corresponding end is unnecessary for aggregate counting. Both lists have one entry per flower.

**Count starts inclusively**

`bisect_right(start, p)` returns the insertion position after all entries equal to `p`. Because the list is sorted, that index equals the number of start times less than or equal to `p`.

A flower beginning exactly when a person arrives is already in full bloom under the inclusive interval and must be included. This is why right insertion is used.

**Count ends strictly before arrival**

`bisect_left(end, p)` returns the first index where `p` could be inserted, before entries equal to `p`. That index equals the number of end times strictly less than `p`.

A flower ending exactly at arrival time is still blooming and must not be subtracted. Using left insertion preserves it.

Subtracting these indices produces the active count:

`bisect_right(start, p) - bisect_left(end, p)`.

**Why subtraction matches each flower exactly**

Any flower counted among starts has begun by `p`. If it ended before `p`, it also appears in the subtracted end count and its net contribution is zero. If its end is `p` or later, it is not subtracted and contributes one.

A flower not yet started appears in neither the inclusive-start count nor necessarily the finished count; interval validity `start <= end` ensures it cannot have ended before it starts. Its net contribution is zero.

Thus, each flower contributes one exactly when its interval contains `p`.

**Preserve people order and duplicates**

The list comprehension evaluates people in their original order. Each result is placed at the matching output index.

If several people arrive at the same time, the same two binary searches produce the same count for each occurrence. Duplicates are retained because output is per person, not per distinct arrival time.

**Trace inclusive boundaries**

For a flower `[3,7]`:

- at time two, its start is not counted;
- at time three, its start is counted and its end is not subtracted;
- at time seven, it remains counted because `bisect_left(end, 7)` does not include end seven;
- at time eight, its end is below arrival and is subtracted.

This precisely implements the closed interval.

**Why endpoint pairing can be discarded**

It might seem dangerous to sort starts and ends independently, but only total counts are needed. The identity “started minus already ended” holds across the whole collection regardless of which end belongs to which start. Valid intervals prevent an end from preceding its own start, ensuring the difference never invents active flowers.

**Exact solution versus the editorial's end-plus-one variant**

One common method stores `end + 1` and uses `bisect_right` for both lists. This exact solution stores raw end times and uses `bisect_left` on them instead. The two formulations are equivalent for integer arrival times, but the boundary searches must match the chosen representation.

The input `flowers` and `people` are not modified; `sorted` creates new endpoint lists.

## Complexity detail

Let `F = len(flowers)` and `P = len(people)`. Building endpoint arrays is `O(F)`, and sorting both costs `O(F \log F)`.

Each person performs two `O(\log F)` binary searches, for `O(P \log F)` query time. Total time is `O((F + P)\log F)`.

The two endpoint arrays contain `2F` integers, using `O(F)` auxiliary space. The returned list uses `O(P)` output space.

## Alternatives and edge cases

- **Heap sweep over sorted people:** Process arrivals chronologically while adding started flowers and removing expired ends. It is also efficient but needs restoring original person order.
- **Difference map and prefix sweep:** Record `+1` at starts and `-1` at `end+1`, sort event times, then binary-search arrivals. This is valid but uses more event bookkeeping.
- **Check every flower per person:** It takes `O(FP)` time.
- **Use `bisect_left` for starts:** It would exclude flowers beginning exactly at arrival.
- **Use `bisect_right` for raw ends:** It would subtract flowers ending exactly at arrival too early.
- **Start equals end:** The flower blooms for that exact time and both boundary choices include it.
- **Person before all starts:** Both relevant counts are zero, producing zero.
- **Person after all ends:** All starts and ends are counted, so the difference is zero.
- **Overlapping intervals:** Each active flower contributes independently to the difference.
- **Repeated arrival times:** Each person gets an output entry with the same correct count.
- **Unsorted people:** Processing order does not matter because each query is independent.
- **Large time values:** Binary search depends on ordering, not the magnitude of timestamps.
- **Input preservation:** New sorted lists are built rather than sorting `flowers` or `people` in place.
