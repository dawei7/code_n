## General

**Represent each row by its remaining suffix**

Seats are always allocated with the smallest available seat numbers. Consequently, occupied seats in a row always form a prefix and empty seats form one contiguous suffix. A row needs only one value: its remaining seat count `s`. If each row has `m` seats, the first free seat is `m-s`.

The segment tree uses one-based leaf indices while public row numbers are zero-based. Leaf one represents public row zero.

**Store two aggregates**

For every segment-tree node, `s` is the sum of remaining seats across its row interval and `mx` is the largest remaining count in any one row there.

The sum answers whether scattered seating has enough total capacity. The maximum answers whether some row can hold a gathered group contiguously. `pushup` restores both aggregates from the two children.

Construction gives every leaf `m` remaining seats and combines upward. The preallocated array of about `4n` nodes stores the complete tree.

**Update one row**

`modify` descends to the leaf for row `x` and replaces both its sum and maximum with new remaining value `v`. On return, each ancestor recomputes its aggregates.

Bookings only decrease leaf values, but replacement rather than subtraction keeps the tree helper general and makes callers responsible for calculating `s-k` or zero.

**Find the earliest row with enough consecutive seats**

`query_idx(..., k)` first rejects a segment whose `mx < k`. At an internal node, it prefers the left child whenever that child's maximum is sufficient. Only when the left cannot work does it consider the right child, and it enters that side only when the prefix boundary `r` extends past the midpoint.

All public searches start at row one, so this logic finds the smallest leaf no greater than `maxRow+1` with at least `k` remaining seats. Returning zero means none exists.

**Perform** `gather`

`gather` converts `maxRow` to one-based form and finds the earliest row with `k` seats. Failure returns an empty list without changing state.

On success, it queries that leaf's remaining count `s`, updates the leaf to `s-k`, and returns public row `i-1` plus starting seat `m-s`. Since the free seats are a suffix, the group receives exactly the leftmost `k` consecutive free seats.

**Check scattered capacity before changing anything**

`scatter` first queries the sum of remaining seats in rows one through `maxRow+1`. If it is smaller than `k`, the method returns false before allocating any seat. This all-or-nothing check is essential: a failed request must not leave a partial booking.

If capacity is sufficient, the method finds the earliest nonempty row using threshold one.

**Consume earliest rows for** `scatter`

Starting from that row, the loop queries each leaf. If the current row has at least `k` seats, it subtracts the remaining request and returns true. Otherwise, it consumes the whole row, subtracts its capacity from `k`, and updates the leaf to zero.

Although the loop syntactically continues through all `n` rows, the prefix-sum precheck guarantees it finishes by the permitted maximum row. It can never need an illegal later row.

This order fills the smallest row numbers first. Within a row, the remaining-suffix representation means the smallest seat numbers are consumed first.

**Why the tree state stays exact**

Initially every leaf equals its row's empty-seat suffix length. Each successful operation removes a prefix of that suffix and writes the new length. No operation creates a hole. Leaf values therefore remain exact.

`pushup` makes every internal sum and maximum exact after each leaf update. Gather uses the maximum to locate the earliest feasible single row; scatter uses the sum to prove global feasibility and then consumes rows greedily. These match the two public contracts.

**Trace the sample**

With two rows of five seats, gather four finds leaf one with `s=5`, returns row zero and seat zero, then stores one. A later gather of two limited to row zero fails because its prefix maximum is one.

Scatter five through row one sees total capacity six. It consumes row zero's last seat, then four seats in row one, leaving one. The next scatter of five fails its sum precheck and changes nothing.

## Complexity detail

Building the complete tree takes `O(n)` time and space. A point update, range-sum query, or earliest-row search follows `O(\log n)` tree levels.

Gather performs a constant number of such operations, so it is `O(\log n)`.

A single scatter may empty many rows and cost `O(t\log n)` for `t` visited rows. Across the entire operation sequence, each row can be made completely empty only once; every successful scatter has at most one partially consumed final row. Thus, over `q` calls, total time is `O((n+q)\log n)` amortized, with `O(n)` tree space.

## Alternatives and edge cases

- **Scan rows linearly:** It is simple but can revisit many full rows across requests and become quadratic.
- **Fenwick tree only:** It supports prefix sums but cannot directly find a row with `k` contiguous remaining seats; the maximum aggregate supplies that need.
- **Balanced set of nonempty rows:** It helps scatter but still needs per-row capacity search for gather thresholds.
- **Gather larger than one row:** It fails even when total prefix capacity is sufficient, because all seats must be together.
- **Scatter across rows:** Sum capacity is the correct feasibility criterion because contiguity is not required.
- **Already full early rows:** Earliest-row search skips leaves whose maximum is zero.
- **Exact row fill:** Updating to zero correctly removes that row from later searches.
- **Failed request:** Both operations check feasibility before mutation.
- **Zero-based API:** `maxRow` and returned row are converted around the one-based tree.
- **Starting seat:** `m-s` equals the number already occupied in that row.
- **Loop beyond** `maxRow`: The capacity precheck guarantees success before crossing it.
- **Amortized bound:** One scatter can be linear in rows, but rows cannot be fully consumed repeatedly.
- **Large seat counts:** Aggregated sums require wide integers; Python handles them.
