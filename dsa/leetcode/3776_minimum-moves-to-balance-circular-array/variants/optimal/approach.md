## General

**Use conservation to detect impossibility**

Each move transfers one unit between neighbors. It changes where balance is stored but does not change the total sum.

If `sum(balance) < 0`, making every entry nonnegative is impossible because nonnegative final entries would have a nonnegative total. The source returns `-1` immediately.

The statement guarantees at most one initially negative index. Under that guarantee, a nonnegative total is also sufficient: all other indices are nonnegative supplies whose total can fill the single deficit.

If `min(balance) >= 0`, the array already satisfies the goal and zero moves are optimal.

**Reduce the problem to supplying one deficit**

Otherwise, `mn = min(balance)` is the unique negative value, `i = balance.index(mn)` is its index, and

`need = -mn`

is the number of units it must receive.

There is no reason to move surplus between nonnegative destinations. Every required unit ultimately travels from some nonnegative index to `i`. Moving one unit across one edge costs one move, so a unit originating at circular distance $d$ costs at least $d$ moves. Sending it along a shortest path attains that cost.

The optimization is therefore to consume available units in nondecreasing shortest circular distance from the deficit.

**Expand simultaneously to the left and right**

For distance counter `j=1,2,...,n-1`, the source reads

`a = balance[(i-j+n) % n]`

and

`b = balance[(i+j-n) % n]`.

Modulo `n` wraps indices around the circle. These expressions are the positions `j` steps counterclockwise and clockwise from `i`.

From side `a`, the source takes

`c1 = min(a, need)`,

decreases `need` by `c1`, and adds `c1*j` to `ans`. It repeats the same operation for `b`.

Because all non-deficit positions are nonnegative, `min(supply, need)` never transfers a negative amount. It consumes no more than the donor owns and no more than the deficit still requires.

**Why nearest supply should be used first**

Suppose a solution uses one unit from distance $d_2$ while leaving an unused unit at smaller distance $d_1<d_2$. Replacing the farther unit with the nearer one preserves the final total supplied and reduces the move count by $d_2-d_1$.

Repeated exchanges transform an optimal plan into one that exhausts nearer distances before using farther ones. The source visits both directions at distance one, then both at distance two, and so on, exactly implementing this order. The order between two donors at the same distance is irrelevant because their per-unit costs are equal.

For `[1,2,-5,2]`, the deficit is five at index two. Its two distance-one neighbors supply two units each, costing four moves total. One unit remains. Index zero is at circular distance two, so its unit costs two more moves, for answer six.

**Understand why the long loop does not reuse supply**

After `j` passes half the circle, the modular left/right positions begin revisiting nodes already encountered. For even `n`, the exactly opposite node also appears as both `a` and `b` at `j=n/2`.

This looks dangerous because the source does not subtract consumed amounts from `balance`. The feasibility check and processing order make the repeats harmless. By the time every distinct non-deficit node has been encountered at its shortest distance, their total available supply is at least `need` because the complete array sum is nonnegative. Hence `need` has become zero before any later revisit can consume a second unit.

At an even-circle opposite node, all closer donors have already been processed. If the first visit to that opposite supply did not fill the remaining need, total supply would be insufficient; feasibility guarantees that cannot happen. The second same-distance access therefore also sees `need=0`.

The source could stop early when `need` reaches zero or iterate only through shortest-distance layers, but it does neither. Later iterations compute zero transfers and do not change `ans`.

**Why the accumulated cost is attainable**

Each selected unit from a donor `j` steps away can be passed along the corresponding clockwise or counterclockwise path one edge at a time, costing exactly `j` moves. Transfers from multiple donors can share intermediate people; an intermediate can receive and forward units without violating the final nonnegative goal.

The greedy exchange argument proves no plan can use a cheaper multiset of source distances. The per-unit path construction realizes the computed cost. Thus `ans` is both a lower bound and achievable.

**The manifest describes a different resource profile**

The manifest says the solution sorts supplies by circular distance in $O(N\log N)$ time and stores them in $O(N)$ space. The exact source creates no list of supplies and performs no sort. It enumerates distance layers arithmetically.

Its actual time is $O(N)$ and its additional space is $O(1)$. The explanation follows that executable implementation.

## Complexity detail

Summing the array, finding its minimum, and locating the negative index each take $O(N)$ time. The distance loop has $N-1$ iterations and constant work per side, so it is also $O(N)$.

Total actual time is $O(N)$.

Only scalar variables are stored. The input list is read but never changed, so auxiliary space is $O(1)$.

The result may multiply large balances by distances; Python integers avoid fixed-width overflow.

## Alternatives and edge cases

- **Sort donors by distance:** It is correct but unnecessary because the circle can be enumerated directly in increasing distance.
- **Breadth-first unit movement:** Simulating every individual transfer can take time proportional to the numeric balances rather than array length.
- **Use only one direction:** The closest supply may lie across the other circular edge, producing a nonminimal cost.
- **Use linear distance `abs(i-j)`:** Circular distance is `min(abs(i-j), n-abs(i-j))`.
- **Negative total:** Conservation makes the goal impossible, so return `-1`.
- **No negative entry:** The answer is zero even when the total is positive.
- **Exactly sufficient total:** All positive supply may be consumed, but every final value can still reach zero.
- **More supply than needed:** The final donor is used only partially through `min(supply, need)`.
- **Two equidistant donors:** Either order has the same cost; the source processes left then right.
- **Even-length opposite node:** It appears from both directions, but feasibility makes `need` zero after its first necessary use.
- **Later modular revisits:** They contribute zero because all distinct supplies have already sufficed.
- **Single-element array:** A negative value has negative total and returns `-1`; a nonnegative value returns zero.
- **At-most-one-negative guarantee:** The greedy single-destination reasoning depends on it. Multiple deficits would require a more general transport argument.
- **Input preservation:** Donor amounts are not decremented in the list; local `need` tracks total demand.
- **Source/manifest mismatch:** This exact solution is linear-time distance expansion, not sorting.
