## General

Each device starts with exactly `n` units, and its rating is the minimum value among the units currently assigned to it. An operation chooses a nonempty source device, removes exactly one unit from it, and adds that unit to a different device. A device may be used as a source at most once, while a receiver may accept multiple transferred units.

Because a minimum determines each rating, removing a large unit from a device cannot improve that device's rating. If a device is going to donate, the only useful candidate is one occurrence of its smallest value. Removing that occurrence exposes the device's second-smallest original value as the best rating it can possibly reach. Incoming units cannot raise a receiver's minimum; they can only preserve or lower it.

For device `i`, define:

- `a_i` as its smallest original unit value;
- `b_i` as its second-smallest original unit value, when `n \ge 2`.

Also define

$$
A=\min_i a_i
\qquad\text{and}\qquad
B=\min_i b_i.
$$

The Optimal construction for `n \ge 2` attains

$$
\sum_i b_i-B+A.
$$

The source calculates exactly this expression after sorting every device's row.

**Why the one-unit case is separate**

When `n=1`, each device contains only its current minimum. Donating that only unit empties the source, whose rating becomes zero. The receiver gains another unit, but its new minimum cannot exceed its old rating. Therefore an operation cannot compensate for the rating lost by the emptied source. Since operations are optional, performing no transfers is optimal.

The source returns

```python
sum(x[0] for x in units)
```

which is the original rating sum in this case.

**What one donation can do when there are at least two units**

For `n \ge 2`, a source remains nonempty after donating once. If it removes one occurrence of its minimum `a_i`, its smallest remaining original unit is `b_i`. This is true even when the two smallest values are equal: then `a_i=b_i`, and removing one minimum correctly leaves another equal minimum.

No sequence of allowed operations can make device `i`'s final rating exceed `b_i`. The device can remove at most one of its own original units, so at least `n-1` original units remain. The smallest of those remaining originals is at most the original second-smallest value `b_i`. Receiving more units cannot increase a minimum.

Thus `\sum_i b_i` is a natural upper bound if every device could independently reach its second minimum. The transfers cannot quite realize all of those upper bounds at once, because every removed unit must be placed somewhere.

**Why one device must absorb the global minimum**

Consider the globally smallest original unit value `A`. There are two possibilities:

- its owner does not remove that occurrence, so the owner's final rating is at most `A`; or
- its owner removes it, in which case some other device receives it and that receiver's final rating is at most `A`.

Either way, at least one device, call it `j`, has final rating no greater than `A`. For all other devices, the general upper bound `b_i` still applies. Therefore

$$
\text{final sum}
\le
\sum_{i\ne j}b_i+A
=
\sum_i b_i-b_j+A.
$$

Since `b_j \ge B`, this is at most

$$
\sum_i b_i-B+A.
$$

This proves that no arrangement can exceed the expression computed by the source. It also explains why the globally smallest first minimum and the globally smallest second minimum are the only two cross-device values needed.

**A transfer plan that reaches the upper bound**

Choose as the receiver, or “sink,” a device `s` whose second-smallest value is `B`. Leave this device as the one whose second-minimum upper bound will be sacrificed. Every other device donates one occurrence of its own smallest unit to `s`.

After these transfers:

- each donor `i \ne s` has removed one minimum and receives nothing, so its rating is exactly `b_i`;
- the sink keeps all its original units and receives every donated minimum;
- the sink's final minimum is `A`.

The last statement remains true whether the global minimum originally belonged to the sink or to a donor. If it belonged to the sink, it was never removed. If it belonged to another device, it was donated into the sink. Therefore the achieved sum is

$$
\sum_{i\ne s}b_i+A
=
\sum_i b_i-B+A,
$$

exactly matching the upper bound.

The argument handles ties naturally. Any device with second minimum `B` can serve as the sink, and multiple copies of the global minimum do not change its final rating.

**How the stored implementation computes the formula**

For every row `x`, the source calls `x.sort()`. After sorting, `x[0]` is `a_i` and `x[1]` is `b_i`. It then:

- adds `x[1]` to `ans`, building `\sum_i b_i`;
- updates `mn2` with the smallest `x[1]`, building `B`;
- updates `mn` with the smallest `x[0]`, building `A`.

The final statement

```python
ans -= mn2 - mn
```

is algebraically `ans = \sum_i b_i-B+A`.

The code computes the maximum value only; it does not need to materialize the transfer sequence because the construction above proves that the value is attainable.

**The stored source does not currently run unaided**

The exact Optimal file annotates its parameter with `List[List[int]]` but does not import or define `List`. In an ordinary Python module, class definition therefore raises `NameError: name 'List' is not defined`.

If `List` is supplied externally, calling the method reaches `mn = mn2 = inf`. The name `inf` is also neither imported nor defined, causing another `NameError`. A conventional implementation would provide `List` from `typing` and `inf` from `math`, or use `float("inf")`.

These are genuine source defects, not algorithmic assumptions. Once those two names are available, the source computes the proven formula. This explanation records the code as it exists rather than silently treating the missing dependencies as present.

## Complexity detail

Let `m` be the number of devices, let `n` be the number of units in each device, and let

$$
U=mn
$$

be the total number of units.

For `n=1`, the generator expression reads one value from each device, so that branch takes `O(m)=O(U)` time and `O(1)` auxiliary space.

For `n \ge 2`, the exact source sorts each of the `m` rows. Sorting one row of length `n` takes `O(n\log n)` time, so all row sorts take

$$
O(mn\log n)=O(U\log n)
$$

time. The subsequent access to the first two elements and the minimum updates cost `O(1)` per row and do not change the bound.

This is a material mismatch with a linear-time claim one might infer from merely “finding two minima.” The stored source does not scan for two minima; it performs full sorts. Its actual time complexity is `O(U\log n)`.

Python's list sort operates in place and may use `O(n)` temporary auxiliary storage for a row in the worst case. Rows are sorted one at a time, so the peak sorting workspace is `O(n)` rather than `O(U)`. Apart from the sorting implementation's workspace, the method stores only scalar accumulators.

For `n \ge 2`, the calls to `x.sort()` sort every inner list in place. Thus the source mutates its input: after the call, each row is in nondecreasing order, which is observable unless that row was already sorted. This mutation does not affect the returned maximum.

As with the previous section, runtime bounds apply after the missing `List` and `inf` names have been supplied. As stored, name resolution prevents a normal completed execution.

## Alternatives and edge cases

- **Linear scan for the smallest two values:** Each row's first and second order statistics can be found in one pass without sorting. That would achieve `O(U)` time, `O(1)` explicit auxiliary space, and no input mutation. It is a stronger implementation choice, but it is not what the exact stored source does.

- **Simulating all transfers:** Trying source, destination, and moved-unit combinations obscures the minimum structure and grows combinatorially. The upper-bound-and-construction argument reduces the optimization to two order statistics per device plus two global minima.

- **Sending donations to several receivers:** Spreading small donated values risks lowering several device ratings. Concentrating all donated minima in the one deliberately sacrificed sink confines that damage to a single rating.

- **Choosing the device with the smallest first minimum as sink:** The sink should minimize the second-minimum value being forfeited, not necessarily its own first minimum. The global first minimum `A` reaches the sink regardless of where it began.

- **Donating a nonminimum unit:** Removing a value larger than the current minimum leaves the source rating unchanged, while the transferred unit cannot raise the receiver's minimum. Such a donation offers no advantage over omitting the operation.

- **Duplicate minimum values in a row:** If `a_i=b_i`, removing one minimum does not raise that donor's rating. The sorted-index formula still handles this exactly.

- **Multiple global minima:** The sink's rating remains `A`. Donating several copies of `A` to it does not lower it below `A` and does not alter the formula.

- **Exactly one unit per device:** Donating empties a source and gives it rating zero, so the optimal choice is no operation. The dedicated branch avoids accessing a nonexistent `x[1]`.

- **Optional operations:** The construction may use each nonsink as a source once, which is permitted, while the sink receives many times. No device is required to act as a source.

- **Input mutation for `n \ge 2`:** Because `x.sort()` operates on each original inner list, callers cannot rely on the rows retaining their original order after this branch runs. The `n=1` branch returns before sorting.

- **Missing `List` and `inf` names:** The file first fails while resolving `List`. If that name alone is injected, it later fails at `inf`. Both omissions must be acknowledged before the algorithm can execute normally.

- **Manifest complexity mismatch:** A claim of `O(U)` time and `O(1)` auxiliary space would describe a two-minimum scan, not this sorting implementation. The faithful bounds for the stored `x.sort()` source are `O(U\log n)` time and up to `O(n)` sorting workspace.
