## General

**Track both possible final directions**

A turbulent subarray alternates less-than and greater-than. Whether a previous run can extend depends only on its last comparison.

The solution keeps:

- `f`: longest turbulent subarray ending at the previous element with last comparison less-than;
- `g`: analogous length with last comparison greater-than.

Both begin at one because a single element is turbulent.

**Increasing pair**

For adjacent `a < b`, the new comparison is less-than. It can extend a run that previously ended greater-than:

`ff = g + 1`.

A greater-ending run cannot use this pair, so `gg = 1`.

**Decreasing pair**

For `a > b`, the new greater-than comparison extends a less-than run:

`gg = f + 1`.

The less-than state resets to one.

**Equality**

For `a == b`, neither strict comparison holds. No turbulent run of length at least two crosses this pair.

Both states reset to one, representing a fresh start at `b`.

**Why simultaneous update matters**

`ff` and `gg` are computed from old `f` and `g`, then assigned together.

Overwriting `f` before calculating `g` could use a state from the current pair rather than the previous pair and mix comparison steps.

**Trace**

For `[4, 2, 10, 7, 8]`:

- Four greater than two creates greater-ending length two.
- Two less than ten extends to less-ending length three.
- Ten greater than seven extends to greater-ending length four.
- Seven less than eight extends to less-ending length five.

The signs alternate, so answer is five.

In `[4, 8, 12, 16]`, every pair increases. Each less state can extend only an old greater state that has reset to one, so maximum stays two.

**Meaning of `ans`**

`ans` stores the best length anywhere, not just at current endpoint.

After each pair it takes maximum of itself, `f`, and `g`. Later equality may shorten current runs without erasing an earlier best.

**Why two scalars are sufficient**

The future does not need start index or complete sign history. Only current length and final direction determine whether the next sign alternates.

This is a dynamic program compressed from arrays to rolling constant state.


Assume `f` and `g` correctly describe best runs ending at `a`.

For `a < b`, every extendable run must end greater-than, so `g + 1` is exact. No greater-ending run crosses that pair. The decreasing case is symmetric, and equality resets both.

Induction proves states at every endpoint. Their global maximum is the longest turbulent subarray.

**Subarray contiguity**

Updates use only consecutive values from `pairwise(arr)`. A reset starts at the current element, so no state skips an index.

The method counts contiguous subarrays, not subsequences.

**Why length one is always represented**

Even after a comparison fails a particular direction, assigning one keeps the current element as a valid singleton. The next opposite comparison may extend it to length two.

Without this reset baseline, future runs after equality or repeated signs could be lost.

**State interpretation after a reset**

When `f = 1`, it does not claim the latest comparison was less-than. It says the best run in that directional category has fallen back to the singleton ending here.

On the next greater-than pair, `g` can use `f + 1 = 2` to form a fresh valid pair. This convention lets both directions share one simple recurrence without zero-length special cases.

**Why absolute index parity is irrelevant**

The formal definition mentions even and odd indices, but it permits either alternating orientation. A subarray can begin at any index.

Tracking comparison direction relative to the previous step captures both allowed patterns. The algorithm does not need to know whether the original array index is even or odd.

**Maximum update after every pair**

A longest run may end anywhere. Recording only the final `f` or `g` after the loop would lose a long run followed by equality or repeated direction.

Updating `ans` online makes the maximum independent of how the array ends.

**Pairwise iterator behavior**

`pairwise(arr)` yields `(arr[0], arr[1])`, then `(arr[1], arr[2])`, and so on. Consecutive pairs overlap at one element, exactly matching how adjacent comparison signs form a turbulent run.

No auxiliary list of pairs is built.

Initialization with `ans = f = g = 1` handles the smallest legal array without a special branch. If the array has one element, `pairwise` yields nothing, the loop does not execute, and the answer correctly remains one. For a longer array, the same initialization gives the first comparison a singleton run that it can extend to length two.

## Complexity detail

Let `N` be array length.

`pairwise` yields `N - 1` pairs, each constant work. Time is `O(N)`.

Only a few integer variables are stored, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Sliding window:** Track last sign and move a left boundary on repeated signs or equality.
- **DP arrays:** Correct but rolling scalars suffice.
- **Check every subarray:** Quadratic or cubic.
- **Single element:** Initial answer one.
- **All equal:** Result one.
- **Strictly monotone:** Maximum two.
- **Perfect alternation:** Whole array qualifies.
- **Equality:** Splits a run completely.
- **Repeated sign:** Starts a new length-two run from latest pair.
- **Large values:** Only comparisons matter.
