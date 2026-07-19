## General
**Sort to expose occupied spans:** Let the sorted positions be $x_0 < x_1 < \dots < x_{N-1}$. A finished arrangement is a block of $N$ consecutive positions. Sorting makes it possible to count how many stones already fit in any interval of length at most $N$ and to measure the empty positions between the endpoints.

**Minimize moves with a sliding window:** Maintain the largest sorted window whose inclusive span is at most $N$, so `x[right] - x[left] + 1 <= N`. If that window contains $k$ stones, the other $N-k$ stones can normally be moved into its unoccupied positions, giving $N-k$ moves. Advancing the right boundary and shrinking the left boundary examines every possible target span in linear time after sorting.

There is one forced exception. If a window contains exactly $N-1$ stones already occupying $N-1$ consecutive positions, its only missing position in an $N$-position completion lies just outside that block. Moving the distant endpoint directly there would leave it as an endpoint, so that move is illegal. One legal move must first create an interior vacancy, and a second move fills it; this candidate therefore costs two moves rather than one.

**Maximize moves by consuming empty positions:** During a longest game, one original endpoint is effectively kept while the opposite endpoint moves inward one empty position at a time. The usable empty-position counts are

$$
G_{\mathrm{left}} = x_{N-1} - x_1 - (N-2)
$$

and

$$
G_{\mathrm{right}} = x_{N-2} - x_0 - (N-2).
$$

The first expression excludes the original left endpoint, while the second excludes the original right endpoint. Choosing the larger count gives the maximum number of legal moves. Each counted gap can be consumed by moving the opposite endpoint inward, and excluding one outer gap prevents an illegal move that would leave the relocated stone outside all others.

## Complexity detail
Sorting the $N$ positions costs $O(N \log N)$ time. Both the sliding window and the endpoint-gap calculation take $O(N)$ additional time. The sorted copy uses $O(N)$ space; an implementation permitted to reorder the input can sort in place and use $O(1)$ auxiliary space apart from the sorting implementation.

## Alternatives and edge cases
- **Quadratic window enumeration:** Try every left boundary and scan rightward while the span fits. It computes the same minimum but takes $O(N^2)$ time.
- **Simulate every legal game:** Exploring move sequences branches extensively and repeats equivalent configurations, making it unsuitable for $N$ up to $10^4$.
- **Already consecutive:** The widest valid window contains all $N$ stones and both endpoint-gap counts are zero, so the answer is `[0,0]`.
- **Almost consecutive special case:** Exactly $N-1$ consecutive stones plus one distant endpoint requires two minimum moves because a direct one-move finish is illegal.
- **Unsorted input:** Stone order in the input carries no geometric meaning; calculations must use positions in ascending order.
- **Large coordinates:** Only differences between positions matter, so gaps near $10^9$ do not require iterating across every coordinate.
