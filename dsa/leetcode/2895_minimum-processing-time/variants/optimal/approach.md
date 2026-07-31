## General

**Only each processor's longest assigned task matters.** All four cores of a processor become available at the same time and each runs one task. If the longest duration assigned to a processor is $x$, that processor finishes at its availability time plus $x$; the other three tasks cannot delay it further.

Sort the task durations from longest to shortest. Pack the first four tasks together, the next four together, and so on. The maximum duration of each group is therefore found at indices $0,4,8,\ldots$. This packing makes the sequence of group maxima as small as possible: each maximum covers itself and up to three durations no larger than it, so no assignment can hide more than four tasks beneath one group maximum.

**Pair opposite extremes.** Sort processor availability times from earliest to latest and pair them with those group maxima from largest to smallest. To see why, consider two availability times $a \le b$ and two group maxima $x \ge y$. The opposite pairing finishes at

$$
\max(a+x,b+y).
$$

The same-order pairing has value $\max(a+y,b+x)=b+x$, which is at least both $a+x$ and $b+y$. Swapping any inverted pair therefore cannot improve on the opposite ordering. Repeating this exchange yields the sorted greedy assignment.

The answer is the maximum of `processorTime[i] + tasks[4 * i]` after sorting processors ascending and tasks descending.

## Complexity detail

There are $n$ processors and $4n$ tasks. Sorting the two arrays takes $O(n\log n)$ time, and scanning the $n$ group maxima takes $O(n)$ time. Python's in-place adaptive sort can use $O(n)$ auxiliary space; the final scan uses only constant additional state.

## Alternatives and edge cases

- **Repeated maximum selection:** Removing the four largest remaining tasks for every processor produces the same assignment, but a list-based implementation can take $O(n^2)$ time.
- **Sorting both arrays in the same direction:** Pairing a late processor with a long task needlessly combines both sources of delay and can increase the maximum completion time.
- **Arbitrary groups of four:** Spreading the largest tasks across different processors creates more large group maxima; packing them together lets one maximum cover three other long tasks.
- **Single processor:** Its availability time is added to the largest of the four task durations.
- **Equal availability times or durations:** Ties can be ordered arbitrarily without changing the result.
- **Large numeric result:** The completion time may exceed $10^9$, so implementations in fixed-width languages need a sufficiently wide integer type.
