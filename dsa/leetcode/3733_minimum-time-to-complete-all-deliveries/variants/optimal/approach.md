## General

**Turn the schedule into three necessary capacity conditions**

Fix a possible finishing hour `T`. Drone `i` cannot deliver at multiples of `r[i]`, so among hours one through `T` it is individually available for

$$
T-\left\lfloor\frac{T}{r_i}\right\rfloor
$$

hours. It needs at least `d[i]` such hours.

There is also one shared machine-like restriction: only one drone may deliver during an hour. An hour is unusable by both drones only when it is a multiple of both recharge intervals, meaning a multiple of

$$
L=\operatorname{lcm}(r_1,r_2).
$$

Consequently, the total number of hours in which at least one drone can deliver is

$$
T-\left\lfloor\frac{T}{L}\right\rfloor.
$$

That shared pool must contain at least `d[0] + d[1]` hours.

These give three requirements:

$$
T-\left\lfloor\frac{T}{r_1}\right\rfloor\ge d_1,
$$

$$
T-\left\lfloor\frac{T}{r_2}\right\rfloor\ge d_2,
$$

and

$$
T-\left\lfloor\frac{T}{L}\right\rfloor\ge d_1+d_2.
$$

The first two protect each drone's private quota. The third prevents both quotas from competing for too few usable hours.

**Why the three conditions are sufficient**

Hours fall into four categories: available only to drone one, available only to drone two, available to both, or available to neither. Assign each drone its exclusive hours first. Any remaining deliveries for either drone must use shared hours.

The individual conditions guarantee that exclusive plus shared hours are sufficient for each drone separately. The combined condition guarantees enough distinct non-neither hours for both quotas together. With only two drones, these are exactly the Hall-type capacity conditions needed to assign different hours to all deliveries. Thus no hidden scheduling constraint remains.

**Invert one drone's availability formula directly**

For `q` required deliveries and recharge interval `p`, the availability pattern repeats as `p-1` usable hours followed by one recharge hour. The time of the `q`-th usable hour is

`q + (q - 1) // (p - 1)`.

The first `q` term counts the delivery hours themselves. Before the last required delivery, every complete block of `p-1` deliveries forces one recharge hour. The number of such completed blocks is `floor((q-1)/(p-1))`.

This is the helper

`required_hours(deliveries, recharge_interval)`.

It returns the smallest `T` satisfying `T - floor(T/p) >= q`. For example, with `p=3`, usable hours are one, two, four, five, seven, eight, and so on. The fourth delivery occurs at hour five, and the formula gives `4 + 3 // 2 = 5`.

**Apply the inverse to all three constraints**

The first two helper calls compute the earliest horizon satisfying each drone's individual availability. The third treats all deliveries as one combined quota whose only forbidden hours are simultaneous recharge hours, using `L` as its interval.

The least `T` satisfying all three lower bounds is their maximum:

`max(required_hours(d[0], r[0]), required_hours(d[1], r[1]), required_hours(d[0] + d[1], L))`.

Any smaller time violates whichever threshold attains this maximum, so completion is impossible. At the maximum, all three capacity conditions hold, and the sufficiency argument proves that a legal assignment exists. Therefore the returned time is minimal.

**Compute the least common multiple safely**

The source uses

`r[0] // gcd(r[0], r[1]) * r[1]`.

Dividing by the greatest common divisor before multiplying avoids counting shared prime factors twice and reduces intermediate growth. The result is exactly the first positive hour at which both drones recharge together; its multiples are precisely the hours unavailable to both.

For `d=[3,1]` and `r=[2,3]`, the individual thresholds are five and one. The LCM is six, and four combined deliveries require four hours because none of hours one through four is a multiple of six. The maximum is five.

For equal recharge intervals two and quotas one and three, both individual capacities matter, but the combined threshold dominates: four deliveries with every second hour unusable finish at hour seven.

## Complexity detail

The method performs one greatest-common-divisor calculation and a constant number of arithmetic operations. Euclid's algorithm takes $O(\log \min(r_1,r_2))$ time in the general numeric model. Because the recharge intervals are bounded by $3\cdot10^4$, the manifest reasonably records this bounded work as $O(1)$. Space usage is $O(1)$.

No loop depends on delivery counts, even though they can reach $10^9$. Python integers safely hold the combined result.

## Alternatives and edge cases

- **Binary search on time:** Testing the same three capacity inequalities gives an $O(\log answer)$ method. The helper algebraically inverts each inequality, making binary search unnecessary.
- **Hour-by-hour simulation:** Delivery counts can be billions, so simulation is far too slow and requires arbitrary scheduling decisions.
- **Check only individual capacities:** Both drones could each have enough available hours while competing for the same shared hours. The LCM-based combined condition is essential.
- **Check only combined capacity:** One drone might be unavailable too often to meet its own quota even though total usable hours are plentiful.
- **Use `r1*r2` instead of the LCM:** This misses simultaneous recharge hours when the intervals share factors and undercounts jointly forbidden hours.
- **Both drones recharge together frequently:** Equal intervals make the combined threshold especially important and are handled naturally by `L=r`.
- **One delivery:** The helper returns one because no recharge must occur before the first usable hour.
- **Quota exactly fills availability blocks:** Using `q-1` ensures a recharge after the last required delivery is not added unnecessarily.
- **Only one drone available in an hour:** That hour is effectively reserved for it; the sufficiency assignment uses exclusive hours first.
- **Both drones available:** The hour can serve either but only once, which the combined capacity counts correctly.
- **Large quotas:** Closed-form arithmetic avoids constructing a schedule or storing hours.
