## General

**Any harvested set can be treated as a position interval**

Fruit positions are sorted and unique. If a path reaches a leftmost harvested position $L$ and a rightmost harvested position $R$, it passes every coordinate between them. Consequently, it also reaches every listed fruit position inside $[L,R]$ and harvests those fruits automatically.

An optimal result can therefore be represented by a contiguous window in the sorted `fruits` array.

Because all fruit amounts are positive, for a fixed right endpoint it is best to keep the widest reachable window: removing an additional reachable left position could only decrease the sum.

**Derive the minimum cost to cover one interval**

For window endpoints at positions $L$ and $R$, the path must cover the full span $R-L$ at least once. Starting at $S=\texttt{startPos}$, it can first reach either endpoint, then traverse to the other.

The minimum movement cost is

$$
(R-L)+\min(\lvert S-L\rvert,\lvert S-R\rvert).
$$

The first term covers the interval from one endpoint to the other. The minimum term chooses the cheaper endpoint to reach first.

This formula also handles intervals entirely on one side. If $S<L$, reaching $L$ is cheaper, and the expression becomes $(R-L)+(L-S)=R-S$, the direct rightward distance. The case $S>R$ is symmetric.

When $S$ lies inside the interval, the formula describes going first to the nearer endpoint, reversing once, then crossing the full interval to the farther endpoint.

**Maintain a sliding window and its fruit sum**

The right pointer `j` moves through `fruits`. Each new amount `fj` is added to `s`.

The left pointer `i` is advanced while the current interval cost exceeds `k`:

`pj - fruits[i][0] + min(abs(startPos - fruits[i][0]), abs(startPos - fruits[j][0])) > k`.

Here `pj` is the right position, so `pj - fruits[i][0]` is the span.

Every time the window shrinks, the removed left amount is subtracted from `s`. Once the condition becomes false, `s` is the sum of a reachable interval ending at `j`, and `ans` is updated.

If even the single right endpoint is unreachable, the loop may advance `i` past `j` and reduce `s` to zero. That empty window contributes nothing and later positions can still be considered.

**Why moving only the left pointer is sufficient**

As `j` advances, the interval's right endpoint never moves left. If the window becomes too expensive, removing leftmost positions reduces the span and cannot make reachability worse. Feasibility is monotonic as `i` moves right.

For the fixed `j`, the first reachable left boundary found by the while loop gives the largest feasible window ending there. Since amounts are positive, it also gives the greatest fruit sum among windows with that right endpoint.

Trying all right endpoints therefore considers an optimal interval.

**Trace the mixed-direction example**

With start 5 and an interval from position 4 to 7, the span is 3. The distances from the start to the endpoints are 1 and 2. The minimum path cost is $3+1=4$: go left to 4, then right through 5, 6, and 7.

This interval can collect fruit at all listed positions 4, 5, 6, and 7 within four steps. The formula captures the one reversal without explicitly simulating the path.

**Why the algorithm is correct**

Every legal path has leftmost and rightmost reached fruit positions, producing a contiguous fruit-array window whose minimum cover cost is no greater than the path's steps. Thus an optimal path corresponds to some feasible window.

For each possible right endpoint, the sliding loop retains the leftmost feasible start and hence the maximum positive fruit sum for that endpoint. `ans` takes the maximum over all of them.

Conversely, every window accepted by the cost formula has an explicit path: reach its nearer endpoint first and traverse to the other. It uses at most `k` steps and harvests exactly all window fruits. Every candidate counted is attainable.

The method relies on the input already being sorted and does not mutate it.

## Complexity detail

Let $n$ be the number of fruit positions.

The right pointer advances $n$ times. The left pointer advances at most $n$ times over the entire run, not once per right endpoint. All formula and sum updates are constant time, so total time complexity is $O(n)$.

Only `ans`, `i`, `s`, and loop values are stored. Excluding the input and returned integer, auxiliary space is $O(1)$.

The fruit sum may be large; Python integers handle it without overflow.

## Alternatives and edge cases

- **Enumerate left and right endpoints:** Testing all intervals costs $O(n^2)$. Sliding-window monotonicity reduces this to linear time.
- **Prefix sums plus binary search:** One can enumerate a turning direction and binary-search the far endpoint, usually in $O(n\log n)$. The direct window is faster.
- **Simulate every route:** There are many step sequences that reach the same interval. The endpoint cost formula collapses them to one value.
- **`k == 0`:** Only fruit exactly at `startPos` can be harvested.
- **No reachable fruit:** Every nonempty window is removed and `ans` remains zero.
- **All fruits on one side:** The formula reduces to direct distance to the farthest window endpoint.
- **Start inside the interval:** The minimum endpoint distance represents the cheaper first direction.
- **Fruit at the start:** It is included in any window containing that position at no initial movement cost.
- **Positive amounts:** This property makes retaining every reachable interior and the widest fixed-right window optimal.
- **Large gaps:** Position distance, not array-index distance, controls the while condition.
- **Unique sorted positions:** These guarantees make each window correspond to one ordered coordinate interval.
- **Input preservation:** No sorting or amount changes occur.
