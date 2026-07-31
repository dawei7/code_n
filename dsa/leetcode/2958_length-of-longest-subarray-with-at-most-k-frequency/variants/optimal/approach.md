## General

Maintain a window `nums[left:right + 1]` and a frequency map for exactly its
contents. When a new value enters at `right`, it is the only value whose count
can newly exceed `k`. If it does, move `left` forward, decrementing departing
values, until that new value's frequency is valid again. Every other count only
decreases during this repair, so the whole window is then good.

For each right endpoint, this process leaves the earliest possible valid left
endpoint. Any window ending there and starting earlier would still contain too
many copies of the newly added value, while every later start is no longer.
Therefore the repaired window is the longest good window with that right
endpoint. Taking the maximum length over all endpoints finds the global
optimum. Because `left` never moves backward, the total repair work is linear.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each endpoint advances at most $N$ times,
so the expected running time is $O(N)$ under standard hash-map behavior. The
map contains at most $N$ distinct values and therefore uses $O(N)$ space.

## Alternatives and edge cases

- **Enumerate every start and end:** Incrementally counting each subarray is correct but takes $O(N^2)$ time.
- **Store occurrence positions:** A queue per value can jump the left boundary past the forbidden occurrence, but it stores more position data than a frequency map needs.
- **One repeated value:** The longest good window has length `k` when the entire array is the same value.
- **No violated frequency:** If every complete-array frequency is at most `k`, the answer is the whole array length.
- **Several values at their limit:** Only the newly inserted value can become invalid; shrinking cannot make another frequency larger.
- **Large element values:** Hash keys handle values up to $10^9$ without allocating an array indexed by value.
