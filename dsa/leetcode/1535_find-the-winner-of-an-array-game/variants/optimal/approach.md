## General
**Replace queue mutation with a champion scan**

Treat `arr[0]` as the current champion and scan each later value as the next challenger. If the champion is larger, its streak increases. If the challenger is larger, that challenger becomes champion and starts with one win.

This produces exactly the same sequence of front champions as physical queue simulation. Every value displaced from the front moves behind all not-yet-seen challengers, so it cannot participate again before the scan reaches the original array maximum.

**Stop at the streak or at the maximum**

Return immediately when a streak reaches `k`. If the scan ends first, the current champion is the maximum array value: every earlier champion was compared with and defeated by a later larger value. The maximum can never lose, so it will eventually accumulate any remaining number of wins and is the guaranteed answer.

Thus no rounds after the first pass need simulation, even when `k` is as large as $10^9$. Distinctness ensures every comparison has one strict winner.

## Complexity detail
Each array value is examined at most once, giving $O(n)$ time independently of `k`. The champion and streak use $O(1)$ auxiliary space.

Literal simulation can require $O(n+k)$ rounds. The one-pass argument removes the `k` term because reaching the maximum makes all future results predetermined.

## Alternatives and edge cases
- **Deque simulation:** faithfully models each round but may require $O(n+k)$ time when `k` is large.
- **Return `max(arr)` immediately:** correct only when no earlier value reaches the required streak first.
- **Track queue positions:** unnecessary because the original challenger order remains sufficient until the maximum appears.
- **`k = 1`:** the larger of the first two values wins immediately.
- **Maximum first:** it is the answer for every `k`, although a small `k` may be reached before scanning all challengers.
- **Maximum last:** earlier champions may win temporarily, but the last value eventually becomes unbeatable.
- **Very large `k`:** the answer is the maximum, found within one pass.
- **Distinct values:** no tie rule is needed and a challenger either replaces the champion or loses.
