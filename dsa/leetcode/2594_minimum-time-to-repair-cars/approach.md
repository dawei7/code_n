## General

**Ask how many cars fit within a fixed time**

Directly choosing how many cars each mechanic should repair creates many allocations. Instead, fix a candidate completion time $t$ and calculate the combined capacity of all mechanics.

A rank-$r$ mechanic repairing $x$ cars needs $rx^2$ minutes. The mechanic can finish $x$ cars by time $t$ when

$$
rx^2\le t.
$$

Solving for the greatest integer $x$ gives

$$
x=
\left\lfloor\sqrt{\frac tr}\right\rfloor.
$$

The helper `check(t)` sums this capacity over every mechanic and returns true when the total is at least `cars`.

**Why capacities can be added**

All mechanics work simultaneously and cars are independent. If one mechanic can complete $a$ cars and another can complete $b$ by time $t$, assign them disjoint cars and complete $a+b$ total.

The capacity sum may exceed the number waiting; that is harmless because feasibility only asks whether at least the required number can be assigned.

**Understand the exact square-root expression**

The code calculates `int(sqrt(t // r))`. Integer division first computes $\lfloor t/r\rfloor$. For nonnegative values,

$$
\left\lfloor\sqrt{\left\lfloor t/r\right\rfloor}\right\rfloor
=
\left\lfloor\sqrt{t/r}\right\rfloor,
$$

so this is mathematically the desired capacity.

`int` truncates the nonnegative floating square root, which acts as floor. An integer function such as `isqrt(t // r)` would express the same calculation without floating-point rounding concerns.

**Feasibility is monotone**

Giving mechanics more time can never reduce how many cars they can finish. Therefore `check(t)` has the form

`False, False, ..., False, True, True, ...`.

The minimum repair time is the first integer for which the predicate is true, making binary search appropriate.

**Search through a lazy range**

The call is

`bisect_left(range(ranks[0] * cars * cars), True, key=check)`.

Let $U=\texttt{ranks[0]}\cdot\texttt{cars}^2$. The mechanic represented by `ranks[0]` can repair all cars alone in exactly $U$ minutes, so $U$ is a guaranteed feasible upper bound even when that mechanic is not the fastest.

The `range(U)` contains candidates zero through $U-1$. If the first feasible time is smaller than $U$, `bisect_left` finds it normally. If the true answer is exactly $U$, every transformed range item is false and the insertion position is `len(range) = U`. Returning that endpoint still gives the correct time despite $U$ not being an element of the range.

A `range` stores only its boundaries, not all possibly enormous time values, so search-space memory is constant.

**Why the first true time is the answer**

If binary search returns $t^\star$, `check(t^\star)` is feasible either as an in-range true boundary or through the guaranteed upper endpoint. The capacity formula gives a concrete maximum allocation per mechanic whose sum covers all cars.

Every time smaller than $t^\star$ fails the predicate, meaning even the sum of all mechanics' maximum capacities is below `cars`. No allocation can finish sooner. Thus $t^\star$ is achievable and minimal.

**Trace the first sample at time 16**

For ranks `[4,2,3,1]`:

- rank four capacity is $\lfloor\sqrt{16/4}\rfloor=2$;
- rank two capacity is $\lfloor\sqrt{16/2}\rfloor=2$;
- rank three capacity is $\lfloor\sqrt{16/3}\rfloor=2$;
- rank one capacity is $4$.

The total is ten, so time 16 is feasible. At time 15 the capacities are $1,2,2,3$, totaling eight, so 16 is the first feasible time.

**Why allocation details are unnecessary**

The quadratic formula depends only on each mechanic's assigned count, and capacity at time $t$ already gives the largest allowed count. If summed capacity reaches the target, select any total of exactly `cars` slots among those capacities. Parallel execution completes them all by $t$.

This avoids constructing or optimizing an explicit allocation inside the binary search.

## Complexity detail

Let $m$ be the number of mechanics and $U=\texttt{ranks[0]}\cdot\texttt{cars}^2$. One predicate call scans all ranks in $O(m)$ time. Binary search performs $O(\log U)$ calls, for total $O(m\log U)$ time. Since ranks are bounded by 100, this is conventionally $O(m\log\texttt{cars})$ up to constant factors.

The generator, range, and binary-search state use $O(1)$ auxiliary space. The input list is not modified.

## Alternatives and edge cases

- **Manual binary search:** Explicit low and high variables implement the same first-true search and may be more familiar than `bisect_left` with a key.
- **Integer square root:** `isqrt(t // r)` avoids any floating-point boundary concern while giving the exact capacity.
- **Heap simulation:** Assign each next car to the mechanic with the earliest next completion, but this can require work proportional to `cars`.
- **One mechanic:** The answer is exactly `rank * cars^2`, and the exclusive range endpoint behavior returns it correctly.
- **Many equal ranks:** Capacities are summed once per mechanic occurrence, correctly reflecting parallel workers.
- **Time zero:** No positive number of cars can be repaired, so the predicate is false.
- **Upper bound not minimum rank:** Any existing mechanic alone supplies a valid bound; using the minimum rank would merely shrink the search interval.
- **Capacity exceeds demand:** Feasibility uses `>=` because extra potential repairs need not be assigned.
- **Input preservation:** Ranks are scanned only and remain in their original order.
