## General

**Carry the previous factorial between generator advances**

Factorials obey the recurrence $i! = i \cdot (i-1)!$. Store a running product initialized to $1$. For each index `value` from `1` through `n`, multiply the product by `value` and yield the result. Immediately before the yield at index $i$, the product equals

$$
1 \cdot 2 \cdot \ldots \cdot i = i!,
$$

so every emitted value is the required factorial. The loop visits indices in increasing order and exactly once, which yields precisely `1!` through `n!` without duplicating the value $1$ for `0!` and `1!`.

The zero input needs special treatment because the positive-index loop would otherwise emit nothing. Iterating through `Math.max(n, 1)` makes that single iteration multiply by $1$ and yield $1$, which is also the defined value of $0!$. For every positive input, the maximum is simply `n`, so the ordinary sequence is unchanged.

Because execution pauses at each `yield`, the running product and next loop index remain inside the generator object. Advancing it resumes exactly where the previous yield stopped; after the final value, the loop terminates and later advances report completion.

## Complexity detail

Each generator advance performs one multiplication, one loop update, and one yield, so it takes $O(1)$ time. The generator retains only the running product and loop index, using $O(1)$ persistent auxiliary space. Fully consuming the generator takes $O(\max(n,1))$ total time and produces that many output values.

The per-yield cost matches the $\Omega(1)$ work necessary to return an observable value. The package therefore uses an asymptotic-optimality certificate backed by recurrence, exhaustion, and boundary regressions.

## Alternatives and edge cases

- **Recompute each factorial from scratch:** This yields correct values but repeats earlier multiplications and takes $O(i)$ work for the $i$-th value.
- **Prebuild an array:** Computing all results eagerly uses $O(n)$ storage and loses the requested lazy generator behavior.
- **Recursive factorial calls:** Recursion can compute each value but adds call-stack overhead and either repeats work or requires extra memoization.
- For `n = 0`, yield exactly one `1` for $0!$.
- For positive `n`, start with $1!$; do not emit a separate $0!$ and create two leading ones.
- `n = 1` and `n = 0` both yield `[1]`, but for different factorial indices.
- After yielding the final `n!`, the generator must terminate rather than continue indefinitely.
- The upper bound `n = 18` keeps every required factorial exactly representable as a JavaScript `Number` integer.
