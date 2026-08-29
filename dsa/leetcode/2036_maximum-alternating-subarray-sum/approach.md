## General

**A subarray needs two ending states**

Every alternating subarray begins with a positive contribution, then uses a negative contribution, then positive again, and so on. When a subarray ends at the current element, that element can therefore occupy one of two roles:

- `f` is the greatest alternating sum of a nonempty subarray ending at the current index with the current value added;
- `g` is the greatest alternating sum of a nonempty subarray ending at the current index with the current value subtracted.

The source updates both states for each value `x`. Keeping only one best ending sum would lose the sign phase needed to decide how the next value may extend it.

**Derive the positive-ending transition**

If current `x` receives a positive sign, there are two possibilities.

First, start a new length-one subarray at `x`. Its alternating sum is simply `x`.

Second, extend a subarray whose previous final element had a negative sign. Such a subarray has value `g`, and adding `x` produces `g + x`.

The better choice is

`max(x, g + x)`,

which the source writes as

`max(g, 0) + x`.

Using zero in this maximum does not represent an empty answer returned to the caller. It is only the option to discard an unhelpful previous state and begin the required nonempty subarray with the current value.

**Derive the negative-ending transition**

If current `x` receives a negative sign, it cannot start a new subarray: the first element of every alternating subarray must be positive. It must extend a subarray whose current end has a positive sign.

The only valid transition is therefore

`new_g = old_f - x`.

There is no `max(0, ...)` in this transition because a length-one subarray `-x` would violate the definition.

**Why simultaneous assignment matters**

The line

`f, g = max(g, 0) + x, f - x`

uses Python's simultaneous assignment semantics. Both right-hand expressions read the old `f` and old `g` before either variable is replaced.

This is essential. `new_g` must extend the previous index's positive-ending state, not the `new_f` that already includes the current value. Using an ordinary sequential update without a temporary would incorrectly use `x` twice in the same subarray.

**Initialization with negative infinity**

Before any element is read, no nonempty subarray exists, so both states begin at negative infinity. On the first element, `new_f = max(-inf, 0) + x = x`, correctly creating the one-element subarray. `new_g` remains negative infinity because no valid subarray can begin with a negative phase.

Initializing the answer to negative infinity is equally important. Input values may all be negative, and the answer still must be some nonempty subarray. Starting `ans` at zero would incorrectly allow an empty subarray with sum zero.

**Record endings of either parity**

After updating the states, `ans = max(ans, f, g)` considers the best subarray ending at the current position in either phase.

Odd-length alternating subarrays end with a positive term and appear in `f`. Even-length ones end with a negative term and appear in `g`. The global optimum may have either length parity, so both states must be compared.

**Trace the first example**

For `nums = [3,-1,1,2]`:

- At three, `f=3` and `g` is unavailable. The best is three.
- At negative one, starting over gives negative one, while no prior `g` helps, so `f=-1`. Extending the prior `f=3` gives `g=3-(-1)=4`, representing `[3,-1]`.
- At one, extending `g=4` gives `f=5`, representing `3-(-1)+1`. The negative-ending state becomes `-1-1=-2`.
- At two, the states do not exceed five.

The recorded maximum is five.

**Why each state is correct**

Assume the two old states correctly describe all subarrays ending at the previous index. Any positive-ending subarray at the current index is either the single current element or an extension of a negative-ending previous subarray. The `f` transition takes the best of exactly those exhaustive cases.

Any negative-ending current subarray must extend a positive-ending previous subarray, and the `g` transition uses the best such state. No other contiguous construction is possible because extending must use the immediately preceding index.

By induction, the states are correct at every index. Every nonempty subarray ends somewhere and in one of the two phases, so comparing both states into `ans` finds the maximum over all subarrays.

**Why this resembles Kadane's algorithm**

Ordinary maximum-subarray Kadane tracks one best sum ending at each position and decides whether to extend or restart. Here the alternating sign creates two phases, so the same local-optimum idea becomes a two-state dynamic program.

No prefix array is needed because each new state depends only on the previous two states.

## Complexity detail

Let $N$ be the length of `nums`. The loop visits each element once and performs constant-time arithmetic and comparisons, for $O(N)$ time.

Only `f`, `g`, `ans`, and the current value are stored. The dynamic-programming history is compressed to the immediately preceding states, so auxiliary space is $O(1)$. The input list is not modified.

## Alternatives and edge cases

- **Quadratic enumeration:** Start at every index and extend every subarray while updating its alternating sum; correct but $O(N^2)$.
- **Alternating prefix sums:** Transform subarray queries by index parity, then track suitable minima; it can be linear but is less direct than the two ending states.
- **Ordinary Kadane state only:** Incorrect because it forgets whether the next element must be added or subtracted.
- **Single element:** It enters `f` and is returned, even when negative.
- **All negative values:** Negative terms in subtracted positions can make a longer alternating subarray beneficial.
- **All equal positive values:** Odd-length runs tie the one-element value, while even-length sums may be zero.
- **Optimal even length:** `ans` must inspect `g` as well as `f`.
- **Restart at current element:** `max(g, 0)` implements that option only for the positive phase.
- **No empty subarray:** Negative-infinity initialization prevents zero from becoming an artificial answer.
- **Large sums:** Python integers safely hold cumulative values beyond individual input bounds.
- **Simultaneous assignment:** Both transitions must read the previous states.
- **Input preservation:** The source scans `nums` without sorting or editing it.
