## General

To make a large value, choose the alternating orientation that rises immediately from `s`. The first high point can be `s + m`, because that uses the entire allowed adjacent difference. Starting downward cannot produce a larger first high point and only spends a position before a rise, so it never improves the maximum.

After a high point, strict alternation requires the next value to be lower. Lower it by exactly `1`, the smallest possible decrease between integers, and then raise the following value by `m`, the largest permitted increase. Each complete low-high pair therefore increases the best high point by `m - 1`.

For $n \ge 2$, there are $\lfloor n/2 \rfloor$ high positions when the sequence starts by rising. The first high contributes a gain of $m$, and every later high contributes another $m-1$. Equivalently, the maximum is

$$
s + \left\lfloor\frac{n}{2}\right\rfloor(m-1) + 1.
$$

This value is attainable by repeatedly using a decrease of `1` and an increase of `m`. It is also an upper bound: the first rise is at most $m$, while every later high must first lose at least $1$ and can then gain at most $m$. Thus no valid alternating sequence can exceed the constructed high points. When $n=1$, the only element is `s`.

## Complexity detail

The formula uses a fixed number of integer operations regardless of $n$, so it takes $O(1)$ time and $O(1)$ auxiliary space. It does not construct the sequence.

## Alternatives and edge cases

- **Explicit sequence construction:** Alternating a decrease of `1` with an increase of `m` finds the same maximum, but it takes $O(n)$ time and is impossible for the largest allowed $n$.
- **Blocked repeated addition:** The product $\lfloor n/2\rfloor(m-1)$ can be accumulated in large groups, but even a cube-block organization still takes $O(\sqrt[3]{n})$ additions without improving the result.
- **Dynamic programming by position and direction:** Tracking the best low and high reachable at every index is correct but stores or iterates over states whose closed-form transition has a constant net gain of $m-1$ per pair.
- **Single element:** When $n=1$, there is no adjacent pair, and the definition explicitly makes the sequence alternating; return `s`.
- **Unit difference limit:** When $m=1$, every low-high pair has zero net gain, so the answer for every $n\ge2$ is `s + 1`.
- **Odd length:** A rise-first sequence ends at a low position when $n$ is odd, so the final element does not create another maximum; integer division counts only complete high positions.
- **Large result:** The answer can exceed $10^9$, so fixed-width implementations need a sufficiently wide integer type.
