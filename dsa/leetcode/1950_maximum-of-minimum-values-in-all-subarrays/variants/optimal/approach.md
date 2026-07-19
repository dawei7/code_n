## General
**Find each value's widest minimum span**

Maintain a stack of indices whose values are strictly increasing after equal
or larger values are popped. Scan from left to right and append a sentinel
smaller than every legal input value. When the current value is at most the
stack top, pop index $i$. The new stack top is the nearest surviving smaller
value to the left, and the current position is a boundary at or below
`nums[i]` on the right.

If those boundary indices are `left` and `right`, then `nums[i]` is a minimum
of the span between them, whose length is

$$
L=\textit{right}-\textit{left}-1.
$$

Record `nums[i]` as a candidate for `answer[L - 1]`. Popping equal values
assigns their overlapping spans consistently; at least one equal occurrence
receives every maximal extent needed for the result.

**Fill answers for shorter windows**

Some lengths may receive no direct candidate. However, the answer cannot
increase as window length grows. Any window of length $L+1$ contains a window
of length $L$ whose minimum is at least as large, so

$$
\texttt{answer}[L-1] \ge \texttt{answer}[L].
$$

Sweep the result from right to left and replace each entry by the maximum of
itself and the entry to its right. A value that is a minimum over a span of
length $L$ is also attainable in an appropriate subwindow of every shorter
length, so this propagation fills all missing lengths without inventing an
invalid candidate.

Every array value is considered at its widest valid minimum span, and every
window minimum is one of the values considered this way. Taking maxima and
then applying the required monotonic relation therefore yields exactly every
query answer.

## Complexity detail
Each index is pushed once and popped once, so the monotonic scan is $O(N)$.
The backward propagation is another $O(N)$ pass. The stack and answer array
each contain at most $N$ integers, giving $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all subarrays:** Extend every starting position while maintaining
  a running minimum. This avoids recomputing each minimum from scratch but
  still costs $O(N^2)$ time.
- **Sliding-window deque per length:** A deque finds all minima for one length
  in $O(N)$ time, but repeating it for all $N$ lengths is quadratic.
- A one-element array returns that element.
- Equal values require consistent boundary handling; popping on equality lets
  one occurrence represent the widest shared span.
- Zero is a legal value, so the flush sentinel must be strictly smaller than
  zero.
- For a strictly increasing or decreasing array, the answers are the values in
  decreasing order.
- The full-length answer is always the minimum of the entire array.
