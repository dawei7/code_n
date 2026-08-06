## Description

A traveler has $k$ weeks to move among $n$ cities while balancing an assignment with vacation time. The objective is
to schedule the weekly locations so that the total number of vacation days is as large as possible.

The schedule follows these rules and restrictions:

- Cities are numbered from `0` through `n - 1`. The traveler is initially in city `0` on Monday morning.
- `flights` is an $n \times n$ directed adjacency matrix and need not be symmetric. A value of `flights[i][j] == 1`
  permits travel from city `i` to city `j`; a zero means that flight is unavailable. Every diagonal entry
  `flights[i][i]` is zero.
- Each of the $k$ weeks contains seven days. A flight may be taken only on Monday morning, with at most one flight on
  that day. Flight duration has no effect on the vacation calculation.
- `days` is an $n \times k$ matrix. The entry `days[i][w]` gives the maximum vacation days available in city `i`
  during week `w`.
- The traveler may stay in a city for the whole week even when its vacation allowance is below seven, but the
  remaining days are work days and do not increase the total.
- When a Monday flight goes from city `A` to city `B`, that week's vacation allowance is taken from city `B`.

Given `flights` and `days`, return the maximum number of vacation days obtainable over all $k$ weeks.
