## General

**Turn minimization into a feasibility question**

Suppose the maximum allowed integer is `x`. Only numbers from 1 through `x` may be placed into the arrays.

Ask whether enough eligible, mutually distinct numbers exist to fill:

- `arr1` with `uniqueCnt1` values not divisible by `divisor1`;
- `arr2` with `uniqueCnt2` values not divisible by `divisor2`.

If a particular `x` is feasible, every larger maximum is also feasible because it preserves all earlier choices and offers additional numbers. This monotonicity makes binary search appropriate.

**Count numbers not divisible by one divisor**

Among integers 1 through `x`, every complete block of `d` consecutive values contains exactly `d-1` values not divisible by `d`. There are `x//d` complete blocks, followed by `x%d` extra values, all of which occur before the next multiple of `d`.

Therefore, the count is

`x//d*(d-1)+x%d`,

which is algebraically equal to

$$
x-\left\lfloor\frac{x}{d}\right\rfloor.
$$

The function computes `cnt1` with `divisor1` and `cnt2` with `divisor2`. The necessary individual conditions are:

`cnt1>=uniqueCnt1`

and

`cnt2>=uniqueCnt2`.

**Count the combined usable pool**

The arrays cannot share an integer. It is not enough for each individual eligibility count to be large: the same flexible numbers might be needed by both.

A number is unusable by both arrays only when it is divisible by both divisors. This occurs exactly at multiples of

$$
\operatorname{lcm}(\texttt{divisor1},\texttt{divisor2}).
$$

The source stores this least common multiple as `divisor` and computes `cnt`, the numbers through `x` not divisible by it. These are exactly the numbers usable by at least one of the two arrays.

The union must contain at least

`uniqueCnt1+uniqueCnt2`

distinct usable numbers.

**Why the three inequalities are sufficient**

Classify candidates into:

- values usable only by `arr1`;
- values usable only by `arr2`;
- values usable by either array.

The individual counts ensure each array has enough candidates when the flexible group is included. The combined count ensures enough total distinct candidates exist for both demands together.

For two recipient sets, these are precisely the necessary matching conditions. Assign forced-only values where useful, then distribute flexible values to cover whatever demand remains. The union inequality prevents both arrays from overclaiming the same numbers.

Thus `f(x)` returns true exactly when maximum `x` can support a valid construction.

**Use `bisect_left` on the Boolean predicate**

The code searches virtual sequence `range(10**10)` with:

`bisect_left(...,True,key=f)`.

Because `f` is false for small infeasible values and true for all values at or above the optimum, the keyed range behaves like a sorted Boolean sequence. `bisect_left` returns the first position whose key is true, which is the minimum feasible maximum.

The search does not materialize ten billion integers. Python's `range` is a compact arithmetic object, and binary search evaluates `f` only at logarithmically many positions.

The upper boundary $10^{10}$ safely exceeds the needed answer under demands totaling at most $10^9$ and divisors at least two.

**Trace the first sample at `x=4`**

With divisors 2 and 7:

- numbers not divisible by 2 are 1 and 3, so `cnt1=2>=1`;
- all 1 through 4 are not divisible by 7, so `cnt2=4>=3`;
- $\operatorname{lcm}(2,7)=14$, so all four numbers are usable by at least one array, meeting combined demand four.

The predicate is true. At `x=3`, only three total numbers exist for a combined demand of four, so it is false. The first true point is four.

**Why no arrays are constructed**

The problem asks only for the minimum possible maximum. The counting conditions prove existence, so explicitly choosing array contents would add work without changing the answer.

All arithmetic uses integer division and remainders, with no precision loss.

## Complexity detail

Computing the least common multiple uses a greatest-common-divisor calculation in $O(\log D)$ time, where $D$ bounds the divisors.

Binary search over the fixed range up to $10^{10}$ performs $O(\log 10^{10})$ predicate evaluations, about 34. Each predicate uses constant-time arithmetic in the ordinary word model. More generally, if the upper bound is tied to counts $C$, this is $O(\log C)$ search time.

Total time is $O(\log D+\log C)$ and auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Manual binary search:** Maintain low and high integers and call the same predicate; it avoids relying on keyed `bisect_left`.
- **Individual counts only:** They can overbook flexible numbers and are insufficient without the combined union condition.
- **Equal divisors:** The least common multiple is that divisor, and both arrays draw from the same eligible pool.
- **One divisor divides the other:** The least common multiple is the larger divisor; the formulas still hold.
- **Distinctness across arrays:** It is enforced by the combined count, not by constructing sets.
- **Positive integers:** Search includes zero as an infeasible boundary, and demands ensure the returned result is positive.
- **Large counts:** Integer formulas avoid enumeration up to the answer.
- **Monotonicity:** Once feasible, every larger `x` remains feasible.
- **Least common multiple:** Multiples of it are the only values forbidden to both arrays.
- **Upper bound:** It must be known feasible; $10^{10}$ is safely chosen for the constraints.
