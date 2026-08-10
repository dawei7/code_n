## General

**Track when the single chef becomes free**

Customers must be served in input order, and the chef can prepare only one order at a time. The entire state needed for the next customer is therefore one time value: `t`, the completion time of the most recently processed order. Before any customer, the source initializes `t = 0`.

For a customer represented by `[a, b]`, `a` is the arrival time and `b` is the preparation duration. The chef cannot start before both conditions hold:

- the customer has arrived, and
- the previous order has finished.

The earliest valid start time is consequently `max(t, a)`. Adding `b` gives the current order's completion time:

`t = max(t, a) + b`.

This one assignment handles both an idle restaurant and a waiting line.

**Case one: the chef is still busy**

If the old `t` is greater than `a`, the customer arrives while an earlier order is being prepared. The maximum chooses `t`, so the new completion time is `old_t + b`. The customer waits from arrival `a` through the remaining busy period and through preparation of their own order.

For example, if the chef is free at time eight, a customer arrives at four, and preparation takes three, delivery happens at eleven. The total waiting time for that customer is `11 - 4 = 7`.

**Case two: the chef has been idle**

If `a` is at least the old `t`, no pending work delays this customer. The maximum chooses `a`, and completion becomes `a + b`. Any gap between the old completion time and this arrival is idle time; it must not be added to the customer's wait.

The resulting waiting time is exactly `b`, because the problem's definition includes preparation time. This point is easy to misread: “waiting time” here runs until the food is finished, not merely until cooking begins.

When `a == t`, either branch interpretation gives the same start time. The next order begins immediately when the previous one ends.

**Accumulate completion minus arrival**

Once `t` has been updated for the current customer, that customer's full waiting time is `t - a`. The source adds it to `tot`:

`tot += t - a`.

The variables `tot = t = 0` are initialized together. Both are integer values throughout the loop: `t` is the current completion time, while `tot` is the sum of completed customers' waiting times. They have distinct roles even though they begin at the same value.

After all customers, `tot / len(customers)` computes the arithmetic mean. Python's `/` operator performs true division and returns a floating-point value, even when the sum is evenly divisible. This satisfies the required numeric return and tolerance.

**Trace the first example**

For `customers = [[1,2],[2,5],[4,3]]`:

- At arrival one, `max(0,1) + 2 = 3`. The first wait is `3 - 1 = 2`, so `tot = 2`.
- At arrival two, the chef is busy until three. Completion becomes `max(3,2) + 5 = 8`. The wait is six, so `tot = 8`.
- At arrival four, the chef is busy until eight. Completion becomes eleven. The wait is seven, so `tot = 15`.

Dividing by three returns `5.0`.

In the second example, the customer arriving at time twenty demonstrates the idle-gap case. Although the preceding order finishes at fourteen, `max(14,20)` resets the start to twenty. The six idle time units do not inflate anyone's wait.

**Why processing input order is sufficient**

The arrival times are non-decreasing, and the contract explicitly says the chef prepares orders in the given order. There is no scheduling choice to optimize. Sorting would be redundant and could incorrectly reorder customers who have equal arrival times relative to the required input order.

Assume before processing a customer that `t` is the exact finish time of all earlier work. No legal schedule can begin the new order before `max(t,a)`, because either the chef or the customer would be unavailable. The chef begins immediately at that time, as the process requires, so the computed finish is both feasible and earliest. Subtracting arrival gives the exact wait. By induction, every added wait and the final total are correct.

**Why a running sum is enough**

The final result needs only the mean, not each individual waiting time. After a wait has been added to `tot`, it never affects future scheduling; only the chef's latest completion `t` does. Storing an array of per-customer waits would provide no information needed later.

## Complexity detail

Let $n$ be the number of customers. The loop visits each input pair exactly once and performs a maximum, additions, and a subtraction, all constant-time under the usual fixed-width arithmetic model. Total time is $O(n)$.

The algorithm uses only `t`, `tot`, and the current unpacked values `a` and `b`. None grows in count with the input, so auxiliary space is $O(1)$. The division creates only the returned floating-point number.

With the stated limits, the final completion and accumulated wait fit comfortably in common 64-bit integer ranges. Python integers also grow automatically, so intermediate arithmetic cannot overflow. Floating conversion occurs only once at the end, avoiding repeated rounding during accumulation.

## Alternatives and edge cases

- **Store every completion time:** A DP-style array can record each finish, but only the preceding finish is needed, so it wastes $O(n)$ space.
- **Event simulation with a queue:** Explicit arrival and completion events reproduce the same process with unnecessary machinery because service order is fixed.
- **Sort the customers:** Arrival order is already non-decreasing, and equal-arrival input order must be preserved; sorting is not needed.
- **Average incrementally:** Updating a floating mean on every customer can introduce repeated rounding. Summing exact integer waits and dividing once is simpler.
- **One customer:** `t` becomes arrival plus preparation, `tot` becomes the preparation duration, and the returned average is that duration.
- **Long idle gap:** `max(t,a)` discards idle time and starts at arrival.
- **Continuous backlog:** When every next arrival precedes `t`, completion simply advances by each preparation duration.
- **Equal arrival times:** The first such customer starts when possible, and subsequent ones wait in their given order.
- **Arrival exactly at completion:** The chef starts the new order immediately, with no extra idle or queue delay.
- **Preparation time is included:** The contribution is completion minus arrival, not start minus arrival.
- **Nonempty input:** The constraint guarantees at least one customer, so division by `len(customers)` cannot divide by zero.
- **Output precision:** Python true division produces a float; the judge accepts answers within the stated tolerance.
